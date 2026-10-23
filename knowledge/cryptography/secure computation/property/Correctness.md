Reference:
- `[Lin17]` — Y. Lindell, _How to Simulate It – A Tutorial on the Simulation Proof Technique_ (2017), §4.2; ePrint 2016/046: https://eprint.iacr.org/2016/046.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - $f = (f_1, f_2): \{0, 1\}^* \times \{0, 1\}^* \to \{0, 1\}^* \times \{0, 1\}^*$: a deterministic two-party functionality; the party with input $x$ wishes to obtain $f_1(x, y)$, the party with input $y$ wishes to obtain $f_2(x, y)$.
> - $\pi$: a two-party protocol. $n$: the security parameter.
> - $\mathrm{view}^\pi_i(x, y, n) = (w, r_i; m^i_1, \dots, m^i_t)$: the view of party $i$ — its input $w \in \{x, y\}$, its random tape $r_i$ and the messages it received.
> - $\mathrm{output}^\pi_i(x, y, n)$: the output of party $i$, computable from its view; $\mathrm{output}^\pi(x, y, n) = (\mathrm{output}^\pi_1(x, y, n), \mathrm{output}^\pi_2(x, y, n))$.
>
> `[Lin17 §4.2]`

> [!definition] Correctness
> $\pi$ computes $f$ **correctly** if there is a negligible function $\mu$ such that for every $x, y \in \{0, 1\}^*$ and every $n$:
> $$\Pr\big[\mathrm{output}^\pi(x, y, n) \neq f(x, y)\big] \leq \mu(n).$$
> `[Lin17 §4.2]`

> [!remark] Correctness and privacy
> For a deterministic $f$, security against static semi-honest adversaries splits into this correctness requirement and a privacy requirement: simulators $S_1, S_2$ with $\{S_1(1^n, x, f_1(x, y))\} \overset{c}{\equiv} \{\mathrm{view}^\pi_1(x, y, n)\}$ and likewise for party 2 (Eq. 4.1, 4.2). For a randomized $f$ the two cannot be separated, and Definition 4.1 compares the simulator's output jointly with the real outputs: $\{(S_1(1^n, x, f_1(x, y)), f(x, y))\} \overset{c}{\equiv} \{(\mathrm{view}^\pi_1(x, y, n), \mathrm{output}^\pi(x, y, n))\}$. `[Lin17 §4.2, Def 4.1]`

> [!remark] Several parties
> `⚠️ CLAUDE – verify:` for $N$ parties with inputs $x_1, \dots, x_N$ the requirement reads the same, with $\mathrm{output}^\pi(x_1, \dots, x_N, n)$ and $f(x_1, \dots, x_N)$; `[Lin17 §4.2]` treats two parties.

## Related

### Siblings
- [[t-Privacy]]

### Prerequisites
- [[Secure Multi-party Computation]]
