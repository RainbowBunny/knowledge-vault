## Example

### The Birthday Paradox

> [!question]
> In a random group of 40 people, consider the following two questions
> 1. What is the probability that someone has the same birthday as you?
> 2. What is the probability that at least two people share the same birthday?

> [!remark] Answer
> 1. Answer: $1 - (\frac{364}{365})^{40} \approx 10.4\%$
> 2. Answer: $1 - \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{326}{365} \approx 89.1\%$

### Coupon Collector's Problem

> [!example] Coupon Collector's problem
> Suppose that there are $N$ different types of coupons. Each time you get a coupon, it is equally likely to be any of the $N$ possible types. Let $X$ be the number of coupons you will need to get before having observed each coupon at least once.
> 1. $X = X_0 + X_1 + \cdots + X_{N - 1}$, where $X_i \sim \text{Geometric}(\frac{N - i}{N})$ ($X_i$ is the number of coupon to get $i$ to $i + 1$ types).
> 2. $E[X] = N \sum_{k = 1}^N \frac{1}{k}$

### Streaks

> [!example] Streaks
> Suppose you flip a fair coin $n$ times. The longest streak of consecutive heads that you expect to see $\Theta(\lg n)$.

### Variance of Geometric Distribution
 
> [!example] Variance of Geometric Distribution
> Let $X \sim \text{Geometric}(p)$. We have $X = 1 + (1 - p) X'$ where $X' \sim \text{Geometrix}$, thus:
> $$E[X^2] = 1 + 2 (1 - p) E[X] + (1 - p)^2 E[x]^2 \rightarrow E[X^2] = \frac{2 - p}{p^2}$$
