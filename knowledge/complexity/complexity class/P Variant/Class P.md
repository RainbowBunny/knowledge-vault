Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.6: The Class P.

## Definition

> [!definition] Class P
> Requires:: [[Class DTIME]]
> 
> ---
>$$\mathsf{P} = \bigcup_{c \geq 1} \mathsf{DTIME}(n^c).$$

> [!definition] Class P (Machine form)
> Unfolded (machine form): $L \in \text{P}$ iff there exist a deterministic Turing machine $M$ and a polynomial $p(\cdot)$ such that
> - On input a string $x$, machine $M$ halts after at most $p(|x|)$ steps, and
> - $M(x) = 1$ if and only if $x \in L$.

> [!remark] Role of Class P
> - $\mathsf{P}$ is invariant for all models of computation that are polynomial-equivalent to the deterministic single-tape Turing machine.
> - $\mathsf{P}$ roughly corresponds to the class of problems that are realistically solvable on a computer.

## Property

> [!theorem]
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

## Member

> [!example] Members of P
> - $\text{CONNECTED} = \{\langle G \rangle \mid G \text{ is a connected undirected graph}\}$
> - $\text{TRIANGLE} = \{\langle G \rangle \mid G \text{ contains a triangle}\}$
> - [[Number Theory#Divisibility and greatest common divisors|RELPRIME]]
> - Every context-free language
