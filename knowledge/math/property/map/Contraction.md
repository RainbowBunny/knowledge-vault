Reference:
- `[ConC]` — K. Conrad, _The contraction mapping theorem_: https://kconrad.math.uconn.edu/blurbs/analysis/contraction.pdf
- `[Hut]` — J. E. Hutchinson, _Fractals and self-similarity_, Indiana Univ. Math. J. 30 (1981): https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf
- `[Sut]` — A. V. Sutherland, MIT 18.785 _Number Theory I_, Lecture 8, Def 8.1 (Cauchy sequences, completeness): https://math.mit.edu/classes/18.785/2025/LectureNotes8.pdf

## Definition

> [!definition] Parameters
> - $(X, d)$: a [[Metric Space]]. $f: X \to X$.
> - $c$: the contraction constant, $0 \leq c < 1$.

> [!definition] Contraction
> Extends:: [[Lipschitz Map]].
>
> ---
> ### Scope
> A map $f: X \to X$ from a metric space to itself.
>
> ---
> ### Property
> $d(f(x), f(x')) \leq c\, d(x, x')$ for some $0 \leq c < 1$ and all $x, x' \in X$. `[ConC §1]`
>
> Equivalently $\mathrm{Lip}\, f < 1$ `[Hut 2.2]`.

## Property

### Banach fixed-point theorem

> [!theorem] Banach fixed-point theorem — a contraction has exactly one fixed point
> ### Scope
> A contraction $f$ on a nonempty complete metric space $(X, d)$ — complete: every Cauchy sequence converges `[Sut Def 8.1]`.
>
> ---
> ### Property
> $f$ has a unique fixed point $a$, and for any $x_0 \in X$ the iterates $x_0, f(x_0), f(f(x_0)), \dots$ converge to $a$. `[ConC Thm 1.1]` The convergence is geometric: $d(x_n, a) \leq \frac{c^n}{1 - c}\, d(x_0, f(x_0))$ `[ConC Cor 2.4]`.

> [!remark] Each hypothesis is needed
> - **Complete**: on $(0, \infty)$, which is not complete `[ConC Ex. 1.2]`, $f(x) = x/2$ is a contraction with no fixed point.
> - **$c < 1$**: the proof uses it `[ConC §3]`; $f(x) = x + 1$ on $\mathbb R$ has $d(f(x), f(y)) = d(x, y)$ and no fixed point.
> - **Nonempty**: the empty space is complete and has no fixed point. `[ConC]` leaves this implicit.

## Related

### Used by
- [[Iterated Function System]] — Hutchinson's theorem is this theorem applied to sets, with the Hausdorff metric

### Prerequisites
- [[Lipschitz Map]], [[Metric Space]]
