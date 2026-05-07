

**Contribution**:
1. **Demonstrating the power of hybrid models**: Show the potential of a hybrid human-AI model in tackling real, highly complex open problems across a diverse set of scientific and mathematical domains.
2. **Advancing state-of-the-art science**: Make concrete, notable contributions to real problems in science, yielding novel results such as resolving conjectures, improving algorithmic bounds, and identifying critical flaws in literature.
3. **Showcasing the future of scientific discovery**: Illustrate what the future of research looks like in practice. By detailing novel workflows, human-AI collaboration techniques, and interactive problem-solving strategies, highlight the real implications for how science is likely to be conducted.

**Technique**:
- **Agentic Execution Loops**: Moving beyond manual chat interfaces, models can be embedded in automated "neuro-symbolic" pipelines. In these setups, the AI proposes a mathematical solution, writes code to numerically verify it, and automatically ingests execution errors to self-correct and autonomously prune invalid mathematical branches.
- **Deep Technical Review and Bug Detection**: Beyond constructive tasks, AI models can act as adversarial reviewers. (Detected a fatal flaw in SNARGs from LWE)
- **Deep Literature Synthesis and Connection**: AI models can identify obscure connections between disparate fields (e.g., linking Steiner trees to the Kirszbraun Extension Theorem) that human experts might overlook.
- **Counterexample Generation**: Models are adept at constructing counterexamples to refute plausible conjectures, saving researchers from pursuing dead ends.
- **Algorithmic Insight and Optimization**: In algorithmic research, AI can propose novel data structures or analysis techniques (e.g., adapting quadtrees for different norms) to improve time complexity bounds.
- **Automated Proof Generation and Verification**: For well-defined subproblems, AI can generate rigorous proofs, sometimes requiring minimal human intervention, or verify complex manual derivations.
- **Interactive Refinement**: A recurring theme is the interactive "conversation" where the researcher guides the model, correcting errors and refining the problem statement, which often leads to the final solution. 
- **Theoretical Justification of Heuristics**: AI models can bridge the gap between empirical success and theory by deriving rigorous justifications for heuristic methods, such as characterizing the implicit regularization induced by specific architectural choices like the Self-regularized Gumbel Sigmoid.

## Technique for AI-Assisted Research

### Iterative Prompting and Refinement

- **Initial Board Query**: Start by asking the model to digest a relevant paper or problem statement to gauge its understanding.
- **Specific Sub-tasks**: Break down the main problem into smaller, verifiable lemmas or calculations.
- **Error Correction**: When the model makes a mistake (e.g., a wrong constant or invalid assumption), pointing it out specifically often leads to a correct and sometimes more elegant solution in the next turn.
- **Scaffolding**: Providing the model with a high-level proof strategy or "scaffold" allows it to fill in the technical details effectively.
- **Adversarial Self-Correction for Review**: When tasked with reviewing complex proofs, standard prompts often yield superficial results. A rigorous protocol instructing the model to:
	1. Generate an initial review.
	2. Critique its own findings for hallucinations.
	3. Iteratively refine the logic, enables deep technical critique.

### Cross-Pollination of Ideas

As models have ingested vast amounts of literature across all fields:
- **Finding Analogies**: Identifying similar problems in different domains (e.g., applying techniques from computational geometry to graph theory).
- **Retrieving obscure theorems**: Bringing relevant but less-known theorems to the researcher's attention (e.g., Stone-Weierstrass or Kirszbraun Extension Theorem) to bridge gaps in a proof.

### Simulation and Counterexample Search

For conjectures, models can be tasked to:
- **Construct Counterexamples**: Generating specific instances (graphs, matrices, set systems) that violate a proposed conjecture.
- **Verify Small Cases**: Writing code to computationally verify a conjecture for small $n$, providing empirical evidence before attempting a general proof.

Example with [[Submodular Welfare Problem]]:
Let $\pi = (\pi_1, \pi_2, \pi_3, \dots, \pi_n)$ be a permutation of $n$ items.

