## Encryption Scheme

> [!algorithm] GGH Public-Key Cryptosystem (Babai Decryption)
> **Participants:** Alice (key owner), Bob (sender)
>
> **Output:**  
> Correct encryption and decryption of a small plaintext vector
> $$m \in \mathbb{Z}^n.$$
>
> ---
>
> ### Key Creation (Alice)
>
> 1. Choose a good (nearly orthogonal) lattice basis:
>    $$(v_1, v_2, \ldots, v_n).$$
>
> 2. Choose an integer matrix $U \in \mathbb{Z}^{n \times n}$ satisfying:
>    $$\det(U) = \pm 1.$$
>
> 3. Compute a bad (public) basis by setting:
>    $$W \gets U V,$$
>    where the rows of $W$ are
>    $$(w_1, w_2, \ldots, w_n).$$
>
> 4. Publish the public key:
>    $$(w_1, w_2, \ldots, w_n).$$
>
> ---
>
> ### Encryption (Bob)
>
> **Input:** Small plaintext vector $m = (x_1, \ldots, x_n)$  
> **Public key:** $(w_1, \ldots, w_n)$
>
> 1. Choose a random small vector:
>    $$r \in \mathbb{Z}^n.$$
>
> 2. Compute the ciphertext:
>    $$e \gets x_1 w_1 + x_2 w_2 + \cdots + x_n w_n + r.$$
>
> 3. Send the ciphertext $e$ to Alice.
>
> ---
>
> ### Decryption (Alice)
>
> 1. Use Babai’s closest vertex algorithm to compute a lattice vector
>    $$v \in L$$
>    closest to the ciphertext $e$.
>
> 2. Compute:
>    $$m \gets v W^{-1},$$
>    recovering the plaintext vector.

> [!remark]
> The security of this system based on recovering the good lattice basis $V$ by applying LLL to the lattice $L$.

## Signature Scheme

> [!algorithm] GGH Digital Signature Scheme
> **Participants:** Samantha (signer), Victor (verifier)
>
> **Output:**  
> A valid lattice-based digital signature for a document
>
> ---
>
> ### Key Creation (Samantha)
>
> 1. Choose a lattice $L \subset \mathbb{R}^n$ together with:
>    - a good (nearly orthogonal) basis $(v_1, v_2, \ldots, v_n)$,
>    - a bad (public) basis $(w_1, w_2, \ldots, w_n)$ for $L$.
>
> 2. Publish the public key:
>    $$(w_1, w_2, \ldots, w_n).$$
>
> ---
>
> ### Signing (Samantha)
>
> **Input:** Document $d \in \mathbb{Z}^n$
>
> 1. Using Babai’s closest vector algorithm with the good basis
>    $(v_1, \ldots, v_n)$, compute a lattice vector
>    $$s \in L$$
>    that is close to the document vector $d$.
>
> 2. Express the lattice vector $s$ in the public basis:
>    $$s = a_1 w_1 + a_2 w_2 + \cdots + a_n w_n.$$
>
> 3. Output the signature:
>    $$(a_1, a_2, \ldots, a_n).$$
>
> ---
>
> ### Verification (Victor)
>
> **Input:** Document $d$ and signature $(a_1, \ldots, a_n)$
>
> 1. Compute the lattice vector:
>    $$s \gets a_1 w_1 + a_2 w_2 + \cdots + a_n w_n.$$
>
> 2. Accept the signature if and only if $s$ is sufficiently close to $d$.

> [!remark]
> The verification step in the GGH digital signature consists in checking that the signature vector $s$, which is in the lattice $L$, is sufficiently close to the non lattice document vector $d$. In order to use GGH, someone must specify a cutoff value $\epsilon$ such that the signature is valid if $$||s - d|| < \epsilon,$$ and invalid otherwise.
