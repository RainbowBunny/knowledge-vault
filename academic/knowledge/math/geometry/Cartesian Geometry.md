## Axiomatic Definition

> [!definition]
> The $x$-coordinate of a point is sometimes called its **abscissa** and the $y$-coordinate is called its **ordinate**.

> [!axiom] Axiomatic Definition of Area
> We assume there exists a class $\mathcal M$ of measurable sets in the plane and a set function $a$, whose domain is $\mathcal M$, with the following properties:
> 1. **Nonnegative property**: For each set $S$ in $\mathcal M$, we have $a(S) \geq 0$.
> 2. **Additive property**: If $S$ and $T$ are in $\mathcal M$, then $S \cup T$ and $S \cap T$ are in $\mathcal M$, and we have $$a(S \cup T) = a(S) + a(T) - a(S \cap T).$$
> 3. **Difference property**: If $S$ and $T$ are in $\mathcal M$ with $S \subseteq T$, then $T - S$ is in $\mathcal M$, and we have $a(T - S) = a(T) - a(S)$.
> 4. **Invariance under congruence**: If a set $S$ is in $\mathcal M$ and if $T$ is congruent to $S$, then $T$ is also in $\mathcal M$ and we have $a(S) = a(T)$.
> 5. **Choice of scale**: Every rectangle $R$ is in $\mathcal M$. If the edges of $R$ have lengths $h$ and $k$, then $a(R) = hk$.
> 6. **Exhaustion property**: Let $Q$ be a set that can be enclosed between two step regions $S$ and $T$, so that $$S \subseteq Q \subseteq T.$$ If there is one and only one number $c$ which satisfies the inequalities $$a(S) \leq c \leq a(T)$$ for all step regions $S$ and $T$ satisfying $S \subseteq Q \subseteq T$, then $Q$ is measurable and $a(Q) = c$.

> [!proposition] Monotone Property
> For sets $S$ and $T$ in $\mathcal M$ with $S \subseteq T$, $a(S) \leq a(T)$.

> [!proposition]
> A point $(x, y)$ in the plane is called a **lattice point** if both coordinates $x$ and $y$ are integers. Let $P$ be a polygon whose vertices are lattice points. The area of $P$ is $I + \frac{1}{2}B - 1$, where $I$ denotes the number of lattice points inside the polygon and $B$ denotes the number on the boundary.

## Integral Definition

> [!theorem]
> Let $f$ be a nonnegative function, integrable on an interval $[a, b]$, and let $Q$ denote the ordinate set of $f$ over $[a, b]$. Then $Q$ is measurable and its area is equal to the integral $\int_a^b f(x) dx$.

## Polar Coordinates

> [!definition] Polar Coordinates
> Let $P$ be a point distinct from the origin. Suppose the line segment joining $P$ to the origin has length $r > 0$ and makes an angle of $\theta$ radians with the positive $x$-axis. The two numbers $r$ and $\theta$ are called **polar coordinates** of $P$. They are related to the rectangular coordinates $(x, y)$ by the equations $$x = r \cos \theta, \quad y = r \sin \theta.$$
> The positive number $r = \sqrt{x^2 + y^2}$ is called the **radial distance** of $P$, and $\theta$ is called a **polar angle**.


> [!definition] Convex
> A set is called **convex** if, for every pair of points $P$ and $Q$ in the set, the line segment joining $P$ and $Q$ is also in the set.

## 3D Version

> [!axiom] Axiomatic Definition of Volume
> We assume there exists a class $\mathcal A$ of solids and a set function $v$, whose domain is $\mathcal A$, with the following properties:
> 1. **Nonnegative property**: For each set $S$ in $\mathcal A$ we have $v(S) \geq 0$.
> 2. **Additive property**: If $S$ and $T$ are in $\mathcal A$, then $S \cup T$ and $S \cap T$ are in $\mathcal A$, and we have $$v(S \cup T) = v(S) + v(T) - v(S \cap T).$$
> 3. **Difference property**: If $S$ and $T$ are in $\mathcal A$ with $S \subseteq T$, then $T - S$ is in $\mathcal A$, and we have $v(T - S) = v(T) - v(S)$.
> 4. **Cavalieri's principle**: If $S$ and $T$ are two Cavalieri solids in $\mathcal A$ with $a(S \cap T) \leq a(T \cap F)$ for every plane $F$ perpendicular to a given line, then $v(S) \leq v(T)$.
> 5. **Choice of scale**: Every box $B$ is in $\mathcal A$. If the edges of $B$ have length $a$, $b$ and $c$, then $v(B) = abc$.
> 6. Every convex set is in $\mathcal A$.

> [!proposition]
> Axiom 3 also implies the monotone property: $$v(S) \leq v(T), \quad \text{for sets } S \text{ and } T \text{ in } \mathcal A \text{ with } S \subseteq T.$$

> [!definition] Cube
> The **cube** in $\mathbb R^n$ with side length $r$ and vertex $(x_1, \dots, x_n) \in \mathbb R^n$ is the set $$\{(y_1, \dots, y_n) \in \mathbb R^n: x_j < y_j < x_j + r \text{ for } j = 1, \dots, n\};$$

> [!theorem]
> If $T \in \mathcal L(\mathbb R^n)$, then $$\text{volume } T(\ohm) = |\det T| (\text{volume } \ohm)$$ for $\ohm \subset \mathbb R^n$.

## Contour Lines

