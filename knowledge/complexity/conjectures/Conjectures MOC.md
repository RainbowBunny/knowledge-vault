# Conjectures MOC

Open problems and unproven hypotheses — the leaves of the proof DAG in complexity theory. Parallel role to `cryptography/assumptions/`: these are starting points from which derived results follow, but the conjectures themselves are believed-but-unproven.

In your callout system: each conjecture's headline claim goes in a `[!conjecture]` block. Implications derived *from* a conjecture (e.g., "if ETH holds then 3-SAT has no $2^{o(n)}$ algorithm") go in `[!theorem]` and `[!security]`-style derived blocks.

## The Big Ones

- [[P vs NP]] — the famous open
- [[Exponential Time Hypothesis]] — ETH and SETH (modern, refines $\text{P} \neq \text{NP}$ quantitatively)
- [[Derandomization Conjecture]] — $\text{P} = \text{BPP}$
- [[Unique Games Conjecture]] — UGC, governs hardness of approximation

## Related Open Problems (stubs to add)

- $\text{NP} \stackrel{?}{=} \text{coNP}$
- $\text{P} \stackrel{?}{\subseteq} \text{NC}$ (does P parallelize?)
- $\text{NL} \stackrel{?}{=} \text{L}$ (does nondeterminism help in log space?)
- $\text{NP} \stackrel{?}{\subseteq} \text{P/poly}$ (Karp-Lipton consequences)
- Does PH collapse? (Stronger than $\text{P} \neq \text{NP}$)
- $\text{BQP} \stackrel{?}{\subseteq} \text{PH}$ (Raz-Tal gives oracle separation)

## Cross-Reference to Cryptography

Cryptographic hardness assumptions (DLP, factoring, LWE) play a structurally identical role on the crypto side — see [[Assumptions MOC]]. The two folders are mirrors: one for complexity-theoretic conjectures (about classes), one for cryptographic assumptions (about specific problems and adversaries).
