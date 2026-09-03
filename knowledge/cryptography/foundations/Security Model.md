

## Bidirectional Ratcheted Key Exchange

> [!definition] Bidirectional Ratcheted Key Exchange (BRKE)
> A BRKE is defined for a finite key space $\mathcal K$ and an associated-data space $\mathcal{AD}$ as a triple $R = (init, send, recieve)$ of algorithms together with a state space $\mathcal S$ and a ciphertext space $\mathcal C$.
> - $init$: the randomized initialization algorithm returns a pair of states $(S_A, S_B) \in \mathcal S \times \mathcal S$.
> - $send(state_i, ad)$: the randomized sending algorithm takes a state $state_i \in \mathcal S$ and an associated-data string $ad \in \mathcal{AD}$, and produces an updated state $state_i' \in \mathcal S$, a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$.
> - $recieve(state_i, ad, c)$: the deterministic receiving algorithm takes a state $state_i \in \mathcal S$, an associated-data string $ad \in \mathcal{AD}$, and a ciphertext $c \in \mathcal C$, and either outputs an updated state $state_i' \in \mathcal S$ and a key $k \in \mathcal K$ or outputs the special symbol $\perp$ to indicate rejection.



## One-wayness CPA (OW-CPA)

> [!definition] OW-CPA
> The adversary is given 
> $$pk, c^* = \mathsf{ENC}(pk, m^*)$$
> Security:
> $$\Pr[\mathcal{A}(pk,c^*) = m^*] < \mathsf{negl}(\lambda)$$

## One-wayness PCA

> [!definition] OW-PCA
> Same as OW-CPA with an additional additional oracle answer:
> $$\mathsf{Pco}(c,m)=
\begin{cases}
1, & \text{if } \mathsf{Dec}(sk,c)=m,\\
0, & \text{otherwise}.
\end{cases}$$
> Security:
> $$\Pr[\mathcal{A}(pk,c^*) = m^*] < \mathsf{negl}(\lambda)$$




## IND-CPA Expriment

> [!definition] $\mathbf{G}^\mathsf{IND-CPA}_{\mathcal{A},\mathsf{P}}$
> 1: $(pk,sk) \leftarrow \mathsf{Gen}$
> 2: $b \leftarrow^\$ \{0,1\}$
> 3: $(m_0^*,m_1^*) \leftarrow \mathcal{A}(pk)$
> 4: $c := \mathsf{Enc}_{pk}(m_b^*)$
> 5: $b'\leftarrow \mathcal{A}(pk, c^*)$
> 6: __return__ $b'=b$

## IND-CCA Kem Expriment

> [!definition] $\mathbf{G}^{\mathsf{IND\text{-}CCA}}_{\mathcal{A},\mathsf{KEM}}$
>
> | $\mathbf{G}^{\mathsf{IND\text{-}CCA}}_{\mathcal{A},\mathsf{KEM}}$ | $\mathsf{oDeca}(c)$ |
> |---|---|
> | 1: $(pk,sk) \leftarrow \mathsf{Gen}$ <br> 2: $b \leftarrow^\$ \{0,1\}$ <br> 3: $(k_0,c^*) \leftarrow \mathsf{Enca}(pk)$ <br> 4: $k_1 \leftarrow^\$ \mathcal{K}$ <br> 5: $b' \leftarrow \mathcal{A}^{\mathsf{oDeca}}(pk,c^*,k_b)$ <br> 6: **return** $b'=b$ | 1: **if** $c=c^*$ <br> 2: $\quad$ **return** $\bot$ <br> 3: **else return** $\mathsf{Deca}(sk,c)$ |

 














