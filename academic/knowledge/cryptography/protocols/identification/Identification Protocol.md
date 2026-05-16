
| Term                                                           | Reference                                                                       |                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------- |
| Attack Game 18.1 (Secure identification: direct attacks)       | [[#Password Protocols\|direct attack]]                                          | $\text{ID1adv}$  |
| Attack Game 18.2 (Secure identification: eavesdropping attack) | [[#Security Against Eavesdropping\|eavesdropping attack]]                       | $\text{ID2adv}$  |
| Attack Game 18.3 (Secure identification: active attacks)       | [[#Security Against Active Attacks\|active attacks]]                            | $\text{ID3adv}$  |
| Attack Game 19.1 ($r$-impersonating eavesdropping attack)      | [[#Repeated Impersonating Attacks\|r-impersonation eavesdropping attack]]       | $\text{rID2adv}$ |
| Attack Game 19.2 (One-way key generation)                      | [[#Identification and Signatures from Sigma Protocols\|one-way key generation]] | $\text{OWadv}$   |
|                                                                |                                                                                 |                  |

> [!definition] Identification Problem
> Party $A$ wished to identify itself to party $B$ to gain access to resources available at $B$.

## Interactive Protocol

> [!definition] Interactive Protocol
> - A protocol may be run many times. Each such protocol run is called a **protocol instance**.
> - When a party executes a protocol instance, it starts by supplying **input value**, which defines the **initial configuration** of the protocol instance for that party.
> - The interaction can be modelled by an **interactive protocol algorithm**, which is an efficient probabilistic algorithm $I$ that takes as input a pair $(config_{\text{old}}, data_{\text{in}})$, where $config_{\text{old}}$ is an encoding of the current configuration and $data_{\text{in}}$ is an encoding of the incoming message; and outputs a pair $(config_{\text{new}}, data_{\text{out}})$ where $(config_{\text{new}})$ is an encoding of the new configuration, and $data_{\text{out}}$ encodes an outgoing message. 
> - The party iterates this as many times required by the protocol, until some **terminal configuration** is reached. This terminal configuration may specify an **output value**, which maybe used by the party, presumably in some higher-level protocol.

## ID Protocol

> [!definition] Identification (ID) Protocols
> The identification problem involves two parties, a **prover** and a **verifier**. The prover has a **secret key** $sk$ that it uses to convince the verifier of its identity. The verifier has a corresponding **verification key** $vk$ that it uses to confirm the prover's claim.

> [!definition] ID Protocol
> An **identification protocol** is a triple $\mathcal I = (G, P, V)$.
> - $G$ is a probabilistic, **key generation** algorithm, that takes no input, and output $(vk, sk)$, where $vk$ is called the **verification key** and $sk$ is called the **secret key**.
> - $P$ is an interactive protocol algorithm called the **prover**, which takes as input a secret key $sk$, as output by $G$.
> - $V$ is an interactive protocol algorithm called the **verifier**, which takes as input a verification key $vk$, as output by $G$, and which outputs `accept` or `reject`.
> 
> We require that when $P(sk)$ and $V(vk)$ interact with one another, $V(vk)$ always outputs `accept`. That is, for all possible outputs $(vk, sk)$ of $G$, if $P$ is initialized with $sk$, and $V$ is initialized with $vk$, then with probability $1$, at the end of the interaction between $P$ and $V$, $V$ outputs `accept`.

> [!definition] Attack models for ID Protocol
> - **Direct Attacks**: The adversity cannot eavesdrop on conversations. Then using no information other than what is publicly available, the adversary must somehow impersonate the prover to the verifier. A simple password protocol is sufficient to defend against such direct attacks.
> - **Eavesdropping Attacks**: The adversary can eavesdrop on the channel and obtain the transcript of several interactions between the prover and the verifier. In this case, the simple password protocol is insecure. However, a slightly more sophisticated protocol based on one-time passwords is secure.
> - **Active Attacks**: The adversary uses the interaction to try and learn something that will let it later impersonate the prover to the verifier. Identification protocols secure against such active attacks require interaction between the prover and verifier. They use a technique called challenge-response.
> - **Concurrent vs Sequential Attacks**: Note that in the active probing phase of the attack game, we allow the adversary to interact concurrently with many instances of the prover. One could consider a weaker attack model in which these interactions must be run sequentially. However, all of the protocols we consider achieve security in this stronger, concurrent attack model.

> [!proposition] Type of ID Protocol
> - **Secret vs Public Verification Keys**: In some ID protocols the verifier must keep its verification key $vk$ secret, while in the other protocols $vk$ can be public. Clearly protocols where $vk$ can be public are preferable since no damage is caused if the verifier is compromised.
> - **Stateless vs Stateful Protocol**: Ideally, $vk$ and $sk$ should not change after they are chosen at setup time. In some protocols, however, $vk$ and $sk$ are updated every time the protocol executes: the prover updates $sk$ and the verifier updates $vk$. Protocols where $vk$ and $sk$ are fixed forever are called **stateless**. Protocols where $vk$ and $sk$ are updated are called **stateful**. Some stateful protocols provide higher levels of security at lower cost than their stateless counterparts. However, stateful protocols can be harder to use because the prover and verifier must remain properly synchronized.
> - **One-sided vs mutual identification**: **One-sided identification** problem is Bob wishes to verify Alice's identity. **Mutual identification** is Bob also identifies itself to Alice.

> [!remark] Security and Limitation of Identification Protocols
> - Identification protocols are designed to prevent an adversary from impersonating Alice without Alice's assistance. When defining the security of the protocols, we may allow the adversary to eavesdrop and possibly interact with Alice; however, when it comes time to impersonate Alice, the adversary must do so without communicating with Alice.
> - ID protocols can be vulnerable to a man in the middle (MiTM) attack.

> [!proposition] Keeping $vk$ secret
> If $vk$ is kept secret, then we must now allow the adversary to interact with the verifier, since such interactions could potentially leak information about $vk$. Therefore, in the active probing phase, we allow the adversary to interact concurrently with multiple instances of both the prover and the verifier. When interacting with an instance of the verifier, the adversary learns if the verifier outputs `accept` or `reject`. In addition, during the impersonation attempt, we let the adversary interact concurrently with several verifiers, and the adversary wins the game if at least one of these verifiers accepts.

