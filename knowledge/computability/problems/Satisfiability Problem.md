
**Boolean variables**: `TRUE`, `FALSE`.

**Boolean operations**: `AND`, `OR`, `NOT`.

**Boolean formula**: Expression involving Boolean variables and operations.

A Boolean formula is **satisfiable** if some assignment of 0s and 1s to the variables makes the formula evaluate to 1.

**Satisfiability problem**: 
$$\text{SAT} = \{\langle \phi \rangle | \phi \text{ is a satisfiable Boolean formula}\}.$$

**Literal**: Boolean variable/negated Boolean variable.

**Clause**: Literals connected with $\lor_{s}$.

**Conjunctive normal form/cnf-formula**: Several clauses connected with $\land_{s}$.

**3cnf-formula**: If all the clauses have three literals
$$3\text{SAT} = \{\langle \phi \rangle | \phi \text{ is a satisfiable 3 cnf-formula}\}.$$**Universal quantifier** $\forall$, **Existential quantifier** $\exists$ 
**Fully quantified**: Each variable of a formula appears within the scope of some quantifier.
$$\text{TQBF} = \{\langle \phi \rangle | \phi \text{ is a true fully quantified Boolean formula}\}.$$

