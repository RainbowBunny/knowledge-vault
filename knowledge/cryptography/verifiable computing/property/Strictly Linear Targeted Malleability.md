---
aliases: [SLTM, Linear Targeted Malleability, LTM]
---
Reference:
- `[BISW17]` — D. Boneh, Y. Ishai, A. Sahai, D. J. Wu, _Lattice-Based SNARGs and Their Application to More Efficient Obfuscation_, EUROCRYPT 2017; ePrint 2017/240: https://eprint.iacr.org/2017/240.pdf
- `[LUNA]` — R. Steinfeld, A. Sakzad, M. F. Esgin, V. Kuchta, M. Yassi, R. K. Zhao, _LUNA: Quasi-Optimally Succinct Designated-Verifier Zero-Knowledge Arguments from Lattices_, ACM CCS 2024; ePrint 2022/1690: https://eprint.iacr.org/2022/1690.pdf
- `[ISW21]` — Y. Ishai, H. Su, D. J. Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, ACM CCS 2021; full version ePrint 2021/977: https://eprint.iacr.org/2021/977.pdf
- `[BSW12]` — D. Boneh, G. Segev, B. Waters, _Targeted Malleability: Homomorphic Encryption for Restricted Computations_, ITCS 2012; ePrint 2011/311: https://eprint.iacr.org/2011/311.pdf — the origin of targeted malleability, cited by `[BISW17]`; not read here.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Vector Encryption]]: Import $(\lambda, \ell, \mathrm{sk})$ and $(\mathsf{Setup}, \mathsf{Enc}, \mathsf{Dec})$. `[BISW17 Def 4.1]` works over $\mathbb Z_p^\ell$, with no public parameters and no $\mathsf{Add}$.
> - $\mathcal M$: a plaintext generation algorithm; on input $1^\ell$ it outputs $(s, \mathbf v_1, \dots, \mathbf v_m)$ with $\mathbf v_i \in \mathbb Z_p^\ell$ and some extra output $s$.
> - $z \in \{0, 1\}^{\mathrm{poly}(\lambda)}$: an auxiliary input.
> - $\mathcal S$: the simulator, possibly computationally unbounded; it outputs an affine map $(\boldsymbol\pi, \mathbf b)$ with $\boldsymbol\pi \in \mathbb Z_p^m$, $\mathbf b \in \mathbb Z_p^\ell$.
> - $D$: an efficient distinguisher.
>
> `[BISW17 Def 4.2]`

