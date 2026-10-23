Reference:
- `[Vai]` — V. Vaikuntanathan, _CS 294: Worst-case to Average-case Reduction for SIS and LWE_, lecture 3 notes (Lemma 2, Lemma 3): https://people.csail.mit.edu/vinodv/CS294/lecture3.pdf
- `[Reg04]` — O. Regev, _Lattices in Computer Science_, lecture notes (Tel Aviv University, Fall 2004), L9 Dual lattices (Claims 3–5): https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/DualLattice.pdf
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 16, Def 16.1.22: https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch16.pdf

## Definition

> [!definition] Parameters
> - $n$: the rank of $\mathcal L$.
> - $\mathcal L \subset \mathbb R^n$: a full-rank [[Lattices|lattice]].
> - $\langle \cdot, \cdot \rangle$: the Euclidean inner product on $\mathbb R^n$.

> [!definition] Lattice Duality
> For a rank-$n$ lattice $\mathcal L$, its dual denoted $\mathcal L^*$ is defined as
> $$\mathcal L^* = \{x \in \mathbb R^n : \forall y \in \mathcal L, \langle x, y \rangle \in \mathbb Z\}$$
>
> `[Vai]` `[Reg04 L9]` `[Gal12 Def 16.1.22]`

> [!remark] Lattices that are not full rank
> For a lattice $\mathcal L \subset \mathbb R^m$ of rank $n < m$, $x$ ranges over $\operatorname{span}(\mathcal L)$ instead of $\mathbb R^m$ `[Reg04 L9]` `[Gal12 Def 16.1.22]`.

### Dual Lattice Vector

> [!definition] Parameters
> - $x \in \mathcal L^*$: a dual lattice vector.
> - $\phi_x : \mathcal L \rightarrow \mathbb Z$, $y \mapsto \langle x, y \rangle$: the linear function it defines.

> [!definition] Dual Lattice Vector
> Each dual lattice vector $x$ corresponds to a linear function $\phi_x: \mathcal L \rightarrow \mathbb Z$ and the dual lattice corresponds to a basis of the space of such linear functions.
>
> `[Vai]`

## Property

> [!lemma] Weak transference — $\lambda_1(\mathcal L^*) \cdot \lambda_1(\mathcal L) \leq n$
> For any rank-$n$ lattice $\mathcal L$, $\lambda_1(\mathcal L^*) \cdot \lambda_1(\mathcal L) \leq n$.
>
> `[Vai Lem 2]` `[Reg04 L9 Claim 4]`

> [!lemma] Lower transference — $\lambda_n(\mathcal L^*) \cdot \lambda_1(\mathcal L) \geq 1$
> For any rank-$n$ lattice $\mathcal L$, $\lambda_n(\mathcal L^*) \cdot \lambda_1(\mathcal L) \geq 1$.
>
> `[Vai Lem 3]` `[Reg04 L9 Claim 5]`

## Related

### Prerequisites
- [[Lattices]] — the successive minima $\lambda_i$ ([[Lattices#Successive Minima]])

### Constructions
- [[Lattices#Smoothing Parameter]] — defined through the Gaussian mass of $\mathcal L^* \setminus \{0\}$
- [[Lattices#Transference]] — Banaszczyk's theorem $1 \leq \lambda_i(\mathcal L) \cdot \lambda_{n-i+1}(\mathcal L^*) \leq n$, which contains both lemmas above
