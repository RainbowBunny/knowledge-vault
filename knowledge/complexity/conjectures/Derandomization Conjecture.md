# Derandomization Conjecture

The conjecture that *randomness adds no power to polynomial-time computation*.

> [!conjecture] Derandomization Conjecture
> $\text{P} = \text{BPP}$.

Every problem solvable in randomized polynomial time can also be solved in deterministic polynomial time.

## Why It's Believed

Multiple converging arguments:

1. **Pseudorandom generators (PRGs).** If sufficiently strong PRGs exist (with hardness against polynomial-size circuits), one can derandomize BPP. Concretely, Nisan-Wigderson (1994) and Impagliazzo-Wigderson (1997) show: if there is a language in $\text{E} = \text{TIME}(2^{O(n)})$ that requires circuits of size $2^{\Omega(n)}$, then $\text{P} = \text{BPP}$.

2. **The Impagliazzo-Wigderson "hardness vs. randomness" paradigm:** strong enough circuit lower bounds give derandomization. Since circuit lower bounds are widely believed, derandomization follows.

3. **Empirical observation.** No natural problem in BPP is known to *require* randomness — primality testing was derandomized (Miller-Rabin → AKS 2002), polynomial identity testing has progressing derandomizations, etc.

## Equivalent and Related Statements

- $\text{BPP} \subseteq \text{P}$ (the same — $\text{P} \subseteq \text{BPP}$ trivially).
- A language in $\text{E}$ has circuit complexity $2^{\Omega(n)}$ (suffices for $\text{P} = \text{BPP}$).
- More fine-grained: $\text{BPP} = \text{P}$ relative to some hardness assumption.

## Cryptographic Connection

If one-way functions exist, then pseudorandom generators exist (Håstad-Impagliazzo-Levin-Luby 1999) — so cryptographic assumptions *imply* derandomization assumptions. Standard crypto belief therefore implies $\text{P} = \text{BPP}$.

## Related

- [[Randomized Complexity]] — BPP definition
- [[Circuit Complexity]] — circuit lower bounds power derandomization
- [[Time Complexity]] — P, the target class
- [[P vs NP]] — independent open problem
- [[Pseudorandom Generators]] (in `cryptography/foundations/`) — the workhorse primitive
