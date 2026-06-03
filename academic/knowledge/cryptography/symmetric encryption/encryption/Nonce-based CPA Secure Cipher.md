## Nonce-based CPA Secure Cipher Construction

### Nonce-based Generic Hybrid Construction

> [!algorithm] Nonce-based Generic Hybrid Construction
> Let $\mathcal E = (E, D)$ is a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, and $F$ is a PRF defined over $(\mathcal K', \mathcal X, \mathcal K)$. We define the nonce-based cipher $\mathcal E'$, which is defined over $(\mathcal K', \mathcal M, \mathcal C, \mathcal X)$, as follows:
> - For $k' \in \mathcal K', m \in \mathcal M$, and $x \in \mathcal X$, we define $E'(k', m, x) = E(k, m)$, where $k = F(k', x)$;
> - For $k' \in \mathcal K', c \in \mathcal C, x \in \mathcal X$, we define $D'(k', c, x) = D(k, c)$, where $k = F(k', x)$.

> [!theorem]
> If $F$ is a secure PRF and $\mathcal E$ is a semantically secure cipher, then the cipher $\mathcal E'$ described above is a CPA secure cipher.
> 
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attacks $\mathcal E'$ which makes at most $Q$ queries to its challenger, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B_F$ that attacks $F$ and an [[#Semantic Security|semantic security]] adversary $\mathcal B_{\mathcal E}$ that attacks $\mathcal E$, where both $\mathcal B_F$ and $\mathcal B_{\mathcal E}$ are elementary wrappers around $\mathcal A$, such that $$\text{nCPAadv}[\mathcal A, \mathcal E'] \leq 2 \cdot \text{PRFadv}[\mathcal B_F, F] + Q \cdot \text{SSadv}[\mathcal B_{\mathcal E}, \mathcal E].$$

### Nonce-based Counter Mode

> [!algorithm] Nonce-based Counter Mode
> Let assume $\ell$ divides $N$, we modify the cipher scheme in [[#Randomized Counter Mode]] by using nonce space $\{0, \dots, N / \ell - 1\}$ and translate the nonce $n$ to the PRF input $x = n \ell$.


> [!theorem]
> If $F$ is a secure PRF, then the nonce-based cipher $\mathcal E$ above is a CPA secure cipher.
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attacks $\mathcal E$, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B$ that attacks $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E] \leq 2 \cdot \text{PRFadv}[\mathcal B, F].$$

### Nonce-based CBC Mode

> [!algorithm] Nonce-based CBC Mode
> Assume that we have a PRF $F$ defined over $(\mathcal K', \mathcal N, \mathcal X)$. Here, the key space $\mathcal K'$ and input space $\mathcal N$ of $F$ may be arbitrary sets, but the output space $\mathcal X$ of $F$ must match the block space of the underlying block cipher $\mathcal E = (E, D)$, which is defined over $(\mathcal K, \mathcal X)$. In the nonce-based CBC scheme $\mathcal E'$, the key space $\mathcal K \times \mathcal K'$, and the encryption and decryption algorithms, the IV is computed from the nonce $n$ and the key $k'$ as $c[0] = F(k', n)$.

> [!theorem]
> If $\mathcal E = (E, D)$ is a secure block cipher defined over $(\mathcal K, \mathcal X)$, and $N = |\mathcal X|$ is super-poly, and $F$ is a secure PRF defined over $(\mathcal K', \mathcal N, \mathcal X)$, then for any poly-bounded $\ell \geq 1$, the nonce-based cipher $\mathcal E'$ is a CPA secure cipher.
> 
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attack $\mathcal E'$, and which makes at most $Q$ queries to its challenger, there exists [[Block Ciphers#Secure Block Cipher|secure block cipher]] adversary $\mathcal B$ that attacks $\mathcal E$, and a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B_F$ that attacks $F$, where $\mathcal B$ and $\mathcal B_F$ are elementary wrappers around $\mathcal A$, such that $$\text{nCPAadv}[\mathcal A, \mathcal E'] \leq \frac{2Q^2 \ell^2}{N} + 2 \cdot \text{PRFadv}[\mathcal B_F, F] + 2 \cdot \text{BCadv}[\mathcal B, \mathcal E].$$

