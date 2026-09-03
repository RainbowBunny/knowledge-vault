# Verifiable Computing MOC

Index for `cryptography/verifiable computing/` — proving that a computation was done correctly, to a verifier who will not redo it.

Organised by the **compilation chain**, because that is what the folder actually is: a statement is expressed as a relation, the relation is arithmetized, an information-theoretic proof system is built for it, and cryptography compiles that into a real argument.

```
relation  →  arithmetization  →  IT proof system  →  compiler  →  argument
 R1CS         QAP / QSP / SSP     LPCP, PCP, MIP     commitment    Groth16
                                                     encoding      LUNA
```

## 1 · Relations — what gets proven

`relations/`

- [[Effective Relation]] — the $(\mathbf x, \mathbf w)$ formulation everything else takes as input
- [[Circuits]] — Boolean and arithmetic circuit satisfiability
- [[Rank-1 Constraint Satisfiability]] — R1CS; NP-complete, and the target language for arithmetization
- [[Split-R1CS]] — partitioning the extended witness into two phases

`relations/arithmetization/`

- [[Quadratic Arithmetic Program]] · [[Quadratic Span Program]] · [[Square Span Program]]
- [[R1CS to QAP Reduction]] — the reduction that makes QAP the working form of R1CS

## 2 · Proof systems

`proof/interactive/`

- [[Interactive Proof Systems]] — the base object
- [[Argument Systems]] — soundness relaxed to computational
- [[Multi-Prover Interactive Proofs]] · [[Linear Multi-Prover Interactive Proofs]]

`proof/non-interactive/`

- [[Non-Interactive Proof Systems]] — $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$, and **the composition table**: which of Completeness / Soundness / Knowledge / Succinctness / ZK each acronym demands
- [[Non-interactive ARGument]] — NARG, SNARG, zk-SNARG
- [[Non-interactive ARgument of Knowledge]] — NARK, SNARK, zk-SNARK

`proof/oracle/` — the information-theoretic layer

- [[Probabilistically Checkable Proofs]]
- [[Linear Probabilistically Checkable Proofs]] — the verifier sees only $\mathbf Q^\top \boldsymbol\pi$, never $\boldsymbol\pi$
- [[Non-Interactive Linear Proofs]] — the prover chooses only the coefficient matrix, never the field elements

`proof/variants/`

- [[Split Prover]] — proving in two phases, with split correctness and split zero-knowledge

## 3 · Properties

`proof/properties/` — the axis each acronym in the composition table refers to.

| property | note | variants |
| --- | --- | --- |
| Completeness | [[Completeness]] | — |
| Soundness | [[Soundness]] | adaptive / non-adaptive |
| Knowledge soundness | [[Knowledge Soundness]] | no adaptive variant — the extractor sees the prover's randomness |
| Succinctness | [[Succinctness]] | succinct / preprocessing / fully succinct |
| Zero knowledge | [[Zero Knowledge]] | HVZK; with leakage (see [[Linear Probabilistically Checkable Proofs]]) |

## 4 · Compilers and building blocks

`commitment/`

- [[Commitment Scheme]] — [[Merkle Tree]], [[From Collision Resistance]]
- [[Commitment with Linear Decommitment]] — [[Basic Commitment with Linear Decommitment]], [[Parallel Commitments with Linear Decommitments]]

`encoding scheme/`

- [[Encoding Scheme]] — [[Pairing-based Encoding Scheme]]

`proof/`

- [[Fiat-Shamir Transform]] — interactive → non-interactive
- [[Sigma Protocols]]
- [[Efficient Arguments from Linear MIPs]]

## 5 · Constructions

| scheme | built from |
| --- | --- |
| [[Kilian Interactive Argument of Knowledge from PCP]] | PCP + [[Merkle Tree]] |
| [[Schnorr Protocol]] | Σ-protocol over a [[Cyclic Group\|cyclic group]] |
| [[Sum-Check Protocol]] | interactive, multilinear |
| [[QAP-based Linear PCP]] | [[Quadratic Arithmetic Program]] → [[Linear Probabilistically Checkable Proofs\|LPCP]] |
| [[Groth16]] | pairing-based SNARK |
| [[LUNA]] | lattice-based, via [[Linear-Only Vector Encryption]] |

> [!todo] Lattice-based construction table
> Still to write: the comparison table across lattice-based constructions — [[LUNA]], [[Module HGSW]], [[Linear-Only Vector Encryption]], [[Vanishing SIS]] — over assumption, proof size, setup, and which succinctness level is achieved.

## Adjacent

- [[MPC MOC]] — `secure computation/`, [[Secure Multi-party Computation]]
- [[Private Information Retrieval]]

## Cross-domain

- **To `complexity/`** — [[Interactive Proofs]] (IP = PSPACE), [[Circuit Satisfaction]], [[Class NP]]
- **To `math/`** — [[Polynomial]], [[Lagrange Interpolation]], [[Vanishing Polynomial]], [[Schwartz-Zippel]], [[Bilinear Pairings]], [[Bilinearity]] (used directly in [[Split-R1CS]])
- **To `cryptography/assumptions/`** — [[Random Oracle Model]] and [[Uniform Random String Model]] for the setup; lattice assumptions for [[LUNA]]
- **From `cryptography/primitive/`** — [[Linear-Only Vector Encryption]] is the primitive [[LUNA]] compiles through
