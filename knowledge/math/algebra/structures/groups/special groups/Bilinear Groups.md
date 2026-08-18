Reference: https://eprint.iacr.org/2016/260.pdf

## Basic Definition

> [!definition] Bilinear Groups
> Bilinear groups $\mathcal{BG}$ is a tuple $(p, \mathbb G_1, \mathbb G_2, \mathbb G_T, e, g_1, g_2)$ with the following properties:
> - $\mathbb G_1, \mathbb G_2, \mathbb G_T$ are groups of prime order $p$.
> - The pairing $e: \mathbb G_1 \times \mathbb G_2 \rightarrow \mathbb G_T$ is a [[Bilinear]] map.
> - $g_1$ is a generator for $\mathbb G_1$, $g_2$ is a generator for $\mathbb G_2$, and $e(g_1, g_2)$ is a generator for $\mathbb G_T$.

> [!definition] Generic Group Operations 
> There are efficient algorithms for:
> - Computing group operations.
> - Evaluating the bilinear map.
> - Deciding membership of the groups.
> - Deciding equality of group elements.
> - Sampling generators of the groups.

### Type I

> [!definition] Type I Bilinear Groups
> - $\mathbb G_1 = \mathbb G_2$

### Type II

> [!definition] Type II Bilinear Groups
> - There is an efficiently computable non-trivial homomorphism $\Psi: \mathbb G_2 \rightarrow \mathbb G_1$.

### Type III

> [!definition] Type III Bilinear Groups
> - There is no efficiently computable non-trivial homomorphism exists in either direction between $\mathbb G_1$ and $\mathbb G_2$.


