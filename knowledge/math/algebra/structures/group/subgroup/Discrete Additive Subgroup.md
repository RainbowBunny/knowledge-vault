Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_ (2016), §2.2.1 Basic Definitions: https://eprint.iacr.org/2015/939.pdf

## Definition

> [!definition] Parameters
> - $L \subseteq \mathbb R^m$: an [[Additive Subgroup]].
> - $\epsilon$: a positive real constant.
> - $\|\cdot\|$: the Euclidean norm on $\mathbb R^m$.

> [!definition] Discrete Additive Subgroup
> Extends:: [[Additive Subgroup]].
>
> ---
> An additive subgroup is called a **discrete additive subgroup** if there is a positive constant $\epsilon > 0$ with the following property: for every $\textbf{v} \in L$,
> $$L \cap \{\textbf{w} \in \mathbb R^m: ||\textbf{v} - \textbf{w}|| < \epsilon\} = \{\textbf{v}\}.$$
> `[Pei16 §2.2.1]`

> [!remark] One radius for all points
> [Pei16 §2.2.1] asks only that every $\mathbf x \in L$ have a neighborhood in $\mathbb R^m$ in which $\mathbf x$ is the only point of $L$. For an additive subgroup this is the same as the uniform condition above: since $L - \mathbf v = L$, translation by $\mathbf v$ maps $L \cap \{\mathbf w : \|\mathbf w\| < \epsilon\}$ onto $L \cap \{\mathbf w : \|\mathbf v - \mathbf w\| < \epsilon\}$, so a radius that works at $\mathbf 0$ works at every point.

## Related

### Siblings
- [[Lattices]] — the same sets: a subset of $\mathbb R^m$ is a lattice iff it is a discrete additive subgroup; [Pei16 §2.2.1] takes this as the definition of a lattice and notes that every lattice has a basis
