
## Finite Automata

> [!definition] Finite Automata
> A Finite Automata $M$ is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$:
> 1. $Q$ is a finite set called the **states**,
> 2. $\Sigma$ is a finite set called the **alphabet**,
> 3. $\delta: Q \times \Sigma \rightarrow Q$ is the **transition function**,
> 4. $q_0 \in Q$ is the **start state**, and
> 5. $F \subseteq Q$ is the **set of accept states**.

Let $A$ is the set of string that $M$ accepts, then we call $M$ recognizes language $A$ or $A = L(M)$.

**Regular Language**: If there exist finite automata accepts a language, the language is regular.

Operation for languages:
- **Union**: $A \cup B = \{x | x \in A \text{ or } x \in B\}$
- **Concatenation**: $A \circ B = \{x y | x \in A \text{ and } y \in B\}$  
- **Star**: $A^{*} = \{x_1x_2 \cdots x_k | k \geq 0 \text{ and each } x_i \in A\}$
For union and intersection, create a combined DFA by using cartesian product of two DFA.
For concatenation, connect accept state of $A$ with start state of $B$.
For star, create a new start node for $A$ and connect accept state with this new start node.
For complement, invert the type of all states.

## Nondeterministic Finite Automaton

> [!Definition] Nondeterministic Finite Automaton
 >A Nondeterministic Finite Automaton is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$:
> 1. $Q$ is a finite set called the **states**,
> 2. $\Sigma$ is the input **alphabet**,
> 3. $\delta: Q \times \Sigma \rightarrow \mathcal P(Q)$ is the **transition function**,
> 4. $q_0 \in Q$ is the **start state**, and
> 5. $F \subseteq Q$ is the **set of accept states**.

## Regular Expression

> [!definition] Regular Expression
 $R$ is a Regular Expression if $R$ is:
> 1. $a$ for some $a$ in $\Sigma$,
> 2. $\varepsilon$,
> 3. $\emptyset$,
> 4. $R_1 \cup R_2$ for some regular expression $R_1, R_2$.
> 5. $R_1 \circ R_2$ for some regular expression $R_1, R_2$, or
> 6. $R_1^{*}$ for a regular expression $R_1$.

## Generalized Nondeterministic Finite Automaton 

> [!Definition] Generalized Nondeterministic Finite Automaton
> A Generalized Nondeterministic Finite Automaton is a 5-tuple $(Q, \Sigma, \delta, q_{start}, q_{accept})$, where:
> 1. $Q$ is a finite set called the **states**,
> 2. $\Sigma$ is the input **alphabet**,
> 3. $\delta: (Q - \{q_{accept}\}) \times (Q - \{q_{start}\}) \rightarrow \mathcal R$ is the **transition function**,
> 4. $q_{start}$ is the **start state**, and
> 5. $q_{accept}$ is the **set of accept states**.

### DFA to GNFA

At $q_{start}$ and transition $\delta(s_{start}, q_0) = \varepsilon$
At $q_{accept}$ and transitions $\delta(F, q_{accept}) = \varepsilon$

### GNFA to Regular Expression

> [!algorithm] Convert GNFA to Regular Expression
> **Input:** A generalized nondeterministic finite automaton $G$  
> **Output:** A regular expression equivalent to $G$
> 
> ---
>
> 1. Let $k \gets |Q|$, the number of states of $G$.
>
> 2. **Base case ($k = 2$):**
>    - If $Q = \{q_{start}, q_{accept}\}$, return the regular expression
>      $\delta(q_{start}, q_{accept})$.
>
> 3. **Recursive case ($k > 2$):**
>    - Choose a state $q_{rip} \in Q$ such that
>      $q_{rip} \neq q_{start}$ and $q_{rip} \neq q_{accept}$.
>
>    - Construct a new GNFA
>      $G' = (Q', \Sigma, \delta', q_{start}, q_{accept})$, where:
>      - $Q' \gets Q \setminus \{q_{rip}\}$
>      - For all $q_i, q_j \in Q'$, define:
>        $$\delta'(q_i, q_j)
>        \gets (\delta(q_i, q_{rip}))
>              (\delta(q_{rip}, q_{rip}))^{*}
>              (\delta(q_{rip}, q_j))
>              \;\cup\;
>              \delta(q_i, q_j)$$
>
> 4. Return `Convert(G')`.


