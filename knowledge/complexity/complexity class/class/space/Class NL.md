Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1.2: Some space complexity classes; Section 4.3.2: NL = coNL.

## Definition

> [!definition] Class Nondeterministic Logarithm space
> Requires:: [[Class NSPACE]]
> 
> ---
> $\mathsf{NL} = \mathsf{NSPACE}(\log{n})$

> [!definition] Class NL (Alternative Definition)
> A [[Language]] $\mathcal{L} \in \mathsf{NL}$ if there exists a [[Offline Turing Machine|Deterministic Turing Machine]] $M$ (called the *verifier*) with an additional special read-once input tape, and a [[Polynomial]] $p: \mathbb{N} \rightarrow \mathbb{N}$ such that:
> $$\forall x \in \{0, 1\}^* : x \in \mathcal{L} \iff \exists u \in \{0, 1\}^p(|x|) \; \text{s.t.} \; M(x, u) = 1$$
> where by $M(x, u)$ we denote the output of $M$ where $x$ is placed on its input tape and $u$ is placed on its special read-once tape, and $M$ uses at most $O(\log |x|)$ space on its read-write tapes for every input $x$.

## Property

### Relation to Other Classes

> [!theorem]
> Requires:: [[Vertex Path]], [[Complement Class]], [[Hardness and Completeness]]
> 
> ---
> $\mathsf{NL} = \mathsf{coNL}$.
> 
> ---
> - $\mathsf{PATH} \in \mathsf{NL} \cap \mathsf{coNL}$.
> - $\mathsf{PATH} \in \mathsf{NL}\mbox{-}\mathsf{complete}$.
> - $\overline{\mathsf{PATH}} \in \mathsf{coNL}\mbox{-}\mathsf{complete}$.
