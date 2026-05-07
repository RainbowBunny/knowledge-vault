
| Term                    | Reference                                             |
| ----------------------- | ----------------------------------------------------- |
| One More Unforgeability | [[#One More Unforgeability\|one more unforgeability]] |
|                         |                                                       |

> [!question]
> A new kind of cryptography to an automated payments system with the following properties:
> 1. Inability of third parties to determine payee, time or amount of payments made by an individual.
> 2. Ability of individuals to provide proof of payment, or to determine the identity of the payee under exceptional circumstances.
> 3. Ability to stop use of payments media reported stolen.

## Basic Definition

> [!definition] Functions
> Blind signature systems might be thought of as including the features of true two key digital signature systems combined in a special way with commutative style public key systems. The following three functions make up the blind signature cryptosystem:
> 1. A signing function $s'$ known only to the signer, and the corresponding publically known inverse $s$, such that $s(s'(x)) = x$.
> 2. A commuting function $c$ and its inverse $c'$, both known only to the provider, such that $c'(s'(c(x))) = s'(x)$, and $c(x)$ and $s'$ give no clue about $x$.
> 3. A redundancy checking predicate $r$, that checks for sufficient redundancy to make search for valid signature impratical.

> [!definition] Protocol
> 1. Provider chooses $x$ at random such that $r(x)$, forms $c(x)$, and supplies $c(x)$ to signer.
> 2. Signer signs $c(x)$ by applying $s'$ and returns the signed matter $s'(c(x))$ to provider.
> 3. Provider strips signed matter by application of $c'$, yielding $c'(s'(c(x))) = s'(x)$.
> 4. Anyone can check that the stripped matter $s'(x)$ was formed by the signer, by applying the signer's public keys and checking that $r(s(s'(x)))$.

> [!definition] Properties
> The following security properties are desired of the blind signature system comprising the above functions and protocols:
> 1. Digital signature - anyone can check that a stripped signature $s'(x)$ was formed using signer's private key $s'$.
> 2. Blind signature - signer knows nothing about the correspondence between the elements of the set of stripped signed matter $s'(x_i)$ and the elements of the set of unstripped signed matter $s'(c(x_i))$.
> 3. Conservation of signatures - provider can create at most one stripped signature for each thing signed by signer (i.e. even with $s'(c(x_1)) \dots s'(c(x_n))$) and choice of $c, c',$ and $x_i$, it is impractical to produce $s'(y)$, such that $r(y)$ and $y \neq x_i$).

> [!definition] Blind Signature Scheme
> A **blind signature scheme** lets one party, Alice, obtain a signature on a message $m$ from Bob, so that Bob learns nothing about $m$.

> [!definition] Blind Signature (Mathematical Detail)
> A blind signature scheme $BS$ consists of PPT algorithms $\text{Gen}, \text{Vrfy}$ along with interactive PPT algorithms $\mathcal S, \mathcal U$ such that for any $\lambda$:
> - $\text{Gen}(1^\lambda)$ generates a key pair $(\text{BSig.sk}, \text{BSig.vk})$.
> - The joint execution of $\mathcal S(\text{BSig.sk})$ and $\mathcal U(\text{BSig.vk}, \mu)$ where $\mu \in \{0, 1\}^*$, generates an output $\sigma$ for the user and no output for the signer; this is denoted as $(\perp, \sigma) \leftarrow \langle \mathcal S(\text{BSig.sk}), \mathcal U(\text{BSig.vk}, \mu) \rangle$.
> - Algorithm $\text{Vrfy}(\text{BSig.vk}, \mu, \sigma)$ outputs a bit $b$.
> 
> The scheme must satisfy completeness: for any $(\text{BSig.sk}, \text{BSig.vk}) \leftarrow \text{Gen}(1^\lambda), \mu \in \{0, 1\}^*$ and $\sigma$ output by $\mathcal U$ in the joint execution of $\mathcal S(\text{BSig.sk})$ and $\mathcal U(\text{BSig.vk}, \mu)$, it holds that $\text{Vrfy}(\text{BSig.vk}, \mu, \sigma) = 1$ with probability $1 - \lambda^{-\omega(1)}$.

## Security Model

### One More Unforgeability

> [!algorithm] One More Unforgeability
> The blind signature $BS = (\text{Gen}, \mathcal S, \mathcal U, \text{Vrfy})$ is one more unforgeable if for any polynomial $Q_S$, and any algorithm $\mathcal U^*$ with run-time $2^{o(\lambda)}$, the success probability of $\mathcal U^*$ in the following game is $2^{-\ohm(\lambda)}$:
> 1. $\text{Gen}(1^\lambda)$ outputs $(\text{BSig.sk}, \text{BSig.vk})$, and algorithm $\mathcal U^*$ is given $\text{BSig.vk}$.
> 2. Algorithm $\mathcal U^*$ interacts concurrently with $Q_S$ instances $\mathcal S_{BSig.sk}^1, \dots, S_{BSig.sk}^{Q_S}$
> 3. Algorithm $\mathcal U^*$ outputs $(\mu_1, \sigma_1, \dots, \mu_{Q_S + 1}, \sigma_{Q_S + 1})$.
> 
> Algorithm $\mathcal U^*$ succeeds if $\text{Vrfy}(\text{BSig.vk}, \mu_i, \sigma_i) = 1$ for all $i \in [Q_S + 1]$ and the $\mu_i$'s are distinct.

### Honest Signer Blindness

> [!algorithm] Honest Signer Blindness
> The blind signature $BS = (\text{Gen}, \mathcal S, \mathcal U, \text{Vrfy})$ satisfies honest signer blindness if for any algorithm $\mathcal S^*$ with run-time $2^{o(\lambda)}$, the advantage of $\mathcal S^*$ in the following game is $2^{-\ohm(\lambda)}$:
> 1. $\text{Gen}(1^\lambda)$ outputs $(\text{BSig.sk}, \text{BSig.vk})$ and gives it to $\mathcal S^*$; algorithm $\mathcal S^*$ outputs two messages $\mu_0, \mu_1$ of its choice.
> 2. A random bit $b$ is chosen and $\mathcal S^*$ interacts concurrently with $\mathcal U_0 = \mathcal U(\text{BSig.vk}, \mu_b)$ and $\mathcal U_1 = \mathcal U(\text{BSig.vk}, \mu_{\overline{b}})$ possibly maliciously; when $\mathcal U_0$ and $\mathcal U_1$ have completed their executions, the values $\sigma_b, \sigma_{\overline{b}}$ are defined as follows:
> 	- If either $\mathcal U_0$ or $\mathcal U_1$ aborts, then $(\sigma_b, \sigma_{\overline{b}}) = (\perp, \perp)$.
> 	- Otherwise, let $\sigma_b$ (resp. $\sigma_{\overline{b}}$) be the output of $\mathcal U_0$ (resp. $\mathcal U_1$).
> 	Algorithm $\mathcal S^*$ is given $(\sigma_0, \sigma_1)$.
> 3. Algorithm $\mathcal S^*$ outputs a bit $b'$.
> 
> Algorithm $\mathcal S^*$ succeeds if $b' = b$. If $\text{succ}$ denotes the latter event, then the advantage of $\mathcal S^*$ is defined as $|P[\text{succ}] - 1/2|$.
 
## Construction

### RSA-based

> [!algorithm] RSA-based Blind Signature
> Let $(n, d) \xrightarrow{R} \text{RSAGen}(\ell, e)$ and set $(n, e)$ as Bob's RSA public key and $(n, d)$ as his corresponding private key. As usual, let $H: \mathcal M \rightarrow \mathbb Z_n$ be a hash function. Alice wants Bob to sign a message $m \in \mathcal M$. They engage in the following three-message protocol:
> 1. Alice chooses $r \xrightarrow{R} \mathbb Z_n$, sets $m' \leftarrow H(m) \cdot r^e \in \mathbb Z_n$, and sends $m'$ to Bob,
> 2. Bob computes $\sigma' \leftarrow (m')^d \in \mathbb Z_n$ and sends $\sigma'$ to Alice.
> 3. Alice computes the signature $\sigma$ on $m$ as $\sigma \leftarrow \sigma'/r \in \mathbb Z_n$.

