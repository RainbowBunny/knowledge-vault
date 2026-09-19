Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.1: Warmup: Interactive proofs with deterministic verifier and prover.

## Definition

> [!definition] Deterministic Function Interaction
> Let $f, g: \{0, 1\}^* \rightarrow \{0, 1\}^*$ be [[Function]] and $k \geq 0$ be an integer (allowed to depend upon the input size). A $k$**-round interaction** of $f$ and $g$ on input $x \in \{0, 1\}^*$, denoted by $\langle f, g \rangle (x)$ is the sequence of strings $a_1, \dots, a_k \in \{0, 1\}^*$ defined as follows:
> $$\begin{align}
> a_1 &= f(x) \\
> a_2 &= g(x, a_1) \\
>     &\cdots \\
> a_{2i + 1} &= f(x, a_1, \dots, a_{2i}) \quad \text{for} \; 2i < k \\
> a_{2i + 2} &= g(x, a_1, \dots, a_{2i + 1}) \quad \text{for} \; 2i + 1 < k
> \end{align}$$
> The **output** of $f$ at the end of the interaction denoted $\mathsf{out}_f \langle f, g \rangle (x)$ is defined to be $f(x, a_1, \dots, a_k) \in \{0, 1\}$.


