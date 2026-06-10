# Oracle Machines

A Turing machine with privileged access to an "oracle" that decides membership in some language in one step. The framework used to study *relativization* — how complexity-class relations change under different oracles.

> [!definition] Oracle
> An **oracle** for a language $A$ is a device that can report whether any string $w$ is a member of $A$.

> [!definition] Oracle Turing Machine
> An **oracle Turing machine** $M^A$ is a modified Turing machine that has the additional capability of querying an oracle for $A$. Whenever $M^A$ writes a string on a special **oracle tape**, it is informed whether that string is a member of $A$ in a single computation step.

> [!definition] Relativized Classes
> $\text{P}^A$ is the class of languages decidable by a polynomial-time oracle Turing machine that uses oracle $A$. The class $\text{NP}^A$ is defined similarly using a nondeterministic oracle TM.

## Relativization

The phenomenon studied: *do relations between complexity classes change when both sides use the same oracle?*

**Baker-Gill-Solovay (1975)** proved:
- There exists an oracle $A$ with $\text{P}^A = \text{NP}^A$.
- There exists an oracle $B$ with $\text{P}^B \neq \text{NP}^B$.

**Consequence**: any proof technique that *relativizes* (works in every oracle world) cannot decide $\text{P} \stackrel{?}{=} \text{NP}$. This rules out diagonalization-based attacks on the P vs NP question.

The relativization barrier was one of the first proven obstacles to a major open problem. See also:
- **Razborov-Rudich (1994)** — the natural-proofs barrier, blocking circuit lower bounds.
- **Aaronson-Wigderson (2008)** — the algebrization barrier, blocking certain stronger techniques.

## Class Constructions Built on Oracle Machines

- [[Polynomial Hierarchy]] — defined as $\Sigma_k = \text{NP}^{\Sigma_{k-1}}$, etc.
- $\text{BQP}$ vs classical classes — quantum oracle separations.
- IP-style classes — oracle access mimics interaction.

## Related

- [[Polynomial Hierarchy]] — built recursively via oracle TMs
- [[Interactive Proofs]] — IP is closely related (multi-prover oracle access)
- [[Hierarchy Theorems]] — diagonalization is the technique that *does* relativize
- [[P vs NP]] — the question that relativization can't resolve
