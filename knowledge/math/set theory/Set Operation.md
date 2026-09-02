## Basic Definition

### Cartesian Product

> [!definition] Cartesian Product
> The **Cartesian Product** of sets $A$ and $B$, written $A \times B$, is the set of **ordered** pairs
> $$A \times B = \{(x, y) \mid x \in A \text{ and } y \in B\}.$$
> The $n$-fold product $A_1 \times \cdots \times A_n$ consists of $n$-tuples; $A^n$ abbreviates the $n$-fold product of $A$ with itself.

> [!remark] Why this definition carries the vault
> Every Scope line in `properties/` is written over a product: a [[Relation]] is a subset of $A \times B$, a [[Function|function]] is a special relation, a [[Binary Operation]] is a function $S \times S \to S$. Ordered pairs are taken as primitive here; the set-theoretic construction $(x,y) := \{\{x\},\{x,y\}\}$ is a foundational detail, noted in [[Foundations of Mathematics]] and used nowhere else.

### Union

> [!definition] Union
> The **union** of two sets $S$ and $T$ denoted $S \cup T$ is the set consisting of all elements in either $S$ or $T$. 

### Intersection

> [!definition] Intersection
> The **intersection** of two sets $S$ and $T$ denoted $S \cap T$ is the set consisting of all elements that in both $S$ and $T$.

### Difference

> [!definition] Difference
> The **difference** of set $S$ and set $T$ denoted $S \setminus T$ (or $S - T$) is the set consisting of all elements of $S$ which are **not** in $T$.

### Complement

> [!definition] Complement
> The **complement** of a subset $T$ of a universal set $S$ is the difference set $S \setminus T$.

### Disjoint Union

> [!definition] Disjoint Union
> The **disjoint union** of set $S$ and set $T$ denoted as $S \; \Pi \; T$ is the set consisting of all elements that only in $S$ or only in $T$.

### Partition

> [!definition] Partition
> A collection of nonempty sets $A_1, A_2, \cdots$ is a **partition** of a set $A$ if they are disjoint and their union is $A$.

### Power Set

> [!definition] Power Set
> The **power set** of $S$, written $P(S)$ or $2^S$, is the set of all subsets of $S$.


## Notation

### Inclusion

| Symbol                | Operation          |
| --------------------- | ------------------ |
| $\in$                 | Belongs to         |
| $\subset, \subsetneq$ | Proper Subset      |
| $\subseteq$           | Subset             |
| $=$                   | Equal              |
| $\lvert s \rvert$     | Number of Elements |
| $2^S$                 | Power Set          |

### Operations

| Symbol      | Operation         |
| ----------- | ----------------- |
| $\cup$      | Union             |
| $\cap$      | Intersection      |
| $\setminus$ | Difference        |
| $\amalg$    | Disjoint Union    |
| $\times$    | Cartesian Product |
### Famous Sets

| Notation    | Meaning                     |
| ----------- | --------------------------- |
| $\emptyset$ | Empty set                   |
| $\mathbb N$ | Set of **natural numbers**  |
| $\mathbb Z$ | Set of **integers**         |
| $\mathbb Q$ | Set of **rational numbers** |
| $\mathbb R$ | Set of **real numbers**     |
| $\mathbb C$ | Set of **complex numbers**  |

### Common Law

| Property         | Description                                                                                                                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Commutative Law  | $A \cup B = B \cup A$, $A \cap B = B \cap A$                                                                                                                                                                                                 |
| Associative Law  | $A \cup (B \cup C) = (A \cup B) \cup C$, $A \cap (B \cap C) = (A \cap B) \cap C$                                                                                                                                                             |
| Distributive Law | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$, $A \cup (B \cap C) = (A \cup B) \cap (A \cap C)$                                                                                                                                           |
|                  | $A \cup A = A$, $A \cap A = A$                                                                                                                                                                                                               |
|                  | $A \subseteq A \cup B$, $A \cap B \subseteq A$                                                                                                                                                                                               |
|                  | $A \cup \emptyset = A$, $A \cap \emptyset = \emptyset$                                                                                                                                                                                       |
|                  | $A \cup (A \cap B) = A$, $A \cap (A \cup B) = A$                                                                                                                                                                                             |
|                  | $A \subseteq C$, $B \subseteq C$, then $A \cup B \subseteq C$                                                                                                                                                                                |
|                  | $C \subseteq A$, $C \subseteq B$, then $C \subseteq A \cap B$                                                                                                                                                                                |
|                  | $A \subset B$, $B \subset C$, then $A \subset C$                                                                                                                                                                                             |
|                  | $A \subseteq B$, $B \subseteq C$, then $A \subseteq C$                                                                                                                                                                                       |
|                  | $A \subset B$, $B \subseteq C$, then $A \subset C$                                                                                                                                                                                           |
|                  | $A - (B \cap C) = (A - B) \cup (A - C)$                                                                                                                                                                                                      |
|                  | $A - (B - C) = (A - B) \cup (A \cap C)$                                                                                                                                                                                                      |
|                  | $A - (B \cup C) = (A - B) - C$                                                                                                                                                                                                               |
| De Morgan's Law  | For any sets $A_1, A_2, ..., A_n$, we have:<br>$(A_1 \cup A_2 \cup A_3 \cup \cdots A_n)^c = A_1^c \cap A_2^c \cap A_3^c \cdots \cap A_n^c$; <br>$(A_1 \cap A_2 \cap A_3 \cap \cdots A_n)^c = A_1^c \cup A_2^c \cup A_3^c \cdots \cup A_n^c$. |