> [!definition] Permutation Variants
> Fix a permutation $\pi$.
> - Let $\pi^{Move, i}$ be the permutation achieved by moving the item $\pi_i$ to the end of the sequence: $$\pi^{Move, i} = (\pi_1, \dots, \pi_{i - 1}, \pi_{i + 1}, \dots, \pi_n, \pi_i)$$
> - Let $\pi^{Copy, i}$ be the sequence of $n + 1$ items achieved by copying $\pi_i$ to the end without removing the original $\pi_i$: $$\pi^{Copy, i} = (\pi_1, \dots, \pi_{i - 1}, \pi_i, \pi_{i + 1}, \dots, \pi_n, \pi_i)$$

> [!definition] MG
> Let $\text{MG}(k, \sigma)$ denote the marginal gain that the Greedy algorithm obtains by allocating the $k$-th arriving item in a sequence $\sigma$. Let $\mathbb S_n$ be the set of all $n!$ permutations.

> [!conjecture]
> For any instance of the online submodular welfare maximization problem, $$\mathbb E_{\pi \sim \mathbb S_n}[\sum_{i = 1}^n \text{MG}(n + 1, \pi^{Copy, i})] \leq \mathbb E_{\pi \sim \mathbb S_n}[\sum_{i = 1}^n \text{MG}(n, \pi^{Move, i})]$$

- **Refutation Strategy**: The model independently selected the minimal non-trivial dimensions ($n = 3$ items, $m = 2$ agents).
- **Autonomous Construction**: In a single output, the model successfully defined the specific, valid submodular valuation functions and the $\varepsilon$-perturbation required to strictly break the bound. 
- **Automated Verification**: Without human intervention, the model correctly performed the tedious calculations of expected marginal gains across all $3! = 6$ permutations to formally verify the violation. 





### Formalization and Rigor Checks

Hallucinate is a problem, but models are increasingly capable:
- **Proof Sketch to Formal Proof**: Asking the model to expand a high-level sketch into a rigorous proof.
- **Sanity Checking**: Using the model to check consistent usage of notation or to verify that all conditions of a theorem are met.
- **Mathematical Derivation**: Researchers can offload the mechanical heavy lifting of complex derivations to the model, such as simplifying expressions, computing limits, or solving integrals, allowing them to focus on the high-level logic.

### Interactive Proof Construction with External Validation

A powerful techniques involves using the model to identify necessary external theorems and then validating those theorems with external sources.
- **Identifying Dependencies**: Asking the model to list all external theorems required for a proof.
- **External Verification**: The researcher finds the formal statements of these theorems and feeds them back to the model.
- **Self-Contained Proof Generation**: The model then incorporates these verified statements to generate a rigorous, self-contained proof.

### Agentic Tool-Use and Automated Feedback

Pipeline:
- **Symbolic Proposal**: The LLM generates a mathematical hypothesis or intermediate expression.
- **Code Generation**: The LLM autonomously writes an executable script (e.g., in Python) to evaluate its proposed math against a known numerical baseline.
- **Automated Feedback**: The system executes the code. If the code fails, hits a runtime error, or reveals numerical instability (such as catastrophic cancellation), the automated harness captures the exact execution traceback and injects it back into the LLM's context window.

### Human-AI Collaboration Dynamics


- **Selection and Refinement**: Models are capable of generating a high volume of diverse mathematical statements. Human expertise is valuable for filtering these outputs and identifying the most promising directions for further investigation.
- **Iterative Guidance**: While models can solve some problems in a single shot, tackling deep open problems is often most successful through an iterative process. The researcher guides the model, refining the problem statement and narrowing the focus to achieve the desired result.
- **Standard Verification**: As with any research collaboration, the AI can make mistakes, and AI-generated proofs and counterexamples benefit from rigorous verification. The model serves as an excellent accelerator for ideation and drafting, while the researcher validates the mathematical correctness.
- **Optimizing Context**: Performance is often optimized by proving clear, self-contained definitions, particularly when using highly specialized notation that may deviate from standard literature.
- **Leverage Literature**: We found that incorporating relevant papers directly into the context significantly enhanced the model's ability to construct correct proofs for specialized domains.
- **Context De-Identification**: The model sometimes avoids non-trivial machinery, treating such proofs as non-elementary, or it may do so because the prompt steers it toward conservatism to avoid hallucinations, causing it to abandon an otherwise viable approach. Separately, on occasion, when shown the paper as context in the prompt, it recognizes the statement to prove as a conjecture in the paper and refuses to attempt it on the grounds that it is an open problem. One way to bypass both issues is via context de-identification (remove the paper and provide only the problem statement and definitions), after which the model typically engages.

