---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-02T22:31
---
## Property

| Property         | Description                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Identity Law     | $\exists e \in O, \forall a \in O$: $ea = ae = a$                                                         |
| Inverse Law      | $\forall a \in O, \exists! a^{-1} \in O$: $a a^{-1} = a^{-1} a = e$                                       |
| Associative Law  | $\forall a, b, c \in O: (a b) c = a (b c)$                                                                |
| Commutative Law  | $\forall a, b \in O: ab = ba$                                                                             |
| Distributive Law | $\forall a, b, c \in O: a(b + c) = ab + ac$                                                               |
| Alternative      | $x (x y) = (x x) y$ left alternative<br>$(y x) x = y (x x)$ right alternative<br>$(xy)x = x(yx)$ flexible |
- [[Ring]]
- [[Field]]

### Frobenius theorem

Finite-dimensional associative division algebras over the real numbers is isomorphic to:
- $\textbf{R}$ (the real numbers)
- $\textbf{C}$ (the complex numbers)
- $\textbf{H}$ (the quaternions)
These algebras have real dimension 1, 2, and 4, respectively.






## Quaternions

This is the extensions of the complex number system where each element $x$ is a 4-dimensions vector:
$$x = a + b i + c j + d k$$
where the basis vector $1, i, j, k$ has the multiplication table:

| x   | 1   | i   | j   | k   |
| --- | --- | --- | --- | --- |
| 1   | 1   | i   | j   | k   |
| i   | i   | -1  | k   | -j  |
| j   | j   | -k  | -1  | i   |
| k   | k   | j   | -i  | -1  |

Which follows the rule: $i^2 = j^2 = k^2 = i j k = -1$

Note: Multiplication is not commutative but associative. 

## Octonion

Octonion is the extensions of quaternions system by combining complex number system and quaternions number system:

$$x = (a, b) = a + \omega b$$
Where $\omega^2 = -1$ and $a, b$ are elements in quaternions.

Note: Multiplication is not commutative and not associative, however, octonion is alternative.



