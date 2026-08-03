## Encryption Scheme

> [!algorithm] NTRU Public-Key Cryptosystem
> **Participants:** Alice (key owner), Bob (sender)
>
> **Public Parameters:**  
> Integers $(N, p, q, d)$ such that:
> - $N$ and $p$ are prime,
> - $\gcd(p,q) = \gcd(N,q) = 1$,
> - $q > (6d+1)p$.
>
> **Output:**  
> Correct encryption and decryption of a plaintext polynomial
> $$m \in R_p.$$
>
> ---
>
> ### Key Creation (Alice)
>
> 1. Choose a private polynomial:
>    $$f \in \mathcal{T}(d+1,d)$$
>    such that $f$ is invertible in both $R_q$ and $R_p$.
>
> 2. Choose a private polynomial:
>    $$g \in \mathcal{T}(d,d).$$
>
> 3. Compute:
>    $$F_q \gets f^{-1} \in R_q, \qquad F_p \gets f^{-1} \in R_p.$$
>
> 4. Compute and publish the public key:
>    $$h \gets F_q \star g \in R_q.$$
>
> ---
>
> ### Encryption (Bob)
>
> **Input:** Plaintext polynomial $m \in R_p$  
> **Public key:** $h$
>
> 1. Choose a random polynomial:
>    $$r \in \mathcal{T}(d,d).$$
>
> 2. Compute the ciphertext:
>    $$e \gets p r \star h + m \pmod q.$$
>
> 3. Send the ciphertext $e$ to Alice.
>
> ---
>
> ### Decryption (Alice)
>
> 1. Compute:
>    $$a \gets f \star e \pmod q.$$
>
> 2. Center-lift $a$ to a polynomial in $R$.
>
> 3. Recover the plaintext:
>     $$m \gets F_p \star a \pmod p.$$

> [!remark] The correctness of NTRU
> $$\begin{align}
> a &\equiv f \star e \pmod q \\
>  &\equiv f \star (pr \star h + m) \pmod q \\
>  &\equiv p r \star f \star F_q \star g + f \star m \pmod q \\
>  &\equiv p r \star g + f \star m \pmod q \\
>  &= p r \star g + f \star m
> \end{align}$$
> Then $$\begin{align}
> F_p \star a \pmod p &\equiv F_p \star (p r \star g + f \star m) \pmod p \\
>   &\equiv F_p \star f \star m \pmod p \\
>   &\equiv m \pmod p   
> \end{align}$$

