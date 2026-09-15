Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP; Section 2.1.2: Nondeterministic Turing Machines; Section 2.2: Reducibility and NP-completeness; Section 2.5: Decision Versus Search.

## Definition

> [!definition] Class NP
> A [[Language]] $\mathcal{L} \subseteq \{0, 1\}^*$ is in $\mathsf{NP}$ if there exists a polynomial $p: \mathbb{N} \rightarrow \mathbb{N}$ and a polynomial-time [[Turing Machine]] $M$ (called the **verifier** for $\mathcal{L}$) such that:
> $$\forall x \in \{0, 1\}^*: x \in L \iff \exists w \in \{0, 1\}^{p(|x|)} \; \text{s.t.} \; M(x, w) = 1.$$
> If $x \in \mathcal{L}$ and $w \in \{0, 1\}^{p(|x|)}$ satisfy $M(x, w) = 1$, then we call $w$ a **certificate** (**witness**) for $x$ (with respect to the language $\mathcal{L}$ and machine $M$). 

## Property

> [!theorem]
> Requires:: [[Class NTIME]].
> 
> ---
> $$\mathsf{NP} = \cup_{c \in \mathbb{N}} \mathsf{NTIME}(n^c).$$
> 
> ---
> The main idea is that the sequence of nondeterministic choices made by an accepting computation of an [[Non-deterministic Turing Machine]] can be viewed as a certificate that the input is in the language, and vice versa.

> [!theorem]
> $$\mathcal{L} \in \mathsf{NP}\mbox{-}\mathsf{complete} \land \mathcal{L} \in \mathsf{P} \implies \mathsf{P} = \mathsf{NP}$$
> $$\mathcal{L} \in \mathsf{NP}\mbox{-}\mathsf{hard} \land \mathcal{L} \in \mathsf{P} \implies \mathsf{P} = \mathsf{NP}$$

> [!theorem]
> Suppose that $\mathsf{P} = \mathsf{NP}$. Then, for every $\mathsf{NP}$ [[Language]] $\mathcal{L}$ and a verifier [[Turing Machine]] $M$ for $\mathcal{L}$, there is a polynomial-time Turing machine $B$ that on input $x \in \mathcal{L}$, outputs a certificate for $x$ (with respect to the language $\mathcal{L}$ and Turing Machine $M$).

## Open Question

> [!example]
> Does $\text{coNP} = \text{NP}$?