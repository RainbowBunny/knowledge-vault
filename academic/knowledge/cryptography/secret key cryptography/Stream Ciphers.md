## Construction

### Construct from PRG

> [!algorithm] Stream Ciphers from PRG
> Let $G$ be a PRG defined over $(\{0, 1\}^\ell, \{0, 1\}^L)$; that is, $G$ stretches an $\ell$-bit seed to an $L$-bit output. The **stream cipher $\mathcal E$ constructed from $G$** is defined over $(\{0, 1\}^\ell, \{0, 1\}^{\leq L}, \{0, 1\}^{\leq L})$; for $s \in \{0, 1\}^\ell$ and $m, c \in \{0, 1\}^{\ell}$, encryption and decryption are defined as follows: if $|m| = v$, then $$E(s, m) = G(s)[0 \dots v - 1] \oplus m,$$ and if $|c| = v$, then $$D(s, c) = G(s)[0 \dots v - 1] \oplus c.$$

> [!theorem]
> If $G$ is a secure PRG, then the stream cipher $\mathcal E$ constructed from $G$ is a semantically secure cipher.
> 
> In particular, for every [[Encryption#Semantic Security|semantic security]] adversary $\mathcal A$ that attacks $\mathcal E$, there exists a [[#Pseudo-Random Generators|secure PRG]] adversary $\mathcal B$ that attacks $G$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{SSAdv}[\mathcal A, \mathcal E] = 2 \cdot \text{PRGadv}[\mathcal B, \mathcal E].$$

### Construction from Block Cipher

> [!algorithm] Stream Cipher from Block Cipher
> Suppose $\mathcal E = (E, D)$ is a block cipher defined over $(\mathcal K, \mathcal X)$, where $\mathcal X = \{0, 1\}^n$. Let $N = |\mathcal X| = 2^n$. Assume that $N$ is super-poly and that $\mathcal E$ is a secure block cipher. We construct a $\mathcal E' = (E', D')$ with key space $\mathcal K$, message and cipher space $\mathcal X^\ell$, where $\ell$ is a poly-bounded value, and in particular, $\ell \leq N$. We denote $\langle i - 1 \rangle_n$ to be $n$-bit binary encoding $i - 1$. Encryption and decryption for $\mathcal E'$ work as follows.
> - For $k \in \mathcal K$ and $m \in \mathcal X^{\leq \ell}$, with $v = |m|$, we define $$E'(k, m) = (E(k, \langle 0 \rangle_n) \oplus m[0], \dots, E(k, \langle v - 1 \rangle_n) \oplus m[v - 1]).$$
> - For $k \in \mathcal K$ and $c \in \mathcal X^{\leq \ell}$, with $v = |m|$, we define $$D'(k, c) = (D(k, \langle 0 \rangle_n) \oplus c[0], \dots, D(k, \langle v - 1 \rangle_n) \oplus c[v - 1]).$$
> 
> This mode of operation of a block cipher is called **deterministic counter mode**. In particular, for any efficient [[#Semantic Security|semantic security]] adversary $\mathcal A$, there exists an [[#Secure Block Cipher|secure block cipher]] adversary $\mathcal B$ such that $$\text{SSadv}[\mathcal A, \mathcal E'] \leq 2 \cdot \text{BCadv}[\mathcal B, \mathcal E] + \ell^2/N.$$

## Limitations


## Case Study


### RC4 Stream Cipher

