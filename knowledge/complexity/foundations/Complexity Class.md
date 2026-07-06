# Complexity Class

Complexity theory studies **languages**, not "problems" in the informal sense. Every class note in this domain (P, NP, PSPACE, BPP, …) is a set of languages — this note fixes that formulation once, so the class notes can use it uniformly.

## Language Formulation

The alphabet / string / language definitions live in [[Languages]]; Turing machines and deciders live in [[Computability Theory]].

> [!definition] Decision Problem as a Language
> A **decision problem** is a yes/no question about an input. Fixing an alphabet $\Sigma$ (usually $\{0, 1\}$), a decision problem is identified with the language $$L = \{w \in \Sigma^* \mid \text{the answer on } w \text{ is yes}\} \subseteq \Sigma^*,$$ and "solving the problem" means **deciding** $L$: a machine $M$ decides $L$ if $M$ halts on every input and accepts $w$ iff $w \in L$.

> [!definition] Encoding
> Objects other than strings (graphs, matrices, machine descriptions, tuples) enter a language via an **encoding** $\langle \cdot \rangle$ that maps the object to a string. We write, e.g., $$\text{PATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a directed path from } s \text{ to } t\}.$$ Any reasonable (polynomially-related) encoding gives the same complexity classes, so the choice is left implicit.

> [!remark]
> 1. **Decision vs search**: the language formulation only captures yes/no questions. A **search problem** (produce a witness, not just decide existence) is formalized as a relation $R \subseteq \Sigma^* \times \Sigma^*$; for NP relations the two are polynomially equivalent via self-reducibility.
> 2. **Promise problems** relax the requirement that every string is a yes- or no-instance: inputs are promised to lie in $\Pi_{\text{yes}} \cup \Pi_{\text{no}}$. Several randomized and interactive classes are more naturally promise classes.

## Complexity Class

> [!definition] Complexity Class
> A **complexity class** is a set of languages. The classes studied here are all specified by three choices:
> 1. A **machine model** (deterministic / nondeterministic / probabilistic TM, circuit family, verifier-prover pair),
> 2. A **resource bound** (time $t(n)$, space $f(n)$, circuit size/depth, number of rounds),
> 3. An **acceptance condition** (always correct, correct on some branch, correct with probability $\geq 2/3$, …).
>
> E.g. $\text{TIME}(t(n))$, $\text{SPACE}(f(n))$, $\text{BPP}$ are the sets of languages decided under the respective choices.

> [!definition] Complement Class
> For a language $L$, the complement is $\overline{L} = \Sigma^* \setminus L$. For a complexity class $\mathcal C$, $$\text{co}\mathcal C = \{L \mid \overline{L} \in \mathcal C\}.$$
> Examples: $\text{coNP}$ (languages whose *non*-membership has short certificates), $\text{coRP}$, $\text{coNL}$. Deterministic classes are closed under complement ($\text{P} = \text{coP}$, and by Immerman–Szelepcsényi even $\text{NL} = \text{coNL}$); whether $\text{NP} = \text{coNP}$ is open.

## Efficient Algorithm

> [!definition] Polynomial-time Computable Function
> A function $f: \Sigma^{*} \rightarrow \Sigma^{*}$ is a **polynomial-time computable function** if some polynomial-time Turing machine $M$ exists that halts with just $f(w)$ on its tape, when started on any input $w$.

> [!definition] Efficient Algorithm (Cryptographic Convention)
> Let $A$ be an algorithm (possibly probabilistic) that takes as input a security parameter $\lambda \in \mathbb Z_{\geq 1}$, as well as other parameters encoded as a bit string $x \in \{0, 1\}^{p(\lambda)}$ for some fixed polynomial $p$. We call $A$ an **efficient algorithm** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$ such that for all $\lambda \in \mathbb Z_{\geq 1}$, and all $x \in \{0, 1\}^{\leq p(\lambda)}$, the probability that the running time of $A$ on input $(\lambda, x)$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

> [!remark]
> The second definition is the Boneh–Shoup convention used throughout `cryptography/` (running time measured in the security parameter, negligible slack allowed); see [[Security Model]]. Complexity-theory notes use the plain "polynomial in the input length" convention, i.e. [[Randomized Complexity#Probabilistic Polynomial Time (PPT)|PPT]].

## Complexity Relationships Among Models

> [!theorem]
> Let $t(n)$ be a function, where $t(n) \geq n$. Then every $t(n)$-time multitape Turing machine has an equivalent $O(t^2(n))$-time single-tape Turing machine.

## Class Inclusions

The standard inclusion lattice among the major classes:

$$\text{P} \subseteq \text{NP} \subseteq \text{PSPACE} = \text{NPSPACE} = \text{IP} \subseteq \text{EXPTIME}$$
$$\text{NL} \subset \text{PSPACE} \subset \text{EXPSPACE}$$
$$\text{P} \subset \text{EXPTIME}$$

Strict inclusions follow from the [[Hierarchy Theorems|time and space hierarchy theorems]]; equalities like $\text{PSPACE} = \text{NPSPACE}$ follow from [[Space Complexity#Savitch's Theorem|Savitch's theorem]] and $\text{IP} = \text{PSPACE}$ from Shamir's theorem (see [[Interactive Proofs]]).

## Related

- [[Languages]] — alphabets, strings, languages (the raw material)
- [[Computability Theory]] — Turing machines, deciders, decidability
- [[Reductions]] — poly-time and log-space mapping reductions, the structural relations among classes
- [[Hierarchy Theorems]] — proofs that more resources yield strictly more computational power
- [[Time Complexity]] / [[Space Complexity]] — the canonical resource bounds
- [[Randomized Complexity]] — what changes when the machine has access to random coins
