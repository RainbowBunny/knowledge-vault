## Definition

> [!definition] Verifier
> A **verifier** for a language $\mathcal L$ is an algorithm $V$, where $$\mathcal L = \{x \mid V \text{ accepts } \langle x, w \rangle \text{ for some string } w\}.$$
> We measure the time of a verifier only in terms of the length of $x$, so a **polynomial-time verifier** runs in polynomial time in the length of $x$. A language $\mathcal L$ is **polynomial verifiable** if it has a polynomial-time verifier.

> [!definition] Certificate
> To test membership in $\mathcal L$, the verifier uses additional information $w$ called a **certificate**, **witness**, or **proof** — a string whose existence proves $x \in \mathcal L$ and which the verifier can check in polynomial time.

> [!definition] Class $\text{NP}$
> A language $\mathcal L$ is in the class $\text{NP}$ if there exists a polynomial time algorithm $\mathcal R_L$ such that
> $$\mathcal L = \{x \; | \; \exists w, |w| = \text{poly(|x|)} \land \mathcal R_L(x, w) = 1\}$$

## Property

> [!theorem]
> A language is in $\text{NP}$ if and only if it is decided by some nondeterministic polynomial-time Turing machine: $$\text{NP} = \bigcup_k \text{NTIME}(n^k).$$

## Open Question

> [!example]
> Does $\text{coNP} = \text{NP}$?