## Pumping Lemma for Regular Language

If $A$ is a regular language, then there is a number $p$ (the pumping length) where if $s$ is any string in $A$ of **length at least** $p$, then $s$ may be divided into three pieces, $s = xyz$ such that:
1. for each $i \ge 0$, $xy^{i}z \in A$,
2. $|y| > 0$, and
3. $|xy| \leq p$
Idea: If $A$ is a regular language then there exist a DFA $M = (Q, \Sigma, \delta, q_0, F)$ of $A$ and we can choose $p = |Q| + 1$ so there exist a cycle in the traversal path of $s$ (this is $y$ and $|xy| \leq p$ means that we go through the cycle in the first $|Q| + 1$ vertexes).

## Finite State Transducer

> [!definition] Finite State Transducer
A Nondeterministic Finite Automaton is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$:
> 1. $Q$ is a finite set called the **states**,
> 2. $\Sigma$ is the input **alphabet**,
> 3. $\Gamma$ is the output **alphabet**,
> 4. $\delta: Q \times \Sigma \rightarrow Q \times \Gamma$ is the **transition function**, and
> 5. $q_0 \in Q$ is the **start state**.
> 
> Then for an input $s$, we can find an output $s'$.

## Index of DFA

**Indistinguishable**: Let $x$ and $y$ be strings and $L$ be any language, if there is a $z$ that $L$ accepts only one of $xz$ and $yz$ then $x$ and $y$ are **distinguishable by language** $L$. Otherwise, if for every string $z$, $xz \in L$ whenever $yz \in L$ then $x$ and $y$ are **indistinguishable by language** $L$.

**Pairwise distinguishable**: Let $L$ be a language and $X$ be a set of strings, if any pair of strings in $X$ are distinguishable by $L$ then $X$ is called **pairwise distinguishable by** $L$. 

### Myhill-Nerode Theorem

Let the **index of language** $L$ be the size of the maximum **pairwise distinguishable** set of $L$ then:
1. If a language $L$ is recognized by a DFA with $k$ state then the index of $L \leq k$.
2. If the index of $L$ is $k$ then $L$ is recognized by a DFA with $k$ state.
3. $L$ is regular if and only if it has a finite index $k$. Moreover, this index $k$ is the size of the smallest DFA recognizes $L$.
**Idea:** If two string end up in the same state, then they are **indistinguishable**.

## Context-Free Grammar

>[!definition] Context-free Grammar
>A **context-free grammar** is a 4-tuple $(V, \Sigma, R, S)$, where
>1. $V$ is a finite set called the **variables**,
>2. $\Sigma$ is a finite set, disjoint from $V$, called the **terminals**,
>3. $R$ is a finite set of **rules**, with each rule being a variable and a string of variables and terminals, and
>4. $S \in V$ is the start variable.

**Context-Free Language**: Language that can be generated by some context-free grammar.

### Designing Context-Free Grammars

