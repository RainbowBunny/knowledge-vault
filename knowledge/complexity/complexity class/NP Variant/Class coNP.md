Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.6.1: coNP.

## Definition

> [!definition] Class coNP
> Requires:: [[Class NP]]
> 
> ---
> $\mathsf{coNP} = \{\mathcal{L} \mid \overline{\mathcal{L}} \in \mathsf{NP}\}$

> [!definition] Class coNP (alternative definition)
> For every $\mathcal{L} \subseteq \{0, 1\}^*$, we say that $L \in \mathsf{coNP}$ if there exists a polynomial $p: \mathbb{N} \rightarrow \mathbb{N}$ and a polynomial-time [[Turing Machine]] $M$ such that:
> $$\forall x \in \{0, 1\}^*: x \in \mathcal{L} \iff \forall w \in \{0, 1\}^{p(|x|)}, M(x, w) = 1$$

## Member

> [!example]
> $\text{TAUTOLOGY} = \{\langle \phi \rangle \mid \phi \text{ is true under every assignment}\}$
