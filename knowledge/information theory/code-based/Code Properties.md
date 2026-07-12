## Code Properties

Structural properties of codes. Unlike code *families* (Reed–Muller, BCH, Goppa, …), these are **composable axes**: one code can be simultaneously linear, quasi-cyclic, systematic, and self-dual. Scheme specifications compose them — e.g. [[Hamming Quasi-Cyclic|HQC]] uses *systematic quasi-cyclic* codes.

| Axis                   | Property                      | What it constrains                                     |
| ---------------------- | ----------------------------- | ------------------------------------------------------ |
| Algebraic structure    | linear                        | $C$ is a subspace of $\mathbb F_q^n$ ([[Linear Code]]) |
| Symmetry               | cyclic, quasi-cyclic          | invariance under coordinate shifts                     |
| Presentation / encoder | systematic                    | how messages map to codewords                          |
| Duality                | self-orthogonal, self-dual    | relation between $C$ and $C^\perp$ ([[Linear Code]])   |
| Alphabet               | subfield, trace, concatenated | derived codes over smaller fields ([[Subfield Codes]]) |

## Systematic

> [!definition] Systematic Encoder
> An encoder for an $[n, k]$-linear code $C$ is **systematic** if the message appears verbatim in a fixed set of $k$ coordinates of the codeword: $$c = (m, p) \in \mathbb F_q^n,$$ where $m \in \mathbb F_q^k$ is the message (**message digits**) and $p \in \mathbb F_q^{n - k}$ is the redundancy (**check digits**). Equivalently, $C$ is used with a generator matrix in [[Linear Code#Generator Matrix and Parity-Check Matrix|standard form]] $G = (I_k \mid X)$, so that $mG = (m, mX)$.

> [!remark]
> 1. Systematic is a property of the *presentation* (choice of $G$), not of the code as a set: every linear code is [[Linear Code#Equivalence of linear codes|equivalent]] to one with a generator matrix in standard form.
> 2. Decoding the message from an uncorrupted systematic codeword is free — read the first $k$ coordinates. This is why scheme specifications (e.g. HQC) fix systematic form.

## Cyclic and Quasi-Cyclic

> [!definition] Quasi-Cyclic Code
> Let $T$ denote the cyclic shift $T(a_0, a_1, \dots, a_{n-1}) = (a_{n-1}, a_0, \dots, a_{n-2})$. A linear code $C \subseteq \mathbb F_q^n$ is **quasi-cyclic of index $\ell$** (where $\ell \mid n$) if $T^\ell(C) = C$, i.e. $C$ is invariant under shifting by $\ell$ positions. A **cyclic code** is the special case $\ell = 1$ (see [[Cyclic Codes]] for the full theory).

> [!proposition]
> Writing $n = \ell m$ and viewing a codeword as $\ell$ blocks of length $m$, a quasi-cyclic code of index $\ell$ is invariant under the simultaneous cyclic shift of all $\ell$ blocks. Algebraically, $C$ is a module over $\mathbb F_q[x]/(x^m - 1)$, and $C$ admits a generator matrix composed of $m \times m$ **circulant blocks**.

> [!remark] Why quasi-cyclic in cryptography
> A circulant block is determined by its first row, so a quasi-cyclic generator (or parity-check) matrix costs $O(n)$ storage instead of $O(n^2)$ — this is the key-size compression used by HQC, BIKE, and other code-based NIST candidates. The price is added algebraic structure, which must be assumed harmless (quasi-cyclic variants of [[Syndrome Decoding]]).

## Related

- [[Linear Code]] — linearity, duality (self-orthogonal / self-dual), standard form
- [[Cyclic Codes]] — the $\ell = 1$ theory: generator polynomial, ideal correspondence, BCH, Reed–Solomon
- [[Subfield Codes]] — alphabet-changing constructions
- [[Hamming Quasi-Cyclic]] — a scheme that composes systematic + quasi-cyclic
