## Definition


## Property

### Multilinear

> [!definition] Multilinear
> A multivariate polynomial $g$ is **multilinear** if the degree of the polynomial in each variable is at most one.

> [!proposition]
> Any function $f: \{0, 1\}^v \rightarrow \mathbb F$ has a unique multilinear extension (MLE) over $\mathbb F$, and we reserve the notation $\tilde f$ for this special extension of $f$.

> [!lemma] Lagrange Interpolation of Multilinear Polynomials
> Let $f: \{0, 1\}^v \rightarrow \mathbb F$ be any function. Then, the following multilinear polynomial $\tilde f$ extends $f$: 
> $$\tilde f(x_1, \dots, x_v) = \sum_{w \in \{0, 1\}^v} f(w) \cdot \chi_w(x_1, \dots, x_v),$$
> where, for any $w = (w_1, \dots, w_v)$,
> $$\chi_w(x_1, \dots, x_v) = \prod_{i = 1}^v (x_i w_i + (1 - x_i)(1 - w_i)).$$
> The set $\{\chi_w: w \in \{0, 1\}^v\}$ is referred to as the set of multilinear Lagrange basis polynomial with interpolating set $\{0, 1\}^v$.

> [!lemma]
> Fix a positive integer $v$ and let $n = 2^v$. Given as input $f(w)$ for all $w \in \{0, 1\}^v$ and a vector $r \in \mathbb F^{\log n}$, $\mathcal V$ can compute $\tilde f(r)$ in $O(\log n)$ words of space with a single streaming pass over the input (regardless of the order in which the $f(w)$ values are presented).

> [!lemma]
> Fix a positive integer $v$, and let $n = 2^v$. Given as input $f(w)$ for all $w \in \{0, 1\}^v$ and a vector $r = (r_1, \dots, r_v) \in \mathbb F^{\log n}$, $\mathcal V$ can compute $\tilde f(r)$ in $O(n)$ time and $O(n)$ space.

