

## Property


## Security

### Knowledge

> [!definition] Knowledge
> There exists an efficient extractor $\mathcal E$, making at most $q_{\mathcal E}$ queries to its oracle, such that for all $x \in \mathbb F^n$ and every $\pi^* \in \mathbb F^\ell$:
> $$\Pr[\text{Verify}(st, x, Q^T \pi^*) \; | \; (st, Q) \leftarrow \text{Query}()] > \epsilon$$
> then
> $$\Pr[\text{CS}(x, w) = 1 \; | \; w \leftarrow \mathcal E^{\langle \pi^*, \cdot \rangle}(x)] = 1$$


### Perfect Honest-Verifier Zero Knowledge

> [!definition] Perfect Honest-Verifier Zero Knowledge
> There exists an efficient simulator $\mathcal S_\text{LPCP} = (\mathcal S_1, \mathcal S_2)$ such that for all instances $(x, w)$ where $\text{CS}(x, w) = 1$,
> $$\{(st, Q, Q^T \pi)\} \equiv \{(\tilde{st}, \tilde Q, \tilde a)\},$$
> where $(st, Q) \leftarrow \text{Query}_\text{LPCP}, \pi \leftarrow \text{Prove}_\text{LPCP}(x, w), (\tilde{st}, \tilde{Q}, st_{\mathcal S}) \leftarrow \mathcal S_1()$ and $\tilde a \leftarrow \mathcal S_2(st_{\mathcal S}, x)$.
