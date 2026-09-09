Reference:
- [[Book Reference|Term Rewriting and All That]]: - Chapter 2: Abstract Reduction Systems, Section 2.1: Equivalence and reduction; Section 2.2: Well-founded induction.

## Definition

> [!definition] Abstract Reduction System
> An **abstract reduction system** is a pair $(A, \rightarrow)$, where:
> - $A$: Original set.
> - $\rightarrow$: A [[Relation]] on $A$ called **reduction**.

> [!remark]
> The reduction $\rightarrow$ might go on forever.

| Notation              | Formula                                |
| --------------------- | -------------------------------------- |
| $\xrightarrow{0}$     | $\{(x, x) \mid x \in A\}$              |
| $\xrightarrow{i+1}$   | $\xrightarrow{i} \circ \rightarrow$    |
| $\xrightarrow{+}$     | $\cup_{i > 0} \xrightarrow{i}$         |
| $\xrightarrow{*}$     | $\xrightarrow{+} \cup \xrightarrow{0}$ |
| $\xrightarrow{=}$     | $\rightarrow \cup \xrightarrow{0}$     |
| $\xrightarrow{-1}$    | $\{(y, x) \mid x \rightarrow y\}$      |
| $\leftarrow$          | $\xrightarrow{-1}$                     |
| $\leftrightarrow$     | $\rightarrow \cup \leftarrow$          |
| $\xleftrightarrow{+}$ | $(\leftrightarrow)^+$                  |
| $\xleftrightarrow{*}$ | $(\leftrightarrow)^*$                  |
### Element of the Reduction

> [!definition] Element of the Reduction
> 1. $x$ is **reducible** iff there is a $y$ such that $x \rightarrow y$.
> 2. $x$ is **in normal form (irreducible)** iff it is not reducible.
> 3. $y$ is **a normal form of** $x$ iff $x \xrightarrow{*} y$ and $y$ is in normal form. If $x$ has a uniquely determined normal form, the latter is denoted by $x \downarrow$.
> 4. $y$ is a **direct successor** of $x$ iff $x \rightarrow y$.
> 5. $y$ is a **successor** of $x$ iff $x \xrightarrow{+} y$.
> 6. $x$ and $y$ are **joinable** iff there is a $z$ such that $x \xrightarrow{*} z \xleftarrow{*} y$, in which case we write $x \downarrow y$.

### Graph Analogy

| ARS                             | Graph                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------- |
| $x \rightarrow y$               | An edge.                                                                              |
| $\rightarrow^+ / \rightarrow^*$ | Reachable by a non-empty path/by a path.                                              |
| $\leftrightarrow$               | Forget the direction                                                                  |
| $(\leftrightarrow)^*$           | Same weakly connected component.                                                      |
| Normal Form                     | A sink — out-degree $0$.                                                              |
| Terminating                     | No infinite forward path.                                                             |
| $x \downarrow y$                | $x$ and $y$ have a **common descendant**.                                             |
| Normalizing                     | Every vertex can reach a sink.                                                        |
| Church-Rosser                   | Any two vertices in the same weakly connected component have a **common descendant**. |

## Property

| Name               | Property                                                                        |
| ------------------ | ------------------------------------------------------------------------------- |
| Church-Rosser      | $x \xleftrightarrow{*} y \implies x \downarrow y$.                              |
| Confluent          | $y_1 \xleftarrow{*} x \xrightarrow{*} y_2 \implies y_1 \downarrow y_2$.         |
| Terminating        | There is no infinite descending chain $a_0 \rightarrow a_1 \rightarrow \cdots$. |
| Normalizing        | Every element has a normal form.                                                |
| Convergent         | It is both confluent and terminating.                                           |
| Semi-Confluent     | $y_1 \leftarrow x \xrightarrow{*} y_2 \implies y_1 \downarrow y_2$.             |
| Finitely Branching | Each element has only finitely many direct successors.                          |
| Globally Finite    | Each element has only finitely many successors.                                 |
| Acyclic            | If there is no element $a$ such that $a \xrightarrow{+} a$.                     |

### Equivalence and reduction

> [!theorem]
> The following conditions are equivalent:
> 1. $\rightarrow$ has the Church-Rosser property.
> 2. $\rightarrow$ is confluent.
> 3. $\rightarrow$ is semi-confluent.

> [!corollary]
> If $\rightarrow$ is confluent and $x \xleftrightarrow{*} y$ then
> 1. $x \xrightarrow{*} y$ if $y$ is in normal form.
> 2. $x = y$ if both $x$ and $y$ are in normal form.

> [!proposition]
> If $\rightarrow$ is confluent, every element has at most one normal form.

> [!theorem]
> $\rightarrow$ is normalizing and confluent iff every element has a unique normal form.

> [!theorem]
> If $\rightarrow$ is normalizing and confluent then $x \xleftrightarrow{*} y \iff x \downarrow = y \downarrow$.

### Branching

> [!lemma]
> A finitely branching relation is global finite iff $\xrightarrow{+}$ is finitely branching.

> [!lemma]
> Any cyclic relation is terminating if it is globally finite.