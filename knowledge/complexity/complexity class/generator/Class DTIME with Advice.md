Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.3: Turing Machine that Take Advice.

## Definition

> [!definition] Class DTIME with Advice
> Let $T, a: \mathbb{N} \rightarrow \mathbb{N}$ be [[Function]]. The class of [[Language]] decidable by time-$T(n)$ [[Turing Machine]] with $a(n)$ bits of advice, denoted $\mathsf{DTIME}(T(n))/a(n)$, contains every $\mathcal{L}$ such that there exists a sequence $\{\alpha_n\}_{n \in \mathbb{N}}$ of strings with $\alpha_n \in \{0, 1\}^{a(n)}$ and a TM $M$ satisfying
> $$\forall x \in \{0, 1\}^n: M(x, \alpha_n) = 1 \iff x \in \mathcal{L}$$
> where on input $(x, \alpha_n)$ the machine $M$ runs for at most $O(T(n))$ steps.

