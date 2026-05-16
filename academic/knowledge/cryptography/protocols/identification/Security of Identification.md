## Security Against Eavesdropping

> [!algorithm] Secure Identification: Eavesdropping Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$ and a given adversary $\mathcal A$, the attack game runs as follow:
> - **Key generation phase**: The challenger runs $(vk, sk) \xleftarrow{R} G()$, and sends $vk$ to $\mathcal A$.
> - **Eavesdropping phase**: The adversary requests some number, say $Q$, of transcripts of conversations between $P$ and $V$. The challenger complies by running the interaction between $P$ and $V$ a total of $Q$ times, each time with $P$ initialized with input $sk$ and $V$ initialized with $vk$. The challenger sends these transcripts $T_1, \dots, T_Q$ to the adversary.
> - **Impersonate attempt**: The challenger and $\mathcal A$ interact, with the challenger following the verifier's algorithm $V$ (with input $vk$), and with $\mathcal A$ playing the role of a prover, but not necessarily following the prover's algorithm $P$.
> 
> We say that the adversary wins the game if $V$ outputs `accept` at the end of the interaction. We define $\mathcal A$'s advantage with respect to $\mathcal I$, denoted $\text{ID2adv}[\mathcal A, \mathcal I]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Secure Against Eavesdropping Attacks
> We say that an identification protocol $\mathcal I$ is **secure against eavesdropping attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{ID2adv}[\mathcal A, \mathcal I]$ is negligible.

