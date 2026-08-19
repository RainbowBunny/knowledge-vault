## Scheme

> [!scheme] QAP for R1CS
> ### Algorithm
> Given a [[Rank-1 Constraint Statisfiability|R1CS]] $\mathcal{CS} = (n, N_g, N_w, \{\mathbf{a}_i, \mathbf{b}_i, \mathbf{c}_i\}_{i \in [N_g]})$, returns a corresponding [[Quadratic Arithmetic Program]] over the same finite field $\mathbb F$.
> 1. Generates $S = \{\alpha_1, \dots, \alpha_{N_g}\} \subset \mathbb F$ (Public interpolation point).
> 2. Generates $A_i(x)$ is the [[Lagrange Interpolation]] of $\{(\alpha_j, \mathbf{a}_{j, i})\}_{i \in [N_g]}$.
> 3. Generates $B_i(x)$ is the [[Lagrange Interpolation]] of $\{(\alpha_j, \mathbf{b}_{j, i})\}_{i \in [N_g]}$.
> 4. Generates $C_i(x)$ is the [[Lagrange Interpolation]] of $\{(\alpha_j, \mathbf{c}_{j, i})\}_{i \in [N_g]}$.
> 5. Generates $Z_S(x)$ is the [[Vanishing Polynomial]] on $S$.
> 6. Returns $(\mathbf{A} = \{A_i(x)\}_{i \in [N_g]}, \mathbf{B} = \{B_i(x)\}_{i \in [N_g]}, \mathbf{C(x)} = \{C_i\}_{i \in [N_g]}, Z_S(x))$.
