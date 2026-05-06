
> [!proposition]
> A good zero-knowledge proof showing that a quantity $y$ has some property $\mathcal P$ should satisfy the following two conditions:
> - **Completeness**: If $y$ does have property $\mathcal P$, then Victor should always accept Peggy's responses as being valid.
> - **Soundness**: If $y$ does not have property $\mathcal P$, then there should be only a very small probability that Victor accepts all of Peggy's responses as begin valid.

> [!example]
> Peggy chooses two large primes $p$ and $q$ and publishes their product $N$. Peggy's task is to prove to Victor that a certain number $y$ is a square modulo $N$. Peggy's task is to prove to Victor that a certain number $y$ is a square modulo $N$ without revealing to Victor any information that would help him to prove to other people that $y$ is a square modulo $N$. We note that since Peggy knows how to factor $N$, if $y$ is a square modulo $N$, then she can find a square root for $y$, say $x$ satisfying $$x^2 \equiv y \pmod N.$$ In each round, Peggy and Victor perform the following steps:
> 1. Peggy chooses a random number $r$ modulo $N$. She computes and sends to Victor the number $$s \equiv r^2 \pmod N.$$
> 2. Victor randomly chooses a value $\beta \in \{0, 1\}$ and sends $\beta$ to Peggy.
> 3. Peggy computes and sends to Victor the number $$z \equiv \begin{cases}r \pmod N &\text{if } \beta = 0. \\ xr \pmod N \; &\text{if } \beta = 1.\end{cases}$$
> 4. Victor computes $z^2 \pmod N$ and checks that $$z^2 \equiv \begin{cases}s \pmod N &\text{if } \beta = 0. \\ ys \pmod N \; &\text{if } \beta = 1.\end{cases}$$
> If this is true, Victor accepts Peggy's response; otherwise, he rejects it.


