Reference:
- `[BQ]` — Y. Benoist, J.-F. Quint, _Introduction to Random Walks on Homogeneous Spaces_, 10th Takagi Lectures, Kyoto (2012): https://www.imo.universite-paris-saclay.fr/~benoist/prepubli/12takagi.pdf
- `[Hut]` — J. E. Hutchinson, _Fractals and self-similarity_, Indiana Univ. Math. J. 30 (1981): https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf

## Definition

> [!definition] Parameters
> - $X$: a locally compact metric space, with its [[Sigma Algebra#Borel Sigma Algebra|Borel σ-algebra]]; all measures are Borel. $\mathcal P(X)$: the probability measures on $X$.
> - $A$: a finite set of continuous transformations of $X$; $\Gamma$: the [[Semigroup]] they generate.
> - $\mu$: a probability measure on $A$ — the law of one step. For $g \in A$, $g_*\nu$ is the [[Measure#Push-forward Measure|push-forward]] of $\nu$ by $g$.
>
> `[BQ §1.1–1.2]`

> [!definition] Convolution
> For a measure $\nu$ on $X$, the **convolution** $\mu * \nu$ is the average of the translates of $\nu$:
> $$\mu * \nu = \int_A g_*\nu \; d\mu(g).$$
> `[BQ §1.2]`

> [!definition] Stationary Measure
> A measure $\nu$ on $X$ is **$\mu$-stationary** if $\mu * \nu = \nu$. `[BQ §1.2]`
>
> On a Borel set $E$, using $g_*\nu(E) = \nu(g^{-1}(E))$: $\;\nu(E) = \int_A \nu\big(g^{-1}(E)\big)\, d\mu(g)$.

> [!remark] As a random walk
> The random walk on $X$ picks $g_1, g_2, \dots$ independently in $A$ with law $\mu$ and moves by $x_n = g_n x_{n-1}$ `[BQ §1.1]`. If $x$ has law $\nu$, then after one step the new point has law $\mu * \nu$ `[BQ §1.2]`. So: if $Y$ is an $A$-valued random variable with law $\mu$ and $Z$ an independent random point of $X$ with law $\nu$, then $YZ$ has law $\mu * \nu$, and **$\nu$ is $\mu$-stationary iff $YZ$ has the same law as $Z$** — the stationary laws are those the random walk leaves unchanged.

## Property

> [!theorem] Kakutani's theorem — on a compact space a stationary measure exists
> When $X$ is compact, there always exists a $\mu$-stationary probability measure on $X$. `[BQ Prop 3.1]`
>
> ---
> The set $\mathcal P(X)$ is compact for weak convergence; the averages $\frac1n \sum_{k=0}^{n-1} \mu^{*k} * \delta_x$ have a weakly convergent subsequence, and its limit is stationary. `[BQ, proof of Prop 3.1]`

> [!proposition] Invariant implies stationary
> Every $\Gamma$-invariant probability measure on $X$ is $\mu$-stationary. `[BQ §3.4]`

> [!theorem] Choquet–Deny theorem — for an abelian semigroup, stationary means invariant
> When $\Gamma$ is abelian, every $\mu$-stationary probability measure on $X$ is $\Gamma$-invariant. `[BQ Cor 3.4]`

## Example

> [!example] The Cantor set
> On $X = [0, 1]$ take $c_0(x) = x/3$, $c_1(x) = (x + 2)/3$ and $\mu = \frac12(\delta_{c_0} + \delta_{c_1})$. The Cantor set $K = \{\sum_{i \geq 1} 2b_i 3^{-i} : b_i \in \{0, 1\}\}$ is closed and $\Gamma$-invariant. Let $\beta = \mu^{\otimes \mathbb N}$ — fair coin flips choosing $c_0$ or $c_1$ — and $\xi$ the coding map from sequences to $K$; then $\nu_X = \xi_*\beta$ is $\mu$-stationary but not $\Gamma$-invariant, and it is the only $\mu$-stationary probability measure on $X$. `[BQ §3.5, Lemma 3.5]`

## Related

### Constructions
- [[Iterated Function System]] — for contractions $S_1, \dots, S_N$ with weights $\rho_i$, Hutchinson's operator $(S, \rho)(\nu) = \sum_i \rho_i\, S_{i\#}\nu$ `[Hut 4.2(1)]` is $\mu * \nu$ for $\mu = \sum_i \rho_i \delta_{S_i}$. So Hutchinson's unique invariant measure `[Hut 4.4(1)]` is the $\mu$-stationary one; the Cantor example is the case $N = 2$, $\rho_i = \frac12$.

### Prerequisites
- [[Measure]], [[Semigroup]], [[Group Action]]
