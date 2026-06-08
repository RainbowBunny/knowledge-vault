## Eigenvalues and Eigenvectors

> [!proposition]
> Suppose $T \in \mathcal L(V)$. Let $\lambda_1, \dots, \lambda_m$ denote the distinct eigenvalues of $T$. Then the following are equivalent:
> 1. $T$ has a diagonal matrix with respect to some basis of $V$;
> 2. $V$ has a basis consisting of eigenvectors of $T$;
> 3. There exist one-dimensional subspaces $U_1, \dots, U_n$ of $V$, each invariant under $T$, such that $$V = U_1 \oplus \cdots \oplus U_n;$$
> 4. $V = \text{null}(T - \lambda_1 I) \oplus \cdots \oplus \text{null}(T - \lambda_m I);$
> 5. $\dim V = \dim \text{null}(T - \lambda_1 I) + \cdots + \dim \text{null} (T - \lambda_m I).$
> 6. Every generalized eigenvector of $T$ is an eigenvector of $T$.
> 7. The minimal polynomial of $T$ has no repeated roots.

### Invariant Subspaces

> [!definition] Invariant Subspaces
> For $T \in \mathcal L(V)$ and $U$ is a subspace of $V$, we say that $U$ is **invariant** under $T$ if $u \in U$ implies $T(u) \in U$ and denote this operator by $T|_U$.

> [!definition] Eigenvalue
> A scalar $\lambda \in \mathbb F$ is called an **eigenvalue** of $T \in \mathcal L(V)$ if there exists a nonzero vector $u \in V$ such that $T(u) = \lambda u$.

> [!definition] Eigenvector
> Suppose $T \in \mathcal L(V)$ and $\lambda \in \mathbb F$ is an eigenvalue of $T$. A vector $u \in V$ is called an **eigenvector** of $T$ (corresponding to $\lambda$) if $T(u) = \lambda u$.

> [!remark]
> The set of eigenvector of $T \in \mathcal L(V)$ corresponding to $\lambda$ equals $\text{null } (T - \lambda I)$. 

> [!theorem]
> Let $T \in \mathcal L(V)$. Suppose $\lambda_1, \dots, \lambda_m$ are distinct eigenvalues of $T$ and $v_1, \dots, v_m$ are corresponding nonzero eigenvectors. Then $(v_1, \dots, v_m)$ is linearly independent.

> [!corollary]
> Each operator on $V$ has at most $\dim V$ distinct eigenvalues.

> [!proposition]
> Suppose $\mathbb F = \mathbb C, T \in \mathcal L(V), p \in \mathcal P(\mathbb C),$ and $a \in \mathcal C$. Then, $a$ is an eigenvalue of $\mathcal p(T)$ if and only if $a = \mathcal p(\lambda)$ for some eigenvalue $\lambda$ of $T$.
> The result does not hold if $\mathbb F = \mathbb R$.

### Polynomials Applied to Operators




### Invariant Subspaces on Real Vector Space

> [!theorem]
> Every operator on a finite-dimensional, nonzero, real vector space has an invariant subspace of dimension $1$ or $2$.

> [!remark]
> There exist real numbers $a_0, \dots, a_n$, not all $0$, such that $$0 = a_0 v + a_1 T(v) + \cdots + a_n T^n(v).$$ Thus we have $$0 = c(T - \lambda_1 I) \dots (T - \lambda_m I) (T^2 + \alpha_1 T + \beta_1 I) \dots (T^2 + \alpha_m T + \beta_m I) (v).$$

> [!theorem]
> Every operator on an odd-dimensional real vector space has an eigenvalue.

> [!proposition]
> Suppose $S, T \in \mathcal L(V)$. Then, $ST$ and $TS$ have the same eigenvalues.

