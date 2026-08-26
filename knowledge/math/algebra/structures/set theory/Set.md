## Basic Definition

> [!definition] Set
> A **set** is a collection of things (elements).

### Famous Sets

| Notation    | Meaning                     |
| ----------- | --------------------------- |
| $\emptyset$ | Empty set                   |
| $\mathbb N$ | Set of **natural numbers**  |
| $\mathbb Z$ | Set of **integers**         |
| $\mathbb Q$ | Set of **rational numbers** |
| $\mathbb R$ | Set of **real numbers**     |
| $\mathbb C$ | Set of **complex numbers**  |

## Representation

> [!definition] Roster Notation 
> The method of listing the members of a set within braces is sometimes referred to as the **roster notation**

> [!definition] List Comprehension
> We often express element of a set $A$ as elements $s$ of some larger (and already known) set $S$, satisfying some property $P$.
> $$A = \{s \in S \;|\; s \text{ satisfies } P\}$$

### Universal Set

> [!definition] Universal Set
> In our applications of set theory, we have a fixed set $S$ given in advance, and we are concerned only with subsets of this given set. This set is referred as the **universal set**.

## Operation

### Inclusion of Sets

| Symbol                | Operation          |
| --------------------- | ------------------ |
| $\in$                 | Belongs to         |
| $\subset, \subsetneq$ | Proper Subset      |
| $\subseteq$           | Subset             |
| $=$                   | Equal              |
| $\lvert s \rvert$     | Number of Elements |
| $2^S$                 | Power Set          |
### Operation between Sets

| Symbol      | Operation         |
| ----------- | ----------------- |
| $\cup$      | Union             |
| $\cap$      | Intersection      |
| $\setminus$ | Difference        |
| $\amalg$    | Disjoint Union    |
| $\times$    | Cartesian Product |

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
|                  | $A - (B - C) = (A - B) \cup C$                                                                                                                                                                                                               |
|                  | $A - (B \cup C) = (A - B) - C$                                                                                                                                                                                                               |
| De Morgan's Law  | For any sets $A_1, A_2, ..., A_n$, we have:<br>$(A_1 \cup A_2 \cup A_3 \cup \cdots A_n)^c = A_1^c \cap A_2^c \cap A_3^c \cdots \cap A_n^c$; <br>$(A_1 \cap A_2 \cap A_3 \cap \cdots A_n)^c = A_1^c \cup A_2^c \cup A_3^c \cdots \cup A_n^c$. |

### Disjoint

> [!definition] Disjoint
> Two sets $S$ and $T$ are **disjoint** if $S \cap T = \emptyset$, that is, if no element is 'simultaneously' in both of them.

### Complement

> [!definition] Complement
> The **complement** of a subset $T$ in a set $S$ is the difference set $S \setminus T$ consisting of all elements of $S$ which are **not** in $T$.

### Partition

> [!definition] Partition
> A collection of nonempty sets $A_1, A_2, \cdots$ is a **partition** of a set $A$ if they are disjoint and their union is $A$.


