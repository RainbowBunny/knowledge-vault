# Symmetric Encryption MOC

Confidentiality with a shared key. Mirrors the structure of [[Public-Key Encryption MOC]]: one canonical primitive note, primitive families, classical & modern schemes.

## Primitive

- [[Symmetric Key Encryption]] — the canonical note: syntax (Shannon / computational), correctness, γ-uniformity, all security notions (perfect security, semantic security, message recovery, parity prediction, multi-key SS, indistinguishability, CPA, nonce-CPA, ciphertext integrity, CCA), and CPA / nonce-CPA constructions.

## Cipher Families

- [[Block Ciphers]] — DES, AES, modes of operation
- [[Stream Ciphers]] — synchronous and self-synchronizing stream ciphers

## Classical Schemes (`classical/`)

- [[One-time Pad]] — perfect-security exemplar
- [[Substitution Cipher]]
- [[Multiplicative Encryption]]
- [[Affine Cipher]]
- [[Hill Cipher]]
- [[Vigenère cipher]]
- [[Other Encoding]] — Enigma, Rot47

## Modern Schemes (`schemes/`)

*Empty for now. Future: AES, ChaCha20, DES / 3DES, Salsa20.*

## Related

- [[Message Authentication MOC]] — MACs and authenticated encryption built on top of symmetric ciphers
- [[Public-Key Encryption MOC]] — the asymmetric counterpart, same canonical-primitive-file pattern
- [[Assumptions MOC]] → idealized models — ideal cipher / random oracle models used in CPA security proofs
- [[knowledge/cs/foundations/Foundations MOC]] → [[Elementary Wrapper]] — the meta-concept used in every reduction theorem
