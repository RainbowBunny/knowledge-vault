## Basic Definition

> [!definition] Probabilistic Polynomial Time (PPT)
> An algorithm $\mathcal A$ is **PPT** if it may use random coins and there is a polynomial $p$ such that on every input of security parameter $\lambda$, $\mathcal A$ halts within $p(\lambda)$ steps.

> [!remark]
> "Efficient adversary" in this vault means PPT. It is the adversary class of the *computational* row of the [[Security Game]] table; the unbounded class gives the perfect and statistical rows. Complexity-theoretic home: [[Randomized Complexity]].