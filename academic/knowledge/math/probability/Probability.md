## Probability Foundations

### Random experiments & events

> [!definition] Random Experiments
> **Trial**: When we repeat a random experiment several times, we call each one of them a **trial**.

> [!definition] Sample Space
> A **sample space (or set of outcomes)** is a finite set $\Omega$. Each outcome $\omega \in \Omega$ is assigned a probability $P(\omega)$, where we require that the probability function $$P: \omega \rightarrow \mathbb R$$ satisfy the following two properties: 
> 1. $0 \leq P(w) \leq 1 \quad \forall \omega \in \Omega$
> 2. $\sum_{\omega \in \Omega} P(\omega) = 1.$

> [!definition] Event
> An **event** is any subset of $\Omega$. We assign a probability to an event $E \subset \Omega$ by setting $$P(E) = \sum_{\omega \in E} P(\omega)$$
> In particular, $P(\emptyset) = 0$ by convention, and $P(\Omega) = 1$

> [!definition] Disjoint
> We say that two events $E$ and $F$ are **disjoint** if $E \cap F = \emptyset$.

### Axiomatic Probability

> [!axiom] Axioms of Probability
> - Axiom 1: For any event $A$, $P(A) \geq 0$.
> - Axiom 2: Probability of the sample space $S$ is $P(S) = 1.$
> - Axiom 3: If $A_1, A_2, A_3, \cdots$ are disjoint events, then $P(A_1 \cup A_2 \cup A_3 \cdots) = P(A_1) + P(A_2) + P(A_3) + \cdots$

> [!example]
> Using the axioms of probability:
> 1. For any event $A$, $P(A^c) = 1 - P(A)$.
> 2. The probability of the empty set is zero, i.e., $P(\emptyset) = 0$.
> 3. For any event $A$, $P(A) \leq 1$.
> 4. $P(A - B) = P(A) - P(A \cap B)$.
> 5. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$,
> 6. If $A \subset B$ then $P(A) \leq P(B)$.

