# Complexity MOC

Index for the complexity domain. The spine is **machine → generator → class**: a machine model (in `computability/computing model/`) with a resource bound left open is a generator ([[Class DTIME]], [[Class SPACE]], …); fixing the bound gives a named class ([[Class P]], [[Class PSPACE]], …). Problems are catalogued separately in `problem/`, and a problem's status (which class it is in, what it is complete for) is a field on the problem note, not a folder.

`conjectures/` plays the role here that `assumptions/` plays in cryptography.

## Foundations — `foundations/`

- [[Complexity Foundations MOC]]
- [[Hierarchy Theorems]] — more resource, strictly more power

## Class machinery — `complexity class/`

- [[Complexity Class]] — what a class is: languages, encodings, co-classes

**Generators** (`generator/`)
- time: [[Class DTIME]] · [[Class NTIME]]
- space: [[Class SPACE]] · [[Class NSPACE]]
- time and space together: [[Class TISP]]
- alternation: [[Class ATIME]] · [[Class SigmaTIME]] · [[Class PiTIME]]
- randomized: [[Class BPTIME]] · [[Class RTIME]] · [[Class ZTIME]]
- circuit: [[Class SIZE]] · [[Class DTIME with Advice]]

**Named classes** (`class/`)
- time: [[Class P]] · [[Class NP]] · [[Class coNP]] · [[Class NP-Intermediate]] · [[Class EXP]] · [[Class NEXP]]
- space: [[Class L]] · [[Class NL]] · [[Class PSPACE]] · [[Class NPSPACE]]
- alternation: [[Class AP]] · [[Class PH]] · [[Level Polynomial Hierarchy]]
- randomized: [[Class BPP]] · [[Class RP]] · [[Class coRP]] · [[Class ZPP]] · [[Class BPL]] · [[Class RL]] · [[Class BP dot NP]]
- circuit: [[Class NC]] · [[Class AC]] · [[Class Ppoly]]
- interactive: [[Class IP]] · [[Class AM]] · [[Class MA]] · [[Class MIP]] · [[Class dIP]]

**Operators** (`operator/`) — build a class from a class
- [[Complement Class]] · [[Complexity Class with Oracle]] · [[Hardness and Completeness]]

**Reducibility** (`reducibility/`)
- [[Polynomial-time Karp Reducibility]] · [[Log-space Reducibility]] · [[Randomized Polynomial Reducibility]]

> [!todo] Pre-refactor hubs still to dissolve (Assignment 4H)
> [[Time Complexity]] · [[Space Complexity]] · [[Randomized Complexity]] · [[Reductions]] still repeat definitions that now have their own notes (e.g. [[Probabilistic Turing Machine]] already exists in `computability/`). Move what is unique into the machine, generator or reducibility notes, then delete the hub.

## Problems — `problem/`

A problem note states the language once; `Member of::`, `Complete for::` and `Hard for::` in its Property callout carry its status. A cryptographic *assumption* (a distribution plus an advantage) stays in `cryptography/assumptions/` and points here with `Requires::`.

- logic: [[Satisfiability]] · [[3Satisfiability]] · [[Circuit Satisfiability]] · [[Circuit Satisfaction]] · [[Circuit Evaluation]] · [[Tautology]] · [[True Quantified Boolean Formula]] · [[Polynomial Hierarchy SAT]] · [[Counting Satisfiability Decision]]
- graph: [[Vertex Path]] · [[Undirected Vertex Path]] · [[Graph Connectivity]] · [[Directed Hamiltonian Path]] · [[Independent Set]] · [[Two Coloring]] · [[Three Coloring]] · [[Traveling Salesperson]] · [[Graph Isomorphism]] · [[Graph Non-Isomorphism]]
- number: [[Integer Multiplication]] · [[Composite Number]] · [[Factoring]] · [[Quadratic Residue]] · [[Subset Sum]] · [[0-1 Integer Programming]] · [[Linear Programming]]
- group: [[Discrete Logarithm Problem]] · [[Elliptic Curve DLP]] · [[Hyperelliptic Curve DLP]]
- lattice: [[Shortest Vector Problem]] · [[Closest Vector Problem]] · [[Shortest Basis Problem]]
- code: [[Syndrome Decoding Problem]] · [[Regular Syndrome Decoding Problem]] · [[Null Syndrome Decoding Problem]] · [[2-Regular Null Syndrome Decoding]]
- machine: [[Turing Machine Satisfiability]] · [[Unary Halting Problem]] · [[Exponential Computation]]
- awaiting merge: [[Subset-Sum Problem]] into [[Subset Sum]]; [[Satisfiability Problem (To be removed)]] into [[Satisfiability]]

