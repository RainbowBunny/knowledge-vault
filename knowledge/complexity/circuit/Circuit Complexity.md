# Circuit Complexity

The non-uniform model: instead of one Turing machine handling all input lengths, we have a family of circuits, one per input length.

## Why Non-Uniform

A circuit family lets each input length get its own circuit — there is no requirement that they all come from one Turing machine via a uniform construction. This makes the model strictly more powerful: there exist undecidable languages with polynomial-size circuits (because the *circuit* can encode the answer for each length non-uniformly).

The class P/poly captures this:

> [!definition] Class P/poly
> $\text{P/poly}$ is the class of languages decidable by polynomial-size (non-uniform) circuit families. Equivalently, languages decidable by a polynomial-time Turing machine taking polynomial-length "advice" depending only on input length.

We have $\text{P} \subseteq \text{P/poly}$, and the question of whether $\text{NP} \subseteq \text{P/poly}$ is open and closely related to the polynomial hierarchy collapse.

## Hierarchy of Circuit Classes

- $\text{NC}^i$ = languages decidable by polynomial-size circuits of depth $O((\log n)^i)$ with bounded fan-in.
- $\text{AC}^i$ = same but with unbounded fan-in.
- $\text{NC} = \bigcup_i \text{NC}^i$ — languages decidable in polylogarithmic depth ("efficiently parallelizable").

## Related

- [[Branching Programs]] — a related non-uniform model
- [[Alternating Turing Machine]] — uniform analog to bounded-fan-in circuits
- [[Randomized Complexity]] — $\text{BPP} \subseteq \text{P/poly}$ via Adleman's theorem
- [[Approximation Hardness]] — circuit lower bounds remain a major open problem
