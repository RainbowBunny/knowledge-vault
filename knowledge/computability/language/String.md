Reference:
- [[Book Reference|Introduction to Automata Theory, Languages, and Computation]] - Chapter 1. Automata: The Methods and The Madness, Section 1.5.1: Alphabets; Section 1.5.2: Strings.

## Definition

> [!definition] Alphabet
> An **alphabet** is any nonempty finite set.

> [!definition] Symbols
> The members of the alphabet are the **symbols** of the alphabet.

> [!definition] String over an Alphabet
> A **string over an alphabet** is a finite sequence of symbols from that alphabet, usually written next to one another and not separated by commas.

> [!definition] Empty String
> The **empty string** is the string with zero occurrences of symbols. Denoted $\varepsilon$.

> [!definition] Length of a String
> Length is the number of positions for symbols in the string. The length of $s$ is denoted as $|s|$.

> [!definition] Set of String by Length
> - For an alphabet $\Sigma$, denote $\Sigma^k$ as the set of all string of length $k$ formed by the alphabet $\Sigma$.
> - $\Sigma^+ = \Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup \cdots$: The set of non-empty strings over an alphabet $\Sigma$.
> - $\Sigma^* = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \cdots = \Sigma^+ \cup \{\varepsilon\}$: The set of all strings over an alphabet $\Sigma$.

### Concatenation

> [!definition] Concatenation
> Let $x$ and $y$ be strings. Then $xy$ denotes the *concatenation* of $x$ and $y$, that is, the string formed by making a copy of $x$ and following it by a copy of $y$. Precisely, let $x$ is the string composed of $i$ symbols $x = a_1 a_2 \dots a_i$ and $y$ is the string composed of $j$ symbols $y = b_1 b_2 \dots b_j$, then $xy$ is the string length $i + j: xy = a_1 a_2 \dots a_i b_1 b_2 \dots b_j$.

> [!remark]
> $(\Sigma^*, \cdot, \varepsilon)$ is a [[Monoid]] on $\Sigma$.
