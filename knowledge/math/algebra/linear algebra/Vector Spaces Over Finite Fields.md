Reference:
- `[Ax]` — S. Axler, _Linear Algebra Done Right_, 4th ed. (2024, open access): https://linear.axler.net/ — §1B, §2B. Numbers checked in the chapter PDFs at https://link.springer.com/book/10.1007/978-3-031-41026-0.
- `[Rud11]` — A. Rudra, _Error Correcting Codes: Combinatorics, Algorithms and Applications_ (Spring 2011), Lecture 7: Dual of a linear subspace: https://cse.buffalo.edu/faculty/atri/courses/coding-theory/spr11/lectures/lect7.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - $q$: a prime power.
> - $\mathbb F_q$: the finite [[Field]] with $q$ elements.
> - $V$: a set with an addition and a scalar multiplication by $\mathbb F_q$.

> [!definition] Vector Space Over $\mathbb F_q$
> Extends:: [[Vector Spaces]].
>
> ---
> A **vector space over $\mathbb F_q$** is a [[Vector Spaces|vector space]] whose field of scalars is the finite field $\mathbb F_q$. `[Ax 1.20]`

### Inner Product on $\mathbb F_q^n$

> [!definition] Parameters
> - $n$: a positive integer.
> - $\langle, \rangle : \mathbb F_q^n \times \mathbb F_q^n \rightarrow \mathbb F_q$: a pairing.

> [!definition] Inner Product on $\mathbb F_q^n$
> An inner product on $\mathbb F_q^n$ is a pairing $\langle, \rangle : \mathbb F_q^n \times \mathbb F_q^n \rightarrow \mathbb F_q$ satisfying the following conditions: for all $u, v, w \in \mathbb F_q^n$
> - $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$;
> - $\langle u, v + w \rangle = \langle u, v \rangle + \langle u, w \rangle$;
> - $\langle u, v \rangle = 0$ for all $u \in \mathbb F_q^n$ if and only if $v = 0$;
> - $\langle u, v \rangle = 0$ for all $v \in \mathbb F_q^n$ if and only if $u = 0$;
>
> `[cf. Rud11 §2]` (the scalar product below)
> ⚠️ CLAUDE – verify: no condition on scalars ($\langle au, v \rangle = a \langle u, v \rangle = \langle u, av \rangle$) is listed. Additivity gives it only for $a \in \mathbb F_p$, so for $q$ not prime a scalar condition seems to be missing. Check against the source of this definition.

> [!definition] Parameters
> - $v = (v_1, \dots, v_n) \in \mathbb F_q^n$: a vector.
> - $w = (w_1, \dots, w_n) \in \mathbb F_q^n$: a vector.
> - $S \subseteq \mathbb F_q^n$: a subset.

> [!definition] Scalar Product and Orthogonal
> Let $v = (v_1, \dots, v_n), w = (w_1, \dots, w_n) \in \mathbb F_q^n$.
> 1. The **scalar product** of $v$ and $w$ is defined as $$v \cdot w = \sum_{i = 1}^n v_i w_i \in \mathbb F_q$$ is an inner product.
> 2. Two vectors $v$ and $w$ are said to be **orthogonal** if $v \cdot w = 0$.
> 3. Let $S$ be a nonempty subset of $\mathbb F_q^n$. The **orthogonal complement** $S^{\perp}$ of $S$ is defined to be $$S^\perp = \{v \in \mathbb F_q^n : v \cdot s = 0 \; \forall s \in S\}.$$ If $S = \emptyset$, then we define $S^{\perp} = \mathbb F_q^n$.
>
> `[Rud11 §2]`

> [!theorem] $\dim \langle S \rangle + \dim S^{\perp} = n$
> Let $S$ be a subset of $\mathbb F_q^n$, then we have $$\dim(\langle S \rangle) + \dim(S^{\perp}) = n.$$ `[Rud11 Thm 2.3]` (stated for subspaces; $S^\perp = \langle S \rangle^\perp$)

## Property

> [!definition] Parameters
> - $V$: a vector space over $\mathbb F_q$ with $\dim V = k$.

> [!theorem] Counting — $q^k$ vectors and $\frac{1}{k!}\prod_{i=0}^{k-1}(q^k - q^i)$ bases
> Let $V$ be a vector space over $\mathbb F_q$. If $\dim(V) = k$, then
> 1. $V$ has $q^k$ elements;
> 2. $V$ has $\frac{1}{k!} \prod_{i = 0}^{k - 1} (q^k - q^i)$ different bases.
>
> `[Ax 2.28]` (each vector has unique coordinates in $\mathbb F_q^k$; for item 2 choose $v_{i+1} \notin \operatorname{span}(v_1, \dots, v_i)$, which has $q^i$ elements, and divide by the $k!$ orderings)

## Related

### Siblings
- [[Inner-Product Spaces]] — over $\mathbb R$ or $\mathbb C$ the inner product is positive definite; over $\mathbb F_q$ a nonzero vector can be orthogonal to itself, so $S \cap S^\perp \neq \{0\}$ is possible
- [[Lattices]] — for prime $q$, the [[Lattices#$q$-ary Lattices|$q$-ary lattices]] $\Lambda_q(A)$ and $\Lambda_q^\perp(A)$ are the integer preimages of the column space of $A$ and of its orthogonal complement $S^\perp$ in $\mathbb F_q^l$

### Prerequisites
- [[Vector Spaces]] — the general definition
- [[Field]] — finite fields $\mathbb F_q$
- [[Modular Arithmetic]] — $\mathbb F_p = \mathbb Z / p\mathbb Z$
