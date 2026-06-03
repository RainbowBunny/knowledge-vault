# Cryptography MOC

Initiative-based index for `academic/knowledge/cryptography/`. Each first-level folder is an application area (a thing you'd want to *do* with crypto), not a primitive role. Hard problems and concrete attacks have their own peer folders.

## Foundations & Primitives

- [[Foundations MOC]] — security model, PRF, PRG, hash functions, cryptographic special functions
- [[Symmetric Encryption MOC]] — block / stream / classical ciphers, encryption-security definitions and constructions
- [[Message Authentication MOC]] — MACs, message integrity, authenticated encryption, authenticated data structures

## Public-Key Initiatives

- [[Public-Key Encryption MOC]] — PKE definitions, trapdoor functions, individual cryptosystems (RSA, ElGamal, …)
- [[Digital Signatures MOC]] — DSA, Schnorr-style signatures, blind signatures, Dilithium
- [[Key Exchange MOC]] — Diffie-Hellman, authenticated key exchange, Kyber KEM

## Interactive Protocols

- [[Identification MOC]] — interactive identification protocols, Σ-protocols
- [[Zero-knowledge MOC]] — interactive / non-interactive ZK, argument of knowledge, Fiat-Shamir
- [[Threshold MOC]] — distributed trust: oblivious transfer, threshold cryptography
- [[MPC MOC]] — secure multi-party computation
- [[Homomorphic Encryption MOC]] — computing on ciphertexts (stub)

## Algebra-Heavy Constructions

- [[Elliptic-Curve Cryptography MOC]] — ECC, hyperelliptic curve cryptography
- [[Post-Quantum Cryptography MOC]] — lattice-based and code-based constructions (umbrella)

## Assumptions & Attacks

- [[Hard Problems MOC]] — discrete log family, factoring (and links to lattice/coding problems)
- [[Cryptanalysis MOC]] — concrete attacks: CRIME, password cracking, collision algorithms

## Folder Layout

```
cryptography/
├── Cryptography MOC.md
├── foundations/
├── symmetric encryption/
│   ├── classical/
│   └── encryption/
├── message authentication/
├── public-key encryption/
│   └── schemes/
├── digital signatures/
├── key exchange/
├── identification protocols/
├── zero-knowledge/
├── threshold cryptography/
├── secure computation/
├── homomorphic encryption/
├── elliptic-curve cryptography/
├── post-quantum cryptography/
│   ├── lattice-based/
│   └── code-based/
├── hard problems/
│   └── dlp/
└── cryptanalysis/
```
