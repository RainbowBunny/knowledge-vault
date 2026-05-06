---
parent: "[[Fleeting MOC]]"
tags:
  - crypto
  - isogeny
date: 2025-08-16T20:20
---
## The set of supersingular j-invariants

We are working with the quadratic extensions of large prime fields $\mathbb F_p$ with $p \equiv 3\; mod\; 4$. The extension is typically represented as $\mathbb F_{p^2} = \mathbb F_{p}(i)$ with $i^2 + 1 = 0$ with elements in the form $u + vi$ where $u, v \in \mathbb Z_p$ and $i^2 + 1 = 0$.

## Isogenies

Montgomery-form elliptic curves are often the preferred choice in isogeny-based cryptography because they facilitate very efficient $x$-only arithmetic, so instead of using the isomorphisms $(x, y) \mapsto (f(x, y), g(x, y))$, we simply use $x \mapsto f(x)$.

Consider the set of points in $\ell$-torsion (i.e $\{P \in E: \ell P = O\}$) with $p \nmid \ell$ form a subgroup: $$ker([\ell]) \simeq \mathbb Z_\ell \times \mathbb Z_\ell$$ and they form $\ell + 1$ subgroups of order $l$ when $l$ is prime.

