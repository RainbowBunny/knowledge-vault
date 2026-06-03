# Hard Problems MOC

Computational problems assumed hard — the foundation under public-key crypto, ZK arguments, and post-quantum schemes. Algorithms that *attack* these problems live alongside the assumption (e.g. BSGS, Pohlig-Hellman are filed under DLP, not under cryptanalysis).

## Discrete Logarithm Family (`dlp/`)

- [[Discrete Logarithm Problem]] — definition over generic groups
- [[Baby-Step Giant-Step]]
- [[Pohlig-Hellman]]
- [[Index Calculus]]
- [[DLP Collision Algorithm]]
- [[Elliptic Curve DLP]]
- [[Hyperelliptic Curve DLP]]

## Other Families (links)

- Lattice problems — see [[Post-Quantum Cryptography MOC]] → lattice-based: [[Learning With Error Problem]], [[Short Integer Solution Problem]]
- Coding problems — see [[Post-Quantum Cryptography MOC]] → code-based

## Stubs (planned)

- Integer factoring (RSA problem, quadratic residuosity)
- CDH / DDH variants

## Related

- [[Cryptanalysis MOC]] — concrete attacks on deployed protocols (CRIME, password cracking, etc.) as opposed to attacks on the underlying assumptions.
