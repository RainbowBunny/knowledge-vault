Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter,  Section 6.2: Examples: Kernel and image.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $G$: a [[Group]].
> - $G'$: a [[Group]].
> - $\varphi: G \rightarrow G'$: a [[Group Homomorphism]].
> - $e_{G'}$: the identity of $G'$.

> [!definition] Kernel of Group Homomorphism
> Requires:: [[Kernel]], [[Group Homomorphism]].
>
> ---
> The **kernel** of $\varphi: G \rightarrow G'$ is the subset of $G$ consisting of elements mapping to the identity in $G'$:
> $$\ker \varphi = \{g \in G \; | \; \varphi(g) = e_{G'}\} = \varphi^{-1}(e_{G'}).$$
> `[Alu II §6.2]` `[Jud §11.1]`

> [!remark] Bridge to the origin
> [[Kernel]] is the relation $a \sim b \iff \varphi(a) = \varphi(b)$; here the kernel is one fibre, $\varphi^{-1}(e_{G'})$. The fibre determines the relation, since $\varphi(a) = \varphi(b) \iff a^{-1}b \in \ker\varphi$: the classes of the relation are the [[Coset|cosets]] $a \ker\varphi$.

## Property

> [!proposition] Universal property of the kernel — $\ker\varphi \hookrightarrow G$ is final among homomorphisms that $\varphi$ sends to the identity
> Let $\varphi: G \rightarrow G'$ be a homomorphism. Then the [[Inclusion Function]] $\iota: \ker \varphi \hookrightarrow G$ is [[Universal Property|Final]] in the [[Category]] of group homomorphism $\alpha: K \rightarrow G$ such that $\varphi \circ \alpha$ is the trivial homomorphism $K \rightarrow G'$, $k \mapsto e_{G'}$ (the one that factors through the [[Trivial Group]]). `[Alu II §6.2]`

## Related

### Siblings
- [[Normal Subgroup]] — the same subgroups: a kernel is normal `[Jud Thm 11.1.5]`, and every normal subgroup is a kernel
- [[Ring Homomorphism#Kernel]] — the ring version, an [[Ideal]]

### Prerequisites
- [[Kernel]] — the origin, as a relation
- [[Group Homomorphism]]
