---
parent: "[[ZK-SNARKS Part 1 (Groth16)]]"
tags:
  - 🪴weedy
date: 2025-10-30T10:02
---
**Schwartz-Zippel Lemma**: Given two polynomials $p(x)$ and $q(x)$ with degrees $d_p$ and $d_q$ respectively, and if $p(x) \neq q(x)$, then the number of points where $p(x)$ and $q(x)$ intersect is less than or equal to $\max(d_p, d_q)$.

With the Schwartz-Zippel Lemma in $\mathbb F_p$, with $p$ and the degree of the polynomials are small, then if we pick a random value $u$ then the probability of $p(u) = q(u)$ is negligible if $p \neq q$.

My thought:
We can create a challenge for the knower of the polynomial $p$ by generating a random point $x$ and check if they know the value of $p(x)$.

