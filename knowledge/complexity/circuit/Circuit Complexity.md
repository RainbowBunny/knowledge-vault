# Circuit Complexity

The non-uniform model: instead of one Turing machine handling all input lengths, we have a family of circuits, one per input length.

## Boolean Circuits

> [!definition] Boolean Circuit
> A **Boolean circuit** is a collection of **gates** and **inputs** connected by **wires**. Cycles aren't permitted. Gates take three forms: AND gates, OR gates, and NOT gates.

> [!definition] Circuit Family
> A **circuit family** $C$ is an infinite list of circuits, $(C_0, C_1, C_2, \cdots)$, where $C_n$ has $n$ input variables. We say that $C$ decides a language $A$ over $\{0, 1\}$ if for every string $w$, $$w \in A \iff C_n(w) = 1,$$
> where $n$ is the length of $w$.

> [!definition] Size of a Circuit
> The **size** of a circuit is the number of gates it contains.

> [!definition] Depth of a Circuit
> The **depth** of a circuit is the length (number of wires) of the longest path from an input variable to the output gate.

> [!definition] Minimal Circuit
> A circuit is **size (depth) minimal** if no smaller circuit is equivalent to it.

> [!definition] Complexity of a Circuit Family
> The **size (depth) complexity** of a circuit family $(C_0, C_1, C_2, \cdots)$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the size of $C_n$.

> [!definition] Circuit Complexity
> The **circuit complexity** of a language is the size complexity of a minimal circuit family for that language. The **circuit depth complexity** is defined similarly, using depth instead of size.

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
