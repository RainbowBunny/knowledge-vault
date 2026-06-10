# Hierarchy Theorems

The hierarchy theorems are the foundational meta-results showing that *more resources strictly increase computational power*. They are what make the inclusion lattice non-trivial — without them, we couldn't prove $\text{P} \subset \text{EXPTIME}$ unconditionally.

## Space Hierarchy

> [!definition] Space Constructible
> A function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is at least $O(\log n)$, is called **space constructible** if the function that maps the string $1^n$ to the binary representation of $f(n)$ is computable in space $O(f(n))$.

> [!theorem] Space Hierarchy Theorem
> For any space-constructible function $f: \mathcal N \rightarrow \mathcal N$, a language $A$ exists that is decidable in $O(f(n))$ space but not in $o(f(n))$ space.

> [!corollary]
> For any two functions $f_1, f_2: \mathcal N \rightarrow \mathcal N$, where $f_1(n)$ is $o(f_2(n))$ and $f_2$ is space-constructible, $\text{SPACE}(f_1(n)) \subset \text{SPACE}(f_2(n))$.

> [!corollary]
> For any two real numbers $0 \leq \epsilon_1 < \epsilon_2$, $$\text{SPACE}(n^{\epsilon_1}) \subset \text{SPACE}(n^{\epsilon_2}).$$

## Time Hierarchy

> [!definition] Time Constructible
> A function $t: \mathcal N \rightarrow \mathcal N$, where $t(n)$ is at least $O(n \log n)$, is called **time constructible** if the function that maps the string $1^n$ to the binary representation of $t(n)$ is computable in time $O(t(n))$.

> [!theorem] Time Hierarchy Theorem
> For any time-constructible function $f: \mathcal N \rightarrow \mathcal N$, a language $A$ exists that is decidable in $O(t(n))$ time but not decidable in time $o(\frac{t(n)}{\log t(n)})$.

> [!corollary]
> For any two functions $t_1, t_2: \mathcal N \rightarrow \mathcal N$, where $t_1(n)$ is $o(\frac{t_2(n)}{\log t_2(n)})$ and $t_2$ is time-constructible, $\text{TIME}(t_1(n)) \subset \text{TIME}(t_2(n))$.

> [!corollary]
> For any two real numbers $1 \leq \epsilon_1 < \epsilon_2$, $$\text{TIME}(n^{\epsilon_1}) \subset \text{TIME}(n^{\epsilon_2}).$$

## EXPSPACE-Complete

> [!definition] EXPSPACE-Complete
> A language $B$ is **EXPSPACE-complete** if
> 1. $B \in \text{EXPSPACE}$, and
> 2. every $A$ in $\text{EXPSPACE}$ is polynomial-time reducible to $B$.

> [!example] Member of EXPSPACE-Complete
> $\text{EQ}_{REX\uparrow} = \{\langle Q, R \rangle | Q \text{ and } R \text{ are equivalent regular expressions with exponentiation}\}$

## Why hierarchy theorems matter

These theorems are what make complexity theory *non-vacuous* unconditionally. Many class separations (e.g. $\text{P} \neq \text{NP}$) are conjectured but unproven; the hierarchy theorems give us $\text{P} \subset \text{EXPTIME}$ and similar strict separations *for free*. Diagonalization is the proof technique — closely related to [[Computability Theory|undecidability]] proofs.

## Related

- [[Complexity Class]] — the inclusion lattice that hierarchy theorems make non-trivial
- [[Time Complexity]] — TIME(t), the resource bound
- [[Space Complexity]] — SPACE(s), the resource bound
- [[Oracle Machines]] — relativization, the technique that *fails* for some separations
