Reference: https://www.di.ens.fr/~nitulesc/files/Survey-SNARKs.pdf

## Basic Definition

> [!definition] Quadratic Arithmetic Program
> A Quadratic Arithmetic Program $Q$ over the field $\mathbb F$ contains three sets of $m + 1$ polynomials $\mathcal V = \{v_i(x)\}, \mathcal W = \{w_i(x)\}, \mathcal Y = \{y_i(x)\}, i \in \{0, 1, \dots, m\}$ and a target polynomial $t(x)$. Suppose $F$ is an arithmetic function that takes as input $n$ elements of $\mathbb F$ and outputs $n'$ elements, for a total of $N = n + n'$ I/O elements. Then, $(c_1, \dots, c_n) \in \mathbb F^N$ is a valid assignment of $F$'s inputs and outputs, if and only if there exist coefficients $(c_{N + 1}, \dots, c_m)$ such that $t(x)$ divides $p(x)$, where:
> $$p(x) = (v_0(x) + \sum_{i = 1}^m c_i v_i(x)) \cdot (w_0(x) + \sum_{i = 1}^m c_i w_i(x)) - (y_0(x) + \sum_{i = 1}^m c_i y_i(x))$$

