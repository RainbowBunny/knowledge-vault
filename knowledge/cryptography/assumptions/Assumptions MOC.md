# Assumptions MOC

Security assumptions — the things crypto reductions actually depend on. Split by *kind* of assumption:

- **Hardness assumptions** — "this problem is intractable *on average*, for instances drawn from this distribution." Organized by algebraic family.
- **Idealized models** — "we pretend our hash / cipher / group is ideal in the proof." Proof-technique conventions, not computational problems.

An assumption names the worst-case problem it averages over with `Requires::`. The problems themselves are stated once in `complexity/problem/` (see [[Complexity MOC]]), and the algorithms that attack them live in `cryptanalysis/` (see [[Cryptanalysis MOC]]).

- [[Assumption Taxonomy]] — how the families relate

## Hardness Assumptions

### Discrete logarithm

- [[Discrete-Logarithm Assumption]] — over [[Discrete Logarithm Problem]]; the elliptic and hyperelliptic instances are [[Elliptic Curve DLP]] and [[Hyperelliptic Curve DLP]]

### Lattice (`lattice-based/`)

- LWE family (`LWE/`): [[Learning With Error]] · [[Module Learning With Error]] · [[Short Secret Learning With Error]]
- SIS family (`SIS/`): [[Short Integer Solution Problem]] · [[Short Integer Solution]] · [[Normal Form Short Integer Solution]] · [[Vanishing SIS]]
- worst-case problems they reduce from: [[Shortest Vector Problem]], [[Closest Vector Problem]], [[Shortest Basis Problem]] (`complexity/problem/lattice/`)

### Code-based (`code-based/`)

- [[Syndrome Decoding Assumption]] · [[Regular Syndrome Decoding Assumption]] · [[Quasi-Cyclic Syndrome Decoding Assumption]]
- rank metric: [[Rank Syndrome Decoding Assumption]] · [[Ideal Rank Syndrome Decoding Assumption]] · [[Rank Support Learning Assumption]]
- worst-case problems: [[Syndrome Decoding Problem]], [[Regular Syndrome Decoding Problem]] (`complexity/problem/code/`)

### Stubs (planned)

- Factoring (RSA problem, quadratic residuosity, strong RSA) — over [[Factoring]]
- CDH / DDH — DDH currently sits as a section inside [[Discrete Logarithm Problem]]
- Pairing assumptions (BDH, q-SDH, LRSW)

## Idealized Models (`idealized models/`)

- [[Random Oracle Model]] · [[Ideal Cipher Model]] · [[Uniform Random String Model]]
- Stubs: Generic Group Model (GGM), Algebraic Group Model (AGM), Common Reference String (CRS)

## Related

- [[Post-Quantum Cryptography MOC]] — schemes built *on* lattice and code-based assumptions
- [[Cryptanalysis MOC]] — attacks, on assumptions (`dlp/`) and on deployed protocols
- [[Cryptography Foundations MOC]] — security definitions and games (*what* we prove, not *what* we assume)
