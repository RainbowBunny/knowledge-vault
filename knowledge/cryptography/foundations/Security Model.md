

## Bidirectional Ratcheted Key Exchange

> [!definition] Bidirectional Ratcheted Key Exchange (BRKE)
> A BRKE is defined for a finite key space $\mathcal K$ and an associated-data space $\mathcal{AD}$ as a triple $R = (init, send, recieve)$ of algorithms together with a state space $\mathcal S$ and a ciphertext space $\mathcal C$.
> - $init$: the randomized initialization algorithm returns a pair of states $(S_A, S_B) \in \mathcal S \times \mathcal S$.
> - $send(state_i, ad)$: the randomized sending algorithm takes a state $state_i \in \mathcal S$ and an associated-data string $ad \in \mathcal{AD}$, and produces an updated state $state_i' \in \mathcal S$, a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$.
> - $recieve(state_i, ad, c)$: the deterministic receiving algorithm takes a state $state_i \in \mathcal S$, an associated-data string $ad \in \mathcal{AD}$, and a ciphertext $c \in \mathcal C$, and either outputs an updated state $state_i' \in \mathcal S$ and a key $k \in \mathcal K$ or outputs the special symbol $\perp$ to indicate rejection.

## The Rényi divergence
>[!definition] The Rényi divergence
>Let $P$ and $Q$ are two discrete probability distributions such that $\mathsf{Supp}(P) \subseteq \mathsf{Supp}(Q)$ and $a \in (1, +\infty)$, we have the Rényi divergence of order $a$:
>$$R_a(P\|Q)=\left(\sum_{x \in \mathsf{Supp}(P)}\dfrac{P(x)^a}{Q(x)^{a-1}}\right)^{\dfrac{1}{a - 1}}$$
> For the cases $a = 2$ and $a = +\infty$ respectively, we have
>- $R_1(P \| Q) = \exp \left( \sum_{x \in \text{Supp}(P)} P(x) \log \frac{P(x)}{Q(x)} \right)$
>- $R_\infty(P \| Q) = \max_{x \in \text{Supp}(P)} \frac{P(x)}{Q(x)}$

















