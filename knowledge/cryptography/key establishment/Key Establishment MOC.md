# Key Establishment MOC

Establishing a shared secret between parties. Two protocol shapes share this umbrella:

- **Interactive key exchange** — both parties send messages; Diffie-Hellman is the canonical example.
- **Key Encapsulation Mechanism (KEM)** — one-shot: the sender encapsulates a random key under the receiver's public key; the receiver decapsulates. Non-interactive, and the standard PQ-era shape.

## Key Exchange (`key exchange/`)

- [[Key Exchange]] — security definitions for interactive KE
- [[Authenticated Key Exchange]] — AKE, identity binding, MITM resistance
- [[Diffie-Hellman Key Exchange]] — DH / ECDH

## Key Encapsulation (`kem/`)

- [[Kyber KEM]] — lattice-based KEM (NIST PQC standard)

## Related

- For digital signatures used to authenticate AKE, see [[Digital Signatures MOC]].
- For the underlying hardness, see [[Assumptions MOC]] (DLP) and [[Post-Quantum Cryptography MOC]] (lattice).
- Hybrid PKE (KEM-DEM construction) — when added, lives under [[Public-Key Encryption MOC|public-key encryption]] since the *output* is a PKE scheme.
