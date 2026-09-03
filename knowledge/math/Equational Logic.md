Reference:
- https://www.sciencedirect.com/science/article/pii/S002198007080014X (Birkhoff–Lipson 1970)
- https://arxiv.org/pdf/2111.07936 (Birkhoff completeness, many-sorted, formalized)

## Intuition

The fragment of logic where every axiom is an equation between terms — no connectives, no ∃, and only implicit ∀. It looks tiny; Birkhoff's theorems say it is exactly the right size for algebra, and it is why the magma → group → ring chain composes so cleanly in this vault.

## Definition

> [!definition] Equational Theory
> Fix a signature of operation symbols. An **equational theory** is a set of equations $s = t$ between terms, read universally quantified. A structure satisfying all of them is a **model**; the class of all models is a **variety**.

## Property

> [!theorem] Birkhoff
> - **Completeness**: an equation follows from a theory iff it is derivable by the rules of equational reasoning (reflexivity, symmetry, transitivity, congruence, substitution).
> - **HSP**: a class of algebras is a variety iff it is closed under Homomorphic images, Subalgebras, and Products.

> [!remark] Which vault structures are varieties
> [[Magma]], [[Semigroup]], [[Monoid]], [[Group]], [[Abelian Group]], [[Ring]], [[Commutative Ring]] — every row of the closure table. **Not** [[Field]]: "every *nonzero* element has an inverse" is conditional, not equational, and indeed fields are not closed under products. Orders satisfy first-order axioms that are not equations ([[Antisymmetry]] has an implication). The tier boundary is exactly here.