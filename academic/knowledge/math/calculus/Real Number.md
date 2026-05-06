
## The Order Axiom

> [!axiom] The Order Axiom
> Assume that there exists a certain subset $\mathbb R^+ \subset \mathbb R$, called the set of **positive** numbers, which satisfies the following order axioms:
> 
>  7. If $x$ and $y$ are in $\mathbb R^+$, so are $x + y$ and $xy$.
>  8. For every real $x \neq 0$, either $x \in \mathbb R^+$ or $-x \in \mathbb R^+$, but not both.
>  9. $0 \notin \mathbb R^+$.

> [!definition] Order Operators 
> Define $<, >, \leq,$ and $\geq$ as **less than**, **greater than**, **less than or equal to**, and **greater than or equal to**, as:
> - $x < y$ means that $y - x$ is positive;
> - $y > x$ means that $x < y$;
> - $x \leq y$ means that either $x < y$ or $x = y$;
> - $y \geq x$ means that $x \leq y$.
> 
> If $x < 0$ means $x$ is **negative**; if $x \leq 0$ means $x$ is **nonnegative**.

| Property       | Description                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------- |
| Trichotomy Law | For arbitrary real numbers $a$ and $b$, exactly one of the three relations $a < b, b < a, a = b$ holds.    |
| Transitive Law | If $a < b$, $b < c$, then $a < c$                                                                          |
|                | If $a < b$, then $a + c < b + c$                                                                           |
|                | If $a < b$ and $c > 0$, then $ac < bc$                                                                     |
|                | If $a \neq 0$, then $a^2 > 0$                                                                              |
|                | $1 > 0$                                                                                                    |
|                | If $a < b$ and $c < 0$, then $ac > bc$                                                                     |
|                | If $a < b$, then $-a > -b$. In particular, if $a < 0$, then $-a > 0$.                                      |
|                | If $ab > 0$, then both $a$ and $b$ are positive or both are negative.                                      |
|                | If $a < c$ and $b < d$, then $a + b < c + d$                                                               |
|                | There is no real number $x$ such that $x^2 + 1 = 0$.                                                       |
|                | The sum of two negative numbers is negative.                                                               |
|                | If $a > 0$, then $1/a > 0$; if $a < 0$, then $1/a < 0$                                                     |
|                | If $0 < a < b$ then $0 < b^{-1} < a^{-1}$                                                                  |
|                | If $a \leq b$ and $b \leq c$, then $a \leq c$                                                              |
|                | If $a \leq b$ and $b \leq c$, and $a = c$, then $b = c$                                                    |
|                | For all real $a$ and $b$ we have $a^2 + b^2 \leq 0$. If $a$ and $b$ are not both $0$, then $a^2 + b^2 > 0$ |
|                | There is no real number $a$ such that $x \leq a$ for all real $x$                                          |
|                | If $x$ has the property that $0 \leq x < h$ for every positive real number $h$, then $x = 0$               |

## Integers and Rational Numbers

> [!definition] Inductive Set
> A set of real numbers is called an **inductive set** if it has the following two properties:
> 1. The number $1$ is in the set.
> 2. For every $x$ in the set, the number $x + 1$ is also in the set.

> [!definition] Positive Integers
> A real number is called a positive integer if it belongs to every inductive set.

> [!definition] Negative Integers
> The negatives of the positive integers are called the **negative integers**.

> [!definition] The Set of Integers
> The positive integers, together with the negative integers and $0$ form a set $\mathbb Z$ is the **set of integers** 

> [!definition] Rational Numbers
> Quotients of integers $a/b$ (where $b \neq 0$) are called **rational numbers**. The set of rational numbers, denoted by $\mathbb Q$.

## Bound

> [!definition] Bounded Above
> Suppose $S$ is a nonempty set of real numbers and suppose there is a number $B$ such that $$x \leq B$$ for every $x$ in $S$. Then $S$ is said to be **bounded above** by $B$. The number $B$ is called an **upper bound** for $S$. If $B \in S$, then $B$ is called the **largest member** or the **maximum element** of $S$ and write $$B = \max S.$$ A set with no upper bound is said to be **unbounded above**.

> [!definition] Least Upper Bound
> A number $B$ is called a **least upper bound** of a nonempty set $S$ if $B$ has the following two properties:
> 1. $B$ is an upper bound for $S$.
> 2. No number less than $B$ is an upper bound for $S$.
> 
> It is common to refer the least upper bound by **supremum**, abbreviated **sup**: $$B = \sup S$$

> [!theorem]
> Two different numbers cannot be least upper bounds for the same set.

> [!axiom] The Least-Upper-Bound Axiom (Completeness Axiom)
> 10. Every nonempty set $S$ of real numbers which is bounded above has a supremum; that is, there is a real number $B$ such that $B = \sup S$.

> [!remark]
> We can define **lower bound**, **bounded below**, **smallest number** (**minimum element**), **greatest lower bound** (**infimum**) similarly.

