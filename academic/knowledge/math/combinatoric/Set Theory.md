
## Basic

> [!definition] Set
> A **set** is a collection of things (elements).

> [!definition] Belongs Notation
> We use the special notation $$x \in S$$ to mean that "$x$ is an element of $S$" or "$x$ belongs to $S$".

> [!definition] Roster Notation 
> The method of listing the members of a set within braces is sometimes referred to as the **roster notation**

> [!definition] Set Equality
> Two sets $A$ and $B$ are said to be equal (or identical) if they consist of exactly the same elements, in which case we write $A = B$. If one of the sets contains an element not in the other, we say the sets are unequal and we write $A \neq B$.

> [!definition] Subset
> A set $A$ is said to be a **subset** of a set $B$, and we write $$A \subseteq B,$$ whenever every element of $A$ also belongs to $B$. We also say that $A$ is contained in $B$ or that $B$ contains $A$. The relation $\subseteq$ is referred to as set inclusion. 

> [!definition] Proper Subset
> If $A \subseteq B$ but $A \neq B$, then we say that $A$ is a **proper subset** of $B$; we indicate this by writing $A \subset B$.

> [!definition] Empty Set
> The set with no elements, i.e., $\emptyset = \{\}$ is the **null set**, **void set** or the **empty set**. For any set $A, \emptyset \subset A$.

> [!definition] Universal Set
> In our applications of set theory, we have a fixed set $S$ given in advance, and we are concerned only with subsets of this given set. This set is referred as the **universal set**.

## Set Operations

> [!definition] Union
> The **union** of two sets, denoted by $A \cup B$, is a set containing all elements that are in $A$ **or** in $B$ (possibly both).

> [!definition] Intersection
> The **intersection** of two sets $A$ and $B$, denoted by $A \cap B$, consists of all elements that are both in $A$ **and** $B$.

> [!definition] Complement
> The **complement** of a set $A$, denoted by $A^c$ or $\overline A$, is the set of all elements that are in the universal set $S$ but are not in $A$.

> [!definition] Difference
> The **difference (subtraction)** is defined as follows. The set $A - B$ consists of elements that are in $A$ but not in $B$.

> [!definition] Disjoint
> Two sets $A$ and $B$ are **mutually exclusive** or **disjoint** if they do not have any shared elements; i.e., their intersection is the empty set, $A \cap B = \emptyset$. More generally, several sets are called disjoint if they are pairwise disjoint, i.e., no two of them
 >share a common elements 

> [!definition] Partition
> A collection of nonempty sets $A_1, A_2, \cdots$ is a **partition** of a set $A$ if they are disjoint and their union is $A$.

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


> [!definition] Cartesian Product
> A **Cartesian product** of two sets $A$ and $B$, written as $A \times B$, is the set containing **ordered** pairs from $A$ and $B$. That is, if $C = A \times B$, then each element of $C$ is of the form $(x, y)$, where $x \in A$ and $y \in B$: $$A \times B = \{(x, y) | x \in A \text{ and } y \in B\}.$$ 

## Cardinality

> [!definition] Cardinality
> Consider a set $A$. If $A$ has only a finite number of elements, its cardinality is simply the number of elements in $A$.

> [!definition] Countable Set
> Set $A$ is called countable if one of the following is true
> 1. If it is a finite set, $|A| < \infty$; or
> 2. it can be put in one-to-one correspondence with natural numbers $\mathbb N$, in which case the set is said to be countably infinite.

> [!definition] Uncountable Set
> A set is called uncountable if it is not countable.

> [!theorem]
> Any subset of a countable set is countable.
> Any superset of an uncountable set is uncountable.
> If $A_1, A_2, \cdots$ is a list of countable sets, then the set $\bigcup_i A_i = A_1 \cup A_2 \cup A_3 \cdots$ is also countable.
> If $A$ and $B$ are countable, then $A \times B$ is also countable.

> [!example]
> The set of all subsets of $\mathbb N$, $A = \{B : B \subset \mathbb N\}$ has a one-to-one correspondence to $[0, 1]$ so the set is uncountable.
> 



