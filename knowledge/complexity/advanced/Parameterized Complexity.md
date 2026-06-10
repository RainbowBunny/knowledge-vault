# Parameterized Complexity

A refined complexity theory where the input is paired with a *parameter* $k$, and we ask whether problems are tractable in $n$ when $k$ is small.

Stub. Topics to cover:

- **Class FPT** (Fixed-Parameter Tractable) — problems solvable in time $f(k) \cdot \text{poly}(n)$.
- **W-hierarchy** — $\text{W}[1] \subseteq \text{W}[2] \subseteq \cdots$ — parameterized analog of NP within FPT-style reductions.
- **Kernelization** — preprocessing to reduce input size to a function of $k$ alone.
- **Tree-width** — a structural parameter on graphs enabling many FPT algorithms.
- **Reductions** — FPT reductions, parameterized hardness proofs.

## Related

- [[Time Complexity]] — FPT refines polynomial time
- [[Fine-Grained Complexity]] — similar spirit, different parameter
