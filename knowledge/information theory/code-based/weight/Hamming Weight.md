## Definition

> [!definition] Hamming Weight
> Let $x$ be words of length $n$ over the alphabet $A$. The **(Hamming) weight** of $x$, denoted $\mathsf{wt}_\mathsf{H}(x)$ is the number of non-zero position. If $x = x_1 \cdots x_n$, then
> $$\mathsf{wt}_\mathsf{H}(x) = |\{i : i \in [n] \land x_i \neq 0\}|$$

## Property

> [!remark] Bridge to Power Set Ring
> $\mathrm{supp}: \mathbb{F}_2^n \rightarrow \mathcal{P}([n]) := \{i \in [n] : z_i = 1\}$.
> - The indicator map $T \mapsto \mathbf{1}_T$ and $\mathrm{supp}$ are mutually inverse.
> - $\mathrm{supp}$ defines a [[Ring Homomorphism|Ring Isomorphism]] between $(\mathbb{F}_2^n, \oplus, \circ)$ and [[Power Set Ring]] $(\mathcal{P}([n]), \Delta, \cap)$.
> - $\mathsf{wt}_\mathsf{H}(z) = |\mathrm{supp}(z)|$.
