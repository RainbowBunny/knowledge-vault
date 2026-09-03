## Syntax

> [!definition] Multi-Party Computation
> An $n$-party protocol $\Pi = (P_i, x_i, \mathsf{Next}_i, \mathsf{Out}_i)_{i \in [n]}$ is specified by:
> - Parties $P_1, \dots, P_n$, party $P_i$ holding private input $x_i$.
> - A functionality $f(x_1, \dots, x_n) \rightarrow (y_1, \dots, y_n)$ they want to compute.
> - A next-message function. For each party, round $\rho$, the messages it sends are 
> $$\mathsf{Next}_i(x_i, r_i, m_i^{(1)}, \dots, m_i^{(\rho - 1)})$$
> where $r_i$ is $P_i$'s random and $m_i^{(k)}$ is everything it received in round $k$.
> - An output function $\mathsf{Out}_i$ applied at the end.

> [!remark] View of Each Party in MPC
> For each party, the view of party $i$ in round $\rho$ is:
> $$\mathsf{View}_i = (x_i, r_i, m_i^{(1)}, \dots, m_i^{(\rho)})$$