> [!theorem]
> Every nonempty set $S$ that is bounded below has a greatest lower bound; that is, there is a real number $L$ such that $L = \inf S$.

> [!theorem]
> The set $\textbf{P}$ of positive integers $1, 2, 3, \dots$ is unbounded above.

> [!Theorem]
> For every real number $x$ there exists a positive integer $n$ such that $n > x$.

> [!theorem] Archimedean Property
> If $x > 0$ and if $y$ is an arbitrary real number, there exists a positive integer $n$ such that $nx > y$.

> [!theorem] 
> If three real numbers $a$, $x$ and $y$ satisfy the inequalities $$a \leq x \leq a + \frac{y}{n}$$ for every integer $n \geq 1$, then $x = a$.

> [!theorem]
> Let $h$ be a given positive number and let $S$ be a set of real numbers.
> 1. If $S$ has a supremum, then for some $x$ in $S$ we have $$x > \sup S - h.$$
> 2. If $S$ has an infimum, then for some $x$ in $S$ we have $$x < \inf S + h.$$

> [!theorem] Additive Property
> Given nonempty subsets $A$ and $B$ of $\mathcal R$, let $C$ denote the set $$C = \{a + b | A \in A, b \in B\}.$$
> 1. If each of $A$ and $B$ has a supremum, then $C$ has a supremum, and $$\sup C = \sup A + \sup B.$$
> 2. If each of $A$ and $B$ has an infimum, then $C$ has an infimum, and $$\inf C = \inf A + \inf B.$$

> [!theorem]
> Given two nonempty subsets $S$ and $T$ of $\mathbb R$ such that $$s \leq t$$ for every $s$ in $S$ and every $t$ in $T$. Then $S$ has a supremum, and $T$ has an infimum, and they satisfy the inequality $$\sup S \leq \inf T.$$

## Roots, Rational Powers

> [!theorem]
> Every nonnegative real number $a$ has a unique nonnegative square root. We denote this square root by $a^{1/2}$ or by $\sqrt{a}$. If $a > 0$, the negative square root is $-a^{1/2}$ or $-\sqrt{a}$.

> [!definition] $n$-th root
> If $n$ is a positive **odd** integer, then for each $x$, there is exactly one real $y$ such that $y^n = x$. This is called the $n$**-th root** of $x$ and is denoted by $$y = x^{1 / n} \quad \text{or} \quad y = \sqrt[n]{x}.$$
> If $n$ is a positive **even** number, then if $x$ is negative, there is no real $y$, if $x$ is positive then there are two real $n$-th root. The symbol $x^{1/n}$ or $\sqrt[n]{x}$ are reserved for the positive root.

> [!definition] Rational Powers
> If $r = m/n$ be a positive rational number where $m, n$ are positive integers, we define $x^r$ to be $(x^m)^{1/n}$, the $n$-th root of $x^m$, whenever this exists. If $x \neq 0$, we define $x^{-r} = 1/x^r$ whenever $x^r$ is defined.

## Absolute Value

> [!definition] Absolute Value
> If $x$ is a real number, the **absolute value** of $x$ is a nonnegative real number denoted by $|x|$ and defined as follows: $$|x| = \begin{cases}x &\text{if } x \geq 0, \\ -x &\text{if } x \leq 0.\end{cases}$$ The number $|x|$ is called the **distance** of $x$ from $0$.

> [!theorem]
> If $a \geq 0$, then $|x| \leq a$ if and only if $-a \leq x \leq a$.

> [!theorem] Triangle Inequality
> For arbitrary real numbers $x$ and $y$, we have $$|x + y| \leq |x| + |y|.$$

> [!theorem]
> For arbitrary real numbers $a_1, a_2, \dots, a_n$, we have $$|\sum_{k = 1}^n a_k| \leq \sum_{k = 1}^n |a_k|.$$

## Floor

> [!definition] Floor
> $\lfloor x \rfloor$ denotes the greatest integer $\leq x$.

> [!proposition]
> $$\lfloor nx \rfloor = \sum_{k = 0}^{n - 1} \lfloor x + \frac{k}{n} \rfloor$$

> [!proposition]
> Let $f$ be a nonnegative function whose domain is the interval $[a, b]$, where $a$ and $b$ are integers, $a < b$. Let $S$ denote the set of points $(x, y)$ satisfying $a \leq x \leq b, 0 < y \leq f(x)$. Then the number of lattice points in $S$ is $$\sum_{n = a}^b \lfloor f(n) \rfloor.$$

> [!example]
> If $a$ and $b$ are positive integers with no common factor, we have the formula $$\sum_{n = 1}^{b - 1} \lfloor \frac{na}{b} \rfloor = \sum_{n = 1}^{b - 1} \lfloor \frac{a(b - n)}{b} \rfloor = \frac{(a - 1)(b - 1)}{2}.$$