> [!proposition] 
>  We let $\text{wIDadv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning when keeping $vk$ secret in this eavesdropping attack. ID protocols secure in these settings are said to be **weakly secure**.

> [!definition] Weakly Secure Against Eavesdropping Attacks
> Let $\text{wIDadv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning the weaker version of Eavesdropping Attacks. We say that an identification protocol $\mathcal I$ is **weakly secure against eavesdropping attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{wID2adv}[\mathcal A, \mathcal I]$ is negligible.

### Hash-based One-Time Password

> [!algorithm] Hash-based One-Time Password
> Let $F$ be a PRF defined over $(\mathcal K, \mathbb Z_N, \mathcal Y)$ for some large integer $N$, say $N = 2^{128}$. This $F$ is used to update the password after every successful invocation. The HOTP protocol HOTP $= (G, P, V)$ works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal K$ and output $sk := (k, 0)$ and $vk := (k, 0)$.
> - Algorithm $P$ given $sk$, and algorithm $V$ given $vk$, interact as follows:
> 	1. $P(sk = (k, i))$: send $r := F(k, i)$ to $V$ and set $sk \leftarrow (k, i + 1)$,
> 	2. $V(vk = (k, i))$: if the received $r$ from $P$ satisfies $r = F(k, i)$ output `accept` and set $vk \leftarrow (k, i + 1)$. Otherwise, output `reject`.
> 
> Here both $vk$ and $sk$ must be kept secret, and therefore HOTP is only **weakly** secure against eavesdropping. Note that the integer $N$ is chosen to be so large that, in practice, the counter $i$ will never wrap around. Implementations of HOTP typically use HMAC-SHA256 as the underlying PRF, where the output is truncated to the desired size, typically six decimal digits.

> [!theorem]
> Let $F$ be a PRF defined over $(\mathcal K, \mathbb Z_N, \mathcal Y)$, where $N$ and $|\mathcal Y|$ are both super-poly. Then the ID protocol HOTP is weakly secure against eavesdropping.

> [!remark] Problem of HOTP
> 1. Counter is required because there is no implicit counter for synchronize between client and server.
> 2. The one-time password of HOTP is only updated when the user initiates the protocol so impersonate is easy.

### Time-based One-Time Password

> [!algorithm] Time-based One-Time Password
> **Time-based one-time passwords**, or **TOTP** is when the counter $i$ is incremented by one every 30 seconds, whether the user authenticates or not. 

### S/Key Protocol

> [!algorithm] The S/key Protocol
> The protocol $\text{SKey}_n = (G, P, V)$, designed for $n$ invocations, works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal X$. Output $sk := (k, n)$ and $vk := H^{(n + 1)}(k)$,
> - Algorithm $P$ given $sk$, and algorithm $V$ given $vk$, interact as follows:
> 	1. $P(sk = (k, i))$: send $t := H^{(i)}(k)$ to $V$ and set $sk \leftarrow (k, i - 1)$,
> 	2. $V(vk)$: if the received $t$ from $P$ satisfies $vk = H(t)$ output `accept` and set $vk \leftarrow t$. Otherwise, output `reject`. 

> [!remark]
> S/key protocol remains secure even if $vk$ is made public. Hence, S/key is fully secure against eavesdropping, while HOTP is only weakly secure.

> [!theorem]
> Let $H: \mathcal X \rightarrow \mathcal X$ be a one-way function on $n$ iterates. Then the ID protocol $SKey_n$ is secure against eavesdropping.

> [!remark]
> Algorithm $G$ could choose a public salt at setup time and prepend this salt to the input on every application of $H$. Moreover, to avoid the attack of **14.18** it is recommended to use a different hash function at every step in the chain.

> [!remark] The trouble with S/Key
> In every authentication attempt, the prover $P$ must send to $V$ an element $t \in \mathcal X$. For $H$ to be one-way, the set $\mathcal X$ must be large and therefore $t$ can not be a 6-digit number as in the TOTP system. In practice, $t$ needs to be at least 128 bits to ensure that $H$ is one-way. This makes it inconvenient to use S/key as a one-time password scheme where the user needs to type in a password. Encoding a 128-bit $t$ as printable characters requires at least 22 characters.

## Security Against Active Attacks

> [!algorithm] Secure Identification: Active Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$ and given adversary $\mathcal A$, the attack game, runs as follows:
> - **Key generation phase**: The challenger runs $(vk, sk) \xleftarrow{R} G()$, and sends $vk$ to $\mathcal A$.
> - **Active probing phase**: The adversary requests to interact with the prover. The challenger complies by interacting with the adversary in an ID protocol with the challenger playing the role of the prover by running algorithm $P$ initialized with $sk$. The adversary plays the role of verifier, but not necessarily following the verifier's algorithm $V$. The adversary may interact concurrently with many instances of the prover - these interactions may be arbitrarily interleaved with one another.
> - **Impersonation attempt**: The challenger and $\mathcal A$ interact, with the challenger following the verifier's algorithm $V$ (with input $vk$), and with $\mathcal A$ playing the role of a prover, but not necessarily following the prover's algorithm $P$.
> 
> We say that the adversary wins the game if the verification protocol $V$ outputs `accept` at the end of the interactions. We define $\mathcal A$'s advantage with respect to $\mathcal I$, denoted $\text{ID3Adv}[\mathcal A, \mathcal I]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Secure Against Active Attacks
> We say that an identification protocol $\mathcal I$ is secure against active attacks if for all efficient adversaries $\mathcal A$, the quantity $\text{ID3adv}[\mathcal A, \mathcal I]$ is negilgile.

> [!definition] Weakly Secure Against Active Attack
> Let $\text{wID3adv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning the weaker version of Active Attacks. We say an identification protocol $\mathcal I$ is **weakly secure against active attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{wID3adv}[\mathcal A, \mathcal I]$ is negligible.

### Challenge Response Protocols

> [!algorithm] MAC Challenge-Response Protocol
> Let $\mathcal I = (S_{\text{mac}}, V_{\text{mac}})$ be a MAC defined over $(\mathcal K, \mathcal M, \mathcal T)$. The challenge-response protocol $\text{ChalResp}_{mac} = (G, P, V)$, works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal K$, and output $sk := k$ and $vk := k$.
> - Algorithm $P$ with input $sk = k$, algorithm $V$ with input $vk = k$, interact as follows:
> 	1. $V$ chooses a random $c \xleftarrow{R} \mathcal M$, and sends $c$ to $P$;
> 	2. $P$ computes $t \xleftarrow{R} S_{\text{mac}}(k, c)$, and sends $t$ to $V$;
> 	3. $V$ outputs $V_{\text{mac}}(k, c, t)$.
> The random $c$ is called the **challenge** while $t$ is called the **response**. Clearly $vk$ must be kept secret for the protocol to be secure.

> [!theorem]
> Suppose $\mathcal I$ is a secure MAC system, and that the size of the message space, $|\mathcal M|$, is super-poly. Then ID protocol $\text{ChalResp}_{mac}$ is weakly secure against active attacks.

> [!algorithm] Signature Challenge-Response Protocol
> Replace the MAC with a signature scheme $(G, S_{sig}, V_{sig})$ defined over $(\mathcal M, \mathcal T)$. The main change is that prover responds to the challenge using algorithm $S_{sig}$ and the secret signing key. The verifier checks the response using algorithm $V_{sig}$ and the public verification key. We refer to the resulting protocol as $\text{ChalResp}_{sig}$.

> [!theorem]
> Assume $\mathcal S$ is a secure signature scheme, and that the size of the message space, $|\mathcal M|$, is super-poly. Then $\text{ChalResp}_{sig}$ is secure against active attacks.

