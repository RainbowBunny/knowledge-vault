# Information Theory MOC

Index for `knowledge/information theory/` — measuring information, and the codes that protect it.

Two halves that share a spine: **entropy** measures uncertainty, and **coding theory** spends redundancy to control it. Cryptography draws on both — [[Perfect Security]] is an entropy statement, and the coding assumptions in [[Assumptions MOC]] are hardness statements about decoding.

## Entropy

- [[Entropy]] — Shannon entropy, joint and conditional entropy, mutual information
- [[Asymptotic Equipartition Property]] — why typical sequences carry $\approx nH$ bits
- [[Information Theory]] — perfect secrecy, key equivocation, and the $\#\mathcal K \geq \#\mathcal M$ bound

## Coding theory

`code-based/`

- [[Coding Theory]] — codes, codewords, encoding and decoding
- [[Linear Code]] — generator and parity-check matrices, syndromes
- [[Code Distance]] — Hamming distance, minimum distance, error detection and correction. Generalises to an arbitrary norm $\omega$ — see the [[Math Properties MOC|norm axioms]]
- [[Code Properties]]
- [[Coding Theory Bounds]] — Singleton, Hamming, Gilbert-Varshamov
- [[Cyclic Codes]] — the ideal-theoretic view; see [[Ring]] on $\mathbb F_q[x]/(x^n - 1)$
- [[New Codes from Old]] — puncturing, shortening, extending
- [[Subfield Codes]]

### Concrete codes

`code-based/schemes/`

- [[Hamming Codes]] · [[Golay Codes]] · [[Reed-Muller]] · [[Hamming Quasi-Cyclic]]

### Rank metric

`code-based/rank-metric/`

- [[Rank Metric Codes]] — distance measured by rank rather than Hamming weight
- [[Gabidulin Vector Codes]] · [[Delsarte Matrix Codes]] · [[Dual Bases Codes]]
- [[Additively-Homomorphic Encryption]]

## Cross-domain

| to | why |
| --- | --- |
| [[Assumptions MOC]] | [[Syndrome Decoding]], [[Rank Syndrome Decoding]], [[Quasi-Cyclic Syndrome Decoding]], [[Rank Support Learning Problem]] are the hardness side of these codes |
| [[Symmetric Encryption MOC]] | [[Perfect Security]] and the [[One-time Pad]] are entropy arguments; [[Hamming Quasi Cyclic SKE]] is code-based |
| [[Probability MOC]] | [[Random Variables]], [[Expectation]], [[Statistical Distance]] |
| [[Algebra MOC]] | [[Field]] — every code here is over $\mathbb F_q$; [[Ring]] for cyclic codes; [[Matrix]] for generator matrices |
| [[Math Properties MOC]] | the norm axioms that [[Code Distance]] generalises over |
| [[Complexity MOC]] | decoding is NP-hard — see [[Class NP-hard]] |

> [!remark] Where code-based cryptography lives
> The *codes* are here; the *cryptographic hardness assumptions* built on them are in `cryptography/assumptions/coding-based/`, and the *schemes* are split between `code-based/schemes/` here and `cryptography/primitive/`. If that split starts costing you, the rule to apply is the same one [[Algebra MOC]] uses for lattices: the mathematical object lives in its home discipline, the hardness assumption lives in `cryptography/assumptions/`.
