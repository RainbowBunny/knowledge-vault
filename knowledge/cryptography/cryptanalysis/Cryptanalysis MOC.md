# Cryptanalysis MOC

Attacks — on the hard problems underneath the assumptions, and on deployed protocols, password schemes and RNGs.

## Attacks on hard problems

- `dlp/`: [[Baby-Step Giant-Step]] · [[Pohlig-Hellman]] · [[Index Calculus]] · [[DLP Collision Algorithm]] — against [[Discrete Logarithm Problem]]
- [[Collision Algorithms]] — generic collision-finding (Pollard's ρ, parallel collision search, …)
- [[Factoring Algorithms]] (in `math/number theory/`) — against [[Factoring]]
- lattice reduction ([[LLL Lattice Reduction Algorithm]], [[Babai's Algorithm]]) lives with the lattice in `math/algebra/structures/lattice/`

## Attacks on deployed systems

- [[Attack List]] — running index of attacks
- [[CRIME]] — compression-side-channel attack on TLS
- [[Password Cracking]]
- [[Random Crack]] — bad-randomness exploits

## Related

- [[Assumptions MOC]] — what these algorithms are trying to break
