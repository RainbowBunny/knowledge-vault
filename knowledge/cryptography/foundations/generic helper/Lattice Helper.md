
## Asymptotic analysis toolkits

## Gaussians over Lattices

### Discrete Gaussian

> [!definition] Discrete Gaussian
> For a full-rank lattice $\Lambda \subset \mathbb{R}^n, s > 0$ and $\mathbf{z} \in \mathbb{R}^n$, the mass function of discrete Gaussian distribution $D_{\Lambda + \mathbf{z},s}$ is defined as:
> $$\Pr_{X \sim D_{\Lambda + \mathbf{z}, s}}[X = \mathbf{x}] = \dfrac{\rho_s(\mathbf{x})}{\rho_s(\Lambda + \mathbf{z})}$$
> where $\rho_s(\mathbf{x}) := \exp(-\pi\|\mathbf{x}/s\|^2)$ for $s> 0$

> [!theorem] Strong tail bound
> For $\mathcal{L} \subset \mathbb{R}^n$ a full-rank lattice, $r \ge 1, s > 0$ and $\mathbf{X} \sim D_{\mathcal{L}+\mathbf{t},s}$, we have
> $$ \Pr \left[ \|\mathbf{X}\| > rs\sqrt{\frac{n}{2\pi}} \right] \le \frac{\rho_s(\mathcal{L})}{\rho_s(\mathcal{L} + \mathbf{t})} r^n e^{-\frac{n}{2}(r^2 - 1)} \le \frac{\rho_s(\mathcal{L})}{\rho_s(\mathcal{L} + \mathbf{t})} e^{-\frac{n}{2}(r - 1)^2}$$

> [!remark]
> For cryptography usage, $r$ is often chosen to be $\mathcal{w}(\sqrt{\log \lambda})$, where $\lambda$ is security parameter. In such case, the theorem yields:
> $$ \Pr \left[ \|\mathbf{X}\| > s\sqrt{n} \cdot\mathcal{w}(\sqrt{\log \lambda}) \right] \le \mathsf{negl}(\lambda)$$

### High-Dimensional Normal over $\mathbb Z^m$

> [!definition] Continuous Normal Distribution
> The continuous Normal distribution over $\mathbb R^m$ centered at $v$ with standard deviation $\sigma$ is defined by the function $$\rho^m_{v, \sigma}(x) = (\frac{1}{\sigma \sqrt{2 \pi}})^m e^{\frac{-||x - v||^2}{2 \sigma^2}}$$

> [!definition] Discrete Normal Distribution
> The discrete Normal distribution over $\mathbb Z^m$ centered at some $v \in \mathbb Z^m$ with standard deviation $\sigma$ is defined as $D^m_{v, \sigma}(x) = \rho^m_{v, \sigma}(x) / \rho^m_\sigma(\mathbb Z^m)$.

> [!lemma]
> For any vector $v \in \mathbb R^m$ and any $\sigma, r > 0$, $$P[|\langle z, v \rangle| > r; z \leftarrow D^m_\sigma] \leq 2e^{-\frac{r^2}{2||v||^2 \sigma^2}}.$$

> [!lemma]
> 1. For any $k > 0, P[|z| > k \sigma; z \leftarrow D^1_\sigma] \leq 2e^{-\frac{k^2}{2}}$,
> 2. For any $z \in \mathbb Z^m$, and $\sigma \geq 3 / \sqrt{2 \pi}, D^m_\sigma(z) \leq 2^{-m}$.
> 3. For any $k > 1, P[||z|| > k \sigma \sqrt{m}; z \leftarrow D^m_\sigma] < k^m e^{\frac{m}{2}(1 - k^2)}$.

> [!lemma]
> For any $v \in \mathbb Z^m$, if $\sigma = \omega(||v|| \sqrt{\log m})$, then $$P[D^m_\sigma(z) / D^m_{v, \sigma}(z) = O(1); z \leftarrow D^m_\sigma] = 1 - 2^{-\omega(\log m)},$$ and more specifically, for any $v \in \mathbb Z^m$, if $\sigma = \alpha ||v||$ for any positive $\sigma$, then $$P[D^m_\sigma (z) / D^m_{v, \sigma}(z) < e^{12 / \alpha + 1 / (2 \alpha^2)}; z \leftarrow D^m_\sigma] > 1 - 2^{-100}.$$

