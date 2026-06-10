# P vs NP

The most famous open problem in computer science: does every polynomially-verifiable language admit a polynomial-time decision procedure?

> [!conjecture] P ≠ NP
> There exists a language $L \in \text{NP}$ such that $L \notin \text{P}$.

Equivalently: there is no polynomial-time algorithm for [[Time Complexity#Class NP-Complete|SAT]] (since SAT is NP-complete).

## What's Known

- **Hierarchy theorem implications:** $\text{P} \subsetneq \text{EXPTIME}$ unconditionally. So at least *some* separation in the time hierarchy is proven.
- **Relativization barrier (Baker-Gill-Solovay 1975):** there exist oracles $A, B$ with $\text{P}^A = \text{NP}^A$ and $\text{P}^B \neq \text{NP}^B$. Hence relativizing techniques cannot resolve P vs NP.
- **Natural proofs barrier (Razborov-Rudich 1994):** "natural" combinatorial circuit lower bounds cannot prove NP $\not\subseteq$ P/poly (assuming pseudorandom functions exist).
- **Algebrization barrier (Aaronson-Wigderson 2008):** an even broader class of techniques is ruled out.

These barriers tell us that resolving P vs NP requires fundamentally new proof techniques.

## Equivalent Formulations

- $\text{SAT} \in \text{P}$
- Every NP-complete problem is in P
- $\text{NP} \subseteq \text{P}$
- $\text{NP} = \text{P}$ (these collapse identically)

## Stronger Conjectures

- $\text{NP} \neq \text{P/poly}$ — even non-uniform poly-size circuits don't suffice.
- $\text{PH}$ does not collapse — the polynomial hierarchy has infinitely many levels.
- [[Exponential Time Hypothesis|ETH/SETH]] — quantitative refinements: SAT needs nearly $2^n$ time.

## Related

- [[Time Complexity]] — definitions of P, NP, NP-Complete
- [[Oracle Machines]] — relativization barrier
- [[Circuit Complexity]] — natural proofs barrier
- [[Exponential Time Hypothesis]] — quantitative form
- [[Conjectures MOC]]
