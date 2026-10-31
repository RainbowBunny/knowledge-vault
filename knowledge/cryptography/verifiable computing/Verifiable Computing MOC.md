# Verifiable Computing MOC

Index for `cryptography/verifiable computing/` — proving that a computation was done correctly, to a verifier who will not redo it.

Organised by the **compilation chain**, because that is what the folder actually is: a statement is expressed as a relation, the relation is arithmetized, an information-theoretic proof system is built for it, and cryptography compiles that into a real argument.

```
relation  →  arithmetization  →  IT proof system  →  compiler  →  argument
 R1CS         QAP / QSP / SSP     LPCP, PCP, MIP     commitment    Groth16
                                                     encoding      LUNA
```

## 1 · Relations — what gets proven

`relation/`

- [[Effective Relation]] — the $(\mathbf x, \mathbf w)$ formulation everything else takes as input
- [[Circuits]] — Boolean and arithmetic circuit satisfiability
- [[Arithmetic Circuit Satisfiability Problem]] — public input $x$, witness $w$
- [[Rank-1 Constraint Satisfiability]] — R1CS; NP-complete, and the target language for arithmetization (`r1cs/`)
- [[Split-R1CS]] — partitioning the extended witness into two phases
- [[Set Membership Relation]] — a committed element lies in a (public or committed) set; the relation behind ring signatures and anonymous credentials

`relation/arithmetization/`

- [[Quadratic Arithmetic Program]] · [[Quadratic Span Program]] · [[Square Span Program]] · [[Span Program]]
- `R1CS to QAP Reduction` — the reduction that makes QAP the working form of R1CS (note currently removed)
- [[Arithmetization of a Boolean formula]] · [[Multilinear Extension of Function]] · [[Linearization Operator on Polynomial]] — the sum-check side, feeding [[Sum-Check Protocol]] and [[True Quantified Boolean Formula Protocol]]
- [[Algebraic Intermediate Representation]]

## 2 · Proof systems — by interaction pattern

`proof system/` is sorted by **what the parties exchange**: messages, an oracle, or one proof after a setup. *Proof* vs *argument* is not a folder: it is the [[Soundness]] row (statistical vs computational, §3), and [[Argument Systems]], [[Non-interactive ARGument]] and [[Non-interactive ARgument of Knowledge]] are named bundles of properties on top of their syntax. The complexity-theoretic definitions — languages, unbounded provers — are in `complexity/proof system/`: [[Probabilistic Interactive Proof System]], [[Multi-Prover Interactive Proofs]], [[Probabilistically Checkable Proofs]], [[Interactive Oracle Proof]].

`proof system/interactive/`

- [[Interactive Proof Systems]] — for a relation, with an efficient prover holding $\mathbf w$; specializes [[Probabilistic Interactive Proof System]]
- [[Argument Systems]] — the same syntax, sound only against efficient provers
- [[Sigma Protocols]] — three moves, public coin, special soundness; OR composition
- [[Trapdoor Sigma Protocol]] — a Σ-protocol in the CRS model for a pair of languages, whose trapdoor computes the one bad challenge; compiles to a NIZK without random oracles
- [[Linear Multi-Prover Interactive Proofs]] — sound only against *linear* provers, so not literally an MIP
- constructions (`scheme/`): [[Schnorr Protocol]]

`proof system/oracle/`

- [[Linear Probabilistically Checkable Proofs]] — the verifier sees only $\mathbf Q^\top \boldsymbol\pi$, never $\boldsymbol\pi$; sound only against linear proofs
- [[Non-Interactive Linear Proofs]] — the prover chooses only the coefficient matrix, never the field elements; [[Split Non-Interactive Linear Proofs]] (`variant/`)
- constructions (`scheme/`): [[QAP-based Linear PCP]]

`proof system/non-interactive/`

- [[Non-Interactive Proof Systems]] — the origin: $\mathsf{Setup}$, keys, and **the composition table** — which of Completeness / Soundness / Knowledge / Succinctness / ZK each acronym demands
- the bundles, one note each: [[Non-interactive ARGument]] (NARG) → [[Succinct Non-interactive ARGument|SNARG]] → [[Zero-Knowledge Succinct Non-interactive ARGument|zk-SNARG]] · [[Non-interactive ARgument of Knowledge]] (NARK) → [[Succinct Non-interactive ARgument of Knowledge|SNARK]] → [[Zero-Knowledge Succinct Non-interactive ARgument of Knowledge|zk-SNARK]]
- [[Relation Generator]] (`relation/`) — the generator behind $(\mathcal R, \mathrm{aux})$
- [[Split Prover]] (`variant/`) — proving in two phases, with split correctness and split zero-knowledge
- constructions (`scheme/`): [[Groth16]], [[LUNA]]

