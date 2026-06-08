## Relativization 

> [!definition] Oracle
>  An **oracle** for a language $A$ is a device that is capable of reporting whether any string $w$ is a member of $A$. An **oracle Turing machine** $M^A$ is a modified Turing machine that has the additional capability of querying an oracle for $A$. Whenever $M^A$ writes a string on a special **oracle tape**, it is informed whether that string is a member of $A$ in a single computation step.
>  Let $P^A$ be the class of languages decidable with a polynomial time oracle Turing machine that uses oracle $A$. Define the class $NP^A$ similarly.

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
