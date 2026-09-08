## Definition

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.
> - $n = wb$: (Assume that $w \mid n$).

> [!definition] Regular Word
> A word $x$ is regular if $x = (x^{(1)}, \dots, x^{(w)})$ with $x^{(i)} \in \mathbb F_2^b$ and $\mathsf{wt}_\mathsf{H}(x^{(i)}) = 1$.
> Also, the regular word set is defined as
> $$\mathrm{Reg}_w(\mathbb{F}_2) := \{x : \mathsf{wt}(x^{(i)}) = 1\ \forall i \in [n]\}$$

> [!proposition] Regular Word Support Size
> Generalize for $\mathbb{F}_q$, each blocks has $b$ position and $q - 1$ value to choose:
   $$|\mathrm{Reg}_w(\mathbb{F}_q)| = b^w (q - 1)^w$$

### Relation to [[Hamming Sphere]]

> [!remark]
> As $w < n$, the regular code word is a strict subset of the [[Hamming Sphere]].
> $$\mathrm{Reg}_w(\mathbb{F}_q) \subsetneq \mathcal{S}_w^n(\mathbb{F}_q)$$


## Variant

### 2-Regular 

> [!definition] 2-Regular Word
> The condition on weight is replaced by $\mathsf{wt}_\mathsf{H}(x^{(i)}) = 0 \lor \mathsf{wt}_\mathsf{H}(x^{(i)}) = 2$.
> And, define the set of 2-Regular Word as:
> $$\mathrm{Reg}_w^{(2)}(\mathbb{F}_2) = \{x: \mathsf{wt}_\mathsf{H}(x^{(i)}) = 0 \lor \mathsf{wt}_\mathsf{H}(x^{(i)}) = 2\}$$

> [!proposition] 2-Regular Word Support Size
> For each block, there are $1 + \binom{b}{2}$ valid options.
> $$|\mathrm{Reg}_w^{(2)}(\mathbb{F}_2)| = (1 + \binom{b}{2})^w$$

> [!proposition]
> $\mathrm{Reg}_w^{(2)}(\mathbb{F}_2) = \{\mathbf{x}_1 + \mathbf{x}_2 : \mathbf{x}_1, \mathbf{x}_2 \in \mathrm{Reg}_w(\mathbb{F}_2)\}$ — the 2-regular words are **exactly** the sums of two regular words. Per block: two $1$s in the same position cancel, in different positions give weight $2$; and every such pattern is reachable.

