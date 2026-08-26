# Post-Quantum Cryptography MOC

Constructions believed to resist quantum adversaries. Organized by the hardness family they rely on.

## Lattice-Based (`lattice-based/`)

- [[knowledge/cryptography/post-quantum cryptography/lattice-based/Lattice]] — definitions, bases, trapdoors
- [[LLL Lattice Reduction Algorithm]]
- For the underlying hardness assumptions ([[Learning With Error|LWE]], [[Short Integer Solution Problem|SIS]]), see [[Assumptions MOC|assumptions]].

## Code-Based (`code-based/`)

- [[Coding Theory]] — fundamentals: channels, decoding rules
- [[Code Distance]] — distance, error detection / correction
- [[Linear Code]] — generator / parity-check matrices, syndrome decoding
- [[Code Properties]] — composable structural properties: systematic, cyclic / quasi-cyclic, duality axes
- [[Cyclic Codes]] — generator polynomial theory, BCH, Reed–Solomon
- [[Reed-Muller]] — the RM family
- [[Subfield Codes]] — concatenated / subfield / trace constructions
- [[Coding Theory Bounds]]
- [[Hamming Quasi-Cyclic]] (`schemes/`) — NIST's backup KEM, composing systematic + quasi-cyclic

## Concrete PQ Schemes Living Elsewhere

- [[Kyber KEM]] (under [[Key Establishment MOC|key establishment]]) — lattice KEM
- [[Dilithium]] (under [[Digital Signatures MOC|digital signatures]]) — lattice signature
- [[NTRU Public Key Cryptosystem]] / [[GGH Public Key Cryptosystem]] / [[Lindner-Peikert Public Key Encryption]] (under [[Public-Key Encryption MOC|PKE schemes]])

## Stubs (planned)

- Hash-based signatures — XMSS, SPHINCS+
- Isogeny-based — SIDH, CSIDH
- Multivariate

## Related

- [[Assumptions MOC]] — the hardness assumptions (LWE / SIS / syndrome decoding) live there; this folder is for the math and the schemes built on top.
