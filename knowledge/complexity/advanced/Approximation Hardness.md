# Approximation Hardness

When a problem is NP-hard to *solve*, the next question is: can it at least be *approximated*? Approximation-hardness theory says when even approximation is intractable.

Stub. Topics to cover:

- **PCP theorem** (Arora-Lund-Motwani-Sudan-Szegedy 1998) — the cornerstone result. Every NP problem has a probabilistically checkable proof of polynomial length with $O(1)$-query verifier.
- **Inapproximability via PCP** — for example, 3-SAT can't be approximated to within $7/8 + \epsilon$ in polynomial time (Håstad 2001) unless P = NP.
- **Optimal hardness via [[Unique Games Conjecture]]** — UGC implies tight hardness for Max-Cut, Vertex Cover, generic CSPs.
- **Long codes and Fourier analysis** — the technical toolkit.
- **Dictator tests** and **noise stability** — proof techniques.

## Related

- [[Unique Games Conjecture]]
- [[Interactive Proofs]] — PCP descends from IP
- [[P vs NP]]
