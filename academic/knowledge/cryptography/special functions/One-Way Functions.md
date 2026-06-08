## Strong One-Way Functions

> [!definition] Strong One-Way Functions
> A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **(strongly) one-way** if the following two conditions hold:
> 1. **Easy to compute**: There exists a (deterministic) polynomial-time algorithm $A$ such that on input $x$ algorithm $A$ outputs $f(x)$.
> 2. **Hard to invert**: For every probabilistic polynomial-time algorithm $A'$, every positive polynomial $p(\cdot)$, and all sufficiently large $n$'s, $$\Pr[A'(f(U_n), 1^n) \in f^{-1}(f(U_n))] < \frac{1}{p(n)}$$

## Weak One-Way Functions

> [!definition] Weak One-Way Functions
> A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **weakly one-way** if the following two conditions hold:
> 1. **Easy to compute**: There exists a (deterministic) polynomial-time algorithm $A$ such that on input $x$ algorithm $A$ outputs $f(x)$.
> 2. **Slightly hard to invert**: There exists a polynomial $p(\cdot)$ such that for every probabilistic polynomial-time algorithm $A'$ and all sufficiently large $n$'s, $$\Pr[A'(f(U_n), 1^n) \notin f^{-1}(f(U_n))] > \frac{1}{p(n)}$$

### Non-Uniformly Strong One-Way Functions

> [!definition] Non-Uniformly Strong One-Way Functions
> A function $f:\{0, 1\}^* \rightarrow \{0, 1\}^*$ is called **non-uniformly one-way** if the following two conditions hold:
> 1. **Easy to compute**: There exists a (deterministic) polynomial-time algorithm $A$ such that on input $x$ algorithm $A$ outputs $f(x)$.
> 2. **Hard to invert**: For every (even non-uniform) family of polynomial-size circuits $\{C_n\}_{n \in \mathbb N}$, every positive polynomial $p(\cdot)$, and all sufficiently large $n$'s, $$\Pr[C_n(f(U_n)) \in f^{-1}(f(U_n))] < \frac{1}{p(n)}$$

