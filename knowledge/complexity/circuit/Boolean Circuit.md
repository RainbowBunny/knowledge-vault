Reference:
- https://eprint.iacr.org/2014/718.pdf

## Definition

> [!definition] Boolean Circuit
> A **Boolean circuit** is a collection of **gates** and **inputs** connected by **wires**. Cycles aren't permitted. Gates take three forms: AND gates, OR gates, and NOT gates.

### Circuit Family

> [!definition] Circuit Family
> A **circuit family** $C$ is an infinite list of circuits, $(C_0, C_1, C_2, \cdots)$, where $C_n$ has $n$ input variables. We say that $C$ decides a language $A$ over $\{0, 1\}$ if for every string $w$, $$w \in A \iff C_n(w) = 1,$$
> where $n$ is the length of $w$.

### Circuit Size

> [!definition] Size of a Circuit
> The **size** of a circuit is the number of gates it contains.

### Circuit Depth

> [!definition] Depth of a Circuit
> The **depth** of a circuit is the length (number of wires) of the longest path from an input variable to the output gate.

### Minimal Circuit

> [!definition] Minimal Circuit
> A circuit is **size (depth) minimal** if no smaller circuit is equivalent to it.

### Circuit Complexity

> [!definition] Complexity of a Circuit Family
> The **size (depth) complexity** of a circuit family $(C_0, C_1, C_2, \cdots)$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the size of $C_n$.

> [!definition] Circuit Complexity
> The **circuit complexity** of a language is the size complexity of a minimal circuit family for that language. The **circuit depth complexity** is defined similarly, using depth instead of size.

## Property

### Linearization of Gate

| Gate                                  | Expression                                     | Range      |
| ------------------------------------- | ---------------------------------------------- | ---------- |
| $\overline{c} = \text{NOT}(c)$        | $1 - c$                                        | $\{0, 1\}$ |
| $c = \text{AND}(a, b)$                | $a + b - 2c$                                   | $\{0, 1\}$ |
| $c = \text{OR}(a, b)$                 | $\overline{a} + \overline{b} - 2 \overline{c}$ | $\{0, 1\}$ |
| $c = \text{XOR}(a, b)$                | $a + b + c$                                    | $\{0, 2\}$ |
| $c = \text{NAND}(a, b)$               | $a + b - 2 \overline{c}$                       | $\{0, 1\}$ |
| $c = \text{NOR}(a, b)$                | $\overline{a} + \overline{b} - 2c$             | $\{0, 1\}$ |
| $c = \text{XNOR}(a, b)$               | $a + b + \overline{c}$                         | $\{0, 2\}$ |
| $c = \overline{a} \land b$            | $\overline{a} + b - 2c$                        | $\{0, 1\}$ |
| $c = \overline{\overline{a} \land b}$ | $\overline{a} + b - 2 \overline{c}$            | $\{0, 1\}$ |
| $c = a \land \overline{b}$            | $a + \overline{b} - 2c$                        | $\{0, 1\}$ |
| $c = \overline{a \land \overline{b}}$ | $a + \overline{b} - 2 \overline{c}$            | $\{0, 1\}$ |
> [!theorem]
> For any circuit $C$ with $m$ wires and $n$ fan-in 2 gates for a total size of $d = m + n$, there exists a matrix $V \in \mathbb Z^{m \times d}$ and a vector $b \in \mathbb Z^d$ such that $C$ is satisfiable if and only if there is a vector $a \in \mathbb Z^m$ satisfying $aV + b \in \{0, 2\}^d$.
> 
> The matrix $V$ and the vector $b$ can be constructed such that $aV + b \in \{0, 2\}^d$ implies $a \in \{0, 1\}^m$ and $a_1, \dots, a_m$ corresponds to the values on the wires in a satisfying assignment for $C$ with the first $\ell$ bits being the input wires.

> [!proof]
> If $x \in \{0, 1\}$ then $2x \in \{0, 2\}$.
> Thus, we can choose:
> $$V = \begin{bmatrix}2I \;|\; G\end{bmatrix}, b = \begin{pmatrix}0 | \delta\end{pmatrix}$$

> [!corollary]
> For any circuit $C$ with $m$ wires and $n$ fan-in 2 gates and for any $p \geq 8$ there exist a matrix $V \in \mathbb Z_p^{m \times d}$ (with $d = m + n$) and a vector $b \in \mathbb Z_p^d$ (giving us $m + 1$ linearly independent row vectors) such that $C$ is satisfiable if and only if there exists a vector $a \in \mathbb Z_p^m$ satisfying $aV + b \in \{0, 2\}^d$. Furthermore, if $a V + b \in \{0, 2\}^d$ then $a \in \{0, 1\}^m$ and $C(a_1, \dots, a_\ell) = 1$.


