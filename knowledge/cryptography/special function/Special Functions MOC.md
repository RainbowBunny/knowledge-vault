# Special Functions MOC

Index for `cryptography/special function/` — the function families cryptography is built out of, and the property vocabulary they share.

The organising idea is in [[Special Functions]]: a family $\mathbb F = \{\mathcal F\}_\lambda$ plus a set of properties. Each family below is that same object with a different subset of properties demanded — the same compositional move [[Non-Interactive Proof Systems]] makes for proof systems.

## The shared vocabulary

[[Special Functions]] defines, once:

| axis | properties |
| --- | --- |
| efficiency | efficient, compressing, extendable |
| security | collision-resistant, prefix-free, unpredictable, pseudorandom, weakly pseudorandom |

## Families

| family | demands |
| --- | --- |
| [[One-Way Functions]] | easy to compute, hard to invert |
| [[Compression Functions]] | compressing + collision-resistant — [[Inefficient Compression Function]], [[Syndrome Based Compression Function]], [[Fast Syndrome Based Compression Function]] |
| [[Hash Function]] | compressing + collision-resistant, on arbitrary-length input — [[Keccak]] |
| [[Universal Hash Function]] | a statistical, not computational, collision guarantee — [[Pairwise Independent Hash Function]] |
| [[Pseudorandom Function]] | keyed, pseudorandom — [[Puncturable Pseudorandom Function]] |
| [[Trapdoor Functions]] | one-way, invertible with a secret |
| [[Pseudorandom Generators]] | `pseudorandom generator/`; stretches a seed |

## Cross-domain

- **To [[Cryptography Foundations MOC]]** — [[Cryptographically Special Function]], [[Indistinguishability]], [[Adversary]]
- **To [[Verifiable Computing MOC]]** — collision resistance is what [[Merkle Tree]] and [[From Collision Resistance]] compile through
- **To [[Assumptions MOC]]** — [[Random Oracle Model]] idealises a hash function; [[Ideal Cipher Model]] idealises a block cipher
- **To [[Cryptanalysis MOC]]** — [[Collision Algorithms]] attack exactly the collision-resistance property

> [!todo] Housekeeping
> [[Universal Hash Function]] is empty.
> [[Special Functions]] has empty `### Prefix-Free` and `### Unpredictability` headings.
