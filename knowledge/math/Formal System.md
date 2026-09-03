Reference:
- https://en.wikipedia.org/wiki/Formal_system

## Intuition

A formal system is syntax with rules: a language of well-formed strings, some strings taken as axioms, and inference rules for deriving new strings. Nothing about *meaning* — that is what semantics adds, and a **logic** is a formal system with a semantics. One logic can be presented by several formal systems (Hilbert style, natural deduction, sequent calculus), so *formal system ≠ logic ≠ first-order logic* — three nested levels.

## Definition

> [!definition] Formal System
> A **formal system** consists of:
> - a **formal language** — the well-formed formulas, generated from an alphabet by a grammar;
> - a **deductive system** — axioms (or schemata) and inference rules deriving theorems from them.

> [!remark] Non-logical formal systems
> Lambda calculus, term rewriting, the grammars and automata of [[Languages]], and Turing machines are formal systems that are not logics. The [[Complexity MOC|complexity]] and `cs/foundations/` folders study formal systems whose derivations are *computations*.

## Property

The vault's tier convention classifies statements by which formal system naturally expresses them: equational ([[Equational Logic]]) ⊂ first-order ([[First-Order Logic]]) ⊂ higher-order; security games sit outside all three ([[Security Game]]).