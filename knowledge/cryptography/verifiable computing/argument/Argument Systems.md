## Syntax

> [!definition] Argument System
> An **argument system** for a function $f$ is an [[Interactive Proof Systems#Syntax|Interactive Proof]] for $f$ in which the [[Interactive Proof Systems#Soundness|Soundness]] condition is only required to hold against prover strategies that run in polynomial time.

> [!remark]
> Argument systems are sometimes referred to as **computationally sound proofs**.

## Property

### Completeness

- See interactive proof system [[Interactive Proof Systems#Completeness|Completeness]].

### Succinct

> [!definition] Succinct
> We say that an argument system for circuit satisfiability is succinct if the total communication is sublinear in the size of the witness $|w|$.

> [!remark]
> Succinctness is important because:
> - Shorter proofs are always better.
> - Witness are naturally large.
> - Efficient transformations from computer programs to circuit satisfiability often produce circuits with very large witnesses.

## Security

### Knowledge Soundness

> [!remark]
> Knowledge soundness means that not only a witness $w$ exists, but the prover also knows $w$.

### Zero Knowledge

- See interactive proof system [[Interactive Proof Systems#Zero Knowledge|Zero Knowledge]].

