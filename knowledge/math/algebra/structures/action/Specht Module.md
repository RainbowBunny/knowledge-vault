Reference:
- `[EGH+]` — P. Etingof, O. Golberg, S. Hensel, T. Liu, A. Schwendner, D. Vaintrob, E. Yudovina, _Introduction to Representation Theory_, AMS Student Mathematical Library 59 (2011); arXiv:0901.0827: https://arxiv.org/abs/0901.0827. Numbers follow the arXiv / MIT OCW 18.712 version; the printed book numbers differently.
- `[Ver]` — A. M. Vershik, _A new approach to the representation theory of the symmetric groups, III: Induced representations and the Frobenius–Young correspondence_, arXiv:math/0609258 (2006): https://arxiv.org/abs/math/0609258

## Definition

> [!definition] Parameters
> - $n$: a positive integer. $S_n$: the [[Symmetric Group]].
> - $\lambda = (\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p)$: a partition of $n$, $n = \lambda_1 + \cdots + \lambda_p$ with positive integers $\lambda_i$ `[EGH+ Def 4.35]`.
> - $Y_\lambda$: its Young diagram — rows of $\lambda_1, \lambda_2, \dots$ boxes. A Young tableau: the numbers $1, \dots, n$ filled into the boxes of $Y_\lambda$. `[EGH+ §4.12]`
> - $P_\lambda \subseteq S_n$: the row subgroup, the permutations that keep every number in its row; $Q_\lambda$: the column subgroup. `[EGH+ §4.12]`
> - $a_\lambda = \frac{1}{|P_\lambda|} \sum_{g \in P_\lambda} g$, $b_\lambda = \frac{1}{|Q_\lambda|} \sum_{g \in Q_\lambda} (-1)^g g$, and $c_\lambda = a_\lambda b_\lambda$ in $\mathbb C[S_n]$, the *Young projectors*; $c_\lambda \neq 0$ because $P_\lambda \cap Q_\lambda = \{1\}$. `[EGH+ §4.12]`

> [!definition] Specht Module
> Instantiates:: [[Group Representation]].
>
> ---
> The **Specht module** of $\lambda$ is $V_\lambda = \mathbb C[S_n]\, c_\lambda$, a subspace of the [[Group Algebra]] $\mathbb C[S_n]$, with $S_n$ acting by left multiplication. `[EGH+ Thm 4.36]`

### Permutation Module

> [!definition] Permutation Module
> $U_\lambda = \mathrm{Ind}_{P_\lambda}^{S_n} \mathbb C$, the representation induced from the trivial representation of the row subgroup; equivalently $U_\lambda = \mathbb C[S_n]\, a_\lambda$ `[EGH+ §4.14]`. The row subgroup $P_\lambda \cong S_{\lambda_1} \times \cdots \times S_{\lambda_p}$ is the *Young subgroup* `[Ver §2]`.

### Dominance and Kostka numbers

> [!definition] Dominance Order
> For partitions $\lambda, \mu$ of $n$: $\mu \trianglerighteq \lambda$ if $\mu_1 + \cdots + \mu_k \geq \lambda_1 + \cdots + \lambda_k$ for every $k$ — the first $k$ rows of $\mu$ hold at least as many boxes as those of $\lambda$ `[Ver §2]`. Equivalently, $\mu - \lambda$ is a sum of vectors $e_i - e_j$ with $i < j$ `[EGH+, remark after Thm 4.47]`.

> [!definition] Kostka Number
> A *semistandard* tableau of shape $\mu$ and weight $\lambda$ fills $Y_\mu$ with $\lambda_1$ ones, $\lambda_2$ twos, and so on, weakly increasing along rows and strictly increasing down columns. The **Kostka number** $K_{\mu\lambda}$ is the number of semistandard tableaux of shape $\mu$ and weight $\lambda$. `[Ver §3]`

## Property

> [!theorem] Classification — the Specht modules are all the irreducible representations of $S_n$
> $V_\lambda$ is an irreducible representation of $S_n$, and every irreducible representation of $S_n$ is isomorphic to $V_\lambda$ for a unique partition $\lambda$. `[EGH+ Thm 4.36]`

> [!remark] Why partitions
> Conjugacy classes of $S_n$ are cycle types, which are partitions of $n$, so the count agrees with [[Group Representation#Property|the number of irreducibles]]. The theorem gives more: an explicit irreducible for each partition.

> [!theorem] Young's rule — permutation modules decompose by Kostka numbers
> $$U_\lambda \cong \bigoplus_{\mu \trianglerighteq \lambda} K_{\mu\lambda}\, V_\mu.$$
> `[Ver §3]`; `[EGH+ Prop 4.44]` proves the same decomposition with the lexicographic order, from $\mathrm{Hom}(U_\lambda, V_\mu) = 0$ for $\mu < \lambda$ and $\dim \mathrm{Hom}(U_\lambda, V_\lambda) = 1$, and calls the multiplicities Kostka numbers (Def 4.45).

> [!proposition] $K_{\lambda\lambda} = 1$ — one tableau of its own shape and weight; $K_{\mu\lambda} > 0$ iff $\mu \trianglerighteq \lambda$
> `[Ver §3]`, `[EGH+ Prop 4.44]`. The one tableau: the $\lambda_1$ ones cannot sit in the same column, so they fill row 1, which has exactly $\lambda_1$ boxes; then the twos fill row 2, and so on. So $V_\lambda$ occurs exactly once in $U_\lambda$, and every other $V_\mu$ in $U_\lambda$ has $\mu$ strictly above $\lambda$ in dominance.

> [!remark] Index order in the literature
> `[EGH+]` writes $K_{\mu\lambda}$ for the multiplicity of $V_\mu$ in $U_\lambda$, and `[Ver]` writes $K(\mu, \lambda)$ with the shape first; both mean shape $\mu$, weight $\lambda$, as here. Many texts write $K_{\lambda\mu}$ with shape $\lambda$ and weight $\mu$.

## Example

- $\lambda = (n)$: $P_\lambda = S_n$ and $V_{(n)}$ is the trivial representation; $\lambda = (1, \dots, 1)$: $Q_\lambda = S_n$ and $V_\lambda$ is the sign representation.

## Related

### Used by
- [[Nilpotent Orbit]] — the same partitions and the same dominance order index the nilpotent orbits

### Prerequisites
- [[Group Representation]], [[Group Algebra]], [[Symmetric Group]]
