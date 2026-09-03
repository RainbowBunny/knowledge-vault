# Complexity MOC

Top-level index for the complexity-theory domain. Organized by **resource bound**: each first-level folder studies how a particular computational resource (time, space, randomness, circuits, interaction) constrains what can be computed.

The structure mirrors `cryptography/`: foundations + initiative folders + a `conjectures/` folder (parallel to crypto's `assumptions/`) for open problems that act as leaves of the proof DAG.

## Foundations

- [[Complexity Class]] — the language formulation (decision problems as languages, encodings, co-classes), efficient algorithms, the class-inclusion lattice
- [[Reductions]] — poly-time and log-space mapping reductions
- [[Hierarchy Theorems]] — time / space hierarchy meta-theorems, EXPSPACE-Complete

## Resource Bounds (Initiatives)

- [[Time Complexity]] — TIME, NTIME, P, NP, NP-Complete, Cook-Levin, EXPTIME, sub-exponential
- [[Space Complexity]] — SPACE, NSPACE, PSPACE, L, NL, Savitch's theorem
- [[Randomized Complexity]] — Probabilistic TM, PPT, BPP, RP, ZPP, Monte Carlo, amplification
- [[Circuit Complexity]] — Boolean circuits, NC, AC, P/poly, branching programs, alternating TMs
- [[Interactive Proofs]] — IP class, verifier/prover, IP = PSPACE; [[Oracle Machines]], [[Polynomial Hierarchy]]
- [[Quantum Complexity MOC|Quantum Complexity]] — BQP, QMA (stub)

## Classes

`complexity class/` — the named classes themselves, as leaves under the resource bounds above.

- [[Class P]] — decidable in polynomial time
- [[Class NP]] — polynomial-time *verifiable*; see [[Circuit Satisfaction]] for the canonical complete problem
- [[Class NP-complete]] · [[Class NP-hard]] — the hardness frontier, via [[Reductions]]
- [[Class coNP]] — complements of NP languages

`circuit/` also holds [[Boolean Circuit]], [[Arithmetic Circuit]] and [[Arithmetic Circuit Satisfiability Problem]], which `cryptography/verifiable computing/` arithmetizes — see [[Verifiable Computing MOC]].

## Open Problems

- [[Conjectures MOC]] — P vs NP, ETH/SETH, Derandomization, Unique Games

## Advanced Subfields

- [[Advanced MOC]] — Approximation Hardness, Communication Complexity, Parameterized Complexity, Average-Case Complexity, Fine-Grained Complexity

## Folder Layout

```
complexity/
├── Complexity MOC.md
├── foundations/
│   ├── Complexity Class.md
│   ├── Reductions.md
│   └── Hierarchy Theorems.md
├── time/
│   └── Time Complexity.md
├── space/
│   └── Space Complexity.md
├── randomized/
│   └── Randomized Complexity.md
├── circuit/
│   ├── Circuit Complexity.md
│   ├── Branching Programs.md
│   └── Alternating Turing Machine.md
├── interactive/
│   ├── Interactive Proofs.md
│   ├── Oracle Machines.md
│   └── Polynomial Hierarchy.md
├── quantum/
│   └── Quantum Complexity MOC.md
├── conjectures/
│   ├── Conjectures MOC.md
│   ├── P vs NP.md
│   ├── Exponential Time Hypothesis.md
│   ├── Derandomization Conjecture.md
│   └── Unique Games Conjecture.md
└── advanced/
    ├── Advanced MOC.md
    ├── Approximation Hardness.md
    ├── Communication Complexity.md
    ├── Parameterized Complexity.md
    ├── Average-Case Complexity.md
    └── Fine-Grained Complexity.md
```

## Cross-Domain Cross-References

- **From `cryptography/foundations/Security Model.md`** to [[Randomized Complexity]] — "PPT adversary" is a complexity-theoretic concept defined there.
- **From `cryptography/assumptions/`** to [[Conjectures MOC]] — hardness assumptions in cryptography play the same structural role as complexity-theoretic conjectures.
- **From `cs/foundations/`** ([[Languages]], [[Computability Theory]]) to [[Complexity Class]] — strings, languages, Turing machines, decidability are prerequisites.
- **To `math/`** for diagonalization techniques used in [[Hierarchy Theorems]].

## Callout Conventions

The same callout taxonomy as cryptography applies:

| Callout | Use |
|---|---|
| `[!definition]` | TIME(t), NP, BPP — class definitions |
| `[!theorem]` | Hierarchy theorems, Savitch, IP = PSPACE, Cook-Levin |
| `[!conjecture]` | P ≠ NP, ETH, Derandomization Conjecture, UGC |
| `[!property]` | Structural properties of classes (e.g. closure under reductions) |
| `[!example]` | Concrete languages in each class |
| `[!remark]` | Cross-references, naming conventions |
| `[!algorithm]` | Algorithms / machine specifications |
