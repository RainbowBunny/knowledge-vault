Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.2: Reducibility and NP-completeness.

## Definition

> [!definition] Polynomial-time Karp Reducibility
> A language $\mathcal{L} \subset \{0, 1\}^*$ is polynomial-time Karp reducible to a language $\mathcal{L}' \subseteq \{0, 1\}^*$ (sometimes shortened to just "polynomial-time reducible"), denoted by $\mathcal{L} \leq_p \mathcal{L}'$, if there is a polynomial-time computable function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ such that: 
> $$\forall x \in \{0, 1\}^*: x \in \mathcal{L} \iff f(x) \in \mathcal{L}'.$$

## Property

> [!theorem]
> [[Transitivity]] holds for polynomial-time Karp reducibility.