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

- [[Special Functions MOC]] — `special functions/`: the shared property vocabulary (efficient, compressing, extendable, collision-resistant, pseudorandom) and the families that instantiate it — [[One-Way Functions]], [[Hash Functions]], [[Pseudorandom Functions]], [[Trapdoor Functions]], [[Compression Functions]]
- [[Pseudorandom Generators]] — `pseudorandom/`

## Protocols and initiatives

- [[Identification MOC]] — [[Identification Protocol]], [[Schnorr Identification]], [[Security of Identification]], [[Password Protocols]]
- [[Verifiable Computing MOC]] — **`verifiable computing/`**: proof systems, R1CS and arithmetization, commitments, SNARKs. The largest and most active area in this folder
- [[Threshold MOC]] — [[Threshold Cryptography]], [[Oblivious Transfer]], [[Threshold Secret-Sharing]], [[Shamir Secret Sharing]]
- [[MPC MOC]] — [[Secure Multi-party Computation]]

## Algebra-heavy constructions

- [[Elliptic-Curve Cryptography MOC]] — [[Elliptic Curve Cryptography]], [[Hyperelliptic Curve Cryptography]]
- [[Post-Quantum Cryptography MOC]] — [[Lattice]], [[LLL Lattice Reduction Algorithm]]; code-based material lives in `information theory/code-based/`, see [[Information Theory MOC]]

## Assumptions and attacks

- [[Assumptions MOC]] — [[Discrete-Logarithm Assumption]]; lattice-based ([[Learning With Error]], [[Short Integer Solution]], [[Shortest Vector Problem]], [[Vanishing SIS]]); coding-based ([[Syndrome Decoding]], [[Rank Syndrome Decoding]]); idealized models ([[Random Oracle Model]], [[Ideal Cipher Model]], [[Uniform Random String Model]])
- [[Cryptanalysis MOC]] — [[Attack List]], [[Collision Algorithms]], [[Password Cracking]], [[CRIME]]

## Folder layout

```
cryptography/
├── Cryptography MOC.md
├── foundations/
│   └── generic helper/
├── primitive/
│   ├── symmetric encryption/     (classical/, schemes/)
│   ├── public-key encryption/    (schemes/)
│   ├── digital signatures/       (schemes/)
│   ├── key establishment/        (key exchange/, kem/schemes/)
│   ├── message authentication/
│   └── linear-only vector encryption/  (scheme/)
├── special functions/
│   ├── one-way functions/    hash functions/    (schemes/)
│   ├── pseudorandom functions/  (schemes/)
│   ├── compression functions/   (schemes/)
│   └── trapdoor functions/
├── pseudorandom/generators/
├── identification protocols/
├── verifiable computing/
│   ├── relations/        (r1cs/, arithmetization/)
│   ├── proof/            (interactive/, non-interactive/, oracle/, properties/, variants/, scheme/)
│   ├── commitment/       (scheme/)
│   ├── encoding scheme/  (scheme/)
│   └── secure computation/
├── threshold cryptography/  (secret sharing/schemes/)
├── elliptic-curve cryptography/
├── post-quantum cryptography/  (lattice-based/)
├── assumptions/         (lattice-based/, coding-based/, idealized models/)
└── cryptanalysis/
```

## Cross-domain

- **To [[Complexity MOC]]** — "PPT adversary" is [[Randomized Complexity]]; [[Assumptions MOC]] plays the role of [[Conjectures MOC]]; [[Interactive Proofs]] underpins [[Verifiable Computing MOC]]
- **To [[Algebra MOC]]** — [[Field]], [[Lattices]], [[Bilinear Pairings]], [[Polynomial]]
- **To [[Information Theory MOC]]** — [[Entropy]] behind [[Perfect Security]]; `code-based/` behind the coding assumptions
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
