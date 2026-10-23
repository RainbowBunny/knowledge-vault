Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 6.1: Definition.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $(G, \cdot)$: a [[Group]].
> - $(H, \circ)$: a [[Group]] with $H \subseteq G$.
> - $i: H \hookrightarrow G$: the [[Inclusion Function]].

> [!definition] Subgroup
> Extends:: [[Substructure]].
>
> ---
> Let $(G, \cdot)$ be a [[Group]], and let $(H, \circ)$ be another group, whose underlying set $H$ is a subset of $G$. $(H, \circ)$ is a **subgroup** of $G$ if the [[Inclusion Function]] $i: H \hookrightarrow G$ is a [[Group Homomorphism]]. `[Alu II §6.1]`
>
> Equivalently, $H \subseteq G$ is a group under the operation of $G$ restricted to $H$ `[Jud §3.3]`.

## Property

> [!proposition] One-step subgroup criterion — a nonempty $H$ with $ab^{-1} \in H$ for all $a, b \in H$ is a subgroup
> A nonempty subset $H$ of a group $G$ is a subgroup if and only if
> $$(\forall a, b \in H): ab^{-1} \in H.$$
> `[Alu II §6.1]` `[Jud Prop 3.3.8]`

> [!lemma] Intersections of subgroups are subgroups
> If $\{H_\alpha\}_{\alpha \in A}$ is any family of subgroups of a group $G$, then
> $$H = \bigcap_{\alpha \in A} H_\alpha$$
> is a subgroup of $G$. `[Alu II §6.1]`

> [!lemma] Preimages of subgroups are subgroups
> Let $\varphi: G \rightarrow G'$ be a group homomorphism, and let $H'$ be a subgroup of $G'$. Then $\varphi^{-1}(H')$ is a subgroup of $G$. `[Alu II §6.1]` `[Jud Prop 11.1.4]`

> [!theorem] Lagrange's theorem — the order of a subgroup divides the order of the group
> Let $H$ be a subgroup of a finite group $G$. Then $|H|$ divides $|G|$. `[Jud Thm 6.2.2]`
>
> With the index: $|G| = [G : H] \cdot |H|$, see [[Quotient Group#Lagrange's Theorem]].

## Related

### Descendants
- [[Normal Subgroup]] — closed under conjugation
- [[Additive Subgroup]] — a subgroup of $(\mathbb R^m, +)$

### Constructions
- [[Coset]] — the translates $aH$ and $Ha$
- [[Quotient Group]] — $G/H$, a group when $H$ is normal

### Siblings
- [[Subring]] — the ring version; it must contain $1$
