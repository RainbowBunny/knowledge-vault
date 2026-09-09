Reference:
- [[Book Reference|Term Rewriting and All That]]: - Chapter 2: Abstract Reduction Systems.

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
> 6. $x$ and $y$ are **joinable** iff there is a $z$ in normal form such that $x \xrightarrow{*} z \xleftarrow{*} y$, in which case we write $x \downarrow y$.

## Property

| Name          | Property                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| Church-Rosser | $x \xleftrightarrow{*} y \implies x \downarrow y$,                              |
| Confluent     | $y_1 \xleftarrow{*} x \xrightarrow{*} y_2 \implies y_1 \downarrow y_2$.         |
| Terminating   | There is no infinite descending chain $a_0 \rightarrow a_1 \rightarrow \cdots$. |
| Normalizing   | Every element has a normal form.                                                |
| Convergent    | It is both confluent and terminating.                                           |