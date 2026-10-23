Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter IV: Groups, second encounter, Section 1.2: Center, centralizer, conjugacy classes.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $G$: a [[Group]].
> - $\sigma: G \rightarrow \mathsf{Aut}_\mathsf{Grp}(G)$: the action of $G$ on itself by conjugation, $\sigma(g)(a) = gag^{-1}$ (see [[Group Action on Group]]).

> [!definition] Group Center
> Extends:: [[Center]].
>
> ---
> The **center** of $G$, denote $Z(G)$, is the [[Subgroup]] $\mathrm{ker} \; \sigma$ of $G$.
> Concretely, the **center** of $G$ is
> $$Z(G) = \{g \in G \mid (\forall a \in G): ag = ga\}$$
> `[Alu IV §1.2]` `[Jud §14.2]`

## Property

> [!proposition] The center is an abelian normal subgroup
> $Z(G)$ is an [[Abelian Group|abelian]] [[Normal Subgroup]] of $G$. `[Jud Thm 11.1.5]`
>
> ---
> Normal: $Z(G) = \ker \sigma$, and the kernel of a homomorphism is a normal subgroup `[Jud Thm 11.1.5]`. Abelian: its elements commute with every element of $G$, in particular with each other.

## Related

### Siblings
- [[Ring Center]] — the center of $(R, \cdot)$; a [[Subring]]

### Properties
- [[p-Group]] — a group of order $p^n$ has a nontrivial center `[Jud Thm 14.2.4]`

### Prerequisites
- [[Group Action on Group]] — the conjugation action $\sigma$
