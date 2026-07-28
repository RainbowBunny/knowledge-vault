## Parameters

> [!definition] Parameters
> - $n$: Length of the code.
> - $w$: Weight of the codeword.
> - $s$: Index of the code (how coarse is the ring structure)
> - $\mathbb F$: Field
> - $\omega$: Norm over $\mathcal R$
> - $\mathcal C$: [[Code Properties#Systematic|systematic]] [[Code Properties#Cyclic and Quasi-Cyclic|Quasi-Cyclic]] code

## Distribution

> [!definition] Quasi-Cyclic Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $s\text{-QCSD}(n, w)$
> 1. $H \xleftarrow{\$} \mathbb F^{(sn - n) \times sn}$: Parity check matrix of $\mathcal C$.
> 2. $x = (x_1, \dots, x_s) \xleftarrow{\$} \mathbb F^{sn}$ with $\omega(x_i) = w$ for $i = 1, \dots, s$.
> 3. Outputs $(H, Hx^T)$.

## Problem

### Search Variant

> [!definition] Search Syndrome Decoding Problem Advantage
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}^\text{search}_\text{SD}(\mathcal A_\text{search}) = \Pr\!\left[ 
> \begin{array}{l}
> \omega(x_i) = w \\
> y^T = Hx^T
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} s\text{-QCSD}(n, w) \\
> x = (x_1, \dots, x_s) \leftarrow \mathcal A_\text{search}(H, y^T)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Parity-Restricted Uniform Distribution
> For a bit $b$, let $\mathbb F_{2, b}^{\,sn - n} = \{\, y \in \mathbb F_2^{\,sn-n} : \textstyle\sum_i y_i = b \,\}$ denote the vectors of parity $b$, and let $\mathcal U_b$ sample $H$ as in $s\text{-QCSD}(n, w)$ and $y \xleftarrow{\$} \mathbb F_{2,b}^{\,sn-n}$, outputting $(H, y^\top)$.
> **Note:** $H$ is sampled identically in both worlds — only $y$ differs. The planted syndrome's parity is *publicly computable* from $(H, w)$ (over $\mathbb F_2$, each block of $y = xH^\top$ has parity determined by $w$ and the row-sums of $H$'s circulant blocks), and $b$ is set to exactly that value.

> [!definition] Decision s-QCSD Advantage
> For any adversary $\mathcal A_{\text{decide}}$, we define the following advantage:
> $$\mathrm{Adv}^{\text{decide}}_{s\text{-QCSD}}(\mathcal A) =
> \left|\;
> \Pr\!\left[\, b' = 1 \;\middle|\;
> \begin{array}{l}
> (H, y^\top) \xleftarrow{\$} s\text{-QCSD}(n, w) \\
> b' \leftarrow \mathcal A_{\text{decide}}(H, y^\top)
> \end{array}
> \right]
> \;-\;
> \Pr\!\left[\, b' = 1 \;\middle|\;
> \begin{array}{l}
> (H, y^\top) \xleftarrow{\$} \mathcal U_b \\
> b' \leftarrow \mathcal A_{\text{decide}}(H, y^\top)
> \end{array}
> \right]
> \;\right|$$

> [!remark] Why the parity restriction is mandatory
> Against the *unrestricted* uniform distribution over $\mathbb F_2^{\,sn-n}$, the assumption is trivially false: the planted world's parity is a deterministic, public function of $(H, w)$, while a uniform $y$ has a uniform parity bit. The distinguisher "output 1 iff $\sum_i y_i = b$" achieves advantage exactly $\tfrac12$ in constant time. We repairs this by quotienting out the one leaked bit — the ideal world is uniform *conditioned on the correct parity*, which is the largest ideal world the planted distribution can plausibly be confused with. (Same repair pattern as the statistical-ceiling discussion: locate the efficiently computable statistic that separates the worlds, and restrict the ideal world to match it.)
