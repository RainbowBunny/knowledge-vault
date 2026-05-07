
## Collision Theorem

> [!question] Setup
> Bob has a box that contains $N$ numbers. He chooses $n$ distinct numbers from the box and puts them in a list. He then makes a second list by choosing $m$ (not necessarily distinct) numbers from the box. The remarkable fact is that if $n$ and $m$ are each slightly larger than $\sqrt{N}$, then it is very likely that the two lists contain a common element.
> 

> [!theorem] Collision Theorem
> An urn contains $N$ balls, of which $n$ are red and $N - n$ are blue. Bob randomly selects a ball from the urn, replaces it in the urn, randomly selects a second ball, replaces it, and so on. He does this until he has looked at a total of $m$ balls.
> 1. The probability that Bob selects at least one red ball is $$P(\text{at least one red}) = 1 - (1 - \frac{n}{N})^m.$$
> 2. A lower bound for the probability above is $$P(\text{at least one red}) \geq 1 - e^{-mn/N}.$$
> If $N$ is large and if $m$ and $n$ are not too much larger than $\sqrt{N}$ (e.g., $m, n < 10 \sqrt{N}$), then the inequality above is almost an equality.

## Pollard's $\rho$ method


> [!definition] Discrete Dynamical System
> Let $S$ be a finite set and let $$f: S \rightarrow S$$ be a function that does a good job at mixing up the elements of $S$. Suppose that we start with some element $x \in S$ and we repeatedly apply $f$ to create a sequence of elements $$x_0 = x, \quad x_1 = f(x_0), \quad x_2 = f(x_1) \quad x_3 = f(x_2), \quad x_4 = f(x_3), \quad \cdots$$
> In other words, $$x_i = \underbrace{(f \circ f \circ f \circ \cdots \circ f)}_{i \text{ iterations of } f}(x).$$
> The map $f$ from $S$ to itself is an example of a **discrete dynamical system**.
> $$x_0, x_1, x_2, x_3, x_4, \cdots$$
> is called the **(forward) orbit of** $x$ by the map $f$ and is denoted by $O^+_f(x).$

> [!definition] $\rho$ algorithms
> Collision algorithms based on following the orbit of an element in a discrete dynamical system are called $\rho$ **algorithms**.

> [!remark]
> Let $T$ is the largest integer such that $x_{T - 1}$ appears only once in $O^+_f(x)$.
> Let $M$ is the smallest integer such that $x_{T + M} = x_T$.

> [!theorem] Pollard's $\rho$ Method: abstract version
> Let $S$ be a finite set containing $N$ elements, let $f: S \rightarrow S$ be a map, and let $x \in S$ be an initial point.
> 1. Suppose that the forward orbit $O^+_f(x) = \{x_0, x_1, x_2, \cdots\}$ of $x$ has a tail of length $T$ and a loop of length $M$. Then $$x_{2i} = x_{i} \quad \text{for some } 1 \leq i < T + M.$$
> 2. If the map $f$ is sufficiently random, then the expected value of $T + M$ is $$E(T + M) \approx 1.2533 \cdot \sqrt{N}.$$
> Hence if $N$ is large, then we are likely to find a collision as described in $O(\sqrt{N})$ steps, where a "step" is one evaluation of the function $f$.

