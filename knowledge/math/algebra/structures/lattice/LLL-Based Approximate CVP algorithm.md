Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (2nd ed., Springer 2014), chapter on lattices: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 18 (Thm 18.1.6, Thm 18.2.1): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch18.pdf

## Definition

> [!definition] Parameters
> - $n$: the dimension of the lattice.
> - $C > 1$: an absolute constant.

> [!algorithm] LLL-Based Approximate CVP Algorithm
> - $v \leftarrow \mathsf{ApprCVP}(v_1, \dots, v_n; w)$: Deterministic approximate closest vector algorithm.
>     - **Input**: a basis $(v_1, v_2, \ldots, v_n)$ of a lattice $L \subset \mathbb{R}^n$; a target vector $w \in \mathbb{R}^n$.
>     - **Output**: a lattice vector $v \in L$ such that $$\|w - v\| \le C^n \cdot \min_{u \in L} \|w - u\|,$$ for some absolute constant $C > 1$.
>     - **Steps**:
>         1. Apply the [[LLL Lattice Reduction Algorithm|LLL lattice reduction algorithm]] to the basis $(v_1, v_2, \ldots, v_n)$ to obtain an LLL-reduced basis.
>         2. Using the LLL-reduced basis, apply [[Babai's Algorithm|Babai’s closest vertex algorithm]] to compute a lattice vector $v \in L$ close to the target vector $w$.
>         3. Return the lattice vector $v$.
>
> `[HPS]`

## Property

> [!theorem] Babai's rounding bound — on an LLL-reduced basis, rounding is within $1 + 2n(9/2)^{n/2}$ of the closest vector
> Let $(v_1, \dots, v_n)$ be LLL-reduced (with $\delta = 3/4$) and let $v$ be the output of Babai's rounding on target $w$. Then for all $u \in L$ $$\|w - v\| \leq \big(1 + 2n (9/2)^{n/2}\big) \|w - u\|,$$ a bound of the form $C^n$ of the Output. Babai's nearest plane algorithm on the same basis gives the factor $2^{n/2}$.
>
> `[Gal12 Thm 18.2.1, Thm 18.1.6]`

## Related

### Prerequisites
- [[LLL Lattice Reduction Algorithm]] — step 1
- [[Babai's Algorithm]] — step 2

### Siblings
- [[Lattice Problem]] — $\text{apprSVP}$, the shortest-vector counterpart, which LLL alone solves within $2^{(n-1)/2}$
