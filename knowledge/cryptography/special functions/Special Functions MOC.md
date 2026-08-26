# Special Functions MOC

Index for `cryptography/special functions/` — the function families cryptography is built out of, and the property vocabulary they share.

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
| [[Compression Functions]] | compressing + collision-resistant — [[Inefficient Compression Function]] |
| [[Hash Functions]] | compressing + collision-resistant, on arbitrary-length input — [[Keccak]] |
| [[Universal Hash Functions]] | a statistical, not computational, collision guarantee |
| [[Pseudorandom Functions]] | keyed, pseudorandom — [[Puncturable Pseudorandom Function]] |
| [[Trapdoor Functions]] | one-way, invertible with a secret |
| [[Pseudorandom Generators]] | `pseudorandom/`; stretches a seed |

## Cross-domain

- **To [[Cryptography Foundations MOC]]** — [[Cryptographically Special Function]], [[Indistinguishability]], [[Adversary]]
- **To [[Verifiable Computing MOC]]** — collision resistance is what [[Merkle Tree]] and [[From Collision Resistance]] compile through
- **To [[Assumptions MOC]]** — [[Random Oracle Model]] idealises a hash function; [[Ideal Cipher Model]] idealises a block cipher
- **To [[Cryptanalysis MOC]]** — [[Collision Algorithms]] attack exactly the collision-resistance property

> [!todo] Housekeeping
> `pseudorandom functions/Pseudorandom Functionsss.md` is a typo'd duplicate of [[Pseudorandom Functions]] — merge or delete.
> [[Universal Hash Functions]] is empty.
> [[Special Functions]] has empty `### Prefix-Free` and `### Unpredictability` headings.
