Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 6.1: Definition.

## Definition

> [!definition] Subgroup
> Let $(G, \cdot)$ be a [[Group]], and let $(H, \circ)$ be another group, whose underlying set $H$ is a subset of $G$. $(H, \circ)$ is a **subgroup** of $G$ if the [[Inclusion Function]] $i: H \hookrightarrow G$ is a [[Group Homomorphism]].

> [!proposition]
> A nonempty subset $H$ of a group $G$ is a subgroup if and only if
> $$(\forall a, b \in H): ab^{-1} \in H.$$

## Property

> [!lemma]
> If $\{H_\alpha\}_{\alpha \in A}$ is any family of subgroups of a group $G$, then
> $$H = \bigcap_{\alpha \in A} H_i$$
> is a subgroup of $G$.

> [!lemma]
> Let $\varphi: G \rightarrow G'$ be a group homomorphism, and let $H'$ be a subgroup of $G'$. Then $\varphi^{-1}(H')$ is a subgroup of $G$.

> [!theorem] Lagrange's Theorem
> Let $H$ be a subgroup of a finite group $G$. Then $|H|$ divides $|G|$.
