## Definition

> [!definition] Hamming Weight
> Let $x$ be words of length $n$ over the alphabet $A$. The **(Hamming) weight** of $x$, denoted $\mathsf{wt}_\mathsf{H}(x)$ is the number of non-zero position. If $x = x_1 \cdots x_n$, then
> $$\mathsf{wt}_\mathsf{H}(x) = |\{i : i \in [n] \land x_i \neq 0\}|$$

## Property

> [!remark] Bridge to Power Set Ring
> Let $\mathrm{supp}: \mathbb{F}_2^n \rightarrow \mathcal{P}([n])$ and the indicator map $T \mapsto \mathbf{1}_T$ are mutually inverse.
> Thus, we have a [[Ring Homomorphism|Ring Isomorphism]] between $(\mathbb{F}_2^n, \oplus, \cdot)$ and [[Power Set Ring]] $(\mathcal{P}([n]), \Delta, \cap)$.
