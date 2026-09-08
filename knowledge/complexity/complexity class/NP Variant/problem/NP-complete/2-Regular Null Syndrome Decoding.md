Reference:
- https://eprint.iacr.org/2003/230

## Definition

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.
> - $w \mid n$; block length $s = n / w$.

> [!definition] Regular and 2-Regular Words
> Split $\mathbf{x} \in \mathbb{F}_2^n$ into $w$ blocks of length $s$.
> - **Regular**: every block has weight exactly $1$. Write $\mathcal{R}$; $|\mathcal{R}| = s^w$.
> - **2-regular**: every block has weight $0$ or $2$. Write $\mathcal{R}^{(2)}$; $|\mathcal{R}^{(2)}| = \left(1 + \binom{s}{2}\right)^w$.

> [!proposition]
> $\mathcal{R}^{(2)} = \{\mathbf{x}_1 + \mathbf{x}_2 : \mathbf{x}_1, \mathbf{x}_2 \in \mathcal{R}\}$ — the 2-regular
> words are **exactly** the sums of two regular words. Per block: two $1$s in the same position cancel, in
> different positions give weight $2$; and every such pattern is reachable.

> [!definition] 2-RNSD Problem
> ### Scope
> A parity-check matrix $\mathbf{H} \in \mathbb{F}_2^{(n-k) \times n}$.
>
> ---
> ### Problem
> $\text{2-RNSD}(n, k, w)$ — find $\mathbf{x} \in \mathcal{R}^{(2)}$, $\mathbf{x} \neq \mathbf{0}$, with $\mathbf{H}\mathbf{x}^T = \mathbf{0}$.

## Property

> [!theorem] Why this problem exists
> The proposition makes the collision reduction **exact**: a collision in the regular-encoded syndrome hash is a
> pair $\mathbf{x}_1 \neq \mathbf{x}_2 \in \mathcal{R}$ with equal syndrome, $\mathbf{x}_1 + \mathbf{x}_2$ is a nonzero
> 2-RNSD solution — **and every** 2-RNSD solution arises this way. With the [[Hamming Sphere]] encoding the same
> argument only reaches [[Null Syndrome Decoding]] at weight $2w$, and the converse fails.
> **Tightness is the reason FSB encodes into regular words rather than the sphere.**