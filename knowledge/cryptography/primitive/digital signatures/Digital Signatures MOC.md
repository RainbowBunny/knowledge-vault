# Digital Signatures MOC

Authenticity for the asymmetric setting — sign with a private key, verify with a public key.

## Theory

- [[Digital Signature]] — the interface note (still a stub; the security model is in the note below)
- [[Old Digital Signature]] — syntax, EUF-CMA, hash-and-sign, security reductions
- [[ID and Signatures from Sigma]] — turning a Σ-protocol identification scheme into a signature scheme

## Concrete Schemes

- [[Digital Signature Algorithm]] — DSA / ECDSA
- [[Blind Signature]]
- [[Dilithium]] (`scheme/`) — lattice-based, post-quantum
- [[New NIBS]]

## Related

- [[Identification MOC]] — the Σ-protocol identification schemes that many signatures derive from.
- [[Fiat-Shamir Transform]] — the bridge from interactive Σ-protocol to non-interactive signature.
- [[Post-Quantum Cryptography MOC]] — Dilithium and other lattice/code-based signatures.
