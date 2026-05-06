---
parent: "[[ZK-SNARKS Part 1 (Groth16)]]"
tags:
  - 🪴weedy
date: 2025-10-30T10:47
---
**Idea**: We have a homomorphisms between vector addition and polynomial addition mapping as:
$$\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
\rightarrow
\begin{bmatrix}
p(1) \\
p(2) \\
p(3)
\end{bmatrix}
\rightarrow p(x)$$
So to test $La \circ Ra = Oa$, we can write:
$L \rightarrow u_1(x), u_2(x), \cdots, u_m(x)$  
$R \rightarrow v_1(x), v_2(x), \cdots, v_m(x)$
$O \rightarrow w_1(x), w_2(x), \cdots, w_m(x)$

Then, we have:
$La \rightarrow \sum_{i = 1}^m a_i u_i(x) = u(x)$
$Ra \rightarrow \sum_{i = 1}^m a_i v_i(x) = v(x)$
$Oa \rightarrow \sum_{i = 1}^{m} a_i w_i(x) = w(x)$

We do not have $u(x) v(x) = w(x)$, but because of the interpolation, we have that $u(i) v(i) = w(i)$. 

Problem: $u(x)v(x) \neq w(x)$ but we need to have $u(i)v(i) = w(i) \forall i \in \{1, \cdots, n\}.$
We have:
$$u(x)v(x) - w(x) = h(x)t(x)$$
With $t(x) = (x - 1)\cdots(x - n)$ 
Thus $h(x) = \frac{u(x)v(x) - w(x)}{t(x)}$


**New Challenge Idea:**
The verifier sends a random $\tau$ to the prover, then the prover responses 
$A = u(\tau)$
$B = v(\tau)$
$C = w(\tau) + h(\tau)t(\tau)$
Then the verifier can check $AB = C$.