## Interaction — `interactive/`

- [[Deterministic Function Interaction]] · [[Deterministic Interactive Proof System]] · [[Probabilistic Interactive Proof System]]
- protocols for one language (`protocol/`): [[Sum-Check Protocol]] · [[True Quantified Boolean Formula Protocol]] · [[Graph Non-isomorphism Protocol]] · [[Quadratic Non Residue Protocol]] · [[Goldwasser-Sipser Set Lower Bound Protocol]]
- the classes they define: [[Class IP]] · [[Class AM]] · [[Class MA]] · [[Class MIP]] · [[Class dIP]]

## Circuits — `circuit/`

Non-uniform models. The circuit *classes* are in `complexity class/class/circuit/`.

- [[Boolean Circuit]] · [[Arithmetic Circuit]] · [[Branching Programs]] · [[Quantified Boolean Formula]]
- families and uniformity: [[Circuit Family]] · [[P-Uniform Circuit Family]] · [[Log-Space Uniform Circuit Family]] · [[Direct Connect Uniform Circuit Family]]

## Quantum — `quantum/`

- [[Quantum Complexity MOC]] · [[Quantum Bit]] · [[Quantum State]] · [[Quantum Circuits]] · [[Parity Game]]

## Open problems — `conjectures/`

- [[Conjectures MOC]] — [[P vs NP]] · [[Exponential Time Hypothesis]] · [[Derandomization Conjecture]] · [[Unique Games Conjecture]]

## Subfields — `advanced/`

- [[Advanced MOC]] — [[Approximation Hardness]] · [[Communication Complexity]] · [[Parameterized Complexity]] · [[Average-Case Complexity]] · [[Fine-Grained Complexity]]

## Folder layout

```
complexity/
├── Complexity MOC.md
├── foundations/
├── complexity class/
│   ├── generator/      (time/, space/, alternation/, randomized/, circuit/)
│   ├── class/          (time/, space/, alternation/, randomized/, circuit/, interactive/)
│   ├── operator/
│   └── reducibility/
├── problem/            (logic/, graph/, number/, group/, lattice/, code/, machine/)
├── interactive/        (protocol/)
├── circuit/
├── randomized/         old hub, to dissolve
├── quantum/
├── conjectures/
└── advanced/
```

## Cross-domain

- **From `computability/`** — the machine models ([[Turing Machine]], [[Oracle Turing Machine]], [[Probabilistic Turing Machine]]) and [[Language]] come first.
- **To `cryptography/assumptions/`** — each assumption names the problem it averages over: [[Discrete-Logarithm Assumption]] over [[Discrete Logarithm Problem]]; `assumptions/lattice-based/` over `problem/lattice/`; `assumptions/code-based/` over `problem/code/`. "PPT adversary" rests on randomized machines.
- **To `cryptography/verifiable computing/`** — [[Arithmetic Circuit Satisfiability Problem]] and the arithmetization notes turn circuits and formulas into polynomial identities; [[Sum-Check Protocol]] is shared.
- **To `math/`** — diagonalization in [[Hierarchy Theorems]].

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
