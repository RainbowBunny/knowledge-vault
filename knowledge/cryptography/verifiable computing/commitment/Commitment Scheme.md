---
dg-publish: true
---
Reference:
- https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf
- https://eprint.iacr.org/2025/2099

## Intuition

> [!example] Coin Flipping by Telephone
> Suppose Alice and Bob are getting a divorce but they can not even stand facing each other, so they have to discuss over the phone how to split the furniture, the kids, etc. Since they can not agree who get which, they decide to flip a coin. To make the game fair, we can use a simple protocol:
> 1. Alice commits to a random bit $b_A$, and sends the resulting commitment $C$ to Bob.
> 2. Bob chooses a random bit $b_B$ and sends it to Alice.
> 3. Alice opens $C$ to let Bob learn $b_A$, and both parties compute the result, which is $b = b_A \oplus b_B$.

## Syntax

> [!definition] Commitment Scheme
> A **commitment scheme** for a finite message space $\mathcal M$, is a tuple of [[PPT]] $\mathcal{CS} = (\mathsf{KeyGen}, \mathsf{Com}, \mathsf{Verify})$ where:
> - $pp \leftarrow \mathsf{Setup}(1^\lambda)$: On input the security parameter $\lambda$, outputs the public parameter $\mathrm{pp}$.
> - $(c, o) \leftarrow \mathsf{Com}(\mathrm{pp}, m)$: Commitment algorithm, with public parameter $\mathrm{pp}$ and message $m$, returns commitment $c$ and opening string $o$.
> - $\{0, 1\} \leftarrow \mathsf{Verify}(\mathrm{pp}, m, c, o)$: Verification algorithm, outputs $1$ for $\mathsf{accept}$ or $0$ for $\mathsf{reject}$.

> [!definition] Commitment Phases
> - Commit Phase: Sender runs $(c, o) \xleftarrow{\$} \mathsf{Com}(\mathrm{pp}, m)$ and sends $c$.
> - Reveal Phase: Sender sends $(m, o)$; receiver runs $\mathsf{Verify}(\mathrm{pp}, m, c, o)$.

## Property

### Correctness

> [!definition] Correctness
> For all $m \in \mathcal M$:
> $$\Pr\!\left[
> \begin{array}{l}
> \text{Verify}(m, c, o) = \text{accept}
> \end{array}
> \; \middle | \; 
> \begin{array}{l}
> (c, o) \leftarrow \text{Com}(m)
> \end{array} \right] = 1$$

## Security

### Binding

> [!definition] Binding
> For any [[Adversary]] $\mathcal{A} = (\mathcal{A}^\mathsf{find})$, we define the binding advantage:
> $$\mathsf{Adv}_{\mathcal{CS}}^\mathsf{Bind}(\mathcal{A}) =  
> \; \Pr\!\left[
> \begin{array}{l}
> m_1 \neq m_2 \\
> \mathsf{Verify}(\mathrm{pp}, m_1, c, o_1) = 1 \\
> \mathsf{Verify}(\mathrm{pp}, m_2, c, o_2) = 1
> \end{array}
> \; \middle | \; 
> \begin{array}{l}
> \mathrm{pp} \leftarrow \mathsf{Setup}(1^\lambda) \\
> (c, m_1, m_2, o_1, o_2) \leftarrow \mathcal{A}^\mathsf{find}(\mathrm{pp})
> \end{array} \right]$$

### Hiding

> [!definition] Hiding
> For any [[Adversary]] $\mathcal{A} = (\mathcal{A}_\mathsf{find}, \mathcal{A}_\mathsf{guess})$, we define the hiding advantage:
> $$\mathsf{Adv}_\mathcal{CS}^{\mathsf{Hide}}(\mathcal{A}) = 
> \left|\; \Pr\!\left[ b = b' \;\middle |\; 
> \begin{array}{l}
> \mathrm{pp} \leftarrow \mathsf{Setup}(1^\lambda) \\
> (m_0, m_1) \leftarrow \mathcal{A}_\mathsf{find}(\mathrm{pp}) \\
> b \xleftarrow{\$} \{0, 1\} \\
> (c_b, o_b) \leftarrow \mathsf{Com}(\mathrm{pp}, m_b) \\
> b' \leftarrow \mathcal{A}_\mathsf{guess}(c_b)
> \end{array} \right] 
> \;- \frac{1}{2}
> \right|.$$

