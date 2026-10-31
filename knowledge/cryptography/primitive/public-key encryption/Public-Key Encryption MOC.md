# Public-Key Encryption MOC

Asymmetric confidentiality — encrypt with a public key, decrypt with a private key.

## Theory

- [[Public-Key Cryptography]] — overview, motivation, public-vs-secret framing
- [[Public-Key Encryption Scheme (Old)]] — PKE syntax and security (CPA / CCA in the asymmetric setting)
- [[Public-Key Encryption Scheme]] — the rewritten note (Goldreich syntax, `aux`); its security notions: [[Indistinguishability under Chosen-Plaintext Attack]] (`property/`)
- [[Trapdoor Functions]] — TDF / TDP and the PKE generic construction
- [[Multi-Receiver Encryption Scheme]] — one public key, $N$ secret keys
- [[Traitor Tracing Encryption Scheme]] — extends it with $\mathsf{Trace}$, run by the holder of all keys
- [[Trace-and-Revoke Scheme]] — extends that with revocation and *public* tracing; its public-traceability and IND-CPA games
- [[Trace-and-Revoke from Inner-Product FE]] — the transform of Agrawal et al.: any inner-product FE of dimension $t + r + 1$ gives a trace-and-revoke scheme

## Concrete Schemes (`scheme/`)

- [[RSA Public Key Cryptosystem]]
- [[ElGamal Public Key Cryptosystem]]
- [[Goldwasser–Micali Cryptosystem]]
- [[Massey-Omura Three-Pass Cryptosystem]]
- [[Merkle–Hellman Subset-Sum Cryptosystem]]
- [[A Congruential Public Key Cryptosystem]]
- [[NTRU Public Key Cryptosystem]]
- [[GGH Public Key Cryptosystem]]
- [[Lindner-Peikert Public Key Encryption]]
- [[Lyubashevsky-Peikert-Regev Public Key Encryption]]
- [[Kyber PKE]]
- [[Alekhnovich Encryption Scheme]]
- [[ID-based Public Key Cryptosystems]]

## Related

- For signatures, see [[Digital Signatures MOC]].
- For key establishment / KEM, see [[Key Establishment MOC]].