> [!definition] NTRU Key Recovery Problem
> Given $h$, find [[Polynomial#Ternary Polynomials|ternary polynomials]] $f$ and $g$ satisfying $f \star h \equiv g \pmod q$.

## NTRU as a lattice cryptosystem

> [!definition] NTRU Lattice
> Let $$h(x) = h_0 + h_1 x + \cdots + h_{N - 1} x^{N - 1}$$ be an NTRU public key. The **NTRU lattice** $L_h^{\text{NTRU}}$ associated to $h(x)$ is the $2N$-dimensional lattice spanned by the rows of the matrix
> $$M_h^{\text{NTRU}} =
> \left(
> \begin{array}{cccc|cccc}
>1 & 0 & \cdots & 0 & h_0 & h_1 & \cdots & h_{N-1} \\
>0 & 1 & \cdots & 0 & h_{N-1} & h_0 & \cdots & h_{N-2} \\
> \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & 1 & h_1 & h_2 & \cdots & h_0 \\
> \hline
> 0 & 0 & \cdots & 0 & q & 0 & \cdots & 0 \\
> 0 & 0 & \cdots & 0 & 0 & q & \cdots & 0 \\
> \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & 0 & 0 & 0 & \cdots & q
> \end{array}
>\right)$$

> [!proposition]
> Assuming that $f(x) \star h(x) \equiv g(x) \pmod q$, let $u(x) \in R$ be the polynomial satisfying $$f(x) \star h(x) = g(x) + q u(x).$$ Then $$(f, -u) M_h^{\text{NTRU}} = (f, g),$$ so the vector $(f, g)$ is in the NTRU lattice $L_h^{\text{NTRU}}$.

> [!proposition]
> Let $(N, p, q, d)$ be NTRU parameters, where for simplicity we will assume that $$d \approx N/3 \quad \text{and} \quad q \approx 6d \approx 2N.$$ Let $L_h^{\text{NTRU}}$ be an NTRU lattice associated to the private key $(f, g)$.
> 1. $\det (L_h^{\text{NTRU}}) = q^N$.
> 2. $||(f, g)|| \approx \sqrt{4d} \approx \sqrt{\frac{4N}{3}} \approx 1.155 \sqrt{N}$.
> 3. The [[Lattices#Gaussian heuristic|Gaussian heuristic]] predicts that the shortest nonzero vector in the NTRU lattice has length $$\sigma (L_h^{\text{NTRU}}) \approx \sqrt{\frac{Nq}{\pi e}} \approx 0.484 N.$$ 
> 
> Hence if $N$ is large, then there is a high probability that the shortest nonzero vectors in $L_h^{\text{NTRU}}$ are $(f, g)$ and its rotations. Further, $$\frac{||(f, g)||}{\sigma (L)} \approx \frac{2.39}{\sqrt{N}}$$ so the vector $(f, g)$ is a factor of $\mathcal O(1/\sqrt{N})$ shorter than predicted by the gaussian heuristic.

> [!remark]
> When we apply LLL to the NTRU lattice, we might find a rotation of $f$ and $g$.

## Digital Signature Scheme

> [!algorithm] Computing Small Polynomials for NTRU Key Generation
> **Input:**  
> - Polynomials $f(x), g(x) \in \mathbb{Z}[x]$  
> - Integer parameters $N$ and $q$
>
> **Output:**  
> Polynomials $F(x), G(x) \in \mathbb{Z}[x]$ satisfying
> $$f(x) \star G(x) - g(x) \star F(x) = q$$
> in $\mathbb{Z}[x]/(x^N - 1)$.
>
> ---
>
> 1. Find polynomials $f_1(x), f_2(x), g_1(x), g_2(x) \in \mathbb{Z}[x]$
>    and positive integers $R_f, R_g$ such that
>
>    $$f_1(x) f(x) + f_2(x)(x^N - 1) = R_f,$$
>
>    $$g_1(x) g(x) + g_2(x)(x^N - 1) = R_g.$$
>
> 2. If $\gcd(R_f, R_g) \neq 1$, terminate and report failure.
>
> 3. Find integers $S_f$ and $S_g$ such that
>
>    $$S_f R_f + S_g R_g = 1.$$
>
> 4. Define
>
>    $$A(x) \gets q S_f f_1(x), \qquad
>      B(x) \gets -q S_g g_1(x).$$
>
>    Then
>
>    $$A(x) \star f(x) - B(x) \star g(x) = q$$
>    in $\mathbb{Z}[x]/(x^N - 1)$.
>
> 5. Compute (to sufficient precision) the inverses
>    $f(x)^{-1}$ and $g(x)^{-1}$ in $\mathbb{R}[x]/(x^N - 1)$.
>
> 6. Compute
>
>    $$C(x) \gets
>      \left\lfloor
>      \tfrac{1}{2}
>      \bigl(
>        B(x) \star f(x)^{-1}
>        + A(x) \star g(x)^{-1}
>      \bigr)
>      \right\rceil,$$
>
>    where rounding is applied coefficient-wise to the nearest integer.
>
> 7. Set
>
>    $$F(x) \gets B(x) - C(x) \star f(x), \qquad
>      G(x) \gets A(x) - C(x) \star g(x).$$ 
>
> 8. Return the polynomials $F(x)$ and $G(x)$.

> [!proposition]
> Fix parameters $(N, p, d)$ with $q = \mathcal O(N)$ and $d = \mathcal O(N)$. Let $f(x)$ and $g(x)$ be [[Polynomial#Ternary Polynomials|ternary polynomials]] in $\mathcal T(d_1, d_2)$ with $d_1 \approx d_2 \approx d$. Suppose that both $f(x)$ and $g(x)$ are relatively prime to $x^N - 1$, and suppose further that their [[Polynomial#The Euclidean Algorithm|resultants]] $$R_f = \text{Res}(f(x), x^N - 1) \quad \text{and} \quad R_g = \text{Res}(g(x), x^N - 1)$$ are relatively prime integers. Then, the algorithm computes polynomials $F(x), G(x) \in \mathbb Z[x] / (x^N - 1)$ satisfying the identity $$f(x) \star G(x) - g(x) \star F(x) = q$$ and with norms satisfying $$||F|| = \mathcal O(N) \quad \text{and} \quad ||G|| = \mathcal O(N).$$

> [!algorithm] NTRU Digital Signature Scheme
> **Participants:** Samantha (signer), Victor (verifier)
>
> **Public Parameters:**  
> NTRU parameters $(N, q, d)$
>
> **Output:**  
> A valid NTRU-based digital signature $(D, s)$ for a document $D$,
> and successful verification of the signature
>
> ---
>
> ### Key Creation (Samantha)
>
> 1. Choose ternary polynomials:
>    $$f, g \in \mathcal{T}(d+1, d).$$
>
> 2. Compute small polynomials $F$ and $G$ satisfying:
>    $$f \star G - g \star F = q.$$
>
> 3. Compute the verification key:
>    $$h \gets f^{-1} \star g \pmod q.$$
>
> 4. Publish the public key $h$.
>
> ---
>
> ### Signing (Samantha)
>
> **Input:** Document
> $$D = (D_1, D_2) \in R_q \times R_q$$
>
> 1. Compute:
>    $$v_1 \gets \left\lfloor \frac{D_1 \star G - D_2 \star F}{q} \right\rceil,$$
>    $$v_2 \gets \left\lfloor \frac{-D_1 \star g + D_2 \star f}{q} \right\rceil.$$
>
> 2. Compute the signature polynomial:
>    $$s \gets v_1 \star f + v_2 \star F.$$
>
> 3. Output the signature:
>    $$(D, s).$$
>
> ---
>
> ### Verification (Victor)
>
> **Input:** Document $D$ and signature $s$
>
> 1. Compute:
>    $$t \gets h \star s \pmod q.$$
>
> 2. Accept the signature if and only if the pair $(s, t)$
>    is sufficiently close to $D$.

