# Cryptography MOC

Index for `knowledge/cryptography/`. Organised by **what you are trying to do**: `primitive/` holds the building blocks, the peer folders hold application areas, and hard problems and concrete attacks sit in their own folders as the leaves of the proof DAG.

Structurally parallel to [[Complexity MOC]]: foundations + initiative folders + an `assumptions/` folder playing the role complexity's `conjectures/` plays.

## Foundations

- [[Cryptography Foundations MOC]] — [[Security Model]], [[Adversary]], [[Indistinguishability]], [[Cryptographically Special Function]], [[Elementary Wrapper]]

## Primitives

`primitive/` — the building blocks, each with its own MOC.

- [[Symmetric Encryption MOC]] — [[Block Ciphers]], [[Stream Ciphers]], [[Perfect Security]], classical ciphers, schemes
- [[Public-Key Encryption MOC]] — [[Public-Key Encryption]], [[Fujisaki-Okamoto Transformation]], and the cryptosystems (RSA, ElGamal, NTRU, GGH, Kyber, …)
- [[Digital Signatures MOC]] — [[Old Digital Signature]], [[Digital Signature Algorithm]], [[Blind Signature]], [[ID and Signatures from Sigma]], [[Dilithium]]
- [[Key Establishment MOC]] — [[Key Exchange]], [[Diffie-Hellman Key Exchange]], [[Authenticated Key Exchange]], [[Key Encapsulation Mechanism]], [[Kyber KEM]]
- [[Message Authentication MOC]] — [[Message Integrity]], [[Authenticated Encryption]], [[Authenticated Data Structures]]
- [[Linear-Only Vector Encryption]] — [[Module HGSW]]; the primitive behind [[LUNA]]

## Function families

- [[Special Functions MOC]] — `special function/`: the shared property vocabulary (efficient, compressing, extendable, collision-resistant, pseudorandom) and the families that instantiate it — [[One-Way Functions]], [[Hash Function]], [[Pseudorandom Function]], [[Trapdoor Functions]], [[Compression Functions]]
- [[Pseudorandom Generators]] — `special function/pseudorandom generator/`

## Protocols and initiatives

- [[Identification MOC]] — [[Identification Protocol]], [[Schnorr Identification]], [[Security of Identification]], [[Password Protocols]]
- [[Verifiable Computing MOC]] — **`verifiable computing/`**: proof systems, R1CS and arithmetization, commitments, SNARKs. The largest and most active area in this folder
- [[Threshold MOC]] — [[Threshold Cryptography]], [[Threshold Secret-Sharing]], [[Shamir Secret Sharing]]
- [[MPC MOC]] — **`secure computation/`**: [[Secure Multi-party Computation]], [[Oblivious Transfer]], [[Private Information Retrieval]]

## Families — `family/`

- [[Elliptic-Curve Cryptography MOC]] — [[Elliptic Curve Cryptography]], [[Hyperelliptic Curve Cryptography]]
- [[Post-Quantum Cryptography MOC]] — [[Lattice Trapdoor]], [[LLL Lattice Reduction Algorithm]]; the codes live in `information theory/coding theory/`, see [[Information Theory MOC]]

## Assumptions and attacks

- [[Assumptions MOC]] — [[Discrete-Logarithm Assumption]]; lattice-based ([[Learning With Error]], [[Short Integer Solution]], [[Vanishing SIS]]); code-based ([[Syndrome Decoding Assumption]], [[Rank Syndrome Decoding Assumption]]); idealized models ([[Random Oracle Model]], [[Ideal Cipher Model]], [[Uniform Random String Model]])
- [[Cryptanalysis MOC]] — attacks on hard problems (`dlp/`: [[Baby-Step Giant-Step]], [[Pohlig-Hellman]], [[Index Calculus]]; [[Collision Algorithms]]) and on deployed systems ([[Attack List]], [[Password Cracking]], [[CRIME]])

## Folder layout

```
cryptography/
├── Cryptography MOC.md
├── foundations/             (generic helper/)
├── primitive/
│   ├── symmetric encryption/     (classical/, scheme/)
│   ├── public-key encryption/    (scheme/)
│   ├── digital signatures/       (scheme/)
│   ├── key establishment/        (key exchange/, kem/scheme/)
│   ├── message authentication/
│   └── linear-only vector encryption/  (scheme/)
├── special function/
│   ├── one-way function/    hash function/  (scheme/)
│   ├── pseudorandom function/    pseudorandom generator/
│   ├── compression function/     (scheme/)
│   └── trapdoor function/
├── identification protocol/
├── verifiable computing/
│   ├── relation/         (r1cs/, arithmetization/)
│   ├── proof system/     (interactive/, oracle/, variant/, scheme/)
│   ├── compiler/
│   ├── commitment/       (scheme/)
│   ├── encoding scheme/  (scheme/)
│   ├── argument/         (interactive/, non-interactive/)
│   └── property/
├── secure computation/   (property/)
├── threshold cryptography/  (secret sharing/scheme/)
├── family/               hubs for families that cut across kinds (elliptic-curve, post-quantum)
├── assumptions/          (lattice-based/, code-based/, idealized models/)
└── cryptanalysis/        (dlp/)
```

## Cross-domain

- **To [[Complexity MOC]]** — "PPT adversary" is [[Randomized Complexity]]; [[Assumptions MOC]] plays the role of [[Conjectures MOC]]; [[Class IP|Interactive Proofs]] underpins [[Verifiable Computing MOC]]
- **To [[Algebra MOC]]** — [[Field]], [[Lattices]], [[Bilinear Pairings]], [[Polynomial]]
- **To [[Information Theory MOC]]** — [[Entropy]] behind [[Perfect Security]]; `coding theory/` behind the code-based assumptions
- **To [[Math Properties MOC]]** — the norm axioms behind lattice and rank-metric distance

## Callout conventions

| Callout | Use |
| --- | --- |
| `[!definition]` | Syntax of a scheme, a property, a hard problem |
| `[!theorem]` / `[!lemma]` | Reductions, security proofs |
| `[!remark]` | Cross-references, naming, intuition |
| `[!example]` | Concrete instantiations |
| `[!algorithm]` | Algorithm / protocol specifications |

Security properties are written as **advantage games** — see [[Soundness]] and [[Zero Knowledge]] for the house style.
