---
dg-publish: true
type: zk-SNARK
---
## Scheme

> [!definition] Parameters
> - [[Quadratic Arithmetic Program]]
> - [[Bilinear Pairings]]

> [!scheme] Groth16
> - $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R})$:
> 	1. $(\tau, \alpha, \beta, \delta, \gamma) \xleftarrow{\$} \mathbb{F}^5$.
> 	2. $\mathrm{td} = (\tau, \alpha, \beta, \delta, \gamma)$.
> 	3. $\mathrm{prk} \leftarrow \begin{pmatrix}[\alpha]_1, [\beta]_1, [\beta]_2, [\delta]_1, [\delta]_2\\([a_j(\tau)]_1, [b_j(\tau)]_1)_{j \in [0, N_v]}, ([b_j(\tau)]_2)_{j \in [0, N_v]} \\ \left( \left[\frac{\beta a_j(\tau) + \alpha b_j(\tau) + c_j(\tau)}{\delta}\right]_1 \right)_{j \in [n + 1, N_v]} \\ \left( \left[\frac{\tau^i t(\tau)}{\delta} \right]_1 \right)_{i \in [0, N_g - 2]}\end{pmatrix}$.
> 	4. $\mathrm{vk} \leftarrow \begin{pmatrix}[\alpha]_1, [\beta]_2, [\delta]_1, [\delta]_2 \\ \left(\left[\frac{\beta a_j(\tau) + \alpha b_j(\tau) + c_j(\tau)}{\gamma}\right]_1\right)_{i \in [0, N_v]}\end{pmatrix}$.
> 	5. Returns $(\mathrm{prk}, \mathrm{vk}, \mathrm{td})$.
> - $\pi \leftarrow \mathsf{Prove}(\mathrm{prk}, \mathbf{x}, \mathbf{w})$:
> 	1. $$



$$$$
