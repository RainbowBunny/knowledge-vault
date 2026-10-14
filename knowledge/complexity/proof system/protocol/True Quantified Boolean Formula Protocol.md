Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.3.3: Protocol for TQBF: proof of Theorem 8.19.

## Definition

> [!definition] Parameters
> - $n$: Number of variable.
> - $\mathbb F$: Finite field.
> - $\Psi$: [[True Quantified Boolean Formula]] in the form:
> $$\Psi = \forall x_1 \exists x_2 \forall x_3 \dots \exists x_n \phi(x_1, \dots, x_n)$$
> - $P_\phi(x_1, \dots, x_n)$: [[Arithmetization of a Boolean formula]].

> [!definition] Statement
> Requires:: [[Linearization Operator on Polynomial]]
> 
> ---
> The prover want to convince the verifier the following statement:
> $$\forall X_1 L_{X_1} \exists X_2 L_{X_1} L_{X_2} \forall X_3 L_{X_1} L_{X_2} L_{X_3} \cdots \exists X_n L_{X_1} L_{X_2} L_{X_3} \cdots L_{X_n} P_\phi(X_1, \dots, X_n) \neq 0$$

> [!definition] Substatement
> Let $U(X_1, \dots, X_l) = \mathcal{O}g(X_1, \dots, X_k)$ for a [[Multivariate Polynomial]] $g$, value $a_1, \dots, a_k$ and a target $K$:

> [!remark]
> The original [[Sum-Check Protocol]] generalization for 
> $$\prod_{b_1 \in \{0, 1\}} \sum_{b_2 \in \{0, 1\}} \cdots \sum_{b_n \in \{0, 1\}} P_\phi(b_1, \dots, b_n) \neq 0$$
> does not work because the degree explodes.

> [!scheme] True Quantified Boolean Formula Protocol
> 
> 
> ---
> 
> - $\mathcal{O} = \exists x_1$:
> $$\begin{array}{llcl} 
\mathcal{P} & & \mathcal{V} \\[4pt] 
h(X_1) = \sum_{b_2 \in \{0, 1\}} \cdots \sum_{b_n \in \{0, 1\}} g(X_1, b_2, \dots, b_n) & \xrightarrow{h} & h(1) + h(0) \stackrel{?}{=} K; \deg(h(X_1)) \leq deg_{X_1}(g) \\
& \xleftarrow{a} & a \in \mathbb{F}
\end{array}$$
> - $\mathcal{O} = \forall x_1$:
> $$\begin{array}{llcl} 
\mathcal{P} & & \mathcal{V} \\[4pt] 
h(X_1) = \sum_{b_2 \in \{0, 1\}} \cdots \sum_{b_n \in \{0, 1\}} g(X_1, b_2, \dots, b_n) & \xrightarrow{h} & h(1) \times h(0) \stackrel{?}{=} K; \deg(h(X_1)) \leq deg_{X_1}(g) \\
& \xleftarrow{a} & a \in \mathbb{F}
\end{array}$$
> - $\mathcal{O} = L_{X_1}$:
> $$\begin{array}{llcl} 
\mathcal{P} & & \mathcal{V} \\[4pt] 
h(X_1) = \sum_{b_2 \in \{0, 1\}} \cdots \sum_{b_n \in \{0, 1\}} g(X_1, b_2, \dots, b_n) & \xrightarrow{h} & h(1) \times h(0) \stackrel{?}{=} K; \deg(h(X_1)) \leq deg_{X_1}(g) \\
& \xleftarrow{a} & a \in \mathbb{F}
\end{array}$$

 
