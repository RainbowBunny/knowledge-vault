## Definition

### Multi-Party Computation Variant

> [!definition] Correctness
> Given a [[Multi-Party Computation]] $\Pi_\mathsf{MPC}$. For any adversary $\mathcal{A} = (\mathcal{A}_\mathsf{find})$, we define the correctness advantage
> $$\mathsf{Adv}_{\Pi_\mathsf{MPC}}^\mathrm{cor}(\mathcal{A}) = \max_{i \in [n]}
> \Pr\!\left[
> \begin{array}{l}
> f(x_1, \dots, x_n)^{(i)} = \mathsf{Out}_i(\mathsf{View}_i)
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (x_1, \dots, x_n) \leftarrow \mathcal{A}_\mathsf{find}() \\
> (r_1, \dots, r_n) \leftarrow \mathcal{U}(\mathcal{R}) \\
> \end{array} \right] 
> $$