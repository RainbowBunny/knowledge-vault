## Definition

> [!definition] Efficient universal Turing Machine
> - (Existence of Interpreter) There exists a [[Turing Machine]] $\mathcal{U}$ such that:
> $$\forall x, \alpha \in \{0, 1\}^*, \mathcal{U}(x, \alpha) = M_\alpha(x),$$ 
> where $M_\alpha$ denotes the Turing Machine represented by $\alpha$.
> - (Existence of Efficient Interpreter) Moreover, if $M_\alpha$ halts on input $x$ within $T$ steps then $\mathcal{U}(x, \alpha)$ halts within $CT \log{T}$ steps, where $C$ is a number independence of $|x|$ and depending only on $M_\alpha$'s alphabet size, number of tapes, and number of states.


