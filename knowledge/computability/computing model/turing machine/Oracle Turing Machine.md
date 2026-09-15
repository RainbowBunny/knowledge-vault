Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 3: Diagonalization, Section 3.4: Oracle Machines and the Limits of Diagonalization.

## Definition

> [!definition] Oracle Turing Machine
> Generalizes:: [[Turing Machine]]
> 
> ---
> An **oracle** Turing Machine is a [[Turing Machine]] $M$ that has:
> - Special read-write tape we call $M$'s **oracle tape**.
> - Three special states $q_\mathrm{query}, q_\mathrm{yes}, q_\mathrm{no}$.
> - A [[Language]] $O \subseteq \{0, 1\}^*$ that is used as the *oracle* for $M$.
> 
> When $M$ enters $q_\mathrm{query}$, the machine moves into the state $q_\mathrm{yes}$ if $q \in O$ and $q_\mathrm{no}$ if $q \notin O$, where $q$ denotes the contents of the special oracle tape. This takes only a single computation step.
> 
> For an oracle machine $M$, oracle language $O \subseteq \{0, 1\}^*$ and input $x \in \{0, 1\}^*$, then we denote the output of $M$ on input $x$ and with oracle $O$ by $M^O(x)$.


