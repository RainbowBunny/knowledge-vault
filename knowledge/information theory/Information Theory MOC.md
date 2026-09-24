# Information Theory MOC

Index for `knowledge/information theory/` — measuring information, and the codes that protect it.

Two halves that share a spine: **entropy** measures uncertainty, and **coding theory** spends redundancy to control it. Cryptography draws on both — [[Perfect Security]] is an entropy statement, and the coding assumptions in [[Assumptions MOC]] are hardness statements about decoding.

## Entropy

- [[Entropy]] — Shannon entropy, joint and conditional entropy, mutual information
- [[Asymptotic Equipartition Property]] — why typical sequences carry $\approx nH$ bits
- [[Information Theory]] — perfect secrecy, key equivocation, and the $\#\mathcal K \geq \#\mathcal M$ bound

## Coding theory

`coding theory/`

- [[Coding Theory]] — codes, codewords, encoding and decoding
- [[Linear Code]] — generator and parity-check matrices, syndromes
- [[Code Distance]] — Hamming distance, minimum distance, error detection and correction. Generalises to an arbitrary norm $\omega$ — see the [[Math Properties MOC|norm axioms]]
- [[Code Properties]]
- [[Coding Theory Bounds]] — Singleton, Hamming, Gilbert-Varshamov
- [[Cyclic Codes]] — the ideal-theoretic view; see [[Ring]] on $\mathbb F_q[x]/(x^n - 1)$
- [[New Codes from Old]] — puncturing, shortening, extending
- [[Subfield Codes]]

### Concrete codes

`coding theory/code/`

- [[Hamming Codes]] · [[Golay Codes]] · [[Reed-Muller]] · [[Reed-Solomon]] · [[Ambiguous Coding]]

### Weight and distance

`coding theory/weight/`

- [[Hamming Weight]] · [[Hamming Distance]] · [[Hamming Sphere]] · [[Regular Word]]

### Rank metric

`coding theory/rank-metric/`

- [[Rank Metric Codes]] — distance measured by rank rather than Hamming weight
- [[Gabidulin Vector Codes]] · [[Delsarte Matrix Codes]] · [[Dual Bases Codes]]

### Schemes built on these codes

These live in `cryptography/primitive/`: [[Hamming Quasi-Cyclic]] (KEM), [[Hamming Quasi Cyclic SKE]] and [[Additively-Homomorphic Encryption]] (symmetric).

## Cross-domain

| to | why |
| --- | --- |
| [[Assumptions MOC]] | [[Syndrome Decoding Assumption]], [[Rank Syndrome Decoding Assumption]], [[Quasi-Cyclic Syndrome Decoding Assumption]], [[Rank Support Learning Assumption]] are the hardness side of these codes |
| [[Symmetric Encryption MOC]] | [[Perfect Security]] and the [[One-time Pad]] are entropy arguments; [[Hamming Quasi Cyclic SKE]] is code-based |
| [[Probability MOC]] | [[Random Variables]], [[Expectation]], [[Statistical Distance]] |
| [[Algebra MOC]] | [[Field]] — every code here is over $\mathbb F_q$; [[Ring]] for cyclic codes; [[Matrix]] for generator matrices |
| [[Math Properties MOC]] | the norm axioms that [[Code Distance]] generalises over |
| [[Complexity MOC]] | decoding is NP-hard — see [[Hardness and Completeness|NP-hard]] |

> [!remark] Where code-based cryptography lives
> The *codes* are here; the *cryptographic hardness assumptions* built on them are in `cryptography/assumptions/code-based/`, and the *schemes* are in `cryptography/primitive/`. Same rule [[Algebra MOC]] uses for lattices: the mathematical object lives in its home discipline, the hardness assumption in `cryptography/assumptions/`, the scheme with its primitive.
