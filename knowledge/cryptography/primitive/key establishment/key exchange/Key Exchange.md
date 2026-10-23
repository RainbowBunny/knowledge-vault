Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023: https://toc.cryptobook.us/ (Ch. 10: Attack Game 10.1 and Definition 10.1 in §10.1, trapdoor functions in §10.2, Diffie–Hellman key exchange in §10.4, Attack Games 10.4–10.6 in §10.5). Copy of Ch. 10, §10.1–10.4: https://www.cis.upenn.edu/~sga001/classes/cis331f19/resources/bs_ch10.pdf. `⚠️ CLAUDE – verify:` §10.5 lies past every copy of the book that could be read, so the DL, CDH and DDH tables redraw the transcription this note already had; check them against Attack Games 10.4–10.6.
- `[KL]` — J. Katz, Y. Lindell, _Introduction to Modern Cryptography_, 2nd ed., CRC Press, 2014, §10.3: the experiment $\mathsf{KE}^{\mathsf{eav}}_{\mathcal A, \Pi}(n)$. `⚠️ CLAUDE – verify:` the book could not be read; the experiment and its definition were checked in lecture slides that cite §10.3: https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/imc/2024/diffie-hellman.pdf

| Term                                            | Reference                                                       |                    |
| ----------------------------------------------- | --------------------------------------------------------------- | ------------------ |
| Attack Game 10.1 (Anonymous key exchange)       | [[#Anonymous Key Exchange\|anonymous key exchange]]             | $\text{AnonKEadv}$ |
| Attack Game 10.4 (Discrete logarithm)           | [[#Discrete Logarithm\|discrete logarithm]]                     | $\text{DLadv}$     |
| Attack Game 10.5 (Computational Diffie-Hellman) | [[#Computational Diffie-Hellman\|computational Diffie-Hellman]] | $\text{CDHadv}$    |
| Attack Game 10.6 (Decisional Diffie-Hellman)    | [[#Decisional Diffie-Hellman\|decisional Diffie-Hellman]]       | $\text{DDHadv}$    |

## Anonymous Key Exchange

> [!definition] Anonymous Key Exchange Problem
> Alice and Bob want to communicate online, adversary can eavesdrop their communication, thus they want to generate a **shared secret unknown to the adversary**. The anonymity in this problem is that there is no guarantee for Alice and Bob that they are talking to each other.

> [!definition] Key Exchange Protocol
> A **key exchange protocol** is a pair of probabilistic machine $(A, B)$ that take turns in sending messages to each other. At the end of the protocol, when both machine terminate, they both obtain the same value $k$.

> [!definition] Protocol Transcript
> A **protocol transcript** $T_P$ is the sequence of messages exchanged between the parties in one execution of the protocol.

> [!definition] Parameters
> - $P = (A, B)$: a key exchange protocol. $k$: the key both machines output. $T_P$: the transcript of the run.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]].

> [!definition] Security against an Eavesdropper
> ### Scope
> A key exchange protocol $P = (A, B)$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ sees the transcript $T_P$ of one honest run of $P$ and nothing else; it cannot send, change or drop messages.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — none: $\mathcal A$ speaks once, after the run has ended.
>
> ---
> ### Experiment
> A search game: one branch; the challenger compares the guess with the key in the last row. `[BS Attack Game 10.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | runs the protocol between $A$ and $B$<br>$k$: the shared key<br>$T_P$: the transcript | $\xrightarrow{\ T_P\ }$ | |
> | 2 | | $\xleftarrow{\ \hat k\ }$ | outputs a guess $\hat k$ for $k$ |
> | 3 | checks whether $\hat k = k$ | | |
>
> **Goal** — $\mathcal A$ wins iff:
> - $\hat k = k$.
>
> ---
> ### Property
> $$\text{AnonKEadv}[\mathcal A, P] = \Pr[\hat k = k].$$
> - $P$ is **secure against an eavesdropper** if $\text{AnonKEadv}[\mathcal A, P]$ is negligible for every efficient $\mathcal A$ `[BS Def 10.1]`.
>
> It is a *search* game, see [[Security Game]].

> [!remark] Why this definition is weak
> `[BS §10.1]` calls it extremely weak, for three reasons:
> - First, we assume the adversary is unable to tamper with messages.
> - Second, we only guarantee that the adversary cannot guess $k$ in its entirety. This does not rule out the possibility that the adversary can guess, say, half the bits of $k$. If we are to use $k$ as a secret session key, the property we would really like is that $k$ is indistinguishable from a truly random key — the game in [[#Real-or-Random Key]].
> - Third, the protocol provides no assurance of the identities of the participants.
>
> `[BS]` strengthens the definition in Chapter 21, authenticated key exchange.

### Real-or-Random Key

> [!definition] Parameters
> - $P = (A, B)$, $k$, $T_P$: as above. $\mathcal K$: the key space of $P$; $\{0, 1\}^n$ in `[KL]`.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]].

> [!definition] Real-or-Random Security against an Eavesdropper
> ### Scope
> A key exchange protocol $P = (A, B)$ with key space $\mathcal K$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ sees the transcript $T_P$ of one honest run and a candidate key $\hat k$; it cannot send, change or drop messages.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — none: $\mathcal A$ speaks once, after the run has ended.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 1 only, **Game 0** (the real key) and **Game 1** (a uniform key). `[KL §10.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | runs the protocol between $A$ and $B$<br>$k$: the shared key<br>$T_P$: the transcript<br>**Game 0**: $\hat k \leftarrow k$<br>**Game 1**: $\hat k \xleftarrow{\$} \mathcal K$ | $\xrightarrow{\ T_P,\, \hat k\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{eav}}_P(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - $P$ is **secure in the presence of an eavesdropper** if $\mathsf{Adv}^{\mathsf{eav}}_P(\mathcal A)$ is negligible for every efficient $\mathcal A$ `[KL §10.3]`.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[KL §10.3]` writes the experiment $\mathsf{KE}^{\mathsf{eav}}_{\mathcal A, \Pi}(n)$: both parties run $\Pi$ on $1^n$; a uniform bit $b$ selects the real key ($b = 0$) or a uniform $\hat k \in \{0, 1\}^n$ ($b = 1$); $\mathcal A$ gets the transcript and $\hat k$, outputs $b'$, and the experiment outputs $1$ iff $b' = b$. Security there is $\Pr[\mathsf{KE}^{\mathsf{eav}}_{\mathcal A, \Pi}(n) = 1] \leq 1/2 + \mathsf{negl}(n)$. That bit-guessing advantage $|\Pr[b' = b] - 1/2|$ is half of $\mathsf{Adv}^{\mathsf{eav}}_P$, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].
> - Real-or-random security implies security in the sense of Attack Game 10.1 when $|\mathcal K|$ is super-polynomial: from a guesser $\mathcal A$, a distinguisher runs $\mathcal A$ on $T_P$ and outputs $1$ iff the guess equals $\hat k$. It outputs $1$ with probability $\text{AnonKEadv}[\mathcal A, P]$ in Game 0 and $1/|\mathcal K|$ in Game 1.

## Construction

### Based on Trapdoor Function Scheme

> [!algorithm] Key Exchange using a One-way Trapdoor Function Scheme
> - Alice computes $(pk, sk) \xleftarrow{R} \mathsf{KeyGen}()$, and sends $pk$ to Bob.
> - Upon receiving $pk$ from Alice, Bob computes $x \xleftarrow{R} \mathcal X$ and $y \leftarrow F(pk, x)$, and sends $y$ to Alice.
> - Upon receiving $y$ from Bob, Alice computes $x \leftarrow I(sk, y)$.
>
> Both now hold $x$, the shared key. `[BS §10.2]`

> [!remark] Notation in the literature
> `[BS §10.2]` writes the trapdoor function scheme as $(G, F, I)$ and the first step as $(pk, sk) \xleftarrow{R} G()$. The vault calls key generation $\mathsf{KeyGen}$ ([[Note Layouts]] § *Game form*).

## Key Exchange

> [!algorithm] Generic Key Exchange Protocol
> The protocol makes use of two functions $E$ and $F$. Alice chooses a random secret $\alpha$, computes $E(\alpha)$, and sends $E(\alpha)$ to Bob over an insecure channel. Likewise, Bob chooses a random secret $\beta,$ computes $E(\beta),$ and sends $E(\beta)$ to Alice over an insecure channel. Alice and Bob both somehow compute a shared key $F(\alpha, \beta)$. In this high level description, $E$ and $F$ are some functions that should satisfy the following properties:
> 1. $E$ should be easy to compute;
> 2. Given $\alpha$ and $E(\beta),$ it should be easy to compute $F(\alpha, \beta)$;
> 3. Given $E(\alpha)$ and $\beta,$ it should be easy to compute $F(\alpha, \beta)$;
> 4. Given $E(\alpha)$ and $E(\beta),$ it should be hard to compute $F(\alpha, \beta)$.

### Diffie-Hellman

> [!algorithm] Diffie-Hellman Key Exchange Protocol
> We assume that the description of $\mathbb G$, including $g \in \mathbb G$ and $q$, is a system parameter that is generated once and for all at system setup time and shared by all parties involved. The protocol runs as follows:
> 1. Alice computes $\alpha \xleftarrow{R} \mathbb Z_q$ and $u \leftarrow g^{\alpha}$, and sends $u$ to Bob.
> 2. Bob computes $\beta \xleftarrow{R} \mathbb Z_q$ and $v \leftarrow g^{\beta}$, and sends $v$ to Alice.
> 3. Upon receiving $v$ from Bob, Alice computes $w \leftarrow v^{\alpha}$.
> 4. Upon receiving $u$ from Alice, Bob computes $w \leftarrow u^{\beta}$.
> 
> The secret shared by Alice and Bob is $$w = v^{\alpha} = g^{\alpha \beta} = u^{\beta}.$$
> `[BS §10.4]`

> [!definition] Discrete Logarithm
> For a fixed element $g \in \mathbb G,$ different from 1, the function from $\mathbb Z_q$ to $\mathbb G$ that sends $\alpha \in \mathbb Z_q$ to $g^{\alpha} \in \mathbb G$ is called the **discrete exponentiation function**. This function is one-to-one and onto, and its inverse function is called the **discrete logarithm function**, and is usually denoted $\text{Dlog}_g$; thus, for $u \in \mathbb G, \text{Dlog}_g(u)$ is the unique $\alpha \in \mathbb Z_q$ such that $u = g^{\alpha}$. The value $g$ is called the **base** of the discrete logarithm.

### Discrete Logarithm

> [!definition] Parameters
> - $\mathbb G$: a cyclic group of prime order $q$ generated by $g \in \mathbb G$. Its description includes $q$ and $g$.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]].

> [!definition] Discrete Logarithm Assumption
> ### Scope
> The group $\mathbb G$ of Parameters and the adversary class $\mathbb A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives the description of $\mathbb G$ and one instance $u$; no oracle.
> - **Promise** — none: $u$ is uniform in $\mathbb G$.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — none: $\mathcal A$ speaks once.
>
> ---
> ### Experiment
> A search game: one branch; the challenger checks the answer in the last row. `[BS Attack Game 10.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\alpha \xleftarrow{\$} \mathbb Z_q$<br>$u \leftarrow g^{\alpha}$ | $\xrightarrow{\ \mathbb G,\, u\ }$ | |
> | 2 | | $\xleftarrow{\ \hat\alpha\ }$ | outputs some $\hat\alpha \in \mathbb Z_q$ |
> | 3 | checks whether $\hat\alpha = \alpha$ | | |
>
> **Goal** — $\mathcal A$ wins iff:
> - $\hat\alpha = \alpha$.
>
> ---
> ### Property
> $$\text{DLadv}[\mathcal A, \mathbb G] = \Pr[\hat\alpha = \alpha].$$
> - The **discrete logarithm (DL) assumption** holds for $\mathbb G$ if $\text{DLadv}[\mathcal A, \mathbb G]$ is negligible for every efficient $\mathcal A$ `[BS §10.5]`.
>
> It is a *search* game, see [[Security Game]].

> [!remark] Notation in the literature
> `[BS Attack Games 10.4–10.6]` give the description of $\mathbb G$, with $q$ and $g$, to both the challenger and the adversary as an input. Here the adversary takes no input, so the challenger sends the description in row 1: the label $\mathbb G$ on the arrow stands for it, in this game and in the CDH and DDH games below.

> [!remark]
> We say that $g^{\alpha}$ is an **instance** of the **discrete logarithm (DL) problem (for $\mathbb G$)**, and that $\alpha$ is a solution to this problem instance. The DL assumption asserts that there is no efficient algorithm that can effectively solve the DL problem for $\mathbb G$.

### Computational Diffie-Hellman

> [!definition] Parameters
> - $\mathbb G$, $q$, $g$: as in the DL game.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]].

> [!definition] Computational Diffie-Hellman Assumption
> ### Scope
> The group $\mathbb G$ of Parameters and the adversary class $\mathbb A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives the description of $\mathbb G$ and one instance $(u, v)$; no oracle.
> - **Promise** — none: $u$ and $v$ are independent and uniform in $\mathbb G$.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — none: $\mathcal A$ speaks once.
>
> ---
> ### Experiment
> A search game: one branch; the challenger checks the answer in the last row. `[BS Attack Game 10.5]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\alpha \xleftarrow{\$} \mathbb Z_q$<br>$\beta \xleftarrow{\$} \mathbb Z_q$<br>$u \leftarrow g^{\alpha}$<br>$v \leftarrow g^{\beta}$<br>$w \leftarrow g^{\alpha\beta}$ | $\xrightarrow{\ \mathbb G,\, u,\, v\ }$ | |
> | 2 | | $\xleftarrow{\ \hat w\ }$ | outputs some $\hat w \in \mathbb G$ |
> | 3 | checks whether $\hat w = w$ | | |
>
> **Goal** — $\mathcal A$ wins iff:
> - $\hat w = w$.
>
> ---
> ### Property
> $$\text{CDHadv}[\mathcal A, \mathbb G] = \Pr[\hat w = w].$$
> - The **computational Diffie-Hellman (CDH) assumption** holds for $\mathbb G$ if $\text{CDHadv}[\mathcal A, \mathbb G]$ is negligible for every efficient $\mathcal A$ `[BS §10.5]`.
>
> It is a *search* game, see [[Security Game]].

> [!remark]
> We say that $(g^{\alpha}, g^{\beta})$ is an **instance** of the **computational Diffie-Hellman (CDH) problem**, and that $g^{\alpha \beta}$ is a solution to this problem instance. The CDH assumption asserts that there is no efficient algorithm that can be effectively solve the CDH problem for $\mathbb G$.

### Decisional Diffie-Hellman

> [!definition] Parameters
> - $\mathbb G$, $q$, $g$: as in the DL game.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]].

> [!definition] Decisional Diffie-Hellman Assumption
> ### Scope
> The group $\mathbb G$ of Parameters and the adversary class $\mathbb A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives the description of $\mathbb G$ and one triple $(u, v, w)$; no oracle.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — none: $\mathcal A$ speaks once.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 1 only, **Game 0** (a DH-triple) and **Game 1** (a random triple). `[BS Attack Game 10.6]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\alpha \xleftarrow{\$} \mathbb Z_q$<br>$\beta \xleftarrow{\$} \mathbb Z_q$<br>$\gamma \xleftarrow{\$} \mathbb Z_q$<br>$u \leftarrow g^{\alpha}$<br>$v \leftarrow g^{\beta}$<br>**Game 0**: $w \leftarrow g^{\alpha\beta}$<br>**Game 1**: $w \leftarrow g^{\gamma}$ | $\xrightarrow{\ \mathbb G,\, u,\, v,\, w\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{DDHadv}[\mathcal A, \mathbb G] = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - The **decisional Diffie-Hellman (DDH) assumption** holds for $\mathbb G$ if $\text{DDHadv}[\mathcal A, \mathbb G]$ is negligible for every efficient $\mathcal A$ `[BS §10.5]`.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> `[BS Attack Game 10.6]` computes both $w_0 \leftarrow g^{\alpha\beta}$ and $w_1 \leftarrow g^{\gamma}$, sends $(u, v, w_b)$ in Experiment $b$, and calls the adversary's bit $\hat b$; its event $W_b$, that $\mathcal A$ outputs $1$ in Experiment $b$, is $\mathsf{Expt}_b(\mathcal A) = 1$ here. A bit-guessing form $|\Pr[b' = b] - 1/2|$ with a uniform $b$ is half of $\text{DDHadv}$, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].

> [!remark]
> For $\alpha, \beta, \gamma \in \mathbb Z_q,$ we call $(g^\alpha, g^\beta, g^\gamma)$ a **DH-triple** if $\gamma = \alpha \beta$; otherwise, we call it a **non-DH-triple**. The DDH assumption says that there is no efficient algorithm that can effectively distinguish between random DH-triples and random triples.

### Random Self-Reducibility

> [!theorem]
> Consider a specific cyclic group $\mathbb G$ of prime order $q$ generated by $g \in \mathbb G$. Suppose $\mathcal A$ is an efficient algorithm with the following property: If $u \in \mathbb G$ is chosen at random, then $P[\mathcal A(u) = \text{Dlog}_g(u)] = \epsilon,$ where the probability is over the random choice of $u$ and the random choices made by $\mathcal A$. Then there is an efficient algorithm $\mathcal B$ with the following property: for all $u \in \mathbb G,$ algorithm $\mathcal B$ either outputs `fail` or $\text{Dlog}_g(u),$ and it outputs the latter with probability $\epsilon,$  where now the probability is only over the random choices made by $\mathcal B$.

> [!algorithm] Proof of Theorem
> Algorithm $\mathcal B$
> Input: $u \in \mathbb G$
> Output: $\text{Dlog}_g(u)$ or `fail`
> 1. $\sigma \xleftarrow R \mathbb Z_q$
> 2. $u_1 \leftarrow u \cdot g^\sigma \in \mathbb G$
> 3. $\alpha_1 \leftarrow \mathcal A(u_1)$
> 4. If $g^{\alpha_1} \neq u_1$ then `fail`, else output $\alpha \leftarrow \alpha_1 - \sigma$.

> [!remark] Importance of self reducibility
> If a problem is hard in the worst case, and we can prove self reducibility then the problem is hard on average.

