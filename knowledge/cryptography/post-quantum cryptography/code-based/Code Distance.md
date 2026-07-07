## Distance of a code

> [!definition] Minimum Distance
> For a code $C$ containing at least two words, the **(minimum) distance** of $C$, denoted by $d(C)$, is $$d(C) = \min\{d(x, y) : x, y \in C, x \neq y\}.$$

> [!definition] Parameters of the Code 
> A code of length $n$, size $M$ and distance $d$ referred to as an $(n, M, d)$-code. The numbers $n, M$ and $d$ are called the **parameters** of the code.

> [!remark] Generalized metric
> The distance $d(\cdot, \cdot)$ above is the Hamming distance. In code-based cryptography the definition is often stated for a code over a ring $\mathcal R$ with an arbitrary norm $\omega$: $$d = \min_{u, v \in C,\, u \neq v} \omega(u - v),$$ recovering the Hamming case with $\omega = \text{wt}$. An $[n, k, d]$-code can correct arbitrary patterns of up to $\lfloor (d-1)/2 \rfloor$ errors (theorem below).

> [!definition] $u$-error-detecting
> Let $u$ be a positive integer. A code $C$ is **$u$-error-detecting** if, whenever a codeword incurs at least one but at most $u$ errors, the resulting word is not a code word. A code $C$ is **exactly $u$-error-detecting** if it is $u$-error detecting but not $(u + 1)$-error-detecting.

> [!theorem]
> A code $C$ is $u$-error-detecting if and only if $d(C) \geq u + 1$; i.e., a code with distance $d$ is an exactly $(d - 1)$-error-detecting.

> [!definition] $v$-error-correcting
> Let $v$ be a positive integer. A code $C$ is **$v$-error-correcting** if minimum distance decoding is able to correct $v$ or fewer errors, assuming that the incomplete decoding rule is used. A code $C$ is **exactly $v$-error-correcting** if it is $v$-error correcting but not $(v + 1)$-error correcting.

> [!theorem]
> A code $C$ is $v$-error-correcting if and only if $d(C) \geq 2v + 1$; i.e., a code with distance $d$ is an exactly $\lfloor (d - 1) / 2 \rfloor$-error-correcting code.

### Hamming Distance

> [!definition] Hamming Distance
> Let $x$ and $y$ be words of length $n$ over the alphabet $A$. The **(Hamming) distance** from $x$ to $y$, denoted by $d(x, y)$, is defined to be the number of places at which $x$ and $y$ differ. If $x = x_1 \cdots x_n$ and $y = y_1 \cdots y_n$, then $$d(x, y) = d(x_1, y_1) + \cdots + d(x_n, y_n),$$ where $x_i$ and $y_i$ are regarded as words of length $1$, and $$d(x_i, y_i) = \begin{cases}1 &\text{ if } x_i \neq y_i \\ 0 &\text{ if } x_i = y_i\end{cases}$$

> [!proposition]
> Let $x, y, z$ be words of length $n$ over $A$. Then we have
> 1. $0 \leq d(x, y) \leq n$,
> 2. $d(x, y) = 0$ if and only if $x = y$,
> 3. $d(x, y) = d(y, x)$
> 4. (Triangle inequality) $d(x, z) \leq d(x, y) + d(y, z)$.

## Weight of a Code

