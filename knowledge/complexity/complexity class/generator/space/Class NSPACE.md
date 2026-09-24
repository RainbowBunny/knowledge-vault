Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1: Definition of Space-bounded Computation.

## Definition

> [!definition] Class Nondeterministic SPACE
> Let $S: \mathbb{N} \rightarrow \mathbb{N}$ and $\mathcal{L} \subseteq \{0, 1\}^*$. We say that $\mathcal{L} \in \mathsf{NSPACE}(s(n))$ if there is a constant $c$ and a nondeterministic [[Offline Turing Machine|Turing Machine]] $M$ deciding $\mathcal{L}$ such at most $c \cdot s(n)$ that never uses more than $c \cdot s(n)$ nonblank tape locations on length $n$ inputs, regardless of its non-deterministic choices.

## Property

> [!theorem]
> Requires: [[Class DTIME]], [[Class SPACE]].
> 
> ---
> For every [[Computable Function|Space Constructible]] $S: \mathbb{N} \rightarrow \mathbb{N}$,
> $$\mathsf{DTIME}(S(n)) \subseteq \mathsf{SPACE}(S(n)) \subseteq \mathsf{NSPACE}(S(n)) \subseteq \mathsf{DTIME}(2^{O(S(n))})$$

> [!theorem] Savitch's Theorem
> Requires:: [[Class SPACE]]
> 
> ---
> For any [[Computable Function|Space-Constructible]] $S: \mathbb{N} \rightarrow \mathbb{N}$ with $S(n) \geq \log n$, 
> $$\mathsf{NSPACE}(S(n)) \subseteq \mathsf{SPACE}(S(n)^2).$$
