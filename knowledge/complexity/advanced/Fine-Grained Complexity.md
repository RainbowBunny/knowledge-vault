# Fine-Grained Complexity

Within polynomial time, *how* polynomial? Fine-grained complexity proves conditional lower bounds — e.g., "no $O(n^{2 - \epsilon})$ algorithm exists for problem X" assuming [[Exponential Time Hypothesis|SETH]].

Stub. Topics to cover:

- **Core problems** — All-Pairs Shortest Paths (APSP), Orthogonal Vectors (OV), Edit Distance, 3-SUM.
- **Lower bounds under SETH** — most central conditional bounds use SETH.
- **Equivalences** — many seemingly-different problems are "fine-grained equivalent" (a reduction in both directions, costing only $\text{polylog}$ in time).
- **Beyond SETH** — 3-SUM hypothesis, BMM hypothesis, k-clique hypothesis.

## Related

- [[Exponential Time Hypothesis]] — the conjecture that powers most fine-grained lower bounds
- [[Time Complexity]] — the polynomial-time setting
- [[Parameterized Complexity]] — related "refined" view of complexity
