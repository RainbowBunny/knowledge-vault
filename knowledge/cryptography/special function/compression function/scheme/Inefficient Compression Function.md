## Scheme

> [!algorithm] Inefficient Compression Function
> Let $p$ be a large prime such that $q = (p - 1) / 2$ is also prime. Let $x$ and $y$ be suitably chosen integers in the range $[1, q]$. Consider the following simple compression function that takes as input two integers in $[1, q]$ and outputs an integer in $[1, q]$: $$H(a, b) = abs(x^a y^b \mod p), \quad \text{where} \quad \text{abs}(z) = \begin{cases}z&\text{if } z \leq q, \\ p - z &\text{if }z > q.\end{cases}$$