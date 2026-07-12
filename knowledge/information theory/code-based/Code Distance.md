## Distance of a code

> [!definition] Minimum Distance
> For a code $\mathcal C$ containing at least two words, the **(minimum) distance** of $\mathcal C$, denoted by $d(\mathcal C)$, is $$d(\mathcal C) = \min\{d(x, y) : x, y \in C, x \neq y\}.$$

> [!definition] Parameters of the Code 
> A code of length $n$, size $M$ and distance $d$ referred to as an $(n, M, d)$-code. The numbers $n, M$ and $d$ are called the **parameters** of the code.

> [!remark] Generalized metric
> The distance $d(\cdot, \cdot)$ above is the Hamming distance. In code-based cryptography the definition is often stated for a code over a ring $\mathcal R$ with an arbitrary norm $\omega$: $$d = \min_{u, v \in C,\, u \neq v} \omega(u - v),$$ recovering the Hamming case with $\omega = \text{wt}$. An $[n, k, d]$-code can correct arbitrary patterns of up to $\lfloor (d-1)/2 \rfloor$ errors (theorem below).

> [!definition] $u$-error-detecting
> Let $u$ be a positive integer. A code $\mathcal C$ is **$u$-error-detecting** if, whenever a codeword incurs at least one but at most $u$ errors, the resulting word is not a code word. A code $C$ is **exactly $u$-error-detecting** if it is $u$-error detecting but not $(u + 1)$-error-detecting.

> [!theorem]
> A code $\mathcal C$ is $u$-error-detecting if and only if $d(\mathcal C) \geq u + 1$; i.e., a code with distance $d$ is an exactly $(d - 1)$-error-detecting.

> [!definition] $v$-error-correcting
> Let $v$ be a positive integer. A code $\mathcal C$ is **$v$-error-correcting** if minimum distance decoding is able to correct $v$ or fewer errors, assuming that the incomplete decoding rule is used. A code $\mathcal C$ is **exactly $v$-error-correcting** if it is $v$-error correcting but not $(v + 1)$-error correcting. This definition is also called the **packing radius**.

> [!theorem]
> Let $\mathcal C$ be an $[n, k, d]$ code over $\mathbb F_q$. The following hold:
> 1. The packing radius of $\mathcal C$ equals $t = \lfloor (d - 1) / 2 \rfloor$.
> 2. The packing radius $t$ of $\mathcal C$ is characterized by the property that nearest neighbor decoding always decodes correctly a received vector in which $t$ or fewer errors have occurred but will not always decode correctly a received vector in which $t + 1$ errors have occurred.

## Hamming Distance

> [!definition] Hamming Distance
> Let $x$ and $y$ be words of length $n$ over the alphabet $A$. The **(Hamming) distance** from $x$ to $y$, denoted by $d(x, y)$, is defined to be the number of places at which $x$ and $y$ differ. If $x = x_1 \cdots x_n$ and $y = y_1 \cdots y_n$, then $$d(x, y) = d(x_1, y_1) + \cdots + d(x_n, y_n),$$ where $x_i$ and $y_i$ are regarded as words of length $1$, and $$d(x_i, y_i) = \begin{cases}1 &\text{ if } x_i \neq y_i \\ 0 &\text{ if } x_i = y_i\end{cases}$$

> [!proposition]
> Let $x, y, z$ be words of length $n$ over $A$. Then we have
> 1. (Non-negativity) $0 \leq d(x, y) \leq n$,
> 2. $d(x, y) = 0$ if and only if $x = y$,
> 3. (Symmetry) $d(x, y) = d(y, x)$
> 4. (Triangle inequality) $d(x, z) \leq d(x, y) + d(y, z)$.

> [!theorem]
> If $x, y \in \mathbb F_q^n$, then $d(x, y) = \text{wt}(x - y)$. If $\mathcal C$ is a [[Linear Code]], the minimum distance is the same as the minimum weight of the nonzero codewords of $\mathcal C$.

## Weight of a Code