### Rejection Sampling

> [!theorem] Rejection Sampling (Gaussian Case)
> Let $V$ be a subset of $\mathbb Z^m$ in which all elements have norms less than $T, \sigma$ be some element in $\mathbb R$ such that $\sigma = \omega(T \sqrt{\log m})$, and $h: V \rightarrow \mathbb R$ be a probability distribution. Then there exists a constant $M = O(1)$ such that the distribution of the following algorithm $\mathcal A$:
> 1. $v \leftarrow h$
> 2. $z \leftarrow D^m_{v, \sigma}$
> 3. Output $(z, v)$ with probability $\min(\frac{D^m_\sigma(z)}{MD^m_{v, \sigma}}, 1)$
> 
> is within [[Statistical Distance|statistical distance]] $\frac{2^{-\omega(\log m)}}{M}$ of the distribution of the following algorithm $\mathcal F$:
> 1. $v \leftarrow h$
> 2. $z \leftarrow D^m_\sigma$
> 3. Output $(z, v)$ with probability $1/M$
> 
> Moreover, the probability that $\mathcal A$ outputs something is at least $\frac{1 - 2^{\omega(\log m)}}{M}$.
> More concretely, if $\sigma = \alpha T$ for any positive $\alpha$, then $M = e^{12 / \alpha + 1 / (2 \alpha^2)}$, the output of algorithm $\mathcal A$ is within statistical distance $\frac{2^{-100}}{M}$ of the output of $\mathcal F$, and the probability that $\mathcal A$ outputs something is at least $\frac{1 - 2^{-100}}{M}$.

> [!lemma] Rejection Sampling (General Case)
> Let $V$ be an arbitrary set, and $h: V \rightarrow \mathbb R$ and $f: \mathbb Z^m \rightarrow \mathbb R$ be probability distributions. If $g_v : \mathbb Z^m \rightarrow \mathbb R$ is a family of probability distributions indexed by all $v \in V$ with the property that $$\exists M \in \mathbb R \text{ such that } \forall v, P[M g_v(z) \geq f(z); z \leftarrow f] \geq 1 - \epsilon$$ then the distribution of the output of the following algorithm $\mathcal A$:
> 1. $v \leftarrow h$
> 2. $z \leftarrow g_v$
> 3. Output $(z, v)$ with probability $\min(\frac{f(z)}{M g_v(z)}, 1)$
> 
> is within [[Statistical Distance|statistical distance]] $\epsilon / M$ of the distribution of the following algorithm $\mathcal F$:
> 1. $v \leftarrow h$
> 2. $z \leftarrow f$
> 3. Output $(z, v)$ with probability $1 / M$.
> 
> Moreover, the probability that $\mathcal A$ outputs something is at least $(1 - \epsilon) / M$.

## The Rényi Divergence

>[!definition] The Rényi divergence
>Let $P$ and $Q$ are two discrete probability distributions such that $\mathsf{Supp}(P) \subseteq \mathsf{Supp}(Q)$ ( $\text{Supp}(P) = \{x | P(x) \neq 0 \}$) and $a \in (1, +\infty)$, we have the Rényi divergence of order $a$:
>$$R_a(P\|Q)=\left(\sum_{x \in \mathsf{Supp}(P)}\dfrac{P(x)^a}{Q(x)^{a-1}}\right)^{\dfrac{1}{a - 1}}$$
> For the cases $a = 2$ and $a = +\infty$ respectively, we have
>- $R_1(P \| Q) = \exp \left( \sum_{x \in \text{Supp}(P)} P(x) \log \frac{P(x)}{Q(x)} \right)$
>- $R_\infty(P \| Q) = \max_{x \in \text{Supp}(P)} \frac{P(x)}{Q(x)}$

## Related

- [[Statistical Distance]] — the math-side distance these lemmas are stated in
- [[Discrete Probability]] / [[Continuous Probability]] — the general distribution catalogs these were extracted from
