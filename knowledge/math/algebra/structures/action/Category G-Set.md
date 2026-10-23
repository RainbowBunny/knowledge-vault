Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 9.3: Transitive actions and the category G-Set.
- `[Lei]` — T. Leinster, _Basic Category Theory_, arXiv:1612.09375, Examples 1.2.8 and 1.3.4: https://arxiv.org/abs/1612.09375

## Definition

> [!definition] Parameters
> - $G$: a [[Group]].
> - $(\rho, A)$, $(\rho', A')$: [[Group Action|actions]] $\rho: G \times A \to A$ and $\rho': G \times A' \to A'$ of $G$ on sets $A$, $A'$.
> - $\varphi: A \to A'$: a [[Function]].

> [!definition] Category G-Set
> Instantiates:: [[Category]].
> Requires:: [[Identity Function]].
>
> ---
> $\mathsf{G} \mbox{-} \mathsf{Set}$ consists of
> - Objects are pairs $(\rho, A)$, where $\rho$ is a [[Group Action]] on $A$.
> - For $(\rho, A)$ and $(\rho', A')$, the morphisms ($G$-equivariant maps) are [[Function]] $\varphi$ such that the diagram
> $$\begin{CD} 
> G \times A @>\mathrm{id}_G \times \varphi>> G \times A'\\ 
> @V{\rho}VV @VV{\rho'}V\\ 
> A @>>{\varphi}> A'
> \end{CD}$$
> commutes.
>
> `[Alu II.9.3]` `[Lei Ex 1.2.8, Ex 1.3.4]`

## Related

### Prerequisites
- [[Group Action]] — the objects
- [[Category]]

### Siblings
- [[Category Group]] — the category of all groups; here the group $G$ is fixed and the sets vary
