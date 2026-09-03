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
> For all [[daily/Temp/PPT]] algorithms $\mathcal A = (\mathcal A^\text{find})$, we define the collision resistant advantage for function $f$:
> $$\text{Adv}_\text{f}^\text{CR}(\mathcal A) = 
> \; \Pr\!\left[
> \begin{array}{l}
> x \neq x' \\
> f(x) = f(x')
> \end{array}
> \; \middle | \; 
> \begin{array}{l}
> (x, x') = \mathcal A^\text{find}()
> \end{array} \right]$$

### Prefix-Free


### Unpredictability


### Pseudorandom

> [!definition] Pseudorandom Advantage
> For all [[daily/Temp/PPT]] algorithms $\mathcal A = (\mathcal A^\text{find}, \mathcal A^\text{guess})$, we define the pseudorandom advantage for a function families $\mathcal F = \{f_k: \mathcal X \rightarrow \mathcal Y\}$:
> $$\text{Adv}_{\mathcal F}^{Q\text{-Pr}}(\mathcal A) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> k \xleftarrow{\$} \mathcal K; f_k \leftarrow \mathcal F; \\
> (x_1, \dots, x_q) \leftarrow \mathcal A_\text{find}(); \\
> y_1 \leftarrow f_k(y_1), \dots, y_q \leftarrow f_k(y_q); \\
> b \leftarrow \mathcal A^\text{guess}(y_1, \dots, y_q)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> f \leftarrow \text{Func}(\mathcal X, \mathcal Y) \\
> (x_1, \dots, x_q) \leftarrow \mathcal A_\text{find}(); \\
> y_1 \leftarrow f(y_1), \dots, y_q \leftarrow f(y_q); \\
> b \leftarrow \mathcal A^\text{guess}(y_1, \dots, y_q)
> \end{array} \right] 
> \right|.$$

> [!definition] Weakly Pseudorandom Advantage
> For all [[daily/Temp/PPT]] algorithms $\mathcal A = (\mathcal A^\text{guess})$, we define the pseudorandom advantage for a function families $\mathcal F = \{f_k: \mathcal X \rightarrow \mathcal Y\}$:
> $$\text{Adv}_{\mathcal F}^{Q\text{-wPr}}(\mathcal A) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> k \xleftarrow{\$} \mathcal K; f_k \leftarrow \mathcal F; \\
> (x_1, \dots, x_q) \xleftarrow{\$} \mathcal X^q; \\
> y_1 \leftarrow f_k(y_1), \dots, y_q \leftarrow f_k(y_q); \\
> b \leftarrow \mathcal A^\text{guess}(y_1, \dots, y_q)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> f \leftarrow \text{Func}(\mathcal X, \mathcal Y) \\
> (x_1, \dots, x_q) \xleftarrow{\$} \mathcal X^q; \\
> y_1 \leftarrow f(y_1), \dots, y_q \leftarrow f(y_q); \\
> b \leftarrow \mathcal A^\text{guess}(y_1, \dots, y_q)
> \end{array} \right] 
> \right|.$$


