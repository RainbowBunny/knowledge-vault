Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.3: One-Sided and "Zero-Sided" Error: RP, coRP, ZPP.

## Definition

> [!definition] Zero-error Randomized Time
> The class $\mathsf{ZTIME}(T(n))$ contains all the [[Language]] $\mathcal{L}$ for which there is a [[Probabilistic Turing Machine]] $M$ that runs in an expected-time $O(T(n))$ such that for every input $x$, whenever $M$ halts on $x$, the output $M(x)$ it produces is exactly $\mathcal{L}(x)$.

 