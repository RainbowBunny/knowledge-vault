## Computational Cipher

> [!algorithm] Computational Cipher
> Let $\mathcal E = (E, D)$ be a computational cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $\mathcal K$ is the key space, $\mathcal M$ is the message space, and $\mathcal C$ is the ciphertext space. We associate with $\mathcal E$ families of key, message, and ciphertext spaces, indexed by
> - A **security parameter**, which is a positive integer, and is denoted by $\lambda$, and
> - A **system parameter**, which is a bit string, and is denoted by $\Lambda$.
> 
> Thus, instead of just finite sets $\mathcal K, \mathcal M$ and $\mathcal C$, we have families of finite sets c which we view as sets of bit strings.

> [!definition] Support
> $\text{Supp}(P(\lambda))$ refer to the **support** of the distribution $P(\lambda)$, which is the set of all possible outputs of algorithm $P$ on input $\lambda$.

> [!definition] System Parameterization
> A **system parameterization** is an efficient probabilistic algorithm $P$ that given a security parameter $\lambda \in \mathbb Z_{\geq 1}$ as input, outputs a bit string $\Lambda$, called a **system parameter**, whose length is always bounded by a polynomial in $\lambda$.

> [!remark]
> A collection $S = \{\mathcal S_{\lambda, \Lambda}\}_{\lambda, \Lambda}$ of finite sets of bits strings, where $\lambda$ runs over $\mathbb Z_{\geq 1}$ and $\Lambda$ runs over $\text{Supp}(P(\lambda))$.

> [!definition] Family of Spaces with System Parameterization
> $S$ is called a **family of spaces with system parameterization** $P$, provided the lengths of all the strings in each of the sets $\mathcal S_{\lambda, \Lambda}$ are bounded by some polynomial $p$ in $\lambda$.

> [!definition] Efficiently Recognizable
> We say that $S$ is **efficiently recognizable** if there is an efficient deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $s \in \{0, 1\}^{\leq p(\lambda)}$, determines if $s \in \mathcal S_{\lambda, \Lambda}$.

> [!definition] Efficiently Sampleable
> We say that $S$ is **efficiently sampleable** if there is an efficient probabilistic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}$ and $\Lambda \in \text{Supp}(P(\lambda))$, outputs an element uniform distributed over $\mathcal S_{\lambda, \Lambda}$.

> [!definition] Effective Length Function
> We say that $S$ **has an effective length function** if there is an efficient deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $s \in \mathcal S_{\lambda, \Lambda}$, outputs a non-negative integer, called the **length** of $s$.

> [!algorithm] Computational Cipher (Mathematical Detail)
> Let $\mathcal E = (E, D)$ be a computational cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $\mathcal K$ is the key space, $\mathcal M$ is the message space, and $\mathcal C$ is the ciphertext space. We associate with $\mathcal E$ families of key, message, and ciphertext spaces, indexed by
> - A **security parameter**, which is a positive integer, and is denoted by $\lambda$, and
> - A **system parameter**, which is a bit string, and is denoted by $\Lambda$.
> 
> Thus, instead of just finite sets $\mathcal K, \mathcal M$ and $\mathcal C$, we have families of finite sets $$\{K = \mathcal K_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad M = \{\mathcal M_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad \text{and} \quad C = \{\mathcal C_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ such that 
> 1. $K, M$, and $C$ are efficiently recognizable.
> 2. $K$ is efficiently sampleable.
> 3. $M$ has an effective length function.
> 4. Algorithm $E$ is an efficient probabilistic algorithm that on input $\lambda, \Lambda, k, m$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $m \in \mathcal M_{\lambda, \Lambda}$, always outputs an element of $\mathcal C_{\lambda, \Lambda}$.
> 5. Algorithm $D$ is an efficient deterministic algorithm that on input $\lambda, \Lambda, k, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $c \in \mathcal C_{\lambda, \Lambda}$, outputs either an element of $\mathcal M_{\lambda, \Lambda}$, or a special symbol $\text{reject} \notin \mathcal M_{\lambda, \Lambda}$.
> 6. For all $\lambda, \Lambda, k, m, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}, m \in \mathcal M_{\lambda, \Lambda}$, and $c \in \text{Supp}(E(\lambda, \Lambda; k, m))$, we have $D(\lambda, \Lambda; k, c) = m$.

### Elementary Wrapper

> [!definition] Efficient Interactive Machine
> We say that $M$ is an **efficient interactive machine** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$, such that for all environments (not even computationally unbounded ones), the probability that the total running time of $M$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

> [!definition] Elementary Wrapper
> An interactive machine $M'$ is called an **efficient interface** if there exists a poly-bounded function $t$ and a negligible function $\epsilon$, such that for all $M$ (not necessarily computationally bounded), when we execute the composed machine $\langle M', M \rangle$ in an arbitrary environment (not necessarily computationally bounded), the following property holds:
> - At every point in the execution of $\langle M', M \rangle$, if $I$ is the number of interactions between $M'$ and $M$ up to at that point, and $T$ is the total running time of $M'$ up to that point, then the probability that $T > t(\lambda + I)$ is at most $\epsilon(\lambda)$.
> 
> If $M'$ is an efficient interface, and $M$ is any machine, then we say $\langle M, M' \rangle$ is an **elementary wrapper around** $M$.

