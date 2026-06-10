# Unique Games Conjecture (UGC)

A conjecture about the hardness of a specific 2-prover game, introduced by Khot (2002). It powers a remarkable amount of optimal hardness-of-approximation results.

> [!conjecture] Unique Games Conjecture (UGC)
> For every $\epsilon, \delta > 0$, there exists a constant $k = k(\epsilon, \delta)$ such that it is NP-hard to distinguish, given a Unique Games instance with label set of size $k$, between:
> - **YES instances**: at least $1 - \epsilon$ fraction of constraints can be satisfied;
> - **NO instances**: at most $\delta$ fraction of constraints can be satisfied.

A *Unique Game* is a constraint satisfaction problem where each constraint is a bijection $\sigma_{uv}$ between labels, with $u$'s label determining $v$'s.

## Why It Matters

The UGC, if true, gives **optimal approximation hardness** for many problems where the gap was previously unknown:

- **Max-Cut**: UGC implies the Goemans-Williamson 0.878 ratio is optimal (Khot-Kindler-Mossel-O'Donnell 2007).
- **Vertex Cover**: UGC implies $2 - \epsilon$ is the best polynomial-time approximation ratio.
- **General constraint satisfaction**: Raghavendra (2008) showed UGC implies a *generic* tight algorithm via SDP rounding.

## Status

Unproven in either direction. Significant progress:
- **Subhash Khot, Dor Minzer, Muli Safra (2018)** proved the **2-to-1 Games Conjecture**, a closely related variant — moving UGC closer to being proven.
- Whether UGC follows from $\text{P} \neq \text{NP}$ is open.

## Related

- [[P vs NP]] — UGC is a strengthening
- [[Approximation Hardness]] — UGC's main use case
- [[Interactive Proofs]] — 2-prover games are interactive structures
