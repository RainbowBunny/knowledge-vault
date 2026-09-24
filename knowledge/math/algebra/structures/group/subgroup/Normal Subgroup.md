Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 7.1: Normal subgroups; Section 7.6: Kernel $\iff$ Normal; Section 8.4: $HK/H$ vs. $K/(H \cap K)$.

## Definition

> [!definition] Normal Subgroups
> A subgroup $N$ of a group $G$ is normal if $\forall g \in G, \forall n \in N$,
> $$gng^{-1} \in N$$

## Property

> [!lemma] 
> If $\varphi: G \rightarrow G'$ is any [[Group Homomorphism]], then $\ker{  \varphi}$ is normal subgroup of $G$.
> 
> ---
> $\varphi(g n g^{-1}) = \varphi(g) \varphi(n) \varphi(g^{-1}) = e_G \implies gng^{-1} \in \ker{\varphi}$.

> [!proposition]
> Every normal subgroup is a [[Group Homomorphism|Kernel]].

> [!proposition]
> Let $H, K$ be [[Subgroup]] of a [[Group]] $G$, and assume that $H$ is normal in $G$. Then:
> - $HK = \{hk \mid h \in H, k \in K\}$ is a [[Subgroup]] of $G$, and $H$ is normal in $HK$.
> - $H \cap K$ is normal in $K$, and
> $$\frac{HK}{H} \cong \frac{K}{H \cap K}.$$

