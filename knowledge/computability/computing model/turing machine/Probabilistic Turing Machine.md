Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.1: Probabilistic Turing Machines; Section 7.4.2: Expected running time versus worst-case running time; Section 7.4.3: Allowing more general random choices than a fair random coin.

## Definition

> [!definition] Probabilistic Turing Machine
> Generalizes:: [[Turing Machine]]
> 
> ---
> - The Turing Machine now has two transition functions $\delta_0, \delta_1$.
> - On execution, the Turing machine will choose in each step with probability $\frac{1}{2}$ to apply the transition function $\delta_0$ and with probability $\frac{1}{2}$ to apply the transition function $\delta_1$. This choice is made independently of all previous choices.
> - Denote $M(x)$ the random variable corresponding to value $M$ writes at the end of this process.

### Running Time

> [!definition] Running Time of Probabilistic Turing Machine
> For a function $T: \mathbb{N} \rightarrow \mathbb{N}$, we say that $M$ runs in $T(n)$-time if for any input $x$, $M$ halts on $x$ within $T(|x|)$ steps regardless of the random choices it makes.

### Expected Running Time

> [!definition] Expected Running Time of Probabilistic Turing Machine
> For a PTM $M$, and input $x$, we define the random variable $T_{M, x}$ to the the running time of $M$ on input $x$. That is, $\Pr[T_{M, x} = T] = p$ if with probability $p$ over the random choices of $M$ on input $x$, it will halt within $T$ steps. We say that $M$ has **expected running time** $T(n)$ if the expectation $E[T_{M, x}]$ is at most $T(|x|)$ for every $x \in \{0, 1\}^*$.

### Expected Running Time versus Worst-Case Running Time

> [!remark]
> We can transform a PTM $M$ whose expected running time is $T(n)$ to a PTM $M'$ that always halts after at most $100 T(n)$ steps by simply adding a counter and halting with an arbitrary output after too many steps have gone by.
> By Markov's inequality, the probability that $M$ runs for more than $100 T(n)$ steps is at most $1/100$, and so this will change the acceptance probability by at most $1/100$.

## Property

### Simulating Coin with Probabilistic Turing Machine

> [!lemma]
> A coin with $\Pr[\mathrm{Heads}] = \rho$ can be simulated by a probabilistic Turing Machine in expected time $O(1)$ provided the $i$-th bit of $\rho$ is computable in $\mathsf{poly}(i)$ time.

> [!lemma] Von-Neumann
> A coin with $\Pr[\mathrm{Heads}] = 1/2$ can be simulated by a probabilistic Turing Machine with access to a stream of $\rho$-biased coins in expected time $O(\frac{1}{\rho(1 - \rho)})$.

