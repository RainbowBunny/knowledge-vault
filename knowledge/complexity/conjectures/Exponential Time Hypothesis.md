# Exponential Time Hypothesis (ETH) and SETH

Quantitative refinements of $\text{P} \neq \text{NP}$ that pin down *how much* time NP-complete problems should need. Introduced by Impagliazzo-Paturi (2001) and Impagliazzo-Paturi-Zane (2001).

## ETH

> [!conjecture] Exponential Time Hypothesis (ETH)
> 3-SAT has no algorithm running in time $2^{o(n)}$, where $n$ is the number of variables.

ETH is strictly stronger than $\text{P} \neq \text{NP}$. It rules out not just polynomial but also sub-exponential algorithms for 3-SAT.

## SETH

> [!conjecture] Strong Exponential Time Hypothesis (SETH)
> For every $\epsilon > 0$, there exists $k$ such that $k$-SAT cannot be solved in time $2^{(1 - \epsilon) n}$, where $n$ is the number of variables.

SETH is the strongest standard form: as $k \to \infty$, the best $k$-SAT algorithm approaches brute-force $2^n$.

## Why ETH / SETH Matter

These conjectures power **fine-grained complexity**: they give *conditional lower bounds* for problems where unconditional bounds are unknown.

Examples of conditional lower bounds under SETH:
- **All-pairs shortest paths**: $O(n^{3-\epsilon})$ is impossible for any $\epsilon > 0$ (under SETH).
- **Edit distance**: $O(n^{2-\epsilon})$ is impossible.
- **Orthogonal vectors problem**: $O(n^{2-\epsilon})$ is impossible.

These match the best known algorithms, so SETH-based lower bounds say the textbook algorithms are essentially optimal.

## Implications

If $\text{P} = \text{NP}$, both ETH and SETH are false. So:
$$\text{SETH} \implies \text{ETH} \implies \text{P} \neq \text{NP}.$$

The reverse implications are not known.

## Related

- [[P vs NP]] — the weaker form
- [[Time Complexity]] — definitions of P, NP, sub-exponential
- [[Fine-Grained Complexity]] — the framework that uses ETH/SETH
