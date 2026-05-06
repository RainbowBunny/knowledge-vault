## Definition

> [!definition] Ring
> A **ring** is a set $R$ that has two operations, which we denote by $+$ and $\star$, satisfying the following properties:
> **Properties of $+$:**
> - **Identity Law**
> - **Inverse Law**
> - **Associative Law**
> - **Commutative Law**
> 
> Briefly, $R$ with operation $+$ is a commutative group with (additive) identity element $0$.
> 
> **Properties of $\star$:**
> - **Identity Law**
> - **Associative Law**
> - **Commutative Law** (Commutative Ring)
> 
> Briefly, $R$ with operation $\star$ is almost a commutative group with (multiplicative) identity element $1$, except that elements are not required to have multiplicative inverses.
> 
> **Properties Linking $+$ and $\star$:**
> - **Distributive Law**

### Quotient rings

> [!definition] Divisibility in Ring
> Let $a$ and $b$ be elements of a ring $R$ with $b \neq 0$. We say that $b$ **divides** $a$, or that $a$ **is divisible by** $b$, if there is an element $c \in R$ such that $$a = b \star c.$$ Similar to integer divisibility, we write $b \mid a$ to indicate that $b$ divides $a$. If $b$ does not divide $a$, then we write $b \nmid a$.

> [!definition] Unit
> Let $R$ be a ring. An element $u \in R$ is called a **unit** if it has a multiplicative inverse.

> [!definition] Irreducible
> An element $a$ of a ring $R$ is said to be **irreducible** if $a$ is not itself a unit and if in every factorization of $a$ as $a = b \star c$, either $b$ is a unit or $c$ is a unit.

> [!definition] Congruent
> Let $R$ be a ring and choose a nonzero element $m \in R$. We say that two elements $a$ and $b$ of $R$ are **congruent modulo** $m$ if their difference $a - b$ is divisible by $m$. We write $$a \equiv b \pmod m$$ to indicate that $a$ and $b$ are congruent modulo $m$.

> [!proposition] 
> Let $R$ be a ring and let $m \in R$ with $m \neq 0$. If $$a_1 \equiv a_2 \pmod m \qquad \text{and} \qquad b_1 \equiv b_2 \pmod m$$ then $$a_1 \pm b_1 \equiv a_2 \pm b_2 \pmod m \qquad \text{and} \qquad a_1 \star b_1 \equiv a_2 \star b_2 \pmod m$$

> [!definition] Congruence Class
> Let $R$ be a ring and let $m \in R$ with $m \neq 0$. For any $a \in R$, we write $\overline a$ for the set of all $a' \in R$ such that $a' \equiv a \pmod m$. The set $\overline a$ is called the **congruence class** of $a$.

> [!definition] Quotient Ring
> We denote the collection of all congruence classes by $R/(m)$ or $R/mR$. Thus $$R/(m) = R/mR = \{\overline a : a \in R\}.$$ We add and multiply congruence classes using the obvious rules $$\overline a + \overline b = \overline {a + b} \qquad \text{and} \qquad \overline a \star \overline b = \overline {a \star b}.$$ We call $R / (m)$ the **quotient ring** of $R$ by $m$.

> [!remark]
> Let $R$ be a ring with property that the only way that a product $a \cdot b$ can be $0$ is if $a = 0$ or $b = 0$. Suppose further that $R$ has only finitely many elements. Then, $R$ is a field.

