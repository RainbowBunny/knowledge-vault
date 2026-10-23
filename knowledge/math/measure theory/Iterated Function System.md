---
aliases: [IFS]
---
Reference:
- `[Hut]` — J. E. Hutchinson, _Fractals and self-similarity_, Indiana Univ. Math. J. 30 (1981): https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf
- `[BQ]` — Y. Benoist, J.-F. Quint, _Introduction to Random Walks on Homogeneous Spaces_, 10th Takagi Lectures, Kyoto (2012): https://www.imo.universite-paris-saclay.fr/~benoist/prepubli/12takagi.pdf

## Definition

> [!definition] Parameters
> - $(X, d)$: a complete [[Metric Space]].
> - $\mathcal S = \{S_1, \dots, S_N\}$: a set of [[Contraction|contraction maps]] on $X$; $r_i = \mathrm{Lip}\, S_i < 1$.
>
> `[Hut §3]`

> [!definition] Iterated Function System
> A finite set $\mathcal S = \{S_1, \dots, S_N\}$ of contraction maps on a complete metric space. For $A \subseteq X$ let $\mathcal S(A) = \bigcup_{i=1}^N S_i(A)$; $A$ is **invariant** (with respect to $\mathcal S$) if $A = \mathcal S(A)$. `[Hut §3, 3.1(1)–(2)]`

## Property

> [!theorem] Hutchinson's theorem — every IFS has exactly one compact invariant set, its attractor
> There is a unique closed bounded set $K$ invariant with respect to $\mathcal S$; it is compact. `[Hut 3.1(3)(i)]` Moreover $K$ is the closure of the set of fixed points of the compositions $S_{i_1} \circ \cdots \circ S_{i_p}$ `[3.1(3)(v)]`, and the coding map from sequences in $\{1, \dots, N\}^{\mathbb N}$ onto $K$ is continuous and surjective `[3.1(3)(vii)]`. `[Hut]` writes $|\mathcal S|$ for $K$ `[3.1(6)]`.
>
> ---
> *Why.* On the class $\mathcal B$ of nonempty closed bounded subsets of $X$, the Hausdorff metric $\delta(A, B) = \sup\{d(a, B), d(b, A) : a \in A, b \in B\}$ is complete `[Hut 2.4]`, and $\mathcal S$ is a contraction on $(\mathcal B, \delta)$ with constant $\max_i r_i$ `[Hut 3.2(1)]`. The [[Contraction#Banach fixed-point theorem|Banach fixed-point theorem]] then gives existence and uniqueness of $K$.

> [!theorem] Invariant measure — weights give one invariant probability measure, supported on $K$
> Let $\rho_i \in (0, 1)$ with $\sum_i \rho_i = 1$, and $(\mathcal S, \rho)(\nu) = \sum_{i=1}^N \rho_i\, S_{i\#}\nu$. Then $(\mathcal S, \rho)$ is a contraction on the probability measures with bounded support, in the metric $L(\mu, \nu) = \sup\{\mu(\varphi) - \nu(\varphi) : \mathrm{Lip}\, \varphi \leq 1\}$; there is a unique $\mu$ with $(\mathcal S, \rho)\mu = \mu$, the iterates $(\mathcal S, \rho)^p(\nu)$ converge to it, and its support is $K$. `[Hut 4.2–4.4]`
>
> This $\mu$ is the [[Stationary Measure|stationary measure]] of the random walk that applies $S_i$ with probability $\rho_i$.

> [!remark] Hutchinson's measures
> `[Hut 2.5]` follows Federer: a "measure" is defined on all subsets and is countably subadditive, and he works with Borel regular measures of bounded support and finite mass.

## Example

> [!example] The Cantor set
> On $[0, 1]$, $\mathcal S = \{x/3, (x + 2)/3\}$. The Cantor set $K = \{\sum_{i \geq 1} 2b_i 3^{-i} : b_i \in \{0, 1\}\}$ is closed `[BQ §3.5]` and bounded, and $K = S_1(K) \cup S_2(K)$, since $S_1$ and $S_2$ put a first digit $b = 0$ or $b = 1$ in front. So $K$ is the attractor; with weights $\frac12, \frac12$ the invariant measure is the one in [[Stationary Measure#Example]].

## Related

### Used by
- [[Stationary Measure]] — the invariant measure above is a stationary measure

### Prerequisites
- [[Contraction]], [[Lipschitz Map]], [[Metric Space]]
