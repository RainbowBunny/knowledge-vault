# Average-Case Complexity

Worst-case hardness can mask the fact that most instances are easy. Average-case complexity studies hardness over input distributions.

Stub. Topics to cover:

- **distNP** — Levin's framework for distributional NP problems.
- **distNP-completeness** — Levin's completeness theory.
- **Average-case vs. worst-case reductions** — when worst-case hardness implies average-case hardness.
- **Cryptographic significance** — pseudorandom generators and one-way functions essentially *require* average-case hardness.

## Cross-Reference to Cryptography

Cryptographic hardness assumptions like [[Learning With Error Problem|LWE]] and [[Discrete Logarithm Problem|DLP]] are *average-case* hardness assumptions (the problem is hard for a random instance, not just some worst-case instance). The lattice reductions (Regev, Langlois-Stehlé) prove average-case M-LWE hardness from *worst-case* lattice problems — a major win.

## Related

- [[P vs NP]] — worst-case version
- [[Derandomization Conjecture]] — average-case hardness powers derandomization
- Cryptographic assumptions in `cryptography/assumptions/`
