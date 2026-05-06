
_What makes some problems computationally hard and others easy?_
Complexity is based on input sizes.
# Complexity

> [!definition] Reduce
> Problem $A$ **reduces** to Problem $B$, written $A \leq B$, if one can efficiently solve $A$ (with non-negligible probability), given an algorithm that efficiently solves $B$ (with non-negligible probability).
 





## Class NP

A **verifier** for a language $A$ is an algorithm $V$, where $$A = \{w | V \text{ accepts } \langle w, c \rangle \text{ for some string } c\}.$$
We measure the time of a verifier only in terms of the length of $w$, so a **polynomial time verifier** runs in polynomial time in the length of $w$. A language $A$ is **polynomial verifiable** if it has a polynomial time verifier.

To test the membership in $A$, the verifier uses an additional information $c$ called a **certificate**, or **proof**.

**Theorem**: A language is in $\text{NP}$ if and only if it is decided by some nondeterministic polynomial time Turing machine.

$\text{NP} = \cup_k \text{NTIME}(n^k)$. 

**Member of** $\text{NP}$:
[[Number Theory#Prime Numbers, Unique Factorization, and Finite Fields|COMPOSITES]]

Observation: $$\text{NP} \subseteq \text{EXPTIME} = \cup_k \text{TIME}(2^{n^k})$$
Separate complexity class: Complements of language in NP.
> [!question] 
> Does $\text{coNP} = \text{NP}$? Does $\text{P} = \text{NP}$?


## Class PSPACE

> [!definition] Class PSPACE 
> **PSPACE** is the class of languages that are decidable in polynomial space on a deterministic Turing machine. In other words, $$\text{PSPACE} = \cup_k \text{SPACE}(n^k).$$

## NP-Complete

> [!definition] NP-complete
> A language $B$ is **NP-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{NP}$, and
> 2. every $A$ in $\text{NP}$ is polynomial time reducible to $B$.
> 
> If $B$ merely satisfies condition 2, we say that it is $\text{NP}$-hard

> [!theorem] 
> If $B$ is **NP-complete** and $B \in \text{P}$, then $\text{P} = \text{NP}$ 

> [!definition] Polynomial time computable function
> A function $f: \Sigma^{*} \rightarrow \Sigma^{*}$ is a **polynomial time computable function** if some polynomial time Turing machine $M$ exists that halts with just $f(w)$ on its tape, when started on any input $w$.

> [!definition] Polynomial time reduction
Language $A$ is **polynomial time mapping reducible**, or simply **polynomial time reducible**, to language $B$, written $A \leq_\text{P} B$, if a polynomial time computable function $f: \Sigma^* \rightarrow \Sigma^*$ exists, where for every $w$, $$w \in A \Longleftrightarrow f(w) \in B.$$
The function $f$ is called the **polynomial time reduction** of $A$ to $B$.

> [!theorem] 
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

> [!theorem] Cook-Levin Theorem
 [[Satisfiability Problem|SAT]] is **NP-complete** (revisit the prove).

**Member of NP-Complete**:
$\text{CLIQUE} = \{\langle G, k \rangle | G \text{ is an undirected graph with a } k \text{-clique}\}.$
$\text{VERTEX-COVER} = \{\langle G, k \rangle | G \text{ is an undirected graph that has a } k\text{-node vertex cover}\}$  
$\text{HAMPATH} = \{\langle G, s, t \rangle | G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}.$
$\text{UHAMPATH} = \{\langle G, s, t \rangle | G \text{ is a undirected graph with a Hamiltonian path from } s \text{ to } t\}.$
[[Subset-Sum Problem|SUBSET-SUM]]

## PSPACE-Completeness

> [!definition] PSPACE-complete
 A language $B$ is **PSPACE-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{PSPACE}$, and
> 2. every $A$ in $\text{PSPACE}$ is polynomial time reducible to $B$.
>
> If $B$ merely satisfies condition 2, we say that it is $\text{PSPACE-hard}$.

> [!theorem] 
> [[Satisfiability Problem|TQBF]] is $\text{PSPACE}$-complete.


**Member of NP-Complete**: 
**Formula game**: Player $\text{A}$ selects values for variable with $\forall$ quantifiers, player $\text{E}$ selects values for variable with $\exists$ quantifiers.
$\text{FORMULA-GAME} = \{\langle \phi \rangle | \text{Player E has a winning strategy in the formula game associated with } \phi\}.$
**Generalized geography**: Match last character of a city with the first character of the next city.
$\text{GG} =\{\langle G, b \rangle | \text{Player I has a winning strategy for the generalized geography game played on graph } G \text{ starting at node } b\}$

## Classes L and NL

When consider these classes, we consider two tape:
- A read-only input tape.
- A read/write work tape (measure this).

> [!definition] Class L
 $\text{L}$ is the class of languages that are decidable in logarithmic space on a deterministic Turing machine: $\text{L} = \text{SPACE}(log\; n)$.

> [!definition] Class NL
$\text{NL}$ is the class of languages that are decidable in logarithmic space on a nondeterministic Turing machine: $\text{NL} = \text{NSPACE}(log\;n)$.

$\text{NL} = \text{coNL}$.

>[!definition] Configuration of Turing machine with a read-only input tape
> If $M$ is a Turing machine that has a separate read-only input tape and $w$ is an input, a **configuration of $M$ on $w$** is a setting of the state, the work tape, and the positions of the two tape heads. The input $w$ is not a part of the configuration of $M$ on $w$ (because $w$ is constant).

## NL-completeness

> [!definition] Class NL-complete
> A language $B$ is $\text{NL}$-complete if
> 1. $B \in \text{NL}$, and
> 2. every $A$ in $\text{NL}$ is log space reducible to $B$.

# Intractable

## Hierarchy Theorems

### Space

> [!definition] Space Constructible
A function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is at least $O(log\;n)$, is called **space constructible** if the function that maps the string $1^n$ to the binary representation of $f(n)$ is computable in space $O(f(n))$.

> [!theorem] Space hierarchy theorem
 For any space constructible function $f: \mathcal N \rightarrow \mathcal N$, a language $A$ exists that is decidable in $O(f(n))$ space but not in $o(f(n))$ space.

> [!corollary]
>  For any two functions $f_1, f_2: \mathcal N \rightarrow \mathcal N$, where $f_1(n)$ is $o(f_2(n))$ and $f_2$ is space constructible, $\text{SPACE}(f_1(n)) \subset \text{SPACE}(f_2(n))$.

> [!corollary] 
> For any two real number $0 \leq \epsilon_1 < \epsilon_2$, $$\text{SPACE}(n^{\epsilon_1}) \subset \text{SPACE}(n^{\epsilon_2}).$$

### Time

> [!definition]
>  A function $t: \mathcal N \rightarrow \mathcal N$, where $t(n)$ is at least $O(n\;log\;n)$, is called **time constructible** if the function that maps the string $1^n$ to the binary representation of $t(n)$ is computable in time $O(t(n))$.

**Time hierarchy theorem**: For any time constructible function $f: \mathcal N \rightarrow \mathcal N$, a language $A$ exists that is decidable in $O(t(n))$ time but not decidable in time $o(\frac{t(n)}{log\;t(n)})$.

**Corollary**: For any two functions $t_1, t_2: \mathcal N \rightarrow \mathcal N$, where $t_1(n)$ is $o(\frac{t_2(n)}{log\;t_2(n)})$ and $t_2$ is time constructible, $\text{TIME}(t_1(n)) \subset \text{TIME}(t_2(n))$.

**Corollary**: For any two real numbers $1 \leq \epsilon_1 < \epsilon_2$, we have $\text{TIME}(n^{\epsilon_1}) \subset \text{TIME}(n^{\epsilon_2})$ 

## EXPSPACE-Complete

> [!definition] EXPSPACE
>  A language $B$ is $\text{EXPSPACE}$-complete if
> 1. $B \in \text{EXPSPACE}$, and
> 2. every $A$ in $\text{EXPSPACE}$ is polynomial time reducible to $B$.

**Member of $\text{EXPSPACE-}$complete**:
$\text{EQ}_{REX \uparrow} = \{\langle Q, R \rangle | Q \text{ and } R \text{ are equivalent regular expressions with exponentiation}\}$   

## Relativization 

> [!definition] Oracle
>  An **oracle** for a language $A$ is a device that is capable of reporting whether any string $w$ is a member of $A$. An **oracle Turing machine** $M^A$ is a modified Turing machine that has the additional capability of querying an oracle for $A$. Whenever $M^A$ writes a string on a special **oracle tape**, it is informed whether that string is a member of $A$ in a single computation step.
Let $P^A$ be the class of languages decidable with a polynomial time oracle Turing machine that uses oracle $A$. Define the class $NP^A$ similarly.

## Circuit Complexity

> [!definition] Boolean circuit
> A **Boolean circuit** is a collection of **gates** and **inputs** connected by **wired**. Cycles aren't permitted. Gates take three forms: `AND` gates, `OR` gates, and `NOT` gates.

> [!definition] Circuit Family 
> A **circuit family** $C$ is an infinite list of circuits, $(C_0, C_1, C_2, \cdots)$, where $C_n$ has $n$ input variables. We say that $C$ decides a language $A$ over $\{0, 1\}$ if for every string $w$, $$w \in A \text{ iff } C_n(w) = 1,$$
where $n$ is the length of $w$.

> [!definition] Size of a circuit 
> The **size** of a circuit is the number of gates that it contains.

> [!definition] Depth of a circuit 
> The **depth** of a circuit is the length (number of wires) of the longest path from an input variable to the output gate.

> [!definition] Minimal circuit 
> A circuit is **size (depth) minimal** if no smaller circuit is equivalent to it.

> [!definition] Complexity of a circuit family
>  The **size (depth) complexity** of a circuit family $(C_0, C_1, C_2, \cdots)$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the size of $C_n$. 

> [!definition] Circuit Complexity
> The **circuit complexity** of a language is the size complexity of a minimal circuit family for that language. The **circuit depth complexity** of a language is defined similarly, using depth instead of size.

# Advanced Topics in Complexity Theory

## Approximation Algorithms


## Branching Program

> [!definition] Branching Program
> A **branching program** is a directed acyclic graph where all nodes are labeled by variables, except for two **output nodes** labeled $0$ or $1$. The nodes that are labeled by variables are called **query nodes**. Every query node has two outgoing edges: one labeled $0$ and the other labeled $1$. Both output nodes have no outgoing edges. One of the nodes in a branching program is designated the start node.

> [!definition] Read-once branching program
 A **read-once branching program** is one that can query each variable at most one time on every directed path from the start node to an output node.

> [!lemma] 
> For every $d \geq 0$, a degree-$d$ polynomial $p$ on a single variable $x$ either has at most $d$ roots, or is everywhere equal to $0$.

> [!lemma] 
> Let $\mathcal F$ be a finite field with $f$ elements and let $p$ be a nonzero polynomial on the variable $x_1$ through $x_m$, where each variable has degree at most $d$. If $a_1$ through $a_m$ are selected randomly in $\mathcal F$, then $\Pr[p(a_1, \cdots, a_m) = 0] \leq \frac{md}{f}.$

## Alternating Turing machine

> [!definition] Alternating Turing machine
An **alternating Turing machine** is a nondeterministic Turing machine with an additional feature. Its states, except for $q_{accept}$ and $q_{reject}$, are divided into **universal states** (accept if all its children accept) and **existential states** (accept if any of its child accept).

## Interactive Proof Systems (Class IP)

> [!definition] Verifier
 The **verifier** is a function $V$ that computes its next transmission to the Prover from the message history sent so far. The function $V$ has three inputs:
> 1. **Input string**: The objective is to determine whether this string is a member of some language.
> 2. **Random input**: 
> 3. **Partial message history**: A function has no memory of the dialog that has been sent so far, so we provide the memory externally via a string representing the exchange of messages up to the present point. We use the notation $m_1$#$m_2$#$\cdots$#$m_i$ to represent the exchange of messages $m_1$ through $m_i$.  
> 
> Form $V: \Sigma^* \times \Sigma^* \times \Sigma^* \rightarrow \Sigma^* \cup \{\text{accept}, \text{reject}\}$

> [!definition] Prover
>  The **prover** is a function $P$ with two inputs:
> 4. **Input string**
> 5. **Partial message history**
>  
> Form $P: \Sigma^* \times \Sigma^* \rightarrow \Sigma^*$

> [!definition] 
> The interaction between the Prover and the Verifier. For particular strings $w$ and $r$, we write $(V \leftrightarrow P)(w, r) = \text{accept}$ if a message sequence $m_1$ through $m_k$ exists for some $k$ whereby
> 6. for $0 \leq i < k$, where $i$ is an even number, $V(w, r,$ $m_1$#$m_2$#$\cdots$#$m_i) = m_{i + 1}$;
> 7. for $0 < i < k$, where $i$ is an odd number, $P(w,$ $m_1$#$m_2$#$\cdots$#$m_i) = m_{i + 1}$; and
> 8. the final message $m_k$ is the message history is $\text{accept}$.

> [!definition] Class IP
>  Say that language $A$ is in $\text{IP}$ if some polynomial time computable function $V$ exists such that for some (arbitrary) function $P$ and for even (arbitrary) function $\tilde P$ and for every string $w$, 
> 9. $w \in A$ implies $\Pr[V \leftrightarrow P \text{ accepts } w] \geq \frac{2}{3}$, and
> 10. $w \notin A$ implies $\Pr[V \leftrightarrow \tilde P \text{ accepts } w] \leq \frac{1}{3}.$ 

# Complexity Group

## Sub-exponential

> [!definition] Sub-exponential
> A function $f(x)$ is **sub-exponential** if the following statements are true:
> 1. $f(x) = \ohm((\ln X)^\alpha)$.
> 2. $f(x) = \mathcal O(X^\beta)$.

## Technique

### Decision Tree

> [!definition] Decision Tree Model
> For a problem with input space $S$, then there exists a decision tree model for classifying an input, thus, we can prove the lower bound an algorithm works for this model by using the equality: $$|S| = \text{Number of leaves}.$$

## Note

$$\text{P} \subseteq \text{NP} \subseteq \text{PSPACE} = \text{NPSPACE} = \text{IP} \subseteq \text{EXPTIME}.$$
$$\text{NL} \subset \text{PSPACE} \subset \text{EXPSPACE}$$
$$\text{P} \subset \text{EXPTIME}$$
Language.