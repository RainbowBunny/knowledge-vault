## Definition

### Non-Interactive Proof Systems Variant

> [!definition] Succinct
> There exists a polynomial $p$, independent of $\mathcal{R}$, indexed by a relation description $i$, and every statement-witness pair $(\mathbf{x}, \mathbf{w}) \in \mathcal R$:
> - $\mathsf{Verify}$ runs in time $p(\lambda + |\mathbf{x}| + \log|i|)$.
> - Proof size $|\pi| \leq p(\lambda + \log|i|)$.
> 
> Also, $\mathsf{Prove}$ should be a [[daily/Temp/PPT]] bounded by $\mathrm{poly}(\lambda + |i| + |\mathbf{w}|)$.

> [!definition] Preprocessing Succint
> Also, $\mathsf{Setup}$ runs in $\mathrm{poly}(\lambda + |i|)$.

> [!definition] Fully Succinct
> The $\mathsf{Setup}$ now is bounded by $p(\lambda + \log |i|)$.
