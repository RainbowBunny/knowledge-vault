status:: seed

The origin note for **kernel**: stated once, for any function. Each structure keeps its own kernel section, which opens with `Specializes [[Kernel]]` and carries only what that structure adds.

## Scope

A [[Function]] $f: A \to B$. Every function has a kernel; a structure on $A$ and $B$ only changes what it looks like.

## Specializations

| where | what the structure adds |
| --- | --- |
| [[Canonical Decomposition]] | the relation $a' \sim a'' \iff f(a') = f(a'')$ — defined there today, under the decomposition's name |
| [[Group Homomorphism#Kernel]] | one fibre, $\varphi^{-1}(e)$, and it is a [[Normal Subgroup]] |
| [[Ring Homomorphism#Kernel]] | $\varphi^{-1}(0)$, an [[Ideal]] |
| [[Linear Maps#Null Spaces and Ranges]] | the null space, a subspace |

> [!todo] To write
> - the definition: the relation above, moved here from [[Canonical Decomposition]]
> - the one-fibre reading, and when one fibre determines the whole relation (groups, rings, modules — yes; monoids — no, see $(\mathbb N, +) \to (\{0,1\}, \max)$)
> - the categorical kernel (equalizer with the zero morphism) and its dual, the **cokernel** — a section here until three notes need it
>
> Draft: [[Foundation Layer]] §3.13.