> [!definition] Linear Targeted Malleability
> ### Scope
> A secret-key [[Vector Encryption]] $\Pi_\mathsf{venc}$, an efficient adversary $\mathcal A$, a plaintext generator $\mathcal M$, a simulator $\mathcal S$ and an auxiliary input $z$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives the ciphertexts and holds $z$; no $\mathrm{sk}$, no oracle. $\mathcal S$ receives only $z$: no ciphertexts, no key, no plaintexts.
> - **Promise** — $\mathcal A$ outputs a valid ciphertext: $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}') \neq \perp$.
> - **Quantifier** — $\forall \mathcal A, \mathcal M\ \exists \mathcal S\ \forall z$: the simulator may depend on both $\mathcal A$ and $\mathcal M$.
> - **Adaptivity** — none: $\mathcal A$ speaks once.
>
> ---
> ### Experiment
> A simulation-based comparison: **Game 0** is the real distribution, **Game 1** the ideal one; in Game 1 the adversary is not run. `[BISW17 Def 4.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(s, \mathbf v_1, \dots, \mathbf v_m) \leftarrow \mathcal M(1^\ell)$ | | |
> | 2 | **Game 0**: $\mathrm{sk} \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$<br>$\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ for $i \in [m]$ | $\xrightarrow{\ \mathrm{ct}_1, \dots, \mathrm{ct}_m\ }$ (Game 0) | |
> | 3 | | $\xleftarrow{\ \mathrm{ct}'\ }$ (Game 0) | outputs a ciphertext $\mathrm{ct}'$ |
> | 4 | **Game 0**: $\mathbf v' \leftarrow \mathsf{Dec}(\mathrm{sk}, \mathrm{ct}')$<br>**Game 1**: $(\boldsymbol\pi, \mathbf b) \leftarrow \mathcal S(z)$<br>**Game 1**: $\mathbf v' \leftarrow [\mathbf v_1 \mid \cdots \mid \mathbf v_m] \cdot \boldsymbol\pi + \mathbf b$ | | |
>
> **Goal**
> - **Output** — the tuple $T_b = \big(\{\mathbf v_i\}_{i \in [m]},\ s,\ \mathbf v'\big)$ in Game $b$.
> - **Measure** — whether an efficient distinguisher $D$ can tell $T_0$ from $T_1$.
>
> ---
> ### Property
> $$\mathsf{Adv}^\mathsf{ltm}(D) = \big|\Pr[D(T_0) = 1] - \Pr[D(T_1) = 1]\big|.$$
> - $\Pi_\mathsf{venc}$ satisfies **linear targeted malleability** if for all efficient $\mathcal A$ and $\mathcal M$ there is a simulator $\mathcal S$ such that, for every $z$, $T_0$ and $T_1$ are computationally indistinguishable: $\mathsf{Adv}^\mathsf{ltm}(D)$ is negligible for every efficient $D$. `[BISW17 Def 4.2]`

> [!remark] What it says
> The only homomorphic operations the adversary can perform on ciphertexts are affine functions of the plaintext vectors `[BISW17 §4.1]`: whatever valid ciphertext it makes decrypts, jointly with the plaintexts, like the output of a fixed affine map. Unlike [[Linear-Only Security]], the map need not be extracted efficiently; it only has to exist.

## Variant

### Several output ciphertexts
$\mathcal A$ outputs $\mathrm{ct}'_1, \dots, \mathrm{ct}'_k$ and the simulator outputs an affine map $(\boldsymbol\Pi, \mathbf B)$ that explains all of them; `[BISW17]` needs only the single-ciphertext version. `[BISW17 Remark 4.3]`

### Efficient simulator
Requiring $\mathcal S$ to be polynomial-size, and an LPCP with knowledge soundness, gives a SNARK — an argument of knowledge — instead of a SNARG `[BISW17 Remark 4.9]`. With an unbounded $\mathcal S$ the requirement for every $z$ is harmless; with an efficient one it may be relaxed to "benign" auxiliary inputs, e.g. uniform strings `[BISW17 Remark 4.4]`.

### Strict
`[LUNA]` assumes a "(statistically simulatable, strict) Linear Targeted Malleability" for its encryption scheme `[LUNA fn. 2]`, defined in its appendix as Def 13, and conjectures:

> [!theorem] Conjecture 1 (HGSW Linear Targeted Malleability) — HGSW is strictly linear targeted malleable
> For security parameter $\lambda$ and the parameters $p, d, \tau$ of HGSW, if $1/|R_p|^\tau = p^{-d\tau}$ is negligible in $\lambda$, then HGSW satisfies strictly linear targeted malleability. `[LUNA, Conj. 1]`

LUNA calls it a weaker, not knowledge-based, linear-only assumption that suffices for a ZK-SNARG — regular, not knowledge, soundness `[LUNA, before Conj. 1]`; with a computationally simulatable version and an LPCP with knowledge soundness, the protocols become ZK-SNARKs `[LUNA fn. 2]`.

`⚠️ CLAUDE – verify:` LUNA's Def 13 was not readable. By analogy with strict linear-only `[ISW21 Remark 3.5]`, "strict" presumably drops the constant term, $\mathbf b = \mathbf 0$, so that $\mathbf v'$ is a linear combination of the $\mathbf v_i$; check against Def 13.

## Related

### Instantiations
- [[Module HGSW]] — conjectured strictly linear targeted malleable `[LUNA, Conj. 1]`

### Constructions
- [[LUNA]] — a designated-verifier ZK-SNARG whose soundness rests on this assumption

### Siblings
- [[Linear-Only Security]] — the extractor form, which gives knowledge soundness
- [[Circuit Privacy]] — the other property asked of the same primitive

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Indistinguishability]]
