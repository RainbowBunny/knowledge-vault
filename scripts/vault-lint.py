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

Links inside fenced or inline code are ignored, matching the vault's
convention that not-yet-existing notes are written in `code`.
No dependencies beyond the standard library.
"""
import os, re, sys, argparse
from collections import Counter, defaultdict

SKIP_DIRS = {'.git', '.obsidian', '.trash', 'node_modules', '_to_delete'}
DEFAULT_SCOPE = ['knowledge']
META = {'North Star', 'Vault Refactoring Plan', 'Foundation Layer'}

FENCE = re.compile(r'```.*?```', re.S)
INLINE = re.compile(r'`[^`\n]*`')
LINK = re.compile(r'\[\[([^\]\|#]*)')
DEFN = re.compile(r'>\s*\[!definition\]\s*(.+)')
HEAD = re.compile(r'^(#{1,6})\s+(.*)$', re.M)


def strip_code(text):
    return INLINE.sub('', FENCE.sub('', text))


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
    ap.add_argument('--only', default=None, help='broken|dupe|orphan|title|empty|hollow')
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

    files = list(walk(scope))
    fileset = set(files)
    inbound = Counter()
    broken, empty, hollow, title = defaultdict(list), [], [], []

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

        stripped = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.S).strip()
        if not stripped or not re.sub(r'^#+.*$', '', stripped, flags=re.M).strip():
            empty.append(p)

        heads = HEAD.findall(raw)
        text_after = re.split(HEAD, raw)[3::3] if heads else []
        levels = [len(h[0]) for h in heads]
        for i, (h, nxt) in enumerate(zip(heads, text_after)):
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
                    and inbound[n] == 0 and 'MOC' not in n and n not in META)
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

    print('SUMMARY  broken=%d dupe=%d title=%d empty=%d hollow=%d orphan=%d'
          % (len(broken), len(dupes), len(title), len(empty), len(hollow), len(orphan)))


if __name__ == '__main__':
    main()
