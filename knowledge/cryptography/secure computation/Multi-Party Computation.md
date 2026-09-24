Reference:
- https://eprint.iacr.org/2016/163.pdf

## Syntax

> [!definition] Parameters
> - $n$: Number of parties.
> - $P_1, \dots, P_n$: The $n$ parties, with each party $P_i$ holds:
> 	- $x_i$: Its private input share.
> 	- $r_i$: Its private random.
> - The parties can communicate through point-to-point secure channel $\mathsf{CH}_{i, j}$ (encrypted channels, OT-channel) in the synchronous model or a boardcast channel.
> - $(y_1, \dots, y_n) \leftarrow f(x_1, \dots, x_n)$: The common function.

> [!definition] Multi-Party Computation
> An $n$-party protocol $\Pi_\mathsf{MPC} = (\mathsf{Next}_i, \mathsf{Out}_i)_{i \in [n]}$ is specified by:
> - A next-message function. For each party, round $\rho$, the messages it sends are 
> $$\mathsf{Next}_i(x_i, r_i, m_i^{(1)}, \dots, m_i^{(\rho - 1)})$$
> where $r_i$ is $P_i$'s random and $m_i^{(k)}$ is everything it received in round $k$.
> - An output function $\mathsf{Out}_i$ applied at the end to $\mathsf{View}_i$.

> [!remark] View of Each Party in MPC
> For each party, the view of party $i$ in round $\rho$ is:
> $$\mathsf{View}_i = (x_i, r_i, m_i^{(1)}, \dots, m_i^{(\rho)})$$

## Property

### Consistency

> [!definition] Consistency
> Each channel $\mathsf{CH}_{i, j}$ defines a relation of **consistency** between views by a function $\varphi$. We say that two views are consistent if the view of the sender implies an input $\mathbf{x}$ to the channel and the view of the receiver implies an input $\mathbf{y}$ and contains an output $\mathbf{z}$ such that $\mathbf{z} = \varphi(\mathbf{x}, \mathbf{y})$.



