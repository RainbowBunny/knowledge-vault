# Introduction

## Cryptography: Main Topics

### Encryption Schemes

 Participants:
 - Two parties communicate with each other (sender/receiver)
 - Wire-tapper: adversary that can listen to the communicating channel.
 Components:
 - **Encryption**: The sender applied this to the message to get the *ciphertext*.
 - **Decryption**: The receiver applied this to the *ciphertext* to get the original message *plaintext*.
 Necessary condition for secret communication: *decryption key* that the wire-tapper doesn't know.
 Two approaches to the security of an encryption scheme:
 - **Information-theoretic**: 
 - **Computational complexity**:

### Pseudorandom Generators

### Digital Signatures

A *scheme for unforgeable signatures* requires:
- that each user be able to *efficiently generate his or her own signature* on documents of his or her choice.
- that each user be able to *efficiently verify* whether a given string is a signature of another (specific) user on a specific document, and
- that *no one be able to efficiently produce the signatures of other users* to documents that those users did not sign.

A *scheme for message authentication* requires:
- that each of the communicating parties be able to *efficiently generate an authentication tag* for any message of his or her choice,
- that each of the communicating parties be able to *efficiently verify* whether a given string is an authentication tag for a given message, and
- that *no external adversary be able to efficiently produce authentication tags* to messages not sent by the communicating parties.

### Fault-Tolerant Protocols and Zero-Knowledge Proofs


# Computational Difficulty

## One-Way Function

> [!definition] Strong One-Way Functions
A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **(strongly) one-way** if the following two conditions hold:
>1. Easy to compute: There exists a (deterministic) polynomial-time algorithm $A$ such that on input $x$ algorithm $A$ outputs $f(x)$.
>2. Hard to invert: For **every** probabilistic polynomial-time algorithm $A'$, every positive polynomial $p(\cdot)$, and all sufficiently large $n$'s, $$P[A'(f(U_n, 1^n)) \in f^{-1} (f(U_n))] < \frac{1}{p(n)}$$
>
**Note**: $U_n$ is uniformly distributed $n$-bit, $1^n$ is unary encoding for length.

> [!definition] Weak One-Way Functions
>  A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **weakly one-way** if the following two conditions hold:
>3. Easy to compute: As in the definition of a strong one-way function.
>4. Slightly hard to invert: There **exists** a polynomial $p(\cdot)$ such that for every probabilistic polynomial-time algorithm $A'$ and all sufficiently large $n$'s, $$\Pr[A'(f(U_n), 1^n) \notin f^{-1}(f(U_n))] > \frac{1}{p(n)}$$

**Proposition**: Let $I$ be a polynomial-time enumerable set, and let $f$ be strongly (weakly) one-way on lengths in $I$. Then $g$ and $g'$ as define below are strongly (weakly) one-way (in the ordinary sense):
$$g(x) \stackrel{\text{def}}{=} f(x')$$
where $x'$ is the longest prefix of $x$ with length in $I$. In the case the function $f$ is length preserving ($|f(x)| = |x|$ for all $x$):
$$g'(x) \stackrel{\text{def}}{=} f(x')x''$$
where $x = x'x''$.

Function $f$ is *length-regular* if for every $x, y \in \{0, 1\}^*$ if $|x| = |y|$ then $|f(x)| = |f(y)|$.

> [!definition] Length-Preserving Functions
>  A function $f$ is **length-preserving** if for every $x \in \{0, 1\}^*$ it holds that $|f(x)| = |x|$.

**Proposition**: If $f$ is a strongly (weakly) one-way function, then so are $f'$ and $f''$ as define below: $$f'(x) \stackrel{\text{def}}{=} f(x)10^{p(|x|) - |f(x)|}$$
and $$f''(x'x'') \stackrel{\text{def}}{=} f'(x')$$where $|x'x''| = p(|x'|) + 1$. ($p$ be a polynomial bounding the length expansion of $f$, $|f(x)| \leq p(|x|)$)

**Candidates for one-way function**:
- [[Integer Factorization]]
- **Decoding of Random Linear Codes**: 
- [[Subset-Sum Problem]]

> [!definition] Non-Uniformly Strong One-Way Functions
>  A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **non-uniformly one-way** if the following two conditions hold:
>1. Easy to compute: There exists a polynomial-time algorithm $A$ such that on input $x$ algorithm $A$ outputs $f(x)$.
>2. Hard to invert: For every (even non-uniform) family of polynomial-size circuits $\{C_n\}_{n \in \mathbb N}$, every positive polynomial $p(\cdot)$, and all sufficiently large $n$'s, $$\Pr[C_n(f(U_n)) \in f^{-1}(f(U_n))] < \frac{1}{p(n)}$$


 