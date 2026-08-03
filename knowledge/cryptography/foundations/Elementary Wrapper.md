# Elementary Wrapper

A *meta-level* concept used pervasively in security reductions: the notion of an adversary that wraps another adversary efficiently. When a reduction says "$\mathcal B$ is an elementary wrapper around $\mathcal A$," it means $\mathcal B$ runs $\mathcal A$ as a subroutine plus only polynomial overhead, so $\mathcal B$'s resource bounds match $\mathcal A$'s up to that overhead.

## Definitions

> [!definition] Efficient Interactive Machine
> An interactive machine $M$ is **efficient** if there exist a poly-bounded function $t$ and a negligible function $\varepsilon$ such that for all environments (even computationally unbounded), the probability that the total running time of $M$ exceeds $t(\lambda)$ is at most $\varepsilon(\lambda)$.

> [!definition] Elementary Wrapper
> An interactive machine $M'$ is an **efficient interface** if there exist a poly-bounded function $t$ and a negligible function $\varepsilon$ such that for all $M$ (not necessarily computationally bounded), when we execute the composed machine $\langle M', M \rangle$ in an arbitrary environment, the following holds:
>
> At every point in the execution of $\langle M', M \rangle$, if $I$ is the number of interactions between $M'$ and $M$ up to that point and $T$ is the total running time of $M'$ up to that point, then the probability that $T > t(\lambda + I)$ is at most $\varepsilon(\lambda)$.
>
> If $M'$ is an efficient interface and $M$ is any machine, then $\langle M, M' \rangle$ is an **elementary wrapper around $M$**.

## Why this matters

Almost every reduction theorem in the vault has the form:

> "For every $(t, \varepsilon)$-adversary $\mathcal A$ against scheme $\Pi$, there exists a $(t', \varepsilon')$-adversary $\mathcal B$ against assumption $X$, where $\mathcal B$ is **an elementary wrapper around $\mathcal A$**, with $t' \approx t + \text{small}$ and $\varepsilon' \geq \varepsilon / L$."

The "elementary wrapper" phrase is what guarantees the *quantitative tightness*: $\mathcal B$ runs $\mathcal A$ once, adds polynomial overhead, and inherits $\mathcal A$'s success probability up to a known reduction factor $L$.

## Related

- Used in essentially every `[!theorem]` block in [[Symmetric Key Encryption]], [[Public Key Encryption]], [[Pseudorandom Functionsss]], and the [[Digital Signatures MOC|signatures]] and [[Zero-knowledge MOC|ZK]] files.
- See [[Security Model]] for the broader game-based framework that elementary wrappers operate inside.