> [!proposition] Continuity of probability
> 1. Let $A_1, A_2, A_3, \cdots$ be a sequence of increasing events, that is $$A_1 \subset A_2 \subset A_3 \subset \cdots$$ then $$P(\bigcup_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(A_n).$$
> 2. Let $A_1, A_2, A_3, \cdots$ be a sequence of decreasing events, that is $$A_1 \supset A_2 \supset A_3 \supset \cdots$$ then $$P(\bigcap_{i = 1}^{\infty}) = \lim_{n \rightarrow \infty} P(A_n).$$
> 3. For any sequence of events $A_1, A_2, A_3, \cdots$ prove 
> $$P(\bigcup_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(\bigcup_{i = 1}^n A_i),$$ 
> $$P(\bigcap_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(\bigcap_{i = 1}^n A_i).$$ 

> [!remark]
> Idea: Let $B_1 = A_1, B_{i + 1} = A_{i + 1} - A_i$

> [!theorem] Difference Lemma
> Let $Z, W_0, W_1$ be events defined over some probability space. Suppose that $W_0 \land \overline{Z}$. Suppose that $W_0 \land \overline{Z}$ occurs if and only if $W_1 \land \overline{Z}$ occurs. Then we have $$|P[W_0] - P[W_1]| \leq P[Z].$$

### Conditional Probability

> [!definition] Conditional Probability
> If $A$ and $B$ are two events in a sample space $S$, then the **conditional probability of** $A$ **given** $B$ is defined as $$P(A | B) = \frac{P(A \cap B)}{P(B)}, \text{when } P(B) > 0.$$

> [!definition] Axiom of Probability for Conditional Probability
> - Axiom 1: For any event $A$, $P(A | B) \geq 0$.
> - Axiom 2: Conditional probability of $B$ given $B$ is $1$, i.e., $P(B | B) = 1$.
> - Axiom 3: If $A_1, A_2, A_3, \cdots$ are disjoint events, then $$P(A_1 \cup A_2 \cup A_3 \cdots | B) = P(A_1 | B) + P(A_2 | B) + P(A_3 | B) + \cdots$$

> [!example]
> For three events, $A$, $B$ and $C$, with $P(C) > 0$, we have
> - $P(A^c | C) = 1 - P(A | C)$;
> - $P(\emptyset | C) = 0$;
> - $P(A | C) \leq 1$;
> - $P(A - B | C) = P(A - C) - P(A \cap B | C)$;
> - $P(A \cup B | C) = P(A | C) + P(B | C) - P(A \cap B | C)$;
> - if $A \subset B$ then $P(A | C) \leq P(B | C)$.

> [!proposition] Chain Rule for Conditional Probability
> Let $A_1, A_2, \ldots, A_n$ be events with
> $$P(A_1 \cap A_2 \cap \cdots \cap A_n) > 0.$$
> Then
> $$P(A_1 \cap A_2 \cap \cdots \cap A_n)
> = P(A_1)
>   P(A_2 \mid A_1)
>   P(A_3 \mid A_1 \cap A_2)
>   \cdots
>   P(A_n \mid A_1 \cap \cdots \cap A_{n-1}).$$

> [!theorem] Law of Total Probability
> 1. If $B_1, B_2, B_3, \cdots$ is a partition of the sample space $S$, then for any event $A$, we have: $$P(A) = \sum_{i} P(A \cap B_i) = \sum_{i} P(A | B_i) P(B_i)$$
> 2. Continuous version: $$P(A) = \int_{-\infty}^\infty P(A | X = x) f_X(x) dx$$

> [!theorem] Bayes's Rule
> - For any two events $A$ and $B$, where $P(A) \neq 0$, we have $$P(B | A) = \frac{P(A | B) P(B)}{P(A)}.$$
> - If $B_1, B_2, B_3, \cdots$ form a partition of the sample space $S$, and $A$ is any event with $P(A) \neq 0$, we have $$P(B_j | A) = \frac{P(A | B_j) P(B_j)}{\sum_i P(A | B_i) P(B_i)}$$

### Independence

> [!definition] Independence
> Two events $A$ and $B$ are independent if $P(A \cap B) = P(A) P(B)$.
> If $P(B) \neq 0$, then $P(A | B) = P(A)$.
> For $n$ events $A_1, A_2, \cdots, A_n$ to be independent, we must have
> $$P(A_i \cap A_j) = P(A_i) P(A_j), \forall i, j \in \{1, 2, \cdots, n\};$$
> $$P(A_i \cap A_j \cap A_k) = P(A_i) P(A_j) P(A_k), \forall i, j, k \in \{1, 2, \cdots, n\};$$
> $$\vdots$$
> $$P(A_1 \cap A_2 \cap A_3 \cdots \cap A_n = P(A_1) P(A_2) P(A_3) \cdots P(A_n).$$

> [!lemma]
> If $A$ and $B$ are independent then
> - $A$ and $B^c$ are independent,
> - $A^c$ and $B$ are independent,
> - $A^c$ and $B^c$ are independent.

> [!proposition]
> If $A_1, A_2, \cdots, A_n$ are independent then
> $$P(A_1 \cup A_2 \cup \cdots \cup A_n) = 1 - (1 - P(A_1))(1 - P(A_2)) \cdots (1 - P(A_n))$$

> [!lemma]
> Consider two events $A$ and $B$, with $P(A) \neq 0$ and $P(B) \neq 0$. If $A$ and $B$ are disjoint, then they are **not** independent.

> [!definition] Conditional Independent
> Two events $A$ and $B$ are **conditional independent** given an event $C$ with $P(C) > 0$ if $$P(A \cap B | C) = P(A | C) P(B | C)$$
> If $A$ and $B$ are conditionally independent given $C$, then $$P(A | B,C) = P(A | C)$$
