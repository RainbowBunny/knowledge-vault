Reference:
- `[Gro16]` — J. Groth, _On the Size of Pairing-based Non-interactive Arguments_ (EUROCRYPT 2016), §2.1 Bilinear groups: https://eprint.iacr.org/2016/260.pdf
- `[BF03]` — D. Boneh, M. Franklin, _Identity-Based Encryption from the Weil Pairing_, SIAM J. Comput. 32(3), 2003, §3: https://crypto.stanford.edu/~dabo/papers/bfibe.pdf
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $p$: a [[Prime]].
> - $\mathbb G_1$: a [[Group]].
> - $\mathbb G_2$: a [[Group]].
> - $\mathbb G_T$: a [[Group]].
> - $e: \mathbb G_1 \times \mathbb G_2 \rightarrow \mathbb G_T$: the pairing, a map.
> - $g_1 \in \mathbb G_1$: an element.
> - $g_2 \in \mathbb G_2$: an element.

> [!definition] Bilinear Groups
> Requires:: [[Group]], [[Bilinearity]].
>
> ---
> Bilinear groups $\mathcal{BG}$ is a tuple $(p, \mathbb G_1, \mathbb G_2, \mathbb G_T, e, g_1, g_2)$ with the following properties:
> - $\mathbb G_1, \mathbb G_2, \mathbb G_T$ are groups of prime order $p$.
> - The pairing $e: \mathbb G_1 \times \mathbb G_2 \rightarrow \mathbb G_T$ is a [[Bilinearity|Bilinear]] map.
> - $g_1$ is a generator for $\mathbb G_1$.
> - $g_2$ is a generator for $\mathbb G_2$.
> - $e(g_1, g_2)$ is a generator for $\mathbb G_T$.
>
> `[Gro16 §2.1]`

> [!remark] Non-degeneracy
> The last condition is the non-degeneracy of $e$: it does not send every pair to the identity of $\mathbb G_T$ `[BF03 §3]`. [BF03] works in the symmetric case $\hat e: \mathbb G_1 \times \mathbb G_1 \rightarrow \mathbb G_2$ (Type I below, with the target written $\mathbb G_2$), writes $\mathbb G_1$ additively, and asks that $\hat e$ be efficiently computable.

> [!definition] Generic Group Operations
> There are efficient algorithms for:
> - Computing group operations.
> - Evaluating the bilinear map.
> - Deciding membership of the groups.
> - Deciding equality of group elements.
> - Sampling generators of the groups.
>
> `[Gro16 §2.1]`

## Variant

The classification below is the one [Gro16 §2.1] attributes to Galbraith, Paterson and Smart.

### Type I

> [!definition] Type I Bilinear Groups
> - $\mathbb G_1 = \mathbb G_2$
>
> `[Gro16 §2.1]`

### Type II

> [!definition] Parameters
> - $\Psi: \mathbb G_2 \rightarrow \mathbb G_1$: a [[Group Homomorphism]].

> [!definition] Type II Bilinear Groups
> - There is an efficiently computable non-trivial homomorphism $\Psi: \mathbb G_2 \rightarrow \mathbb G_1$.
>
> `[Gro16 §2.1]`

### Type III

> [!definition] Type III Bilinear Groups
> - No efficiently computable non-trivial homomorphism exists in either direction between $\mathbb G_1$ and $\mathbb G_2$.
>
> `[Gro16 §2.1]`

## Related

### Instantiations
- [[Bilinear Pairings]] — the Weil and Tate pairings on elliptic curves
- [[Weil Pairing over Prime Power Fields]]

### Prerequisites
- [[Bilinearity]] — the property of the pairing $e$
- [[Cyclic Group]] — a group of prime order is cyclic, and every non-identity element generates it `[Jud Cor 6.2.4]`
