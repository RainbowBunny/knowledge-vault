
## Turing Machines

> [!definition] Turing Machine
>  A Turing Machine is a 7-tuple, $(Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$, where $Q, \Sigma, \Gamma$ are all finite sets and
> 1. $Q$ is the set of states,
>2. $\Sigma$ is the input alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$ is the transition function,
>5. $q_0 \in Q$ is the start state,
>6. $q_{accept} \in Q$ is the accept state, and
>7. $q_{reject} \in Q$ is the reject state, where $q_{reject} \neq q_{accept}$.

**Turing-recognizable**: A language is called **Turing-recognizable** if some Turing machine recognizes it.

**Turing-decidable**: A language is called **Turing-decidable** or simply **decidable** if some Turing machine decides it. (Halts on all input)

**Note**: Invariant of Turing machine are equivalence in power.

## Multitape Turing Machines

Replace the transition function:
	$\delta: Q \times \Gamma^{k} \rightarrow Q \times \Gamma^k \times \{L, R, S\}^k$


## Nondeterministic Turing Machines

Replace the transition function:
	$\delta: Q \times \Gamma \rightarrow \mathcal P(Q \times \Gamma \times \{L, R\})$

## Enumerators

> [!definition] Enumerator
> An Enumerator is a 5-tuple $(Q, \Sigma, \Gamma, \delta, q_0)$ where $Q, \Sigma, \Gamma$ are all finite sets:
>1. $Q$ is the set of states,
>2. $\Sigma$ is the input alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma^2 \rightarrow Q \times \Gamma^2 \times \{L, R, S\} ^2$ is the transition function.
>5. $q_0 \in Q$ is the start state.

## Algorithm

**Church Turing thesis**: 

## Decidability

These following languages are decidable:
$$A_{DFA} = \{\langle B, w \rangle | B \text{ is a } DFA \text{ that accepts input string } w \}$$
$$A_{NFA} =  \{\langle B, w \rangle | B \text{ is a } NFA \text{ that accepts input string } w \}$$$$A_{REX} = \{\langle B, w \rangle | B \text{ is a regular expression that accepts input string } w \}$$$$E_{DFA} =  \{\langle A \rangle | A \text{ is a } DFA \text{ and } L(A) = \emptyset \}$$$$EQ_{DFA} =  \{\langle A, B \rangle | A \text{ and } B \text{ are } DFAs \text{ and } L(A) = L(B) \}$$$$A_{CFG} =  \{\langle G, w \rangle | G \text{ is a } CFG \text{ that generates string } w \}$$$$E_{CFG} =  \{\langle G \rangle | G \text{ is a } CFG \text{ and } L(G) = \emptyset \}$$$$EQ_{CFG} =  \{\langle G, H \rangle | G \text{ and } H \text{ are } CFGs \text{ and } L(G) = L(H) \}$$$$A_{LBA} = \{\langle M, w \rangle | M \text{ is an } LBA \text{ that accepts string } w\}$$
## Undecidability

These following languages are undecidable:
$$A_{TM} = \{\langle M, w \rangle | M \text{ is a } TM \text{ and } M \text{ accepts } w \}$$$$HALT_{TM} = \{\langle M, w \rangle | M \text{ is a } TM \text{ and } M \text{ halts on input } w\}$$$$E_{TM} = \{\langle M \rangle | M \text{ is a } TM \text{ and } L(M) = \emptyset\}$$$$REGULAR_{TM} = \{\langle M \rangle | M \text{ is a } TM \text{ and } L(M) \text{ is a regular language}\}$$$$EQ_{TM} = \{\langle M_1, M_2 \rangle | M_1 \text{ and } M_2 \text{ are } TMs \text{ and } L(M_1) = L(M_2)\}$$
$$E_{LBA} = \{\langle M \rangle | M \text{ is an } LBA \text{ where } L(M) = \emptyset\}$$

$$ALL_{CFG} = \{\langle G \rangle | G \text{ is a } CFG \text{ and } L(G) = \Sigma^*\}$$
**Corollary**: Some languages are not Turing-recognizable.
**Theorem**: A language is decidable if and only if it is Turing-recognizable and co-Turing-recognizable.
Not Turing-recognizable languages:
$$MIN_{TM} = \{\langle M \rangle | M \text{ is a minimal } TM \}$$

## Post Correspondence Problem

An instance of the PCP is a collection $P$ of dominos: 
$$P = \begin{Bmatrix}
\begin{bmatrix}\frac{t_1}{b_1}\end{bmatrix},
\begin{bmatrix}\frac{t_2}{b_2}\end{bmatrix},
\cdots,
\begin{bmatrix}\frac{t_k}{b_k}\end{bmatrix}
\end{Bmatrix}$$
and a match is a sequence $i_1, i_2, \cdots, i_l$, where $t_{i_1} t_{i_2} \cdots t_{i_l} = b_{i_1} b_{i_2} \cdots b_{i_l}$.
$$PCP = \{\langle P \rangle | P \text{ is an instance of the Post Correspondence Problem with a match}\}$$
And $PCP$ is undecidable.

## Reducibility

**Computation history**: The intermediate computation for a TM $M$ and an input string $w$, assuming that $M$ halts on $w$.

**Linear bounded automaton (LBA)**: Turing machine where the tape head isn't permitted to move off the portion of the tape containing the input.

## Mapping Reducibility

**Computable function**: A function $f: \Sigma^* \rightarrow \Sigma^*$ is a computable function if some Turing machine $M$, on every input $w$, halts with just $f(w)$ on its tape.

**Definition**: Language $A$ is **mapping reducible** to language $B$, written $A \leq_m B$, if there is a computable function $f: \Sigma^* \rightarrow \Sigma^*$, where for every $w$, $$w \in A \Longleftrightarrow f(w) \in B.$$ The function $f$ is called the **reduction** from $A$ to $B$.

**Theorem**: If $A \leq_m B$ and $B$ is decidable, then $A$ is decidable.
**Corollary**: If $A \leq_m B$ and $A$ is undecidable, then $B$ is undecidable.
**Theorem**: If $A \leq_m B$ and $B$ is Turing-recognizable, then $A$ is Turing-recognizable.
**Corollary**: If $A \leq_m B$ and $A$ is not Turing-recognizable, then $B$ is not Turing-recognizable.
**Theorem**: $EQ_{TM}$ is neither Turing-recognizable nor co-Turing-recognizable.

## Recursion Theorem

**Lemma**: There is a computable function: $q: \Sigma^* \rightarrow \Sigma^*$, where if $w$ is any string, $q(w)$ is the description of a Turing machine $P_w$ that prints out $w$ and then halts.

Turing machine $SELF$: $\langle SELF \rangle = \langle AB \rangle$:
1. $A = P_{\langle B \rangle}$
2. $B$: On input $\langle M \rangle$ returns $\langle M \rangle + q(\langle M \rangle)$ 

**Theorem**: Let $T$ be a Turing machine that computes a function $t: \Sigma^* \times \Sigma^* \rightarrow \Sigma^*$. There is a Turing machine $R$ that computes a function $r: \Sigma^* \rightarrow \Sigma^*$, where for every $w$, $$r(w) = t(\langle w \rangle, w).$$
**Theorem**: Let $t: \Sigma^* \rightarrow \Sigma^*$ be a computable function. Then there is a Turing machine $F$ for which $t(\langle F \rangle)$ describes a Turing machine equivalent to $F$. Here, we'll assume that if a string isn't a proper Turing machine encoding, it describes a Turing machine that always rejects immediately.

## Decidability of Logical Theories

**Operations**: $\land, \lor, \lnot$
**Quantifiers**: $\forall, \exists$

## A Definition of Information

> [!definition] Minimal Description
>  Let $x$ is a binary string. The **minimal description** of $x$, written $d(x)$, is the shortest string $\langle M, w \rangle$ where TM $M$ on input $w$ halts with $x$ on its tape. If several such strings exist, select the lexicographically first among them. The **descriptive complexity** of $x$, written $K(x)$, is $$K(x) = |d(x)|.$$

> [!definition] Description Language 
> For a computable function $p: \Sigma^* \rightarrow \Sigma^*$, $d_p(x)$ is the first string $s$ where $p(s) = x$, $K_p(x) = |d_p(x)|$ is the descriptive complexity in language $p$.

**Theorem**: 
- $\exists c \; \forall x \; [K(x) \leq |x| + c]$ ($c = |\langle M \rangle|$ with $M$ halts as soon as it started)
- $\exists c \; \forall x \; [K(xx) \leq K(x) + c]$ ($c = \langle M \rangle$ with $M$ is a double machine)
- $\exists c \; \forall x \; [K(xy) \leq 2K(x) + K(y) + c]$ ($d(x) + d(y)$ but we need separation)
- $\exists c \; \forall x \; [K(xy) \leq 2 log_2(K(x)) + K(x) + K(y) + c]$ ($d(x) + d(y)$ separation by adding length).
- $\forall x \; [K(x) \leq K_p(x) + c]$

## Incompressible Strings and Randomness

**Definition ($c$-compressible)**: Let $x$ be a string. Say that $x$ is **$c$-compressible** if $$K(x) \leq |x| - c.$$If $x$ is not $c$-compressible, we say that $x$ is **incompressible by $c$.** 
If $x$ is incompressible by $1$, we say that $x$ is **incompressible**.

**Theorem**: Incompressible strings of every length exist.
**Corollary**: At least $2^n - 2^{n - c + 1} + 1$ strings of length $n$ are incompressible by $c$.

**Theorem**: Let $f$ be a computable property that holds for almost all strings. Then, for any $b > 0$, the property $f$ is `FALSE` on only finitely many strings that are incompressible by $b$.

**Theorem**: For some constant $b$, for every string $x$, the minimal description $d(x)$ of $x$ is incompressible by $b$.


# Note

- Language: Set of strings.
- Turing-Recognizable > Decidable > Context-Free > Regular.
- CFG = PDA (Context-Free) > DFA = GNFA = Regular Expression (Regular).
- Turing machine $M$ has a unique description $\langle M \rangle$ is a string.
