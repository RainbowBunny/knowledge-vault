Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 9.3: Transitive actions and the category G-Set.

## Definition

> [!definition] Category G-Set
> Instantiates:: [[Category]].
> Requires:: [[Identity Function]].
> 
> ---
> $\mathsf{G} \mbox{-} \mathsf{Set}$ consists of
> - Objects are pairs $(\rho, A)$, where $\rho$ is a [[Group Action]] on $A$.
> - For $(\rho, A)$ and $(\rho', A')$, the morphisms are [[Function]] $\varphi$ such that the diagram
> $$\begin{CD} 
G \times A @>\mathrm{id}_G \times \varphi>> G \times A'\\ 
@V{\rho}VV @VV{\rho'}V\\ 
A @>>{\varphi}> A'
\end{CD}$$
> commutes.
