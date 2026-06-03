
| Term                                                | Reference                                                       |                 |
| --------------------------------------------------- | --------------------------------------------------------------- | --------------- |
| Attack Game 10.2 (One-way trapdoor function scheme) | [[#One-way Security\|inverting]]                                | $\text{OWadv}$  |
| Attack Game 10.3 (RSA)                              | [[#A Trapdoor Permutation Scheme Based on RSA\|RSA assumption]] | $\text{RSAadv}$ |
## Basic Definition


> [!definition] Trapdoor Function Scheme (Conceptually)
> Let $\mathcal X$ and $\mathcal Y$ be finite sets. A **trapdoor function scheme** $\mathcal T$, defined over $(\mathcal X, \mathcal Y)$, is a triple of algorithms $(G, F, I)$, where
> - $G$ is a probabilistic key generation algorithm that is invoked as $(pk, sk) \xleftarrow{R} G()$, where $pk$ is called a **public key** and $sk$ is called a **secret key**.
> - $F$ is a deterministic algorithm that is invoked as $y \leftarrow F(pk, x)$, where $pk$ is a public key (as output by $G$) and $x$ lies in $\mathcal X$. The output of $y$ is an element of $\mathcal Y$.
> - $I$ is an deterministic algorithm that is invoked as $x \rightarrow I(sk, y)$, where $sk$ is a secret key (as output by $G$) and $y$ lies in $\mathcal Y$. The output $x$ is an element of $\mathcal X$.
> 
> Moreover, the following **correctness property** should be satisfied: for all possible outputs $(pk, sk)$ of $G()$, and for all $x \in \mathcal X$, we have $I(sk, F(pk, x)) = x$.

> [!algorithm] Trapdoor Function Scheme (Mathematical Detail)
> A **trapdoor function scheme** is a triple of efficient algorithms $(G, F, I)$ along with families of spaces with system parameterization $P$: $$\textbf{X} = \{X_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \textbf{Y} = \{\mathcal Y_{\lambda, \Lambda}\}_{\lambda, \Lambda}.$$
> $\lambda \mathbb Z_{\geq 1}$ is a security parameter and $\Gamma \in \text{Supp}(P(\lambda))$ is a domain parameter. We require that
> 1. $\textbf{X}$ is efficiently recognizable and sampleable.
> 2. $\textbf{Y}$ is efficiently recognizable.
> 3. $G$ is an efficient probabilistic algorithm that on input $\lambda, \Lambda$ where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, outputs a pair $(pk, sk)$, where $pk$ and $sk$ are bits strings whose lengths are always bounded by a polynomial in $\lambda$.
> 4. $F$ is an efficient deterministic algorithms that on input $\lambda, \Lambda, pk, x$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda))$ for some $sk$, and $x \in \mathcal X_{\lambda, \Lambda}$ outputs an element of $\mathcal Y_{\lambda, \Lambda}$.
> 5. $I$ is an efficient deterministic algorithm that on input $\lambda, \Lambda, sk, y$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda))$ for some $pk$, and $y \in \mathcal Y_{\lambda, \Lambda}$, outputs an element of $\mathcal X_{\lambda, \Lambda}$.
> 6. For all $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda))$, and $x \in \mathcal X_{\lambda, \Lambda}$, we have $I(\lambda, \Lambda; sk, F(\lambda, \Lambda; pk, x)) = x$.

> [!remark]
> In the case $\mathcal X = \mathcal Y$, we have a **trapdoor permutation scheme** defined over $\mathcal X$.

### One-way Security

> [!algorithm] One-way Trapdoor Function Scheme
> For a given trapdoor function scheme $\mathcal T = (G, F, I)$, defined over $(\mathcal X, \mathcal Y)$, and a given adversary $\mathcal A$, the attack game runs as follow:
> - The challenger computes $$(pk, sk) \xleftarrow{R} G(), \quad, x \xleftarrow{R} \mathcal X, \quad y \leftarrow F(pk, x) \mathcal Y$$ and sends $(pk, y)$ to the adversary.
> - The adversary outputs $\hat x \in \mathcal X$.
> 
> We define the adversary's advantage in inverting $\mathcal T$, denoted $\text{OWadv}[\mathcal A, \mathcal T]$, to be the probability that $\hat x = x$.

> [!definition] One Way Function
> We say that a trapdoor function scheme $\mathcal T$ is **one way** if for all efficient adversaries $\mathcal A$, the quantity $\text{OWadv}[\mathcal A, \mathcal T]$ is neglible.

