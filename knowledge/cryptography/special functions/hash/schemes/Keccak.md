
Link: https://keccak.team/files/Keccak-reference-3.0.pdf
Standard: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf (FIPS 202, 2015)

## Scheme

> [!scheme] Keccak (Sponge Construction)
> Reference Name: $\text{Keccak}[r, c]$ (NIST standardized variants: SHA-3 family + SHAKE)
> ### Parameters
> - $b \in \{25, 50, 100, 200, 400, 800, 1600\}$: width of the underlying permutation (standardized: $b = 1600$).
> - $r$: **rate** — bit-rate at which message is absorbed / output is squeezed.
> - $c = b - r$: **capacity** — internal state width hidden from the adversary; determines security level (target security $\approx c / 2$ bits).
> - $\ell$: output digest length in bits.
> - $d$: domain-separation suffix (multi-bit tag distinguishing SHA-3 vs. SHAKE vs. cSHAKE, etc.).
>
> NIST-standardized parameter sets (all $b = 1600$):
>
> | Variant      | $c$  | $r$    | $\ell$ (output) | Domain suffix |
> | ------------ | ---- | ------ | --------------- | ------------- |
> | SHA3-224     | 448  | 1152   | 224             | `01`          |
> | SHA3-256     | 512  | 1088   | 256             | `01`          |
> | SHA3-384     | 768  | 832    | 384             | `01`          |
> | SHA3-512     | 1024 | 576    | 512             | `01`          |
> | SHAKE128     | 256  | 1344   | arbitrary       | `1111`        |
> | SHAKE256     | 512  | 1088   | arbitrary       | `1111`        |
>
> ---
> ### Building Block
> - $f = \text{Keccak-}f[b]$: the **Keccak-f permutation** on $b$-bit states, 24 rounds of (θ, ρ, π, χ, ι) operations. Treated as a public random permutation for analysis.
> - $\text{pad}_{r}: \{0,1\}^* \rightarrow \{0,1\}^{r \mathbb{Z}_{\geq 1}}$: multi-rate padding (the pad10*1 rule): append `1`, then minimal zeros, then `1`, padding to a multiple of $r$.
>
> ---
> ### Algorithms
> - $H \leftarrow \text{Keccak}[r, c](M, \ell)$:
>   1. $P \leftarrow M \,\|\, d \,\|\, \text{pad}_r(|M| + |d|)$  (append domain suffix $d$, then multi-rate padding)
>   2. Split $P$ into $n$ blocks $P_0, P_1, \dots, P_{n-1}$ of $r$ bits each.
>   3. **Absorb phase:** initialize state $S \leftarrow 0^b$.
>      For $i = 0, \dots, n - 1$:
>      - $S \leftarrow f(S \oplus (P_i \,\|\, 0^c))$
>   4. **Squeeze phase:** $Z \leftarrow$ empty.
>      While $|Z| < \ell$:
>      - $Z \leftarrow Z \,\|\, \text{trunc}_r(S)$ (output the first $r$ bits of $S$)
>      - $S \leftarrow f(S)$
>   5. Return $H \leftarrow \text{trunc}_{\ell}(Z)$.

## Property

### Correctness (Determinism)

> [!property] Determinism
> $\text{Keccak}[r, c](M, \ell)$ is a deterministic function of $(M, \ell)$ and the parameters; identical inputs always produce identical outputs.

### Indifferentiability from Random Oracle

> [!property] Sponge Indifferentiability
> If $\text{Keccak-}f[b]$ is modeled as a random permutation, then the sponge construction $\text{Keccak}[r, c]$ is **indifferentiable** from a [[Ideal Cipher Model and Random Oracles|random oracle]] up to roughly $2^{c/2}$ queries (Bertoni-Daemen-Peeters-Van Assche 2008).
>
> Indifferentiability is the right composition notion for random oracles: any protocol secure with a random oracle remains secure when the random oracle is replaced by $\text{Keccak}[r, c]$, with security loss bounded by the indifferentiability bound $\approx q^2 / 2^c$.

## Security

### Collision Resistance

