Reference:
- `[BGSTZ23]` — D. Boneh, S. Goldwasser, D. Song, J. Thaler, Y. Zhang, ZKP MOOC Lecture 5: _The Plonk SNARK_ (2023): https://rdi.berkeley.edu/zkp-course/assets/lecture5-2023.pdf
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §17.2 (numbering as in the HTML edition https://judsonbooks.org/aata-files/aata-html/).

## Definition

> [!definition] Parameters
> - $\mathbb F$: a [[Field]].
> - $S \subseteq \mathbb F$: a finite subset.

> [!definition] Vanishing Polynomial
> Extends:: [[Polynomial]].
>
> ---
> The vanishing polynomial of $S$ is defined as:
> $$Z_S(X) = \prod_{\alpha \in S}(X - \alpha)$$
> which is a monic polynomial of degree $|S|$. `[BGSTZ23]`

## Property

> [!proposition] Zero test — $f$ vanishes on $S$ iff $Z_S$ divides $f$
> For every $f \in \mathbb F[X]$:
> $$f|_S = 0 \Longleftrightarrow Z_S \;|\; f$$
> `[BGSTZ23]` `[Jud Cor 17.2.3]`

## Related

### Siblings
- [[Lagrange Interpolation]] — the basis polynomial $\delta_i$ is $Z_S(X) / (X - x_i)$ rescaled to equal $1$ at $x_i$

### Prerequisites
- [[Polynomial]] — [[Polynomial#Roots and Factors]]: $\lambda$ is a root iff $X - \lambda$ divides