## 3 · Properties

`property/` — the axis each acronym in the composition table refers to. *Proof* vs *argument* is the strength row of [[Soundness]]: against every prover, or only against efficient ones.

| property            | note                    | variants                                                               |
| ------------------- | ----------------------- | ---------------------------------------------------------------------- |
| Completeness        | [[Completeness]]        | —                                                                      |
| Soundness           | [[Soundness]]           | adaptive / non-adaptive                                                |
| Knowledge soundness | [[Knowledge Soundness]] | no adaptive variant — the extractor sees the prover's randomness       |
| Succinctness        | [[Succinctness]]        | succinct / preprocessing / fully succinct                              |
| Zero knowledge      | [[Zero Knowledge]]      | [[Honest Verifier Zero Knowledge]]; with leakage (see [[Linear Probabilistically Checkable Proofs]]) |
| Circuit privacy     | [[Circuit Privacy]]     | with respect to a set of coefficients; multiple evaluations; computational / statistical |
| Linear-only         | [[Linear-Only Security]], [[Strictly Linear Targeted Malleability]] | strict / affine; extractor / simulator |
| Key-dependent messages | [[Key-Dependent Message Security]] | circular security (weak) |

## 4 · Compilers and building blocks

`compiler/`

- [[Fiat-Shamir Transform]] — interactive → non-interactive
- [[Efficient Arguments from Linear MIPs]]
- [[Multi-Party Computation-in-the-Head]] — an MPC protocol → a zero-knowledge proof; [[Zero-Knowledge Proof from Multi-Party Computation-in-the-Head]] is the same construction written a second time
- [[Kilian Interactive Argument of Knowledge from PCP]] — PCP + [[Merkle Tree]] → a succinct interactive argument
- [[zk-SNARK from NILP]] — NILP + a linear-only encoding → zk-SNARK (Groth16's route; seed)

`commitment/`

- [[Commitment Scheme]] — `Setup`, `Commit`, `Open`; hiding and binding games
    - constructions (`scheme/`): [[Pedersen Commitment]] (discrete log) · [[Ajtai Commitment]] (SIS, short messages) · [[BDLOP Commitment]] (Module-SIS / Module-LWE, any message; extractable mode) · [[Merkle Tree]] · [[From Collision Resistance]]
- [[Cryptographic Accumulator]] — a set compressed to one value, with membership witnesses; the lattice Merkle-tree accumulator
- [[Commitment with Linear Decommitment]] — [[Basic Commitment with Linear Decommitment]], [[Parallel Commitments with Linear Decommitments]]

`encoding scheme/`

- [[Encoding Scheme]] — [[Pairing-based Encoding Scheme]]

## 5 · Constructions

| scheme | built from |
| --- | --- |
| [[Kilian Interactive Argument of Knowledge from PCP]] | PCP + [[Merkle Tree]] |
| [[Schnorr Protocol]] | Σ-protocol over a [[Cyclic Group\|cyclic group]] |
| [[Sum-Check Protocol]] | interactive, multilinear |
| [[QAP-based Linear PCP]] | [[Quadratic Arithmetic Program]] → [[Linear Probabilistically Checkable Proofs\|LPCP]] |
| [[Groth16]] | pairing-based SNARK |
| [[LUNA]] | lattice-based, via [[Vector Encryption]] |

> [!todo] Lattice-based construction table
> Still to write: the comparison table across lattice-based constructions — [[LUNA]], [[Module HGSW]], [[Vector Encryption]], [[Vanishing SIS]] — over assumption, proof size, setup, and which succinctness level is achieved.

## Adjacent

- [[MPC MOC]] — `cryptography/secure computation/`: [[Secure Multi-party Computation]], [[Oblivious Transfer]], [[Private Information Retrieval]]

## Cross-domain

- **To `complexity/`** — [[Probabilistic Interactive Proof System]], [[Multi-Prover Interactive Proofs]], [[Probabilistically Checkable Proofs]], [[Interactive Oracle Proof]], [[Class IP]] (IP = PSPACE), [[Sum-Check Protocol]], [[Circuit Satisfaction]], [[Class NP]]
- **To `math/`** — [[Polynomial]], [[Lagrange Interpolation]], [[Vanishing Polynomial]], [[Schwartz-Zippel]], [[Bilinear Pairings]], [[Bilinearity]] (used directly in [[Split-R1CS]])
- **To `cryptography/assumptions/`** — [[Random Oracle Model]] and [[Uniform Random String Model]] for the setup; lattice assumptions for [[LUNA]]
- **From `cryptography/primitive/`** — [[Vector Encryption]] is the primitive [[LUNA]] compiles through
