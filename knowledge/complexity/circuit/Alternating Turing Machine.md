# Alternating Turing Machine

A generalization of nondeterministic Turing machines: states have universal ($\forall$) and existential ($\exists$) flavors.

> [!definition] Alternating Turing Machine
> An **alternating Turing machine** is a nondeterministic Turing machine with an additional feature. Its states, except for $q_{accept}$ and $q_{reject}$, are divided into **universal states** (accept iff all child branches accept) and **existential states** (accept iff some child branch accepts).

## Relation to Other Classes

Alternation lets you simulate the polynomial hierarchy uniformly:
- $\Sigma_k\text{TIME}$ = languages decidable by alternating TMs with $k$ alternations starting from an existential state.
- $\Pi_k\text{TIME}$ = similarly, starting from a universal state.
- $\text{AP}$ = polynomial-time alternating computation. **Theorem (Chandra-Kozen-Stockmeyer):** $\text{AP} = \text{PSPACE}$.
- $\text{AL}$ = log-space alternating. **Theorem:** $\text{AL} = \text{P}$.

Alternation thus gives a uniform-machine view of [[Circuit Complexity|bounded-depth circuits]] (logspace alternation ↔ polynomial-time uniform circuits).

## Related

- [[Circuit Complexity]] — non-uniform analog
- [[Polynomial Hierarchy]] — defined via $\Sigma_k, \Pi_k$
- [[Space Complexity]] — $\text{AP} = \text{PSPACE}$
