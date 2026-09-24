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

`relation/arithmetization/`

- [[Quadratic Arithmetic Program]] · [[Quadratic Span Program]] · [[Square Span Program]] · [[Span Program]]
- [[R1CS to QAP Reduction]] — the reduction that makes QAP the working form of R1CS
- [[Arithmetization of a Boolean formula]] · [[Multilinear Extension of Function]] · [[Linearization Operator on Polynomial]] — the sum-check side, feeding [[Sum-Check Protocol]] and [[True Quantified Boolean Formula Protocol]]
- [[Algebraic Intermediate Representation]]

## 2 · Information-theoretic proof systems

`proof system/interactive/`

- [[Interactive Proof Systems]] — the base object; the definition itself lives in [[Probabilistic Interactive Proof System]]
- [[Multi-Prover Interactive Proofs]] · [[Linear Multi-Prover Interactive Proofs]]

`proof system/oracle/`

- [[Probabilistically Checkable Proofs]] · [[Interactive Oracle Proof]]
- [[Linear Probabilistically Checkable Proofs]] — the verifier sees only $\mathbf Q^\top \boldsymbol\pi$, never $\boldsymbol\pi$
- [[Non-Interactive Linear Proofs]] — the prover chooses only the coefficient matrix, never the field elements; [[Split Non-Interactive Linear Proofs]] (`variant/`)

`proof system/`

- [[Sigma Protocols]] · [[Zero-Knowledge Proof from Multi-Party Computation-in-the-Head]]
- [[Split Prover]] (`variant/`) — proving in two phases, with split correctness and split zero-knowledge
- constructions (`scheme/`): [[QAP-based Linear PCP]], [[Schnorr Protocol]]

## 3 · Properties

`property/` — the axis each acronym in the composition table refers to.

| property            | note                    | variants                                                               |
| ------------------- | ----------------------- | ---------------------------------------------------------------------- |
| Completeness        | [[Completeness]]        | —                                                                      |
| Soundness           | [[Soundness]]           | adaptive / non-adaptive                                                |
| Knowledge soundness | [[Knowledge Soundness]] | no adaptive variant — the extractor sees the prover's randomness       |
| Succinctness        | [[Succinctness]]        | succinct / preprocessing / fully succinct                              |
| Zero knowledge      | [[Zero Knowledge]]      | [[Honest Verifier Zero Knowledge]]; with leakage (see [[Linear Probabilistically Checkable Proofs]]) |

## 4 · Compilers and building blocks

`compiler/`

- [[Fiat-Shamir Transform]] — interactive → non-interactive
- [[Efficient Arguments from Linear MIPs]]
- [[Multi-Party Computation-in-the-Head]] — an MPC protocol → a zero-knowledge proof

`commitment/`

- [[Commitment Scheme]] — [[Merkle Tree]], [[From Collision Resistance]]
- [[Commitment with Linear Decommitment]] — [[Basic Commitment with Linear Decommitment]], [[Parallel Commitments with Linear Decommitments]]

`encoding scheme/`

- [[Encoding Scheme]] — [[Pairing-based Encoding Scheme]]

## 4½ · Arguments — the compiled output

`argument/interactive/`

- [[Argument Systems]] — soundness relaxed to computational; [[Kilian Interactive Argument of Knowledge from PCP]] (`scheme/`)

`argument/non-interactive/`

- [[Non-Interactive Proof Systems]] — $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$, and **the composition table**: which of Completeness / Soundness / Knowledge / Succinctness / ZK each acronym demands
- [[Non-interactive ARGument]] — NARG, SNARG, zk-SNARG
- [[Non-interactive ARgument of Knowledge]] — NARK, SNARK, zk-SNARK
- [[zk-SNARK from NILP]]; constructions (`scheme/`): [[Groth16]], [[LUNA]]

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

- [[MPC MOC]] — `cryptography/secure computation/`: [[Secure Multi-party Computation]], [[Oblivious Transfer]], [[Private Information Retrieval]]

## Cross-domain

- **To `complexity/`** — [[Probabilistic Interactive Proof System]], [[Class IP]] (IP = PSPACE), [[Sum-Check Protocol]], [[Circuit Satisfaction]], [[Class NP]]
- **To `math/`** — [[Polynomial]], [[Lagrange Interpolation]], [[Vanishing Polynomial]], [[Schwartz-Zippel]], [[Bilinear Pairings]], [[Bilinearity]] (used directly in [[Split-R1CS]])
- **To `cryptography/assumptions/`** — [[Random Oracle Model]] and [[Uniform Random String Model]] for the setup; lattice assumptions for [[LUNA]]
- **From `cryptography/primitive/`** — [[Linear-Only Vector Encryption]] is the primitive [[LUNA]] compiles through
