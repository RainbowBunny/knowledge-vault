Reference:
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[BV x]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `[BGV]` — Brakerski, Gentry, Vaikuntanathan, _Fully Homomorphic Encryption without Bootstrapping_ (ePrint 2011/277): https://eprint.iacr.org/2011/277
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Homomorphic Encryption]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal C_E, f_\mathsf{Dec})$.
> - $\Gamma$: a fixed set of gates with inputs and outputs in $\mathcal M$ `[S Def 3]`.
> - $d \in \mathbb Z^+$: the depth bound.

> [!definition] Leveled Fully Homomorphic Encryption `[T 2.1.5]` `[S Def 3]`
> Requires:: [[Homomorphic Encryption]]
>
> ---
> A family $\{E^{(d)} : d \in \mathbb Z^+\}$ of [[Homomorphic Encryption|homomorphic encryption schemes]] is **leveled fully homomorphic** if
> 1. all members share the same decryption circuit $f_\mathsf{Dec}$;
> 2. $E^{(d)}$ compactly evaluates all circuits of depth at most $d$ over $\Gamma$ (that is, $\mathcal C_E$ of $E^{(d)}$ is that class);
> 3. the cost of the algorithms of $E^{(d)}$ is polynomial in $\lambda$, in $d$ and, for $\mathsf{Eval}$, in $|C|$.

> [!remark] Requires, not Extends
> `⚠️ CLAUDE – verify:` by the direction test in [[Note Layouts]], "every X is a Y" fails here: the object is a *family*, and only its members are homomorphic encryption schemes. So the field is `Requires::`. If you prefer to define one member $E^{(d)}$ as the object, `Extends:: [[Homomorphic Encryption]]` would be correct for it.

## Property

> [!remark] How the key material grows with $d$
> - In Gentry's construction the public key of $E^{(d)}$ grows linearly in $d$: it contains $d+1$ public keys and a chain of encrypted secret keys `[T Thm 1.3.1, informal]`; see [[Gentry Bootstrapping Transformation]].
> - In the scheme of `[BV]` the public key does not depend on the number of levels $L$; the **evaluation key** has bit-length that grows linearly with $L$ `[BV Def 3.6, §4.1, §4.5]`.
> - **Notation.** `[S §2]` writes key generation as $\mathsf{KeyGen}_E(\lambda, d)$ and evaluation at level $\delta$ as $\mathsf{Evaluate}_E^{(\delta)}$; `[BV Def 3.6]` writes $\mathsf{HE.Keygen}(1^\kappa, 1^L)$ with a separate evaluation key.
> - `⚠️ CLAUDE – verify:` I read these as the same phenomenon under two names (the key material $\mathsf{Eval}$ needs), but the split between "public key" and "evaluation key" differs, so state which one you mean. The previous version of the Homomorphic Encryption note said "the public key grows linearly in $d$" and cited `[BV]`; for `[BV]` that is true of the evaluation key only.

> [!remark] Leveled FHE without bootstrapping
> Leveled FHE does not require [[Bootstrappable Encryption|bootstrapping]]. `[BGV]` builds leveled schemes from LWE or ring-LWE without it, with a new way of managing noise (abstract only; I did not read the construction).

## Related

### Constructions
- [[Gentry Bootstrapping Transformation]] — builds a leveled scheme from a [[Bootstrappable Encryption|bootstrappable]] one

### Siblings
- [[Fully Homomorphic Encryption]] — one scheme for every depth
- [[Bootstrappable Encryption]]

### Prerequisites
- [[Homomorphic Encryption]]
