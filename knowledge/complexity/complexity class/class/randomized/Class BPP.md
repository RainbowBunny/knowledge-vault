Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.1: Probabilistic Turing Machines; Section 7.4.1: Role of precise constants: Error reduction; Section 7.5.1: BBP $\subseteq \mathsf{P_{/\mathsf{poly}}}$; Section 7.5.2: BBP is in PH.

## Definition

> [!definition] Class Bounded Probabilistic Polynomial
> Requires:: [[Class BPTIME]]
> 
> ---
> $\mathsf{BPP} = \cup_c \mathsf{BPTIME}(n^c)$.

> [!definition] Class BPP (alternative definition)
> A [[Language]] $\mathcal{L}$ is in $\mathsf{BPP}$ if there exists a polynomial-time [[Turing Machine]] $M$ and a polynomial $p: \mathbb{N} \rightarrow \mathbb{N}$ such that for every $x \in \{0, 1\}^*$:
> $$\Pr_{r \in_R \{0, 1\}^{p(|x|)}}[M(x, r) = \mathcal{L}(x)] \geq \frac{2}{3}.$$

## Property

### Error Reduction

> [!lemma]
> For $c > 0$, let $\mathsf{BPP}_{\frac{1}{2} + n^{-c}}$ denotes the class of [[Language]] $\mathcal{L}$ for which there is a polynomial-time [[Probabilistic Turing Machine]] $M$ satisfying 
> $$\forall x \in \{0, 1\}^*: \Pr[M(x) = \mathcal{L}(x)] \geq \frac{1}{2} + |x|^{-c}.$$
> Then $\mathsf{BPP}_{\frac{1}{2} + n^{-c}} = \mathsf{BPP}$.

> [!theorem] Error Reduction for BPP
> Let $\mathcal{L} \subseteq \{0, 1\}^*$ be a [[Language]] and suppose that there is a polynomial-time [[Probabilistic Turing Machine]] $M$ such that:
> $$\forall x \in \{0, 1\}^*: \Pr[M(x) = \mathcal{L}(x)] \geq \frac{1}{2} + |x|^{-c}.$$
> Then for every $d > 0$, there exists a polynomial-time [[Probabilistic Turing Machine]] $M'$ such that
> $$\forall x \in \{0, 1\}^*: \Pr[M'(x) = \mathcal{L}(x)] \geq 1 - 2^{-|x|^d}.$$

### Relation with Other Classes

> [!theorem]
> Requires:: [[Class Ppoly]]
> 
> ---
> $\mathsf{BPP} \subseteq \mathsf{P_{/\mathsf{poly}}}$.

> [!theorem] Sipser-Gács Theorem
> Requires:: [[Level Polynomial Hierarchy]]
> 
> ---
> $\mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$.
