---
aliases: [p-adic Numbers, p-adic Integers, p-adic Absolute Value]
---
Reference:
- `[Sto]` — M. Stoll, _p-adic Analysis in Arithmetic Geometry_, lecture notes, Bayreuth, WS 2015/16: https://mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf
- `[Ev]` — Leiden course notes on Diophantine approximation, Chapter 8 _P-adic numbers_ (on J.-H. Evertse's page; the PDF names no author): https://pub.math.leidenuniv.nl/~evertsejh/dio14-8.pdf
- `[Sut]` — A. V. Sutherland, MIT 18.785 _Number Theory I_, Lecture 8 _Complete fields and valuation rings_ and Lecture 9 _Local fields and Hensel's lemmas_: https://math.mit.edu/classes/18.785/2025/LectureNotes8.pdf, https://math.mit.edu/classes/18.785/2025/LectureNotes9.pdf
- `[ConO]` — K. Conrad, _Ostrowski's theorem for Q_: https://kconrad.math.uconn.edu/blurbs/gradnumthy/ostrowskiQ.pdf

## Definition

> [!definition] Parameters
> - $p$: a [[Prime]].
> - $K$: a field; an **absolute value** on $K$ is a function $|\cdot|: K \to \mathbb R_{\geq 0}$ with $|x| = 0 \iff x = 0$, $|xy| = |x| \cdot |y|$ and $|x + y| \leq |x| + |y|$; it is **non-archimedean** (ultrametric) if moreover $|x + y| \leq \max\{|x|, |y|\}$ `[Sto Def 2.1]`.

> [!definition] p-adic Valuation
> For an integer $a \neq 0$, $v_p(a) = \max\{n \in \mathbb Z_{\geq 0} : p^n \mid a\}$; for $a = r/s \in \mathbb Q^\times$, $v_p(a) = v_p(r) - v_p(s)$ `[Sto Def 2.5]`. On integers this is $\mathrm{ord}_p$ of [[Prime#Unique Factorization and Order]].

> [!definition] p-adic Absolute Value
> $|x|_p = p^{-v_p(x)}$ for $x \neq 0$, and $|0|_p = 0$ `[Sto Def 2.5]`. Equivalently: write $x = p^m b / c$ with integers $b, c$ not divisible by $p$, and put $|x|_p = p^{-m}$ `[Ev §8.1]`.

> [!definition] p-adic Number
> The **field of $p$-adic numbers** $\mathbb Q_p$ is the completion of $\mathbb Q$ with respect to $|\cdot|_p$ `[Sto Def 2.9; Ev §8.3]`, and $|\cdot|_p$ extends to it. Here, for a field with an absolute value, the metric is $d(x, y) = |x - y|$ `[Sto §2]`, and the completion is the set of Cauchy sequences up to equivalence, with $d([(x_n)], [(y_n)]) = \lim d(x_n, y_n)$ and $x \mapsto [(x, x, \dots)]$ embedding the original space `[Sut Def 8.3]`; a sequence is Cauchy if $d(x_m, x_n) < \epsilon$ for all $m, n \geq N$, and a space is complete if every Cauchy sequence converges `[Sut Def 8.1]`.

> [!definition] p-adic Integer
> $\mathbb Z_p = \{x \in \mathbb Q_p : |x|_p \leq 1\}$, the **ring of $p$-adic integers** `[Ev §8.3]`.

## Property

### Absolute value

> [!proposition] $|\cdot|_p$ is a non-archimedean absolute value on $\mathbb Q$ — $|x + y|_p \leq \max(|x|_p, |y|_p)$
> `[Sto Lemma 2.6]`. Multiplicativity follows from $v_p(ab) = v_p(a) + v_p(b)$, a consequence of unique factorisation, and the ultrametric inequality from $v_p(a + b) \geq \min\{v_p(a), v_p(b)\}$ `[Sto, proof of Lemma 2.6]` — the properties of $\mathrm{ord}_p$ in [[Prime#Unique Factorization and Order]].

> [!theorem] Ostrowski's theorem — $\mathbb R$ and the $\mathbb Q_p$ are all the completions of $\mathbb Q$
> Every nontrivial absolute value on $\mathbb Q$ is equivalent to the ordinary absolute value or to $|\cdot|_p$ for some prime $p$ `[Ev Thm 8.1]`; precisely, $|\cdot| = |\cdot|_\infty^t$ or $|\cdot| = |\cdot|_p^t$ for some $t > 0$ `[ConO Thm 1]`. So every completion of $\mathbb Q$ with respect to a nontrivial absolute value is $\mathbb R$ or some $\mathbb Q_p$ `[ConO §1]`. Two absolute values are equivalent if $|x|_2 = |x|_1^\alpha$ for some $\alpha > 0$ `[Ev §8.1]`.

### The ring $\mathbb Z_p$

> [!proposition] $\mathbb Z_p$ is a subring
> If $x, y \in \mathbb Z_p$ then $|x - y|_p \leq \max(|x|_p, |y|_p) \leq 1$, and $|xy|_p \leq 1$; so $\mathbb Z_p$ is a ring `[Ev §8.3]`. In general $\{x \in K : |x| \leq 1\}$ is a subring for any non-archimedean absolute value `[Sto Lemma 2.2]`.

### Units

> [!proposition] Units of $\mathbb Z_p$ — exactly the elements of absolute value $1$
> $\mathbb Z_p^\times = \{x \in \mathbb Q_p : |x|_p = 1\}$ `[Ev §8.3]`. Here $\mathbb Z_p^\times$ is the group of units, the invertible elements of the ring.

### Ideals and residue field

> [!theorem] Ideals of $\mathbb Z_p$ — $\mathbb Z_p / p\mathbb Z_p \cong \mathbb F_p$
> The nonzero ideals of $\mathbb Z_p$ are $p^m \mathbb Z_p$, $m = 0, 1, 2, \dots$, and $\mathbb Z_p / p^m \mathbb Z_p \cong \mathbb Z / p^m \mathbb Z$. In particular $\mathbb Z_p / p\mathbb Z_p \cong \mathbb F_p$. `[Ev Thm 8.6]`

### Topology

> [!theorem] Topology of $\mathbb Q_p$ — compact open balls, locally compact, totally disconnected
> - Every closed ball $B(a, p^{-m}) = \{x : |x - a|_p \leq p^{-m}\}$ is both open and compact `[Ev Thm 8.11]`. In particular $\mathbb Z_p$ is compact, so $\mathbb Q_p$ is locally compact `[Sto Thm 2.11]`.
> - Since $|x|_p$ takes a discrete set of values, $\mathbb Z_p = \{|x|_p \leq 1\} = \{|x|_p < p\}$ is closed and open, and any two distinct points have disjoint open neighbourhoods covering $\mathbb Q_p$: $\mathbb Q_p$ is totally disconnected `[Sto p. 6]`.
>
> The terms are those of [[Topological Space]].

> [!remark] Notation clash
> In this note $\mathbb Z_p$ is the ring of $p$-adic integers. In the cryptography notes of this vault $\mathbb Z_p$ means $\mathbb Z / p\mathbb Z$, which here is $\mathbb Z_p / p\mathbb Z_p = \mathbb F_p$.

## Related

### Used by
- [[Hecke Algebra]] — $\mathrm{GL}_n(\mathbb Q_p)$, its maximal compact subgroup $\mathrm{GL}_n(\mathbb Z_p)$, and the reduction to $\mathrm{GL}_n(\mathbb F_p)$

### Prerequisites
- [[Prime]], [[Metric Space]], [[Topological Space]]
