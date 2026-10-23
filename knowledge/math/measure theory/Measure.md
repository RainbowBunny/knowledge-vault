Reference:
- `[Bas]` — R. F. Bass, _Real Analysis for Graduate Students_, version 5.0 (2024), free from the author's page: https://r-bass.scholar.uconn.edu/
- `[LG]` — J.-F. Le Gall, _Intégration, Probabilités et Processus Aléatoires_, course notes (ENS): https://www.imo.universite-paris-saclay.fr/~jean-francois.le-gall/IPPA2.pdf
- `[Tao]` — T. Tao, _254A Notes 0: A review of probability theory_ (2010), §2: https://terrytao.wordpress.com/2010/01/01/254a-notes-0-a-review-of-probability-theory/
- `[Hut]` — J. E. Hutchinson, _Fractals and self-similarity_, Indiana Univ. Math. J. 30 (1981): https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf

## Definition

> [!definition] Parameters
> - $(X, \mathcal A)$: a set with a [[Sigma Algebra]] $\mathcal A$ on it.

> [!definition] Measure
> A **measure** on $(X, \mathcal A)$ is a function $\mu: \mathcal A \to [0, \infty]$ such that
> 1. $\mu(\emptyset) = 0$;
> 2. if $A_i \in \mathcal A$, $i = 1, 2, \dots$, are pairwise disjoint, then $\mu\big(\bigcup_{i=1}^\infty A_i\big) = \sum_{i=1}^\infty \mu(A_i)$.
>
> The triple $(X, \mathcal A, \mu)$ is a **measure space**. `[Bas Def 3.1]`

> [!definition] Probability Measure
> A **probability** or **probability measure** is a measure $\mu$ with $\mu(X) = 1$. `[Bas §3.1]`

> [!example] Finite probability
> The [[Probability]] of this vault is the case $X = \Omega$ finite, $\mathcal A = \mathcal P(\Omega)$, and $\mu(E) = \sum_{\omega \in E} P(\omega)$; countable additivity holds because a disjoint union over a finite set has only finitely many nonempty pieces.

### Push-forward Measure

> [!definition] Parameters
> - $(E, \mathcal A, \mu)$: a measure space. $(F, \mathcal B)$: a set with a σ-algebra.
> - $f: E \to F$ measurable: $f^{-1}(B) \in \mathcal A$ for every $B \in \mathcal B$.

> [!definition] Push-forward Measure
> The **image measure** of $\mu$ by $f$ is the measure on $(F, \mathcal B)$
> $$f_*\mu(B) = \mu\big(f^{-1}(B)\big), \qquad B \in \mathcal B.$$
> `[LG Déf 1.3.2]` writes $f(\mu)$; `[Hut 2.5(3)]` writes $f_\#\mu$; *push-forward* and $f_*\mu$ are the names in `[Tao §2]`.

> [!example] The law of a random variable
> For a random variable $X$ on a probability space $(\Omega, \mathcal F, P)$, its distribution $\mu_X(S) = P(X \in S)$ is the push-forward $X_* P$. `[Tao §2]`

## Property

> [!proposition] Change of variables — $\int g \, d(f_*\mu) = \int g \circ f \, d\mu$
> For every measurable $g: F \to [0, \infty]$,
> $$\int_F g \, d(f_*\mu) = \int_E g \circ f \, d\mu,$$
> and a real $g$ is $f_*\mu$-integrable iff $g \circ f$ is $\mu$-integrable, with equal integrals.
>
> ---
> *Proof.* For $g = \mathbf 1_B$ both sides are $\mu(f^{-1}(B))$, because $\mathbf 1_B \circ f = \mathbf 1_{f^{-1}(B)}$. Both sides are linear in $g$, so the formula holds for simple functions; an increasing sequence of simple functions converging to $g$ and the monotone convergence theorem give it for nonnegative $g$; and $g = g^+ - g^-$ gives the integrable case. `[Hut 2.5(3)]` states it for bounded continuous $g$: $f_\#\mu(\varphi) = \mu(\varphi \circ f)$.

## Related

### Descendants
- [[Stationary Measure]] — a measure unchanged by a random push-forward

### Prerequisites
- [[Sigma Algebra]], [[Probability]]
