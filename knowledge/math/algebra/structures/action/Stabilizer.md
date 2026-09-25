Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter IV: Groups, second encounter, Section 1.1: Actions of groups on sets, reminder.

## Definition

> [!definition] Stabilizer
> Requires:: [[Group Action]].
> 
> ---
> The **stabilizer** [[Subgroup]] of $a$ consists of the elements of $G$ which fix $a$:
> $$\mathsf{Stab}_G(a) = \{g \in G \mid ga = a\}$$

## Property

> [!proposition]
> Every [[Transitivity]] left-action of $G$ on a nonempty [[Set]] $A$ is [[Morphism|Isomorphic]] to the left-multiplication of $G$ on $G/H$, for $H$ = the stabilizer of any $a \in A$.
> 
> ---
> $H = \mathsf{Stab}_G(a)$
> $\varphi: G/H \rightarrow A,\quad gH \mapsto ga$

> [!corollary]
> Requires:: [[Quotient Group]].
> 
> ---
> If $O$ is an orbit of the action of a finite [[Group]] $G$ on a [[Set]] $A$, then $O$ is a finite set and
> $$|O| \mid |G|.$$
> 
> ---
> $|O| \cdot |\mathsf{Stab}_G(a)| = |G|$.

> [!proposition]
> Suppose a [[Group]] $G$ acts on a [[Set]] $A$, and let $a \in A, g \in G, b = ga$. Then
> $$\mathsf{Stab}_G(b) = g \mathsf{Stab}_G(a) g^{-1}$$

