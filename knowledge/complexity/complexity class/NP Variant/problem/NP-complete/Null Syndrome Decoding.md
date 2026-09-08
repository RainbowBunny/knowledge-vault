Reference:
- https://ieeexplore.ieee.org/document/1055873/

## Definition

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.

> [!definition] Null Syndrome Decoding Problem
> ### Scope
> A parity-check matrix $\mathbf{H} \in \mathbb{F}_2^{(n-k) \times n}$.
>
> ---
> ### Problem
> $\mathrm{NSD}(n, k, w)$ — find $\mathbf{x} \in \mathbb{F}_2^n$ with
> $$\mathbf{x} \neq \mathbf{0}, \qquad \mathsf{wt}_\mathsf{H}(\mathbf{x}) \leq w, \qquad \mathbf{H}\mathbf{x}^T = \mathbf{0}.$$

> [!remark] It is the codeword-finding problem
> $\mathbf{H}\mathbf{x}^T = \mathbf{0}$ says exactly that $\mathbf{x}$ is a codeword of the [[Linear Code]] with
> parity-check matrix $\mathbf{H}$. NSD asks for a nonzero codeword of weight $\leq w$; deciding it for every $w$
> computes the [[Code Distance|minimum distance]].

> [!remark] No planted solution
> [[Syndrome Decoding Problem]] plants an $\mathbf{x}$ and publishes its syndrome, so a solution exists **by
> construction**. NSD publishes only $\mathbf{H}$ — a solution exists **by counting**, once the admissible set
> outgrows $2^{n-k}$. That is why the `## Distribution` block has two steps instead of three.

## Property

> [!proposition] A syndrome collision is a null word
> If $\mathbf{x}_1 \neq \mathbf{x}_2$ both have weight $\leq w$ and equal syndrome, then $\mathbf{x}_1 + \mathbf{x}_2$
> solves $\mathrm{NSD}(n, k, 2w)$. The weight **doubles**, and the converse fails — not every weight-$2w$ null word
> splits into two weight-$w$ words. [[2-Regular Null Syndrome Decoding]] is the variant where it does.

## Claim

> [!remark]
> NP-complete: BMvT's **subspace weights** problem, companion to the *coset weights* problem behind
> [[Syndrome Decoding Problem]]. Same two caveats — worst case, and $w$ part of the input.