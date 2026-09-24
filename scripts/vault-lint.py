#!/usr/bin/env python3
"""
vault-lint.py — structural linter for the Knowledge Vault.

Run from the vault root:      python scripts/vault-lint.py
Wider scope:                  python scripts/vault-lint.py --all
Only one check:               python scripts/vault-lint.py --only title

Checks
  broken   wikilink targets that do not resolve
  dupe     duplicate note basenames (Obsidian short links become ambiguous)
  orphan   notes with no inbound link (MOCs excluded)
  title    [!definition] callout titles that match no filename in the note
  empty    zero-byte notes, or notes that are only headings
  hollow   a heading immediately followed by another heading
  anchor   [[Note#Heading]] where Note has no such heading (the link resolves,
           so Obsidian and the broken check both stay silent)
  field    Dataview inline fields that will never be indexed: a key holding a
           [[link]], or a relation key written with one colon

Links inside fenced or inline code are ignored, matching the vault's
convention that not-yet-existing notes are written in `code`. Links inside
$math$ are ignored too, so notation like $[[a]]$ (authenticated sharing) is
not read as a wikilink.

A note carrying `status:: seed` (inline field) or `status: seed`
(frontmatter) is a deliberate placeholder for something you want to learn:
it is counted under SEEDS, not EMPTY or HOLLOW.

The practical areas (language/, security/, computer/) sit outside the layout
system, so they are indexed for link resolution but not counted as orphans or
hollow.
No dependencies beyond the standard library.
"""
import os, re, sys, argparse
from collections import Counter, defaultdict

SKIP_DIRS = {'.git', '.obsidian', '.trash', 'node_modules', '_to_delete'}
DEFAULT_SCOPE = ['knowledge']
META = {'North Star', 'Vault Refactoring Plan', 'Foundation Layer'}
PRACTICAL = {'language', 'security', 'computer'}   # outside the layout system

FENCE = re.compile(r'```.*?```', re.S)
INLINE = re.compile(r'`[^`\n]*`')
MATHBLOCK = re.compile(r'\$\$.*?\$\$', re.S)
MATHINLINE = re.compile(r'(?<![\\$])\$(?!\s)[^$\n]+?(?<![\\\s])\$')
SEED = re.compile(r'^(?:status::\s*seed|status:\s*seed)\s*$', re.M | re.I)
LINK = re.compile(r'\[\[([^\]\|#]*)')
FULLLINK = re.compile(r'\[\[([^\]\|#]*)#([^\]\|]*)(?:\|[^\]]*)?\]\]')
RELKEYS = r'(?:Extends|Generalizes|Instantiates|Requires|Member of|Complete for|Hard for|Hardness for|Transforms)'
BADKEY = re.compile(r'^[ \t]*(?:>[ \t]*)*([^:\n]*\[\[[^\n]*?)::', re.M)
ONECOLON = re.compile(r'^[ \t]*(?:>[ \t]*)*(?:[-*][ \t]+)?(' + RELKEYS + r')[ \t]*:(?!:)', re.M)
ODDKEY = re.compile(r'^[ \t]*(?:>[ \t]*)*(?:[-*][ \t]+)?(Hardness for)[ \t]*::', re.M)
DEFN = re.compile(r'>\s*\[!definition\]\s*(.+)')
HEAD = re.compile(r'^(#{1,6})\s+(.*)$', re.M)


def strip_code(text):
    text = INLINE.sub('', FENCE.sub('', text))
    return MATHINLINE.sub('', MATHBLOCK.sub('', text))


def hnorm(h):
    h = re.sub(r'\[\[([^\]|]*\|)?([^\]]*)\]\]', r'\2', h)
    return re.sub(r'[^a-z0-9]', '', h.lower())


def domain_of(p):
    parts = os.path.normpath(p).split(os.sep)
    return parts[1] if len(parts) > 2 and parts[0] == 'knowledge' else parts[0]


def norm(s):
    s = re.sub(r'\(.*?\)', '', s)                 # drop parentheticals
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s[:-1] if s.endswith('s') else s        # crude singular/plural fold


