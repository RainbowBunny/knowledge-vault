---
parent: "[[ZK-SNARKS Part 1 (Groth16)]]"
tags:
date: 2025-10-29T21:04
---
**Rank 1 Constraint System (R1CS)**: An arithmetic circuit with the requirement that each equality constraint has one multiplication (and no restriction on the number of additions).

**Witness vector**: A vector contains the value of all the input variables, the output variables, and the intermediate values.

Let this vector be $a$, we can create matrix $L, R, O$ and check the multiplication constraint by equation:
$$O a = L a \cdot Ra$$
Example 1: 
Proof for $r = xyzu$
Equation:
$$\begin{cases}
	v_1 &= xy \\
	v_2 &= zu \\
	r   &= v_1 v_2
\end{cases}$$
Witness vector: $w = (1, r, x, y, z, u, v_1, v_2)$
For first equation, if we choose $O_1 = \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\end{bmatrix}$,   $L_1 = \begin{bmatrix}0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\end{bmatrix}$,  $R_1 = \begin{bmatrix}0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\end{bmatrix}$, then $Oa = v_1$, $La = x$, $Ra = y$ thus $La \cdot Ra = xy = Oa$.
Similarly, we can construct the full matrix:
$$O = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}$$
$$L = \begin{bmatrix}
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}$$
$$R = \begin{bmatrix}
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{bmatrix}$$
Example 2:
Proof for $z = xy + 2$
Addition is free because we can modify the equation so that we do not need a new variable for $xy$.
Equation:
$$\begin{cases}
	-2 + z = xy
\end{cases}$$
Witness vector: $w = (1, z, x, y)$
$$O = \begin{bmatrix}
-2 & 1 & 0 & 0 
\end{bmatrix}$$
$$L = \begin{bmatrix}
0 & 0 & 1 & 0
\end{bmatrix}$$
$$R = \begin{bmatrix}
0 & 0 & 0 & 1
\end{bmatrix}$$

## Building a Zero Knowledge Proof from an R1CS

Given $O, L, R$, we can create a problem that accepts $a$ as a proof, however, If we use the raw $a$ as the proof, we do not have a zero knowledge system.

In order to create a zero knowledge proof system, we can use the bilinear pairing with three groups $G_1, G_2, G_T$:
$$
\begin{bmatrix}
l_{1, 1} [a_1 G_1]_1 + \cdots + l_{1, m} [a_m G_1]_1 \\
\vdots \\
l_{n, 1} [a_1 G_1]_1 + \cdots + l_{n, m} [a_m G_1]_1
\end{bmatrix}
\circ
\begin{bmatrix}
r_{1, 1} [a_1 G_2]_2 + \cdots + r_{1, m} [a_m G_2]_2 \\
\vdots \\
r_{n, 1} [a_1 G_2]_2 + \cdots + r_{n, m} [a_m G_2]_2
\end{bmatrix}
=
\begin{bmatrix}
\sum_{i = 1}^m o_{i, 1} [a_i G_1]_1 \\
\vdots \\
\sum_{i = 1}^m o_{i, n} [a_i G_1]_1
\end{bmatrix}
\circ 
\begin{bmatrix}
G_2 \\
\vdots \\
G_2
\end{bmatrix}
$$

Then, if a variable $a$ need to be encrypted, we will send $a G_1$ and $aG_2$ for a witness vector $La$ and $Ra$ respectively. However, we also need to prove the relationship between $La$ and $Ra$ by using the relationship:
$$\begin{bmatrix}
a_1 G_1 \\
a_2 G_1 \\
\vdots \\
a_m G_1
\end{bmatrix}
\circ
\begin{bmatrix}
G_2 \\
G_2 \\
\vdots \\
G_2
\end{bmatrix}
= 
\begin{bmatrix}
a_1 G_2 \\
a_2 G_2 \\
\vdots \\
a_m G_2
\end{bmatrix}
\circ
\begin{bmatrix}
G_1 \\
G_1 \\
\vdots \\
G_1
\end{bmatrix}
$$