### One-way on $d$ iterates

> [!algorithm] One-way on $d$ iterates
> For a given function $f: \mathcal X \rightarrow \mathcal X$ and a given adversary $\mathcal A$, the attack game runs as follows:
> - The adversary chooses $j \in \{1, \dots, d\}$ and sends $j$ to the challenger.
> - The challenger computes $x \xleftarrow{R} \mathcal X$ and $y \xleftarrow f^{(i)}(x)$, and sends $y$ to $\mathcal A$.
> - The adversary outputs $x \in \mathcal X$.
> We say $\mathcal A$ wins the game if $f(x') = y$. We define the adversary's advantage $\text{iOWadv}[\mathcal A, f, d]$ to be the probability that it wins.

> [!definition] One-way on $d$ iterates
> For an integer $d > 0$, we say that $f: \mathcal X \rightarrow \mathcal X$ is **one-way on $d$ iterates** if $\text{iOWadv}[\mathcal A, f, d]$ is negligible for all efficient adversaries $\mathcal A$.

## Construction

### A Trapdoor Permutation Scheme Based on RSA

> [!algorithm] RSA Key Generation
> $\text{RSAGen}$ is a probabilistic algorithm that takes input an integer $\ell > 2$, and an odd integer $e > 2$.
> $\text{RSAGen}(\ell, e)$
> 1. Generate a random $\ell$-bit prime $p$ such that $\gcd(e, p - 1) = 1$
> 2. Generate a random $\ell$-bit prime $q$ such that $\gcd(e, q - 1) = 1$ and $q \neq p$.
> 3. $n \leftarrow pq$
> 4. $d \leftarrow e^{-1} \mod (p - 1)(q - 1)$
> 5. Output $(n, d)$.

> [!algorithm] RSA Trapdoor Permutation Scheme
> RSA trapdoor permutation scheme is a group of algorithms $\mathcal T_{RSA} = (G, F, I)$. It is parameterized by fixed values of $\ell$ and $e$.
> - Key generation runs as follows: $$G() = (n, d) \xleftarrow{R} \text{RSAGen}(\ell, e), pk \leftarrow (n, e), sk \leftarrow (n, d)$$ and output $(pk, sk)$.
> - For a given public key $pk = (n, e),$ and $x \in \mathbb Z_n,$ we define $F(pk, x) = x^e \in \mathbb Z_n$.
> - For a given secret key $sk = (n, d),$ and $y \in \mathbb Z_n,$ we define $I(sk, y) = y^d \in \mathbb Z_n$.

> [!algorithm] RSA
> For given $\ell > 2$ and odd $e > 2,$ and a given adversary $\mathcal A,$ the attack game runs as follows:
> - The challenger and the adversary $\mathcal A$ take $(\ell, e)$ as input.
> - The challenger computes $$(n, d) \xleftarrow{R} \text{RSAGen}(\ell, e), x \xleftarrow{R} \mathbb Z_n, y \leftarrow x^e \mathbb Z_n$$ and sends $(n, y)$ to the adversary.
> - The adversary output $\hat{x} \in \mathbb Z_n$.
> We define the adversary's advantage in breaking RSA, denoted $\text{RSAadv}[\mathcal A, \ell, e],$ as the probability that $\hat{x} = x$.

> [!definition] RSA Assumption
> We say that the RSA assumption holds for $(\ell, e)$ if for all efficient adversaries $\mathcal A,$ the quantity $\text{RSAadv}[\mathcal A, \ell, e]$ is negligible.

> [!remark]
> - $n$: **RSA modulus**.
> - $e$: **Encryption exponent**.
> - $d$: **Decryption exponent**.
> - $(n, y)$: An **instance** of the **RSA problem**.
> - $x$: **Solution** to this instance of the RSA problem.

> [!algorithm] Key Exchange based on the RSA assumption
> - Alice computes $(n, d) \xleftarrow{R} \text{RSAGen}(\ell, e),$ and sends $(n, e)$ to Bob.
> - Upon receiving $(n, e)$ from Alice, Bob computes $x \xleftarrow{R} \mathbb Z_n, y \leftarrow x^e,$ and sends $y$ to Alice.
> - Upon receiving $y$ from Bob, Alice computes $x \leftarrow y^d$.
> 
> The secret shared by Alice and Bob is $x$. Under the RSA assumption, this is a secure anonymous key exchange protocol.
