Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.3: NL Completeness.

## Definition

> [!definition] Log-space Reducibility
> A [[Language]] $\mathcal{B}$ is **log-space reducible** to language $\mathcal{C}$, denoted $\mathcal{B} \leq_l \mathcal{C}$, if 
> - There is a function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ that is an [[Computable Function|Implicitly Log-space Computable Function]].
> - $x \in \mathcal{B} \iff f(x) \in \mathcal{C} \; \forall \; x \in \{0, 1\}^*$.

## Property

> [!lemma]
> [[Transitivity]] holds for log-space reducibility.