def walk(roots):
    for root in roots:
        if os.path.isfile(root) and root.endswith('.md'):
            yield os.path.normpath(root)
            continue
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in SKIP_DIRS]
            for f in sorted(fn):
                if f.endswith('.md'):
                    yield os.path.normpath(os.path.join(dp, f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true', help='scan the whole vault, not just knowledge/')
    ap.add_argument('--only', default=None, help='broken|anchor|field|dupe|orphan|title|empty|hollow|seed')
    ap.add_argument('--full', action='store_true', help='list everything (default caps each section at 15)')
    args = ap.parse_args()

    scope = ['.'] if args.all else [p for p in DEFAULT_SCOPE if os.path.isdir(p)]
    if not scope:
        sys.exit('run me from the vault root (no knowledge/ here)')

    # index every note in the vault, so links out of scope still resolve
    every = list(walk(['.']))
    base = defaultdict(list)
    for p in every:
        base[os.path.splitext(os.path.basename(p))[0]].append(p)
    # normalised path index, so full-path links are checked as paths, not basenames
    pathset = set(os.path.normpath(p).replace(os.sep, '/') for p in every)
    # headings of every note, for anchor checks
    heads_of = defaultdict(set)
    for p in every:
        t = FENCE.sub('', open(p, encoding='utf-8', errors='replace').read())
        key = os.path.splitext(os.path.basename(p))[0]
        for _, h in HEAD.findall(t):
            heads_of[key].add(hnorm(h))
            heads_of[os.path.splitext(os.path.normpath(p).replace(os.sep, '/'))[0]].add(hnorm(h))
    anchors, fields = [], []

    files = list(walk(scope))
    fileset = set(files)
    inbound = Counter()
    broken, empty, hollow, title, seeds = defaultdict(list), [], [], [], []

    for p in files:
        raw = open(p, encoding='utf-8', errors='replace').read()
        name = os.path.splitext(os.path.basename(p))[0]
        body = strip_code(raw)

        for m in LINK.finditer(body):
            t = m.group(1).strip().rstrip('\\')
            if not t:
                continue
            b = os.path.basename(t)
            if '/' in t:
                # Obsidian resolves a link containing a slash as a path, not a basename
                cand = os.path.normpath(t).replace(os.sep, '/')
                hit = (cand + '.md') in pathset or cand in pathset
            else:
                hit = b in base
            if hit:
                inbound[b] += 1
            else:
                broken[t].append(p)

        if SEED.search(raw):
            seeds.append(p)
            continue
        for m in FULLLINK.finditer(INLINE.sub('', FENCE.sub('', raw))):   # math kept: anchors may contain $q$
            t, a = m.group(1).strip(), m.group(2).strip().rstrip('\\').strip()
            if not t:
                t = name                                  # [[#Heading]] — same note
            a = a.split('#')[-1]
            if not a or a.startswith('^'):
                continue                                  # block reference
            key = os.path.normpath(t).replace(os.sep, '/') if '/' in t else t
            if key in heads_of and hnorm(a) not in heads_of[key]:
                anchors.append((p, '[[%s#%s]]' % (t, a)))
        nocode = FENCE.sub('', raw)
        for m in BADKEY.finditer(nocode):
            fields.append((p, 'key holds a link: %s::' % m.group(1).strip()))
        for m in ONECOLON.finditer(nocode):
            fields.append((p, 'one colon: %s:' % m.group(1)))
        for m in ODDKEY.finditer(nocode):
            fields.append((p, 'nonstandard key: %s:: (use Hard for::)' % m.group(1)))

        stripped = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.S).strip()
        if not stripped or not re.sub(r'^#+.*$', '', stripped, flags=re.M).strip():
            empty.append(p)

        heads = HEAD.findall(raw)
        text_after = re.split(HEAD, raw)[3::3] if heads else []
        levels = [len(h[0]) for h in heads]
        for i, (h, nxt) in enumerate(zip(heads, text_after)):
            if domain_of(p) in PRACTICAL:
                break
            if nxt.strip():
                continue
            # a heading with no text is fine if it has children (a deeper heading next)
            if i + 1 < len(levels) and levels[i + 1] > levels[i]:
                continue
            hollow.append((p, h[0] + ' ' + h[1].strip()))

        titles = [t.strip() for t in DEFN.findall(raw)]
        # only single-definition notes: a note defining several sub-concepts
        # legitimately has titles that differ from its filename
        if len(titles) == 1:
            a, b = norm(titles[0]), norm(name)
            if a and b and not (a == b or a in b or b in a):
                title.append((p, name, titles[0]))

    orphan = sorted(n for n, ps in base.items()
                    if any(q in fileset for q in ps)
                    and inbound[n] == 0 and 'MOC' not in n and n not in META
                    and domain_of(ps[0]) not in PRACTICAL)
    dupes = {k: v for k, v in base.items() if len(v) > 1 and 'CTF Challenges' not in k}

    want = lambda k: args.only in (None, k)
    CAP = None if args.full else 15
    def cut(seq):
        seq = list(seq)
        if CAP is None or len(seq) <= CAP:
            return seq, 0
        return seq[:CAP], len(seq) - CAP
    print('vault-lint · %d notes in scope · %d in vault\n' % (len(files), len(every)))

    if want('broken'):
        print('BROKEN LINKS (%d distinct)' % len(broken))
        shown, more = cut(sorted(broken))
        for k in shown:
            print('  [[%s]]  x%d   e.g. %s' % (k, len(broken[k]), broken[k][0]))
        if more: print('  ... and %d more' % more)
        print()
    if want('dupe'):
        print('DUPLICATE NAMES (%d)' % len(dupes))
        for k in sorted(dupes):
            print('  %s' % k)
            for q in sorted(dupes[k]):
                print('      %s' % q)
        print()
    if want('title'):
        print('CALLOUT TITLE vs FILENAME (%d)' % len(title))
        shown, more = cut(title)
        for q, n, ttl in shown:
            print('  %s   its only [!definition] says "%s"' % (q, ttl))
        if more: print('  ... and %d more' % more)
        print()
    if want('empty'):
        print('EMPTY NOTES (%d)' % len(empty))
        shown, more = cut(empty)
        for q in shown: print('  %s' % q)
        if more: print('  ... and %d more' % more)
        print()
    if want('hollow'):
        print('HOLLOW HEADINGS (%d)' % len(hollow))
        shown, more = cut(hollow)
        for q, h in shown: print('  %s   %s' % (q, h))
        if more: print('  ... and %d more' % more)
        print()
    if want('anchor'):
        print('BROKEN ANCHORS (%d)  the note exists, the heading does not' % len(anchors))
        shown, more = cut(anchors)
        for q, l in shown: print('  %s   %s' % (q, l))
        if more: print('  ... and %d more' % more)
        print()
    if want('field'):
        print('DATAVIEW FIELDS (%d)  will not be indexed' % len(fields))
        shown, more = cut(fields)
        for q, l in shown: print('  %s   %s' % (q, l))
        if more: print('  ... and %d more' % more)
        print()
    if want('seed'):
        print('SEEDS (%d)  status:: seed placeholders' % len(seeds))
        shown, more = cut(seeds)
        for q in shown: print('  %s' % q)
        if more: print('  ... and %d more' % more)
        print()
    if want('orphan'):
        print('ORPHANS (%d)' % len(orphan))
        byarea = defaultdict(list)
        for n in orphan:
            parts = base[n][0].split(os.sep)
            byarea[parts[1] if len(parts) > 2 else parts[0]].append(n)
        for area in sorted(byarea):
            print('  %-22s %d' % (area + '/', len(byarea[area])))
        print()
        shown, more = cut(orphan)
        for n in shown: print('    %-44s %s' % (n, base[n][0]))
        if more: print('    ... and %d more (--full to list)' % more)
        print()

    print('SUMMARY  broken=%d anchor=%d field=%d dupe=%d title=%d empty=%d hollow=%d orphan=%d seed=%d'
          % (len(broken), len(anchors), len(fields), len(dupes), len(title), len(empty), len(hollow), len(orphan), len(seeds)))
    print('         (orphan/hollow exclude %s)' % ', '.join(sorted(p + '/' for p in PRACTICAL)))


if __name__ == '__main__':
    main()
