## Parameters

> [!definition] Parameters
> 
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Solution distribution, usually interval $[-B, \dots, B]$.

## Problem

### Search Variant

> [!definition] Normal-Form Search Short Integer Solution Problem Advantage
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}_{\text{nf-SSIS}}^\text{search}(\mathcal A_\text{search}) = 
> \Pr\!\left[ 
> \begin{array}{l}
> As = 0
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> A' \xleftarrow{\$} \mathbb Z_q^{m \times (n - m)} \\
> A \leftarrow [A'][I] \\
> s \leftarrow \mathcal A_\text{search}(A)
> \end{array} \right]$$

> [!lemma]
> Normal-form SIS is as hard as [[Short Integer Solution#Search Variant|SIS]].

