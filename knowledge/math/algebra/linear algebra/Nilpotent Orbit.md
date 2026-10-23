Reference:
- `[Cro]` — P. Crooks, arXiv:1505.07729, §2.2 and Example 1: https://arxiv.org/abs/1505.07729
- `[Hen]` — A. Henderson, arXiv:1408.3888, Example 2.1 and Theorem 2.4: https://arxiv.org/abs/1408.3888
- Original: M. Gerstenhaber, _Dominance over the classical groups_, Ann. of Math. 74 (1961), 532–569 (cited by `[Cro]`); in the textbook D. Collingwood, W. McGovern, _Nilpotent Orbits in Semisimple Lie Algebras_ (1993), Thm 6.2.5, as the Gerstenhaber–Hesselink theorem.

## Definition

> [!definition] Parameters
> - $n$: a positive integer. $\mathfrak{sl}_n(\mathbb C)$: the $n \times n$ complex matrices of trace $0$.
> - A matrix $N$ is nilpotent if $N^k = 0$ for some $k$, as for operators in [[Operators#Generalized Eigenvectors]].
> - $\lambda \vdash n$: a partition of $n$; $\trianglelefteq$: the dominance order, see [[Specht Module#Dominance and Kostka numbers]].

> [!definition] Nilpotent Orbit
> The nilpotent elements of $\mathfrak{sl}_n(\mathbb C)$ are exactly the nilpotent $n \times n$ matrices `[Cro, Example 1]`. A **nilpotent orbit** is the orbit of one of them under conjugation, $\mathcal O_N = \{ g N g^{-1} \}$ — by $\mathrm{SL}_n(\mathbb C)$ or, with the same orbits, by $\mathrm{GL}_n(\mathbb C)$, since scalar matrices act trivially.

> [!definition] Closure Order
> $\mathcal O_1 \leq \mathcal O_2$ iff $\mathcal O_1 \subseteq \overline{\mathcal O_2}$. `[Cro §2.2]`

## Property

> [!proposition] Orbits are partitions — by Jordan type
> The nilpotent orbits of $\mathfrak{sl}_n(\mathbb C)$ are indexed by the partitions of $n$ through the Jordan canonical form: $\mathcal O_\lambda$ consists of the nilpotent matrices whose Jordan blocks have sizes $\lambda_1, \lambda_2, \dots$ `[Cro, Example 1; Hen, Example 2.1]`. See [[Operators#Jordan Form]].

> [!theorem] Gerstenhaber's theorem — the closure order is the dominance order
> $\mathcal O_\lambda \leq \mathcal O_\mu$ iff $\lambda \trianglelefteq \mu$, i.e. $\lambda_1 + \cdots + \lambda_k \leq \mu_1 + \cdots + \mu_k$ for every $k$. `[Cro, Example 1; Hen, Thm 2.4]`

> [!remark] Which topology
> A complex nilpotent orbit is a constructible subset of $\mathfrak g_\mathbb C$, so its Zariski closure and its closure in the usual topology of $\mathbb C^{n^2}$ agree `[Cro §2.2]`. The theorem holds with either.

## Example

- $n = 2$: two orbits. $\lambda = (2)$, one Jordan block — the nonzero nilpotent matrices, such as $\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}$; and $\lambda = (1, 1)$ — the zero matrix. Since $\begin{pmatrix}0 & t \\ 0 & 0\end{pmatrix} \in \mathcal O_{(2)}$ tends to $0$ as $t \to 0$, $\mathcal O_{(1,1)} \leq \mathcal O_{(2)}$, matching $(1, 1) \trianglelefteq (2)$.

## Related

### Siblings
- [[Specht Module]] — the same partitions and dominance order, for the representations of $S_n$

### Prerequisites
- [[Operators]], [[Matrix]], [[Orbit]]