> [!security] Collision Resistance Bound
> For any adversary $\mathcal A$ that makes at most $q$ queries to the underlying $\text{Keccak-}f[b]$ permutation (modeled as random), there is no $\mathcal B$ such that
> $$\text{Adv}^{\text{cr}}_{\text{Keccak}[r, c]}(\mathcal A) \leq \frac{q(q + 1)}{2^{c + 1}} + \frac{q(q + 1)}{2^{\ell + 1}}.$$
>
> The dominant term is the birthday bound on the capacity: $q \approx 2^{c/2}$ queries suffice to find a collision in expectation. Choosing $c = 2\lambda$ targets $\lambda$-bit collision security.

### Preimage Resistance

> [!security] Preimage Resistance Bound
> For any adversary $\mathcal A$ making at most $q$ queries to $\text{Keccak-}f[b]$, modeled as random,
> $$\text{Adv}^{\text{pir}}_{\text{Keccak}[r, c]}(\mathcal A) \leq \frac{q}{2^{\min(c, \ell)}}.$$
>
> Hence preimage security is $\min(c, \ell)$ bits — a digest-length attack against the output, plus a capacity attack against the internal state.

### Second-Preimage Resistance

> [!security] Second-Preimage Resistance Bound
> For any adversary $\mathcal A$ making at most $q$ queries to $\text{Keccak-}f[b]$, modeled as random,
> $$\text{Adv}^{\text{2pir}}_{\text{Keccak}[r, c]}(\mathcal A) \leq \frac{q}{2^{\min(c, \ell)}}.$$
>
> Same asymptotic bound as preimage resistance.

### Concrete Security Levels

> [!remark]
> Setting $c = 2\lambda$ targets $\lambda$-bit collision and $\lambda$-bit preimage security simultaneously. SHA3-256 has $c = 512$, achieving 256-bit preimage / 128-bit collision security. SHAKE128 has $c = 256$, achieving 128-bit both-sides security (suitable for use as a [[Extendable Output Function|XOF]] in PQ schemes like [[Kyber KEM]] and [[Dilithium]]).

## Construction

### Sponge Construction

> [!construction] Sponge
> The sponge construction transforms a fixed-width permutation $f: \{0,1\}^b \to \{0,1\}^b$ into a variable-input-length, variable-output-length function. It consists of two phases:
> - **Absorb**: XOR each padded message block into the *rate* portion of the state (first $r$ bits), then apply $f$. Repeat until the message is consumed.
> - **Squeeze**: extract the first $r$ bits of state as output; if more output is needed, apply $f$ and repeat.
>
> The *capacity* portion (last $c$ bits) is never directly XORed with the input or output — it acts as an internal secret that the permutation diffuses, providing the security margin.

### Keccak-f Permutation

> [!construction] Keccak-f[b]
> The internal permutation operates on a $b$-bit state organized as a $5 \times 5 \times w$ array (with $w = b/25$). It applies 24 rounds, each consisting of five steps:
> - $\theta$: column parity mixing (long-range diffusion).
> - $\rho$: lane rotation by per-lane offsets.
> - $\pi$: lane permutation (transposing the 5×5 grid).
> - $\chi$: nonlinear step (the only nonlinear step; a degree-2 row mixing).
> - $\iota$: per-round constant addition (breaks symmetry).

## Used By

- [[Hash Functions]] — Keccak is the SHA-3 family, the modern standard hash.
- [[Pseudorandom Functions]] — KMAC uses cSHAKE as a PRF.
- [[Extendable Output Function]] — SHAKE128 / SHAKE256 are the standardized XOFs.
- [[Kyber KEM]] / [[Kyber PKE]] — use SHA3-256, SHA3-512, SHAKE128, SHAKE256 internally for KDF, hashing, and sampling (`ExpandA`, `ExpandMask`, CBD sampling).
- [[Dilithium]] — same family of SHAKE-based sampling internally.

## Names for this scheme

> [!remark] Synonyms
> Also known as **SHA-3** (when referring to the NIST-standardized fixed-output variants SHA3-224/256/384/512), **SHAKE128** / **SHAKE256** (variable-output / XOF variants per FIPS 202), and **cSHAKE** (customizable variant from NIST SP 800-185). All are instances of the Keccak sponge construction with different $(r, c, \ell, d)$ parameter choices.
