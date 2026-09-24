# Computability MOC

Index for computability: what can be computed at all, and by which machine. [[Complexity MOC]] asks what it costs; [[Algorithms MOC]] asks how to do it well.

## Machines — `computing model/`

- [[Computable Function]] · [[Enumerator]]
- automata (`automata/`): [[Deterministic Finite Automaton]] · [[Non-deterministic Finite Automaton]] · [[Generalized Nondeterministic Finite Automaton]] · [[Pushdown Automaton]] · [[Finite State Transducer]]
- Turing machines (`turing machine/`): [[Turing Machine]] · [[Multitape Turing Machine]] · [[Offline Turing Machine]] · [[Turing Machine with Stay Option]] · [[Non-deterministic Turing Machine]] · [[Alternating Turing Machine]] · [[Probabilistic Turing Machine]] · [[Oracle Turing Machine]] · [[Universal Turing Machine]]

`Abstract Machine` is being retired: acceptance moves into each model (Assignment 4A-4).

## Languages — `language/`

- [[String]] · [[Language]] · [[Simple Encoding]] · [[Machine Encoding]]
- regular: [[Regular Language]] · [[Regular Expression]]
- context-free: [[Context-Free Language]] · [[Context-Free Grammar]]
- decidable and recognizable: [[Decidable Language]] · [[Recognizable Language]]

## Uncomputability — `uncomputability/`

- [[Halting Problem]] · [[Uncomputable Function]]

## Pre-refactor hub

- [[Computability Theory]] (`foundations/`) still holds a decidability list ($A_\mathsf{DFA}$, $E_\mathsf{DFA}$, …). Each item belongs in `language/decidable/` or `uncomputability/`; then the note goes (Assignment 4H).

## Folder layout

```
computability/
├── Computability MOC.md
├── computing model/   (automata/, turing machine/)
├── language/          (regular/, context-free/, decidable/, recognizable/)
├── uncomputability/
└── foundations/       old hub, to dissolve
```

## Cross-domain

- **To [[Complexity MOC]]** — a generator is a machine model from here plus a resource bound; decision problems with a complexity status are catalogued in `complexity/problem/`.
- **To `math/foundation/`** — [[Formal System]], [[Abstract Reduction System]]: the proof-theoretic and rewriting side of the same questions.
