Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 7.1: Normal subgroups; Section 7.6: Kernel $\iff$ Normal; Section 8.4: $HK/H$ vs. $K/(H \cap K)$.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $G$: a [[Group]].
> - $N \leq G$: a [[Subgroup]].

> [!definition] Normal Subgroups
> Extends:: [[Subgroup]].
>
> ---
> A subgroup $N$ of a group $G$ is normal if $\forall g \in G, \forall n \in N$,
> $$gng^{-1} \in N$$
> `[Alu II §7.1]` `[Jud Thm 10.1.3]`

> [!remark] Judson's definition
> [Jud §10.1] defines $N$ to be normal when $gN = Ng$ for all $g \in G$; this is equivalent to the condition above, $gNg^{-1} \subseteq N$ for all $g \in G$ `[Jud Thm 10.1.3]`. So $N$ is normal exactly when its left and right [[Coset|cosets]] agree.

## Property

> [!lemma] Kernels are normal — $\ker \varphi$ is a normal subgroup of $G$
> If $\varphi: G \rightarrow G'$ is any [[Group Homomorphism]], then $\ker{\varphi}$ is normal subgroup of $G$. `[Alu II §7.6]` `[Jud Thm 11.1.5]`
>
> ---
> For $n \in \ker\varphi$: $\varphi(g n g^{-1}) = \varphi(g) \varphi(n) \varphi(g^{-1}) = \varphi(g)\, e_{G'}\, \varphi(g)^{-1} = e_{G'} \implies gng^{-1} \in \ker{\varphi}$.

> [!proposition] Normal subgroups are kernels — $N$ is the kernel of $G \rightarrow G/N$
> Every normal subgroup is a [[Kernel of Group Homomorphism]]. `[Alu II §7.6]`
>
> Namely of the canonical homomorphism $G \rightarrow G/N$, $g \mapsto gN$ `[Jud §11.2]`.

> [!theorem] Second isomorphism theorem — $HK/H \cong K/(H \cap K)$
> Let $H, K$ be [[Subgroup]] of a [[Group]] $G$, and assume that $H$ is normal in $G$. Then:
> - $HK = \{hk \mid h \in H, k \in K\}$ is a [[Subgroup]] of $G$;
> - $H$ is normal in $HK$;
> - $H \cap K$ is normal in $K$;
> - $$\frac{HK}{H} \cong \frac{K}{H \cap K}.$$
>
> `[Alu II §8.4]` `[Jud Thm 11.2.3]`

## Related

### Siblings
- [[Kernel of Group Homomorphism]] — the same subgroups, seen through a homomorphism
- [[Group Center]] — an abelian normal subgroup

### Constructions
- [[Quotient Group]] — $G/N$ is a group exactly when $N$ is normal
- [[Subgroup of Quotient Group]] — correspondence theorem and third isomorphism theorem

### Prerequisites
- [[Coset]] — left and right cosets
