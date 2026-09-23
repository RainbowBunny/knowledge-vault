## Definition

> [!definition] Parameters
> - $n$: Number of variables.
> - $\mathbb{F}$: [[Field]].

> [!definition] Scope 
> A [[Function]] $f: \{0, 1\}^n \rightarrow \mathbb F$.

> [!definition] Multilinear Lagrange Basis
> We define the set $\{\chi_w \mid w \in \{0, 1\}^n\}$ with:
>  $$\chi_w(x_1, \dots, x_n) = \prod_{i = 1}^n (x_i w_i + (1 - x_i)(1 - w_i))$$
> as the set of [[Multilinear Polynomial|Multilinear Lagrange Basis Polynomial]] with interpolating set $\{0, 1\}^n.$

> [!scheme] Multilinear Extension of Function
> The following [[Multilinear Polynomial]] is the Multilinear Extension (MLE) of function $f$: 
> $$\tilde{f}(x_1, \dots, x_n) = \sum_{w \in \{0, 1\}^n} f(w) \cdot \chi_w(x_1, \dots, x_n).$$

## Property

> [!lemma]
> Fix a positive integer $v$ and let $n = 2^v$. Given as input $f(w)$ for all $w \in \{0, 1\}^v$ and a vector $r \in \mathbb F^{\log n}$, $\mathcal V$ can compute $\tilde f(r)$ in $O(\log n)$ words of space with a single streaming pass over the input (regardless of the order in which the $f(w)$ values are presented).

> [!lemma]
> Fix a positive integer $v$, and let $n = 2^v$. Given as input $f(w)$ for all $w \in \{0, 1\}^v$ and a vector $r = (r_1, \dots, r_v) \in \mathbb F^{\log n}$, $\mathcal V$ can compute $\tilde f(r)$ in $O(n)$ time and $O(n)$ space.
