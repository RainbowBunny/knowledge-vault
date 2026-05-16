# Cryptography MOC

Top-level index for `academic/knowledge/cryptography/`. The folder is organized by the role each primitive plays: foundational primitives, then symmetric (secret-key) constructions, then asymmetric (public-key) constructions, then interactive protocols and the underlying hard-problem families they rely on.

## Sub-MOCs

- [[Foundations MOC]] — security model, PRFs, PRGs, hash functions
- [[Secret Key MOC]] — encryption (subfolder), block / stream ciphers, classical ciphers, MAC, AE
- [[Public Key MOC]] — PKE, signatures, key exchange, KEMs, elliptic-curve crypto, individual cryptosystems
- [[Protocols MOC]] — identification protocols (subfolder), ZK proofs
- [[Attack MOC]] — attack catalog and DLP (subfolder), collision algorithms
- [[Lattice MOC]] — LLL, LWE, SIS
- [[Coding Theory MOC]] — error-correcting codes (under `coding theory/`)

## Folder Layout

```
cryptography/
├── Cryptography MOC.md
├── foundations/
│   ├── Foundations MOC.md
│   ├── Security Model.md
│   ├── Pseudorandom Functions.md
│   ├── Pseudorandom Generators.md
│   └── Hash Functions.md
├── secret key cryptography/
│   ├── Secret Key MOC.md
│   ├── Symmetric Ciphers.md
│   ├── Vigenère cipher.md
│   ├── Block Ciphers.md
│   ├── Stream Ciphers.md
│   ├── encryption/                  (NEW subfolder — split from Encryption.md)
│   │   ├── Encryption MOC.md
│   │   ├── Encryption.md
│   │   ├── Computational Cipher.md
│   │   ├── Notions of Security.md
│   │   ├── Ideal Cipher Model and Random Oracles.md
│   │   ├── CPA Secure Cipher Construction.md
│   │   ├── Nonce-based CPA Secure Cipher.md
│   │   └── Examples.md
│   ├── Authenticated Encryption.md
│   ├── Authenticated Data Structures.md
│   └── Message Integrity.md
├── public key cryptography/
│   ├── Public Key MOC.md
│   ├── Public Key Cryptography.md
│   ├── Public Key Encryption.md
│   ├── Trapdoor Functions.md
│   ├── Key Exchange.md
│   ├── Digital Signature.md
│   ├── Digital Signature Algorithm.md
│   ├── Blind Signature.md
│   ├── Oblivious Transfer.md
│   ├── Elliptic Curve Cryptography.md     (moved from elliptic curve/)
│   ├── Hyperelliptic Curve Cryptography.md (moved from elliptic curve/)
│   ├── public key encryption/             (10 cryptosystems)
│   └── key encapsulation method/          (Diffie-Hellman, Kyber)
├── protocols/
│   ├── Protocols MOC.md
│   ├── Zero-knowledge Proof.md
│   └── identification/                    (NEW subfolder — split from Identification Protocol.md)
│       ├── Identification MOC.md
│       ├── Identification Protocol.md
│       ├── Password Protocols.md
│       ├── Security of Identification.md
│       ├── Schnorr Identification.md
│       ├── Sigma Protocols.md
│       └── ID and Signatures from Sigma.md
├── attack/
│   ├── Attack MOC.md
│   ├── Attack List.md, CRIME.md, Password Cracking.md, Random Crack.md
│   ├── Collision Algorithms.md
│   └── dlp/                               (NEW subfolder — split from Discrete Logarithm Problem.md)
│       ├── DLP MOC.md
│       ├── Discrete Logarithm Problem.md
│       ├── Baby-Step Giant-Step.md
│       ├── Pohlig-Hellman.md
│       ├── Index Calculus.md
│       ├── DLP Collision Algorithm.md
│       ├── Elliptic Curve DLP.md
│       └── Hyperelliptic Curve DLP.md
├── lattice/
│   ├── Lattice MOC.md
│   └── LLL, LWE, SIS
└── coding theory/
    ├── Coding Theory MOC.md
    ├── Coding Theory.md
    ├── Code Distance.md
    ├── Linear Code.md
    ├── Coding Theory Bounds.md
    ├── Subfield Codes.md
    └── Cyclic Codes.md
```
