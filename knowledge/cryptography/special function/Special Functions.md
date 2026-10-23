Reference:
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, v0.6: https://toc.cryptobook.us/ (Attack Games 4.2 and 8.1, Definitions 4.2, 4.3 and 8.1, Eq. 4.22).

## Definition

> [!definition] Functions Family
> A collection of function families is denoted as $\mathbb F = \{\mathcal F\}_\lambda$, where each $\mathcal F$ is a function family $\mathcal F = \{f : \{0, 1\}^{q(\lambda)} \rightarrow \{0, 1\}^{\ell(\lambda)}\}$.

## Property

### Efficient

> [!definition] Efficient
> - The function $q(\lambda)$ and $\ell(\lambda)$ are polynomially-bounded.
> - Given $\lambda$ and $x \in \{0, 1\}^{q(\lambda)}$ the value $f(x)$ can be computed in $\text{poly}(\lambda)$ time. 
> - The sampling of $f$ from its $\mathcal F$ should be efficient.

### Compressing

> [!definition] Compressing
> For all $\lambda$, we have that $q(\lambda) > \ell(\lambda)$.

### Extendable

> [!definition] Extendable
> A function family $\mathcal F: \{f: \mathcal \{0, 1\}^* \rightarrow \mathcal Y\}$ is extendable if
> $$f(x) = f(y) \rightarrow f(x || a) = f(y || a)$$

## Security

### Collision Resistant

> [!definition] Collision Resistant Advantage
> A search game: one branch, and the challenger checks the output in the last row. `[BS Attack Game 8.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | | $\xleftarrow{\ x,\, x'\ }$ | takes no input; outputs two inputs $x, x'$ |
> | 2 | checks whether $x \neq x'$<br>checks whether $f(x) = f(x')$ | | |
>
> **Goal** — $\mathcal A$ wins iff both hold:
> - $x \neq x'$;
> - $f(x) = f(x')$.
>
> $$\text{Adv}_\text{f}^\text{CR}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> $f$ is **collision resistant** if $\text{Adv}_\text{f}^\text{CR}(\mathcal A)$ is negligible for all [[PPT]] algorithms $\mathcal A$ `[BS Def 8.1]`.

> [!remark] The source's form
> `[BS Attack Game 8.1]` writes $\mathsf{CRadv}[\mathcal A, H]$ for a hash function $H$ over $(\mathcal M, \mathcal T)$ and calls $\mathcal A$ a *collision finder*.


### Prefix-Free


### Unpredictability


### Pseudorandom

> [!definition] Pseudorandom Advantage
> A distinguishing game: **Game 0** (the family) and **Game 1** (a random function) differ in row 1 only. `[BS Attack Game 4.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$<br>**Game 0**: $f \leftarrow f_k$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X, \mathcal Y]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Evaluation queries** (repeated, adaptive, at most $Q$ times): sends $x_i \in \mathcal X$ |
> | | $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}_{\mathcal F}^{Q\text{-Pr}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> $\mathcal F$ is **pseudorandom** (a secure PRF) if this is negligible for all [[PPT]] algorithms $\mathcal A$ `[BS Def 4.2]`.

> [!definition] Weakly Pseudorandom Advantage
> The same distinguishing game, except that $\mathcal A$ does not choose the inputs: each query returns the value at a fresh uniform point, together with the point. `[BS Def 4.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$<br>**Game 0**: $f \leftarrow f_k$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X, \mathcal Y]$ | | |
> | 2 | | $\xleftarrow{\ \mathsf{sample}\ }$ | **Sample queries** (repeated, at most $Q$ times): asks for a sample |
> | | $x_i \xleftarrow{\$} \mathcal X$<br>$y_i \leftarrow f(x_i)$ | $\xrightarrow{\ x_i,\, y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}_{\mathcal F}^{Q\text{-wPr}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> $\mathcal F$ is **weakly pseudorandom** (a weakly secure PRF) if this is negligible for all [[PPT]] algorithms $\mathcal A$ `[BS Def 4.3]`.

> [!remark] The source's form
> - `[BS]` writes the two advantages $\mathsf{PRFadv}[\mathcal A, F]$ (Attack Game 4.2) and $\mathsf{wPRFadv}[\mathcal A, F]$ (Section 4.4.1), with $F$ defined over $(\mathcal K, \mathcal X, \mathcal Y)$. Its bit-guessing form $\mathsf{PRFadv}^*[\mathcal A, F] = |\Pr[\hat b = b] - 1/2|$ satisfies $\mathsf{PRFadv} = 2 \cdot \mathsf{PRFadv}^*$ (Eq. 4.22); this note uses the difference.
> - The queries of Attack Game 4.2 are adaptive: each $x_i$ may depend on the earlier answers. In the weak game the adversary sees the random points $x_i$ as well as the values $f(x_i)$.
