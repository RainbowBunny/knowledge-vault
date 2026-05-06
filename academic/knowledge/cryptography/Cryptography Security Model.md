

## Bidirectional Ratcheted Key Exchange

> [!definition] Bidirectional Ratcheted Key Exchange (BRKE)
> A BRKE is defined for a finite key space $\mathcal K$ and an associated-data space $\mathcal{AD}$ as a triple $R = (init, send, recieve)$ of algorithms together with a state space $\mathcal S$ and a ciphertext space $\mathcal C$.
> - $init$: the randomized initialization algorithm returns a pair of states $(S_A, S_B) \in \mathcal S \times \mathcal S$.
> - $send(state_i, ad)$: the randomized sending algorithm takes a state $state_i \in \mathcal S$ and an associated-data string $ad \in \mathcal{AD}$, and produces an updated state $state_i' \in \mathcal S$, a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$.
> - $recieve(state_i, ad, c)$: the deterministic receiving algorithm takes a state $state_i \in \mathcal S$, an associated-data string $ad \in \mathcal{AD}$, and a ciphertext $c \in \mathcal C$, and either outputs an updated state $state_i' \in \mathcal S$ and a key $k \in \mathcal K$ or outputs the special symbol $\perp$ to indicate rejection.