1. We can easily create the union of many CFLs.
2. We can create CFG for a regular language (based on the [[Automata and Languages#Finite Automata|DFA]])
3. We can create string that have substrings are linked.
4. We can create recursive structures.

**Leftmost derivation**: A derivation of a string $w$ in a grammar $G$ is a **leftmost derivation** if at every step the leftmost remaining variable is the one replaced.

**Ambiguously**: A string $w$ is derived **ambiguously** in context-free grammar $G$ if it has two or more different leftmost derivations. Grammar $G$ is **ambiguous** if it generates some string ambiguously.

## Chomsky Normal Form

> [!definition] Chomsky Normal Form
A context-free grammar is in **Chomsky normal form** if every rule is of the form: $$\begin{split}
A &\rightarrow BC \\
A &\rightarrow a
\end{split}$$
where $a$ is any terminal and $A, B$ and $C$ are any variables with $B, C$ is not the start variable. Additionally, $S \rightarrow \varepsilon$ is permitted.

> [!theorem]
 Any context-free grammar is generated by a context-free grammar in Chomsky normal form.

### Convert From CFG to Chomsky Normal Form

> [!algorithm] Conversion of a CFG to Chomsky Normal Form
> **Input:** A context-free grammar $G = (V, \Sigma, R, S)$  
> **Output:** An equivalent grammar in proper (normalized) form
>
> 1. **Add a new start symbol.**  
>    Introduce a new start variable $S_0$ and add the rule:
>    $$S_0 \rightarrow S.$$
>
> 2. **Remove $\varepsilon$-rules.**  
>    For each $\varepsilon$-rule $A \rightarrow \varepsilon$:
>    - Find every rule whose right-hand side contains $A$.
>    - Add additional rules obtained by removing $A$ from the right-hand side.
>
> 3. **Remove unit rules.**  
>    Eliminate all rules of the form:
>    $$A \rightarrow B,$$
>    where $A$ and $B$ are variables.
>
> 4. **Convert remaining rules into proper form.**  
>    For each rule of the form:
>    $$A \rightarrow u_1 u_2 \cdots u_k \quad \text{with } k \ge 3,$$
>    introduce new variables $A_1, A_2, \ldots, A_{k-2}$ and replace the rule by:
>    - $A \rightarrow u_1 A_1$
>    - $A_1 \rightarrow u_2 A_2$
>    - $\vdots$
>    - $A_{k-2} \rightarrow u_{k-1} u_k$


## Pushdown Automaton

>[!definition] Pushdown Automaton
> A **pushdown automaton** is a 6-tuple $(Q, \Sigma, \Gamma, \delta, q_0, F)$ where $Q, \Sigma, \Gamma, F$ are all finite sets, and
>1. $Q$ is the set of states,
>2. $\Sigma$ is the set of input alphabet,
>3. $\Gamma$ is the set of stack alphabet,
>4. $\delta: Q \times \Sigma_\varepsilon \times \Gamma_\varepsilon \rightarrow \mathcal P(Q \times \Gamma_\varepsilon)$ is the transition function.
>5. $q_0 \in Q$ is the start state, and
>6. $F \subseteq Q$ is the set of accept states.

Note: For a transition $\delta(q, a, b) \rightarrow c$ (at state $q$, reading input $a$, stack popping $b$ and add $c$ to stack), we have:
- If $a = \varepsilon$ then we are not reading from input.
- If $b = \varepsilon$ then we are not popping and reading from the stack (so we are first checking if stack top $= b$ then pop if we make the transition).
- If $c = \varepsilon$ then we are not pushing to the stack.
Because we can not get stack size or input size, we can use $\$$ symbol for tracking input end and stack end.

Note: Pushdown automaton is nondeterministic.

## Relationship Between Context-Free Grammar and Pushdown Automaton

>[!theorem] 
>A language is context free if and only if some pushdown automaton recognizes it.

### CFG to PDA

> [!algorithm] Algorithm (CFG → PDA Construction)
> **Input:** A context-free grammar $G = (V, \Sigma, R, S)$  
> **Output:** A pushdown automaton $P$ recognizing $L(G)$
> 
> ---
>
> 1. Initialize the PDA:
>    - $Q \gets \{q_{start}, q_{loop}, q_{accept}\} \cup E$,  
>      where $E$ is a set of auxiliary (support) states.
>
> 2. Define the transition function $\delta$ as follows:
>
>    **(a) Initialization**
>    - $\delta(q_{start}, \varepsilon, \varepsilon)
>       \gets \{(q_{loop}, S\$)\}$
>
>    **(b) Variable expansion**
>    - For each production rule $A \rightarrow w \in R$:
>      - If the top of the stack is $A$, then  
>        $\delta(q_{loop}, \varepsilon, A)$ expands $A$.
>
>      - If $w = u_1 u_2 \cdots u_\ell$:
>        1. Introduce new states $q_1, q_2, \ldots, q_{\ell-1} \in E$
>        2. Add transitions:
>           - $\delta(q_{loop}, \varepsilon, A) \ni (q_1, u_\ell)$
>           - For $i = 1$ to $\ell - 2$:
>             - $\delta(q_i, \varepsilon, \varepsilon)
>                \gets \{(q_{i+1}, u_{\ell-i})\}$
>           - $\delta(q_{\ell-1}, \varepsilon, \varepsilon)
>              \gets \{(q_{loop}, u_1)\}$
>
>    **(c) Terminal matching**
>    - For each terminal $a \in \Sigma$:
>      - $\delta(q_{loop}, a, a)
>         \gets \{(q_{loop}, \varepsilon)\}$
>
>    **(d) Acceptance**
>    - If the stack contains only $\$$:
>      - $\delta(q_{loop}, \varepsilon, \$)
>         \gets \{(q_{accept}, \varepsilon)\}$

### PDA to CFG

> [!algorithm] Algorithm (PDA → CFG Construction)
> **Input:** A pushdown automaton  
> $P = (Q, \Sigma, \Gamma, \delta, q_0, \{q_{accept}\})$
>
> **Output:** A context-free grammar  
> $G = (V, \Sigma, R, S)$ such that $L(G) = L(P)$
> 
> ---
>
> 1. Define the set of variables:
>    - $V \gets \{ A_{pq} \mid p, q \in Q \}$
>
> 2. Define the set of terminals:
>    - Terminals$(G) \gets \Sigma$
>
> 3. Construct the set of production rules $R$ as follows:
>
>    **(a) Stack-matching rules**
>    - For all states $p, q, r, s \in Q$, stack symbol $u \in \Gamma$,
>      and input symbols $a, b \in \Sigma_\varepsilon$:
>      - If
>        - $(r, u) \in \delta(p, a, \varepsilon)$, and
>        - $(q, \varepsilon) \in \delta(s, b, u)$,
>      - then add the production:
>        - $A_{pq} \rightarrow a \, A_{rs} \, b$
>
>    **(b) Concatenation rules**
>    - For all states $p, q, r \in Q$, add:
>      - $A_{pq} \rightarrow A_{pr} A_{rq}$
>
>    **(c) Empty-path rules**
>    - For all states $p \in Q$, add:
>      - $A_{pp} \rightarrow \varepsilon$
>
> 4. Define the start variable:
>    - $S \gets A_{q_0, q_{accept}}$

## Pumping Lemma for Context-Free Languages

If $A$ is a context-free language, then there is a number $p$ (the pumping length) where, if $s$ is any string in $A$ of length at least $p$, then $s$ may be divided into five pieces $s = uvxyz$ satisfying the conditions
1. for each $i \geq 0, uv^ixy^iz \in A$
2. $|vy| > 0$, and
3. $|vxy| \leq p$.

Let $b$ be the maximum number of symbols in the right-hand side of a rule, then we can choose $p = b^{|V| + 1}$

## Deterministic Pushdown Automaton

> [!definition] Deterministic Pushdown Automaton
> A **deterministic pushdown automaton (DPDA)** is a 6-tuple
> $(Q, \Sigma, \Gamma, \delta, q_0, F)$ where $Q, \Sigma, \Gamma, F$ are all finite sets, and:
>
> 1. $Q$ is the set of states,
> 2. $\Sigma$ is the input alphabet,
> 3. $\Gamma$ is the stack alphabet,
> 4. $\delta : Q \times \Sigma_\varepsilon \times \Gamma_\varepsilon
>    \rightarrow (Q \times \Gamma_\varepsilon) \cup \{\emptyset\}$
>    is the transition function,
> 5. $q_0 \in Q$ is the start state, and
> 6. $F \subseteq Q$ is the set of accepting states.
>
> The transition function $\delta$ must satisfy the following determinism condition:
>
> For every $q \in Q$, $a \in \Sigma$, and $x \in \Gamma$, **exactly one** of
> $$\delta(q, a, x),\ \delta(q, a, \varepsilon),\ \delta(q, \varepsilon, x),\ \delta(q, \varepsilon, \varepsilon)$$
> is nonempty.
