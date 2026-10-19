Reference:
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[C x]` — Gentry, _Computing Arbitrary Functions of Encrypted Data_ (CACM): https://dl.acm.org/doi/pdf/10.1145/1666420.1666444
- `[BV x]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `[BGV]` — Brakerski, Gentry, Vaikuntanathan, _Fully Homomorphic Encryption without Bootstrapping_ (ePrint 2011/277): https://eprint.iacr.org/2011/277
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

> [!todo] Draft — replaces the old [[Fully Homomorphic Encryption]] note when you swap it in; delete this block then.

## Definition

> [!definition] Parameters
> - [[Homomorphic Encryption]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal C_E, f_\mathsf{Dec})$.

> [!definition] Fully Homomorphic Encryption `[T 2.1.4]` `[S Def 2]`
> Extends:: [[Homomorphic Encryption]]
>
> ---
> A **fully homomorphic encryption (FHE)** scheme is a [[Homomorphic Encryption|homomorphic encryption scheme]] $E$ that compactly evaluates *all* circuits: $E$ is compact (the circuit $f_\mathsf{Dec}$ has size $\mathrm{poly}(\lambda)$) and correct for $\mathcal C_E$ = all circuits over $\mathcal M$. In addition, $\mathsf{Eval}$ should cost at most $|C| \cdot \mathrm{poly}(\lambda)$ `[C §2.2]`.

## Property

> [!remark] Leveled and fully homomorphic
> `⚠️ CLAUDE – verify:` every FHE scheme $E$ gives a leveled family by taking $E^{(d)} = E$ for all $d$ (same keys, same $\mathsf{Eval}$), so FHE implies [[Leveled Fully Homomorphic Encryption|leveled FHE]]. The converse is the point of the next two items. This is my observation, not a statement from the sources.

> [!remark] Where known FHE comes from
> - From a [[Bootstrappable Encryption|bootstrappable]] scheme one gets leveled FHE with no extra assumption `[S Thm 3]` `[BV Thm 3.1]`; the construction is the [[Gentry Bootstrapping Transformation]].
> - To get a scheme whose parameters do not depend on the depth, the known route adds a circular security assumption: weak circular security of the bootstrappable scheme `[BV Thm 3.2, Def 3.8]` `[S §2]` `[T §1.3]`. See [[Key-Dependent Message Security|KDM Security]].
> - Leveled FHE can also be built **without** bootstrapping, from LWE or ring-LWE `[BGV]` (abstract only). Per its abstract, bootstrapping is then an optional optimization that makes the per-gate cost independent of the depth. I read only the abstract, so I do not state which assumption that step needs.
> - `⚠️ CLAUDE – verify:` `[BV]` is from 2011. I searched once for whether unbounded FHE from LWE without any circularity assumption is known today and found nothing conclusive, so I state only what the cited papers say.

## Security

> [!remark]
> The security notion of the definition is that of the `## Security` remark of [[Homomorphic Encryption]]. Circular security is a property of a *construction* (the self-loop in [[Gentry Bootstrapping Transformation]]), not part of the definition of FHE.

## Related

### Constructions
- [[Gentry Bootstrapping Transformation]] — its self-loop variant gives unbounded depth under [[Key-Dependent Message Security|KDM Security]]

### Properties
- [[Key-Dependent Message Security|KDM Security]]

### Siblings
- [[Leveled Fully Homomorphic Encryption]] — the depth bound is a key-generation input, not the cost
- [[Bootstrappable Encryption]] — the condition the transformation needs from a base scheme

### Prerequisites
- [[Homomorphic Encryption]]
