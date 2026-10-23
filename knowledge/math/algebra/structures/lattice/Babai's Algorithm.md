Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (2nd ed., Springer 2014), chapter on lattices: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 18, §18.1 (Babai's nearest plane algorithm, Thm 18.1.6), §18.2 (Babai's rounding technique): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch18.pdf
- `[Reg04]` — O. Regev, _Lattices in Computer Science_, lecture notes (Tel Aviv University, Fall 2004), L3 Babai's nearest plane algorithm (Lemma 6): https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/cvp.pdf

## Definition

> [!definition] Parameters
> - $n$: the dimension of the lattice.
> - $\lfloor \cdot \rceil$: rounding to the nearest integer.

> [!algorithm] Babai’s Closest Vertex Algorithm
> - $v \leftarrow \mathsf{Babai}(v_1, \dots, v_n; w)$: Deterministic closest vertex (rounding) algorithm.
>     - **Input**: a basis $(v_1, v_2, \ldots, v_n)$ of a lattice $L \subset \mathbb{R}^n$; a target vector $w \in \mathbb{R}^n$.
>     - **Output**: a lattice vector $v \in L$ approximating the closest lattice vector to $w$.
>     - **Steps**:
>         1. Express the target vector in the basis: $$w = t_1 v_1 + t_2 v_2 + \cdots + t_n v_n,$$ where $t_1, t_2, \ldots, t_n \in \mathbb{R}$.
>         2. For each $i = 1, 2, \ldots, n$, set: $$a_i \gets \lfloor t_i \rceil,$$ where $\lfloor \cdot \rceil$ denotes rounding to the nearest integer.
>         3. Return the lattice vector: $$v \gets a_1 v_1 + a_2 v_2 + \cdots + a_n v_n.$$
>
> `[HPS]` `[Gal12 §18.2]`

## Related

### Constructions
- [[LLL-Based Approximate CVP algorithm]] — runs this algorithm on an LLL-reduced basis, which bounds the error by $C^n$

### Prerequisites
- [[Lattices]] — bases and fundamental domains: the output is a vertex of the translate of $\mathcal F(v_1, \dots, v_n)$ that contains $w$, chosen by rounding each coordinate

### Siblings
- Babai's nearest plane algorithm (no note) — rounds against the Gram–Schmidt vectors one coordinate at a time, from $v_n$ down to $v_1$; on an LLL-reduced basis it is within $2^{n/2}$ of the closest vector `[Gal12 Thm 18.1.6]` `[Reg04 L3 Lem 6]`
