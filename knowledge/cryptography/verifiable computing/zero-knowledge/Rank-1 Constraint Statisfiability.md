## Basic Definition

> [!definition] Rank-1 Constraint Satisfiability
> A rank-1 constraint satisfiability (R1CS) system over a finite field $\mathbb F$ is specified by a tuple $\text{CS} = (n, N_g, N_w, \{a_i, b_i, c_i\}_{i \in [N_g]})$ where $n, N_g, N_w \in \mathbb N, n \leq N_w$, and $a_i, b_i, c_i \in \mathbb F^{N_w + 1}$. The system $\text{CS}$ is **satisfiable** for a statement $x \in \mathbb F^n$ if there exists a witness $w \in \mathbb F^{N_w}$ such that
> - $x = (w_1, \dots, w_n)$.
> - $[1 | w^T] a_i \cdot [1 | w^T] b_i = [1 | w^T] c_i$ for all $i \in [N_g]$.
> 
> We denote this by writing $\text{CS}(x, w) = 1$, and refer to $n$ as the statement size, $N_w$ as the number of variables, and $N_g$ as the number of constraints. Given an R1CS system $\text{CS}$, we define the corresponding relation 
> $$\mathcal R_{\text{CS}} = \{(x, w) \in \mathbb F^n \times \mathbb F^{N_w}: \text{CS}(x, w) = 1\}.$$

> [!remark]
> - $n$: Statement size.
> - $N_w$: Length of witness.
> - $N_g$: Number of constraints (gates).

> [!remark] Boolean and Arithmetic Circuit Satisfiability
> The language of R1CS capture Boolean and arithmetic circuit satisfiability as special cases.
> - Boolean circuit satisfiability instance for a Boolean circuit $C: \{0, 1\}^n \times \{0, 1\}^h \rightarrow \{0, 1\}$ with $\alpha$ wires and $\beta$ bilinear gates yields an R1CS instance with $N_w = \alpha$ variables and $N_g = \beta + h + 1$ constraints.
> - An arithmetic circuit $C: \mathbb F^n \times \mathbb F^h \rightarrow \mathbb F^\ell$ with $\alpha$ wires and $\beta$ bilinear gates corresponds to a R1CS instance with $N_w = \alpha$ variables and $N_g = \beta + \ell$ constraints.


