# Assumptions MOC

Security assumptions — the things crypto reductions actually depend on. Split by *kind* of assumption:

- **Hardness assumptions** — "this computational problem is intractable." Organized by algebraic family.
- **Idealized models** — "we pretend our hash / cipher / group is ideal in the proof." Proof-technique conventions, not computational problems.

Algorithms that *attack* the hardness assumptions live alongside the assumption (BSGS, Pohlig-Hellman, Index Calculus are filed under DLP, not under cryptanalysis). Attacks on deployed protocols (CRIME, password cracking) live in [[Cryptanalysis MOC]] instead.

## Hardness Assumptions

### Discrete Logarithm Family (`dlp/`)

- [[Discrete Logarithm Problem]] — definition over generic groups
- [[Baby-Step Giant-Step]]
- [[Pohlig-Hellman]]
- [[Index Calculus]]
- [[DLP Collision Algorithm]]
- [[Elliptic Curve DLP]]
- [[Hyperelliptic Curve DLP]]

### Lattice (`lattice-based/`)

- [[Learning With Error]] — LWE / Ring-LWE
- [[Short Integer Solution Problem]] — SIS

### Stubs (planned)

- Factoring (integer factoring, RSA problem, quadratic residuosity, strong RSA)
- CDH / DDH variants of DLP
- Pairing assumptions (BDH, q-SDH, LRSW)
- Coding-theory assumptions (syndrome decoding, McEliece)

## Idealized Models (`idealized models/`)

- [[Ideal Cipher Model]] — ICM (ideal block / permutation), ROM
- Stubs: Generic Group Model (GGM), Algebraic Group Model (AGM), Common Reference String (CRS)

## Related

- [[Post-Quantum Cryptography MOC]] — schemes built *on* lattice / coding assumptions; the math (lattices, codes) lives there too
- [[Cryptanalysis MOC]] — concrete attacks on deployed protocols (CRIME, …), as opposed to attacks on the underlying assumptions
- [[knowledge/cs/foundations/Foundations MOC]] — security definitions and games (these are *what* we prove, not *what* we assume)
