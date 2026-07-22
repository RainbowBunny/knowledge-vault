## Syntax

> [!definition] Linear Probabilistically Checkable Proof
> Let $\mathbb F$ be a finite field and let $\text{CS} = (n, N_g, N_w, \{a_i, b_i, c_i\}_{i \in [N_g]})$ be a single [[Rank-1 Constraint Statisfiability#Basic Definition|R1CS]] system over $\mathbb F$.
> A $k$-query input-independent linear linear PCP for $\text{CS}$ with query length $\ell \in \mathbb N$ is a tuple $\Pi = (\text{Query}, \text{Prove}, \text{Verify})$
> - $(st, Q) \leftarrow \text{Query}()$: A probabilistic algorithm that, using only its own randomness (in particular, without seeing $x$), outputs a query matrix $Q \in \mathbb F^{\ell \times k}$ and a verification state $st$.
> - $\pi \leftarrow \text{Prove}(x, w)$: On a statement $x \in \mathbb F^n$ and witness $w \in \mathbb F^{N_w}$, outputs a proof vector $\pi \in \mathbb F^\ell$.
> - $b \leftarrow \text{Verify}(st, x, a)$: On the state, the statement, and a response vector $a \in \mathbb F^k$, outputs a bit $b \in \{0, 1\}$.

## Property

### Completeness

> [!definition] Completeness
> For every $x \in \mathbb F^n$ and $w \in \mathbb F^{N_w}$ with $\text{CS}(x, w) = 1$:
>  $$
> \Pr\!\left[ \text{Verify}(st, x, Q^T \pi) = 1 \;\middle |\; 
> \begin{array}{l}
> (st, Q) \leftarrow \text{Query}() \\
> \pi \leftarrow \text{Prove}(x, w)
> \end{array} \right] = 1$$

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
