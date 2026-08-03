## Parameters

> [!definition] Parameters
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Error distribution, usually interval $[-B, \dots, B]$.

## Distribution

> [!definition] Short-Secret Learning With Error
> ### Distribution
> Sampling Experiment: $\text{ss-LWE}(n, m, q, \chi)$
> 1. $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$
> 2. $s \leftarrow \chi^n$
> 3. $e \leftarrow \chi^m$
> 4. Output $(A, b = As + e)$

> [!definition] Short-Secret Learning With Error (ss-LWE) Problem
> Let $s \in [-B, B]^n$ and $e \in [-B, B]^m$ where . Given $A \in \mathbb Z_q^{m \times n}$ and $b = As + e \pmod q$. Find $s$.
> Denote an instance of this problem by $(A, b)$ for $\text{ss-LWE}(m, n, q, B)$.

> [!remark]
> - We should choose $B \ll q/2$.
> - We don't need $m \gg n$ for unique solutions.

## Problem

### Search Variant

> [!definition] Search Short Secret Learning With Error Problem Advantage
> Reference Name: $\text{Sss-LWE}(n, m, q, \chi)$
> 
> ---
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}_\text{ss-LWE}^\text{search}(\mathcal A_\text{search}) = 
> \Pr\!\left[ 
> \begin{array}{l}
> s \in \chi^n \\
> As - b \in \chi^m
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \xleftarrow{\$} \text{ss-LWE}(n, m, q, \chi) \\
> s \leftarrow \mathcal A_\text{search}(A, b)
> \end{array} \right] 
> $$

> [!proposition]
> ss-LWE and LWE are equivalent.
> - $\text{Sss-LWE}(n, m, q, \chi) \leq \text{SLWE}(n, m, q, \chi)$ 
> - $\text{SLWE}(n, m, q, \chi) \leq \text{Sss-LWE}(n - m, m, q, \chi)$.

### Decision Variant

> [!definition] Decision Short Secret Learning With Error Problem Advantage
> Reference Name: $\text{Dss-LWE}(n, m, q, \chi)$
> 
> ---
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{ss-LWE}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \xleftarrow{\$} \text{ss-LWE}(n, m, q, \chi) \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \xleftarrow{\$} \mathbb Z_q^{n \times m} \times \mathbb Z_q^n \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \right|.
> $$
