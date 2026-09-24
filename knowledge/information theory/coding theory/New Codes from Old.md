## Puncturing Codes

> [!definition] Puncturing Codes
> Let $\mathcal C$ be an $[n, k, d]$ code over $\mathbb F_q$. We can **puncture** $\mathcal C$ by deleting the same coordinate $i$ in each codeword. The resulting code is still linear; its length is $n - 1$, and we often denote the punctured code by $\mathcal C^*$.

> [!theorem]
> Let $\mathcal C$ be an $[n, k, d]$ code over $\mathbb F_q$, and let $\mathcal C^*$ be the code $\mathcal C$ punctured on the $i$-th coordinate.
> 1. If $d > 1$, $\mathcal C^*$ is an $[n - 1, k, d^*]$ code where $d^* = d - 1$ if $\mathcal C$ has a minimum weight codeword with a nonzero $i$-th coordinate and $d^* = d$ otherwise.
> 2. When $d = 1$, $\mathcal C^*$ is an $[n - 1, k, 1]$ code if $\mathcal C$ has no codeword of weight $1$ whose nonzero entry is in coordinate $i$; otherwise, if $k > 1$, $\mathcal C^*$ is an $[n - 1, k - 1, d^*]$ code with $d^* \geq 1$.

## Extending Codes

> [!remark]
> We can also create new codes by adding a new coordinate.

> [!definition] Extended Code
> If $\mathcal C$ is an $[n, k, d]$ code over $\mathbb F_q$, define the **extended** code $\widehat{\mathcal C}$ to be the code
> $$\widehat{\mathcal C} = \{x_1 x_2 \dots x_{n + 1} \in \mathbb F_q^{n + 1} \; | \; x_1 x_2 \dots x_n \in \mathcal C \; \text{with} \; x_1 + x_2 + \dots + x_{n + 1} = 0\}$$

## Shortening Codes

> [!definition] Shortening Codes
> Let $\mathcal C$ be an $[n, k, d]$ code over $\mathbb F_q$ and let $T$ be any set of $t$ coordinates. Consider the set $\mathcal C(T)$ of codewords which are $0$ on $T$; this set is a subcode of $\mathcal C$. Puncturing $\mathcal C(T)$ on $T$ gives a code over $\mathbb F_q$ of length $n - t$ called the code **shortened** on $T$ and denoted $\mathcal C_T$.

> [!theorem]
> Let $\mathcal C$ be an $[n, k, d]$ code over $\mathbb F_q$. Let $T$ be a set of $t$ coordinates and define the shortened code $\mathcal C_T$ and punctured code $\mathcal C^T$. Then:
> 1. $(\mathcal C^\perp)_T = (\mathcal C^T)^\perp$ and $(\mathcal C^\perp)^T = (\mathcal C_T)^\perp$, and
> 2. If $t < d$, then $\mathcal C^T$ and $(\mathcal C^\perp)_T$ have dimensions $k$ and $n - t - k$, respectively;
> 3. If $t = d$ and $T$ is the set of coordinates where a minimum weight codeword is nonzero, then $\mathcal C^T$ and $(\mathcal C^\perp)_T$ have dimensions $k - 1$ and $n - d - k + 1$, respectively.

## Direct Sums

> [!definition] Direct Sums
> For $i \in \{1, 2\}$ let $\mathcal C_i$ be an $[n_i, k_i, d_i]$ code, both over the same finite field $\mathbb F_q$. Then their **direct sum** is the $[n_1 + n_2, k_1 + k_2, \min\{d_1, d_2\}]$ code 
> $$\mathcal C_1 \oplus \mathcal C_2 = \{(c_1, c_2) \; | \; c_1 \in \mathcal C_1, c_2 \in \mathcal C_2\}$$

> [!proposition] Generator Matrix of Direct Sums
> If $\mathcal C_i$ has generator matrix $G_i$ and parity check matrix $H_i$, then
> $$G_1 \oplus G_2 = \begin{bmatrix}G_1 & O \\ O & G_2\end{bmatrix} \quad \text{and} \quad H_1 \oplus H_2 = \begin{bmatrix}H_1 & O \\ O & H_2\end{bmatrix}$$
> are a generator matrix and parity check matrix for $\mathcal C_1 \oplus \mathcal C_2$.

## The $(u | u + v)$ construction

> [!definition] The $(u | u + v)$ Construction
> Let $\mathcal C_i$ be an $[n_i, k_i, d_i]$ code for $i \in \{1, 2\}$, both over the same finite field $\mathbb F_q$. The $(u | u + v)$ construction produces the $[2n, k_1 + k_2, \min\{2 d_1, d_2\}]$ code
> $$\mathcal C = \{(u, u + v) \; | \; u \in \mathcal C_1, v \in \mathcal C_2\}$$

> [!proposition] Generator Matrix of $(u | u + v)$ Construction
> If $\mathcal C_i$ has generator matrix $G_i$ and parity check matrix $H_i$, then generator and parity check matrices for $\mathcal C$ are 
> $$\begin{bmatrix}G_1 & G_1 \\ O & G_2\end{bmatrix} \quad \text{and} \quad \begin{bmatrix}H_1 & O \\ -H_2 & H_2\end{bmatrix}$$

