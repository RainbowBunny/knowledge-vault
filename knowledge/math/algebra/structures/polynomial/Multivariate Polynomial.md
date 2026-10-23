Reference:
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §17.1 (numbering as in the HTML edition https://judsonbooks.org/aata-files/aata-html/).
- `[Tha22]` — J. Thaler, _Proofs, Arguments, and Zero-Knowledge_ (2022), §3.4: https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]] with identity.
> - $n \geq 1$: the number of indeterminates $x_1, \dots, x_n$.

> [!definition] Multivariate Polynomial
> Generalizes:: [[Polynomial]].
>
> ---
> A **multivariate polynomial** in $x_1, \dots, x_n$ over $R$ is an element of the **ring of polynomials in $n$ indeterminates** $R[x_1, \dots, x_n]$, built one indeterminate at a time from the [[Polynomial Ring]]:
> $$R[x_1, \dots, x_n] = R[x_1, \dots, x_{n-1}][x_n].$$
> The order of the indeterminates does not matter: $(R[x])[y] \cong (R[y])[x]$, and both are written $R[x, y]$. Concretely, a multivariate polynomial is a finite sum of terms $a \, x_1^{e_1} \cdots x_n^{e_n}$ with $a \in R$ and integers $e_1, \dots, e_n \geq 0$; it widens the single indeterminate of a [[Polynomial]] to $n$. `[Jud §17.1]`

### Total Degree

> [!definition] Parameters
> - $g \in R[x_1, \dots, x_n]$: a multivariate polynomial.

> [!definition] Total Degree
> The degree of a term $a \, x_1^{e_1} \cdots x_n^{e_n}$ of $g$ is the sum of the exponents $e_1 + \cdots + e_n$. The **total degree** of $g$ is the maximum of the degree of any term of $g$. `[Tha22 §3.4]`

## Property

> [!proposition] Polynomials in several indeterminates over a domain form a domain
> If $R$ is an [[Integral Domain]], then so is $R[x_1, \dots, x_n]$. `[Jud Prop 17.1.4]`, applied once per indeterminate.

## Related

### Descendants
- [[Multilinear Polynomial]] — degree at most one in each variable

### Properties
- [[Schwartz-Zippel]] — a nonzero polynomial of low total degree rarely vanishes at a random point

### Prerequisites
- [[Polynomial Ring]] — the one-indeterminate case, iterated
