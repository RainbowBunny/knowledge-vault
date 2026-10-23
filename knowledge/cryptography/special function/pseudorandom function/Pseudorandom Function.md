Reference:
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, v0.6: https://toc.cryptobook.us/ (Ch. 4, §4.4: Attack Games 4.2 and 4.3, Definition 4.2; Ch. 6, §6.4: prefix-free PRFs; Ch. 8: Attack Game 8.4).
- `[BR x]` — M. Bellare, P. Rogaway, _Introduction to Modern Cryptography_, Ch. 3 "Pseudorandom Functions": https://www.cs.ucdavis.edu/~rogaway/classes/227/fall03/book/prf.pdf (Definition 3.6, Lemma 3.17).
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

| Term                                             | Reference                                                    |                             |
| ------------------------------------------------ | ------------------------------------------------------------ | --------------------------- |
| Attack Game 4.2 (PRF)                            | [[Pseudorandom Function#Definition\|secure PRF]]                                | $\text{PRFadv}$             |
| Attack Game 4.3 (Permutation vs. Function)       | [[#Permutation vs. Function\|permutation vs function]]       | $\text{PFadv}$              |
| Prefix Free PRF                                  | [[#Secure Prefix-free PRF\|secure prefix-free PRF]]          | $\text{PRF}^{pf}\text{adv}$ |
| Attack Game 8.4 (PRF in the Random Oracle Model) | [[#PRF in the Random Oracle Model\|random oracle model PRF]] | $\text{PRF}^{ro}\text{adv}$ |

## Definition

> [!definition] Pseudo-Random Function
> A **pseudo-random function (PRF)** $F$ is a deterministic algorithm that has two inputs: a key $k$ and an **input data block** $x$; its output $y = F(k, x)$ is called an **output data block**. As usual, there are associated, finite spaces: the key space $\mathcal K$, in which $k$ lies, the input space $\mathcal X$, in which $x$ lies, and the output space $\mathcal Y$, in which $y$ lies. We say that $F$ is **defined over** $(\mathcal K, \mathcal X, \mathcal Y)$.

> [!algorithm] Pseudo-Random Function (Mathematical details)
> A **pseudo-random function** consists of an algorithm $F$, along with three families of spaces with system parameterization $P$: $$K = \{\mathcal K_{\lambda, \Lambda}\}_{\lambda, \Lambda}, X = \{\mathcal X_{\lambda, \Lambda}\}_{\lambda, \Lambda}, Y = \{\mathcal Y_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ such that
> 1. $K, X$, and $Y$ are efficiently recognizable.
> 2. $K$ and $Y$ are efficiently sampleable.
> 3. Algorithm $F$ is a deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $x \in \mathcal X_{\lambda, \Lambda}$, runs in time bounded by a polynomial in $\lambda$, and outputs an element of $\mathcal Y_{\lambda, \Lambda}$.

### Secure PRF

Specializes [[Special Functions#Pseudorandom]].

> [!definition] Parameters
> - $F$: a PRF defined over $(\mathcal K, \mathcal X, \mathcal Y)$, as above.
> - $\mathrm{Funs}[\mathcal X, \mathcal Y]$: the set of all functions from $\mathcal X$ to $\mathcal Y$.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]]. $Q$: a bound on the number of evaluation queries.

> [!definition] Secure PRF
> ### Scope
> A PRF $F$ defined over $(\mathcal K, \mathcal X, \mathcal Y)$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — an evaluation oracle for $f$, which is $F(k, \cdot)$ in Game 0 and a uniformly random function in Game 1. $\mathcal A$ never sees $k$.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — adaptive: each query may depend on the answers to the earlier ones.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 1 only, **Game 0** (the PRF) and **Game 1** (a random function). `[BS Attack Game 4.2]`; `[BR Def 3.6]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$<br>**Game 0**: $f \leftarrow F(k, \cdot)$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X, \mathcal Y]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Evaluation queries** (repeated, adaptive, at most $Q$ times): sends $x_i \in \mathcal X$ |
> | | $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{PRFadv}[\mathcal A, F] = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - $F$ is a **secure PRF** if $\text{PRFadv}[\mathcal A, F]$ is negligible for every $\mathcal A \in \mathbb A$ `[BS Def 4.2]`.
> - The theorems in this note bound $\text{PRFadv}[\mathcal A, F]$ for an $\mathcal A$ that makes at most $Q$ queries.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[BS Attack Game 4.2]` names the branches Experiment 0 and Experiment 1, samples $k$ only in Experiment 0, calls the output bit $\hat b$, and writes $W_b$ for the event that $\mathcal A$ outputs $1$ in Experiment $b$, so $\Pr[W_b] = \Pr[\mathsf{Expt}_b(\mathcal A) = 1]$. Sampling $k$ in Game 1 as well changes nothing, since it is not used there.
> - The bit-guessing form $\text{PRFadv}^*[\mathcal A, F] = |\Pr[\hat b = b] - 1/2|$, with a hidden uniform $b$, is exactly half of $\text{PRFadv}[\mathcal A, F]$; this note uses the difference.
> - `[BR Def 3.6]` writes the real game as $\mathbf{Exp}^{\mathrm{prf}\text{-}1}_F(A)$ (a uniform key $K$, oracle $F_K$), the random one as $\mathbf{Exp}^{\mathrm{prf}\text{-}0}_F(A)$ (oracle $g \xleftarrow{\$} \mathrm{Rand}(D, R)$), and $\mathbf{Adv}^{\mathrm{prf}}_F(A) = \Pr[\mathbf{Exp}^{\mathrm{prf}\text{-}1}_F(A) = 1] - \Pr[\mathbf{Exp}^{\mathrm{prf}\text{-}0}_F(A) = 1]$, without the absolute value. Its adversary is an oracle machine, the same single stateful machine as here.

### Permutation vs. Function

> [!definition] Parameters
> - $\mathcal X$: a finite set, $N = |\mathcal X|$.
> - $\mathrm{Perms}[\mathcal X]$: the set of all permutations of $\mathcal X$. $\mathrm{Funs}[\mathcal X, \mathcal X]$: the set of all functions from $\mathcal X$ to $\mathcal X$.
> - $Q$: a bound on the number of queries.

> [!definition] Permutation vs. Function
> ### Scope
> A finite set $\mathcal X$ and any [[Adversary]] $\mathcal A$. There is no primitive and no key.
>
> ---
> ### Condition
> - **Access** — an evaluation oracle for $f$, a random permutation in Game 0 and a random function in Game 1.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A$ that makes at most $Q$ queries, efficient or not: the bound in the theorem below is information-theoretic.
> - **Adaptivity** — adaptive: each query may depend on the answers to the earlier ones.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 1 only, **Game 0** (a random permutation) and **Game 1** (a random function). `[BS Attack Game 4.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $f \xleftarrow{\$} \mathrm{Perms}[\mathcal X]$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X, \mathcal X]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Evaluation queries** (repeated, adaptive, at most $Q$ times): sends $x_i \in \mathcal X$ |
> | | $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{PFadv}[\mathcal A, \mathcal X] = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - The theorem below bounds it by $Q^2 / 2N$ for every $\mathcal A$ that makes at most $Q$ queries.

> [!remark] Notation in the literature
> - `[BS Attack Game 4.3]` names the branches Experiment 0 and Experiment 1 and writes $W_b$ for the event that $\mathcal A$ outputs $1$ in Experiment $b$; the answers $y_i = f(x_i)$ lie in $\mathcal X$.
> - `[BR Lemma 3.17]` compares a random function with a random permutation on $\{0, 1\}^n$ and gets the sharper bound $q(q - 1) / 2^{n + 1}$ for $q$ queries.

> [!theorem]
> Let $\mathcal X$ be a finite set of size $N$. Let $\mathcal A$ be an adversary that makes at most $Q$ queries to its challenger. Then $$\text{PFadv}[\mathcal A, \mathcal X] \leq Q^2 / 2N.$$

### PRF in the Random Oracle Model

> [!definition] Parameters
> - $F$: a PRF defined over $(\mathcal K, \mathcal X, \mathcal Y)$ that uses a hash function $H$ defined over $(\mathcal M, \mathcal T)$ as an oracle.
> - $\mathcal O$: the random oracle that replaces $H$, a uniform element of $\mathrm{Funs}[\mathcal M, \mathcal T]$.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]]. $Q_{ro}$: a bound on the number of $\mathcal O$-queries.

> [!definition] PRF in the Random Oracle Model
> ### Scope
> A PRF $F$ whose hash function $H$ is modeled as a random oracle, and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — two oracles: $F$-queries, answered by $f$, and $\mathcal O$-queries, answered by the random oracle. In Game 1, $f$ is independent of $\mathcal O$.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — both kinds of query are adaptive and may be interleaved in any order.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 1 only, **Game 0** ($F$ keyed with a random key, over the random oracle) and **Game 1** (a random function). `[BS Attack Game 8.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathcal O \xleftarrow{\$} \mathrm{Funs}[\mathcal M, \mathcal T]$<br>$k \xleftarrow{\$} \mathcal K$<br>**Game 0**: $f \leftarrow F^{\mathcal O}(k, \cdot)$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X, \mathcal Y]$ | | |
> | 2 | | $\xleftarrow{\ x\ }$ | **$F$-queries** (repeated, adaptive): sends $x \in \mathcal X$ |
> | | $y \leftarrow f(x)$ | $\xrightarrow{\ y\ }$ | |
> | 3 | | $\xleftarrow{\ m\ }$ | **$\mathcal O$-queries** (repeated, adaptive, at most $Q_{ro}$ times): sends $m \in \mathcal M$ |
> | | $t \leftarrow \mathcal O(m)$ | $\xrightarrow{\ t\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{PRF}^{ro}\text{adv}[\mathcal A, F] = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - $F$ is a **secure PRF in the random oracle model** if $\text{PRF}^{ro}\text{adv}[\mathcal A, F]$ is negligible for every $\mathcal A \in \mathbb A$.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> `[BS Attack Game 8.4]` names the branches Experiment 0 and Experiment 1, samples $k$ only in Experiment 0, and writes $W_b$ for the event that $\mathcal A$ outputs $1$ in Experiment $b$. Its two kinds of query are listed together; rows 2 and 3 above may come in any order.

> [!theorem]
> If $\mathcal K$ is large then $F_{pre}$ is a secure PRF when $H$ is modeled as a random oracle.
> In particular, if $\mathcal A$ is a [[#PRF in the Random Oracle Model|random oracle model PRF]] adversary $\mathcal A$, that makes at most $Q_{ro}$ oracle queries, then $$\text{PRF}^{ro}\text{adv}[\mathcal A, F_{pre}] \leq Q_{ro} / |\mathcal K|$$

## Prefix-free PRF

> [!remark] Goal
> Given a secure PRF on short inputs construct a secure PRF on long inputs.

### Secure Prefix-free PRF

> [!definition] Parameters
> - $F$: a PRF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y)$; $\mathcal X^{\leq \ell}$ is the set of strings over $\mathcal X$ of length at most $\ell$, and $\mathcal X^{\leq \ell}_{> 0}$ its non-empty strings.
> - $\mathbb A$: the class of efficient prefix-free [[Adversary|adversaries]]. $Q$: a bound on the number of queries.

> [!definition] Secure Prefix-free PRF
> ### Scope
> A PRF $F$ defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y)$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — the evaluation oracle of the [[#Secure PRF|secure PRF game]].
> - **Promise** — $\mathcal A$ is a **prefix-free adversary**: all of its queries are non-empty strings over $\mathcal X$ of length at most $\ell$, no one of which is a proper prefix of another.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — adaptive, as in the secure PRF game.
>
> ---
> ### Experiment
> The [[#Secure PRF|secure PRF game]] on the input space $\mathcal X^{\leq \ell}$, played by a prefix-free adversary: two branches that differ in row 1 only. `[BS §6.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$<br>**Game 0**: $f \leftarrow F(k, \cdot)$<br>**Game 1**: $f \xleftarrow{\$} \mathrm{Funs}[\mathcal X^{\leq \ell}, \mathcal Y]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Evaluation queries** (repeated, adaptive, at most $Q$ times): sends $x_i \in \mathcal X^{\leq \ell}_{> 0}$ that is not a proper prefix of an earlier query and has no earlier query as a proper prefix |
> | | $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{PRF}^{pf}\text{adv}[\mathcal A, F] = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - $F$ is a **prefix-free secure PRF** if $\text{PRF}^{pf}\text{adv}[\mathcal A, F]$ is negligible for every efficient prefix-free adversary $\mathcal A$.

> [!remark] Notation in the literature
> `[BS §6.4]` defines no new attack game: a prefix-free adversary plays Attack Game 4.2 against $F$, and $\text{PRF}^{pf}\text{adv}[\mathcal A, F]$ is its advantage there.

## Construction

### Construction from Block Cipher

> [!theorem] PRF Switching Lemma
> Let $\mathcal E = (E, D)$ is a block cipher defined over $(\mathcal K, \mathcal X)$, and let $N := |\mathcal X|$. Let $\mathcal A$ be an adversary that makes at most $Q$ queries to its challenger. Then $$|\text{BCadv}[\mathcal A, \mathcal E] - \text{PRFadv}[\mathcal A, E]| \leq Q^2 / 2N$$

> [!corollary]
> Let $\mathcal E = (E, D)$ be a block cipher defined over $(\mathcal K, \mathcal X)$, and assume that $N = |\mathcal X|$ is super-poly. Then $\mathcal E$ is a secure block cipher if and only if $E$ is a secure PRF.

### Construction from PRG

> [!algorithm] Tree Construction
> Given a PRG $G$ defined over $(\mathcal S, \mathcal S^2)$ that we can write as $G(s) = (G_0(s), G_1(s))$, we shall build a PRF $F$ with key space $\mathcal S$, input space $\{0, 1\}^\ell$ (where $\ell$ is an arbitrary, poly-bounded value), and output space $\mathcal S$. 
> Define the algorithm $G^*$, that takes as input $s \in \mathcal S$ and $x = (a_1, \dots, a_n) \in \{0, 1\}^n$, where $a_i \in \{0, 1\}$ for $i = 1, \dots, n$, and outputs an element $t \in S$, computes as follows:
> 1. $t \leftarrow s$
> 2. For $i \leftarrow 1$ to $n$ do $t \leftarrow G_{a_i}(t)$.
> 3. Output $t$. 
> 
> For $s \in \mathcal S$ and $x \in \{0, 1\}^\ell$, we define $$F(s, x) = G^*(s, x).$$ 
> 
> We shall call the PRF $F$ derived from $G$ in this way the **tree construction**.

> [!theorem]
> If $G$ is a secure PRG, then the PRF $F$ obtained from $G$ using the tree construction is a secure PRF.
> 
> In particular, for every [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal A$ with respect to $F$, and which makes at most $Q$ queries to its challenger, there exists a [[Pseudorandom Generators#Secure PRG|secure PRG]] adversary $\mathcal B$ with respect to $G$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRFadv}[\mathcal A, F] = \ell Q \cdot \text{PRGadv}[\mathcal B, G].$$

### Construction from DDH

> [!algorithm] Simple PRF from DDH
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \in \mathbb G$. Let $H: \mathcal M \rightarrow \mathbb G$ be a hash function, which we shall model as a random oracle. Let $F$ be the PRF defined over $(\mathbb Z_q, \mathcal M, \mathbb G)$ as follows: $$F(k, m) = H(m)^k \quad \text{for } k \in \mathbb Z_q, m \in \mathcal M.$$
> 

> [!theorem]
> $F$ is a secure PRF in the random oracle model for $H$ under the DDH assumption for $\mathbb G$.
> In particular, for every [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal A$ attacking $F$ as a PRF, there exists a [[Key Exchange#Decisional Diffie-Hellman|decisional Diffie-Hellman]] adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{PRF}^{ro}\text{adv}[\mathcal A, F] \leq \text{DDHadv}[\mathcal B, \mathbb G] + 1/q.$$

### Construction from CDH

> [!algorithm] Simple PRF from CDH
> Let $H': \mathcal M \times \mathbb G \rightarrow \mathcal Y$ be a hash function and $H$ is the [[#Construction from DDH|PRF from DDH]], which we again model as a random oracle. Let $F'$ be the PRF defined over $(\mathbb Z_q, \mathcal M, \mathcal Y)$ as follows: $$F'(k, m) = H'(m, H(m)^k) \quad \text{for } k \in \mathbb Z_q, m \in \mathcal M.$$

> [!theorem]
> $F'$ is a [[Pseudorandom Function#Definition|secure PRF]] assuming [[Key Exchange#Computational Diffie-Hellman|computational Diffie-Hellman]] for $\mathbb G$, and when $H$ and $H'$ are modeled as random oracles.

## Prefix-free PRF Construction

### Variable Length Tree Construction

> [!algorithm] Variable Length Tree Construction
> Let $G$ be a PRG defined over $(\mathcal S, \mathcal S^2)$, and let $G^*$ be as defined above. For any poly-bounded value $\ell$ we define the PRF $\tilde{F}$, with key space $\mathcal S$, input space $\{0, 1\}^{\leq \ell}$, and output space $\mathcal S$, as follows: for $s \in \mathcal S$ and $x \in \{0, 1\}^{\leq \ell}$, we define $$\tilde{F}(s, x) = G^*(s, x).$$

> [!remark] Extension Attack
> $\tilde{F}$ is not a secure PRF. The reason is that there is a trivial **extension attack**. Suppose $u, v \in \{0, 1\}^{\ell}$ such that $u$ is a proper prefix of $v$; that is, $v = u || w$ for some non-empty string $w$. Then given $u$ and $v$, along with $y = \tilde{F}(s, u)$, we can easily compute $F(s, v)$ as $G^*(y, w)$. Of course, for a truly random function, we could not predict its value at $v$, given its value at $u$, and so it is easy to distinguish $\tilde{F}(s, \cdot)$ from a random function.

> [!theorem]
> If $G$ is a secure PRG, then the variable length tree construction $\tilde{F}$ derived from $G$ is a prefix-free secure PRF.
> 
> In particular, for every prefix-free [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal A$ with respect to $\tilde{F}$, and which makes at most $Q$ queries to its challenger, there exists a [[Pseudorandom Generators#Secure PRG|secure PRG]] adversary $\mathcal B$ with respect to $G$, where $\mathcal B$ is an elementary wrapper $\mathcal A$, such that $$\text{PRF}^{pf}\text{adv}[\mathcal A, \tilde{F}] = \ell Q \cdot \text{PRGadv}[\mathcal B, G].$$ 

### CBC Construction

> [!algorithm] CBC Construction
> Let $F$ be a PRF that maps $n$-bit inputs to $n$-bit outputs. In symbols, $F$ is defined over $(\mathcal K, \mathcal X, \mathcal X)$ where $\mathcal X = \{0, 1\}^n$. For any poly-bounded value $\ell$, we build a new PRF, denoted $F_{CBC}$, that maps message in $\mathcal X^{\leq \ell}$ to outputs in $\mathcal X$. The function $F_{CBC}$, works as follows:
> 
> ---
> **Input**: $k \in \mathcal K$ and $m = (a_1, \dots, a_v) \in \mathcal X^{\leq \ell}$ for some $v \in \{0, \dots, \ell\}$
> **Output**: A tag in $\mathcal X$
> 1. $t \leftarrow 0^n$
> 2. For $i \leftarrow 1$ to $v$ do: $$t \leftarrow F(k, a_i \oplus t)$$
> 3. Output $t$

> [!theorem]
> Let $F$ be a secure PRF defined over $(\mathcal K, \mathcal X, \mathcal X)$ where $\mathcal X = \{0, 1\}^n$ and $|\mathcal X| = 2^n$ is super-poly. Then for any poly-bounded value $\ell$, we have that $F_{CBC}$ is a prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal X)$.
> 
> In particular, for every [[Pseudorandom Function#Secure Prefix-free PRF|secure prefix-free PRF]] adversary $\mathcal A$ that attacks $F_{CBC}$, and issues at most $Q$ queries, there exists a [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal B$ that attacks $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRF}^{pf}\text{adv}[\mathcal A, F_{CBC}] \leq \text{PRFadv}[\mathcal B, F] + \frac{(Q \ell)^2}{2 |\mathcal X|}.$$

### Cascade Construction

> [!algorithm] Cascade Construction
> Let $F$ be a PRF that takes keys in $\mathcal K$ and produces outputs in $\mathcal K$. In symbols, $F$ is defined over $(\mathcal K, \mathcal X, \mathcal K)$. For any poly-bounded value $\ell$, we build a new PRF $F^*$, called the **cascade of $F$**, that maps messages in $\mathcal X^{\leq \ell}$ to outputs in $\mathcal K$. The function $F^*$, works as follows:
> 
> ---
> **Input**: $k \in \mathcal K$ and $m = (a_1, \dots, a_v) \in \mathcal X^{\leq \ell}$ for some $v \in \{0, \dots, \ell\}$
> **Output**: A tag in $\mathcal K$
> 1. $t \leftarrow k$
> 2. For $i \leftarrow 1$ to $v$ do: $t \leftarrow F(t, a_i)$
> 3. Output $t$

> [!theorem]
> Let $F$ be a secure PRF defined over $(\mathcal K, \mathcal X, \mathcal K)$. Then for any poly-bounded value $\ell$, the cascade $F^*$ of $F$ is a prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal K)$.
> 
> In particular, for every [[Pseudorandom Function#Secure Prefix-free PRF|secure prefix-free PRF]] adversary $\mathcal A$ that attacks $F^*$, and issues at most $Q$ queries, there exists a [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal B$ that attacks $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRF}^{pf}\text{adv}[\mathcal A, F^*] \leq Q \ell \cdot \text{PRFadv}[\mathcal B, F].$$

## From Prefix-free Secure PRF to Fully Secure PRF

### Encrypted PRF

> [!algorithm] Encrypted PRF
> Let PF be a PRF mapping $\mathcal X^{\leq \ell}$ to $\mathcal Y$ and let $F$ be a PRF mapping $\mathcal Y$ to $\mathcal T$. Define $$\text{EF}((k_1, k_2), m) = F(k_2, PF(k_1, m))$$ 

> [!theorem]
> Let PF be an extendable and prefix-free secure PRF defined over $(\mathcal K_1, \mathcal X^{\leq \ell + 1}, \mathcal Y)$, where $|\mathcal Y|$ is super-poly and $\ell$ is poly-bounded. Let $F$ be a secure PRF defined over $(\mathcal K_2, \mathcal Y, \mathcal T)$. Then EF is a secure PRF defined over $(\mathcal K_1 \times \mathcal K_2, \mathcal X^{\leq \ell}, \mathcal T)$.
> 
> In particular, for every [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal A$ that attacks EF, and issues at most $Q$ queries, there exist a [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal B_1$ attacking $F$, and a [[#Secure Prefix-free PRF|secure prefix-free PRF]] adversary $\mathcal B_2$ attacking PF, where $\mathcal B_1$ and $\mathcal B_2$ are elementary wrappers around $\mathcal A$, such that $$\text{PRFadv}[\mathcal A, EF] \leq \text{PRFadv}[\mathcal B_1, F] + \text{PRF}^{pf}\text{adv}[\mathcal B_2, PF] + \frac{Q^2}{2|\mathcal Y|}.$$

### Prefix-free Encodings

> [!remark] Idea
> Idea: Encode the input to the PRF so that no encoded input is a prefix of another.
> - We say that a set $S \subset \mathcal X^{\leq \ell}$ is a **prefix-free set** if no element in $S$ is a proper prefix of any other.
> - Let $\mathcal X^{\leq \ell}_{> 0}$ denote the set of all non-empty strings over $\mathcal X$ of length at most $\ell$. We say that a function $pf: \mathcal M \rightarrow \mathcal X^{\leq \ell}_{> 0}$ is a **prefix-free encoding** if $pf$ is injective and the image of $pf$ is a prefix-free set.

> [!algorithm] Prefix-free Encoding
> Let PF be a prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y)$ and $pf: \mathcal M \leftarrow \mathcal X^{\leq \ell}_{> 0}$ be a prefix-free encoding. Define the derived PRF $F$ as $$F(k, m) = PF(k, pf(m)).$$ 
> Then $F$ is defined over $(\mathcal K, \mathcal M, \mathcal Y)$.

> [!theorem]
> If PF is a prefix-free secure PRF and $pf$ is a prefix-free encoding then $F$ is a secure PRF.

> [!algorithm] Prepend Length
> Set $\mathcal M = \mathcal X^{\ell - 1}$ and let $m = (a_1, \dots, a_v) \in \mathcal M$. Define $$pf(m) = (\langle v \rangle, a_1, \dots, a_v) \in \mathcal X^{\leq \ell}_{> 0}$$ where $\langle v \rangle \in \mathcal X$ is the binary representation of $v$, the length of $m$. We assume that $\ell < 2^n$ so that the message length can be encoded as an $n$-bit binary string.

> [!algorithm] Stop Bits
> Let $\overline{\mathcal X} = \{0, 1\}^{n - 1}$ and let $\mathcal M = \overline{X}^{\leq \ell}_{> 0}$. For $m = (a_1, \dots, a_v) \in \mathcal M$, define $$pf(m) = ((a_1 || 0), (a_2 || 0), \dots, (a_{v - 1} || 0), (a_v) || 1) \in \mathcal X^{\leq \ell}_{> 0}$$

### CMAC

> [!definition] Prefix
> For two strings $x, y \in \mathcal X^{\leq \ell}$, let us write $x \sim y$ if $x$ is a prefix of $y$ or $y$ is a prefix of $x$.

> [!definition] Randomized $\epsilon$-prefix-free
> Let $\epsilon$ be a real number, with $0 \leq \epsilon \leq 1$. A **randomized $\epsilon$-prefix-free** encoding is a function $rpf: \mathcal K \times \mathcal M \rightarrow \mathcal X^{\leq \ell}_{> 0}$ such that for all $m_0, m_1 \in \mathcal M$ with $m_0 \neq m_1$, we have $$P[rpf(k, m_0) \sim rpf(k, m_1)] \leq \epsilon,$$ 
> where the probability is over the random choice of $k$ in $\mathcal K$.

> [!algorithm] Simple $rpf$
> Let $\mathcal K = \mathcal X$ and $\mathcal M = \mathcal X^{\leq \ell}_{> 0}$. Define $$rpf(k, (a_1, \dots, a_v)) = (a_1, \dots, a_{v - 1}, (a_v \oplus k)) \in \mathcal X^{\leq \ell}_{> 0}$$

> [!algorithm] Using $rpf$
> Let $PF$ be a prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y)$ and $rpf: \mathcal K_1 \times \mathcal M \rightarrow \mathcal X^{\leq \ell}_{> 0}$ be a randomized prefix-free encoding. Define the derived PRF $F$ as $$F((k, k_1), m) = \text{PF}(k, rpf(k_1, m)).$$
> Then $F$ is defined over $(\mathcal K \times \mathcal K_1, \mathcal M, \mathcal Y)$.

> [!theorem]
> If PF is a prefix-free secure PRF, $\epsilon$ is negligible, and $rpf$ a randomized $\epsilon$-prefix-free encoding, then $F$ is a secure PRF.
> 
> In particular, for every [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal A$ that attacks $F$, and issues at most $Q$ queries, there exist [[#Secure Prefix-free PRF|secure prefix-free PRF]] adversaries $\mathcal B_1$ and $\mathcal B_2$ that attack PF, where $\mathcal B_1$ and $\mathcal B_2$ are elementary wrappers around $\mathcal A$, such that $$\text{PRFadv}[\mathcal A, F] \leq \text{PRF}^{pf}\text{adv}[\mathcal B_1, PF] + \text{PRF}^{pf}\text{adv}[\mathcal B_2, PF] + Q^2\epsilon / 2.$$

## Block-wise PRF to Bit-wise PRF

> [!algorithm] Conversion from Block-wise to Bit-wise PRF
> Let $F$ be a PRF taking inputs in $\mathcal X^{\ell + 1}$. Let $inj: \{0, 1\}^{\leq n \ell} \rightarrow \mathcal X^{\ell + 1}$ be an injective function. Define the derived PRF $F_{bit}$ as $$F_{bit}(k, x) = F(k, inj(x)).$$

> [!theorem]
> If $F$ is a secure PRF defined over $(\mathcal K, \mathcal X^{\ell + 1}, \mathcal Y)$ then $F_{bit}$ is a secure PRF defined over $(\mathcal K, \{0, 1\}^{\leq n \ell}, \mathcal Y)$.

> [!algorithm] Injective Function
> For $\mathcal X = \{0, 1\}^n$, a standard example of an injective $inj$ from $\{0, 1\}^{\leq n \ell}$ to $\mathcal X^{\ell + 1}$.
> 
> ---
> **Input**: $m \in \{0, 1\}^{\leq n \ell}$
> 1. $u \leftarrow |m| \mod n, \quad m' \leftarrow m || 1 || 0^{n - u - 1}$
> 2. Output $m'$ as a sequence of $n$-bit message blocks.

