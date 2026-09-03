# Symmetric Encryption MOC

Confidentiality with a shared key. Mirrors the structure of [[Public-Key Encryption MOC]]: one canonical primitive note, primitive families, classical & modern schemes.

## Primitive

- [[Symmetric Key Encryption]] — the canonical note, mirroring [[Public-Key Encryption]] section-for-section: syntax, correctness, min-entropy (γ-spread), perfect security, IND-ATK (eav / cpa / cca), multi-key SS, nonce-CPA, and CPA / nonce-CPA constructions.
- [[Perfect Security]] — equivalent characterizations (counting, predicate, independence forms)

### Attack-Game Index (Boneh–Shoup numbering)

| Term                                                      | Reference                                                        |                    |
| --------------------------------------------------------- | ---------------------------------------------------------------- | ------------------ |
| Attack Game 2.1 (Semantic Security)                       | [[Symmetric Key Encryption#Indistinguishability]] (atk = eav)     | $\text{SSadv}$     |
| Attack Game 2.2 (Message Recovery)                        | [[Symmetric Key Encryption#Indistinguishability]]                 | $\text{MRadv}$     |
| Attack Game 2.3 (Parity Prediction)                       | [[Symmetric Key Encryption#Indistinguishability]]                 | $\text{Parityadv}$ |
| Attack Game 2.4 (Semantic Security: Bit-guessing Version) | [[Symmetric Key Encryption#Indistinguishability]]                 | $\text{SSadv}^*$   |
| Attack Game 3.3 (Distinguishing $P_0$ from $P_1$)         | [[Indistinguishability]]                            | $\text{Distadv}$   |
| Attack Game 5.1 (Multi-key Semantic Security)             | [[Symmetric Key Encryption#Multi-key Semantic Security]]          | $\text{MSSadv}$    |
| Attack Game 5.2 (CPA Security)                            | [[Symmetric Key Encryption#Indistinguishability]] (atk = cpa)     | $\text{CPAadv}$    |
| Attack Game 5.3 (Nonce-based CPA Security)                | [[Symmetric Key Encryption#Nonce-based CPA Security]]             | $\text{nCPAadv}$   |
| Attack Game 8.3 (Guessing Advantage)                      | [[Key Derivation Problem]]                                        | $\text{Guessadv}$  |
| Attack Game 9.1 (Ciphertext Integrity)                    | [[Authenticated Encryption#Ciphertext Integrity]]                 | $\text{CIadv}$     |
| Attack Game 9.2 (Chosen Ciphertext Attack)                | [[Symmetric Key Encryption#Indistinguishability]] (atk = cca)     | $\text{CCAadv}$    |

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
- [[Indistinguishability]] and [[Statistical Distance]] — the distribution-distinguishing toolkit extracted from the primitive note
- [[Key Derivation Problem]] — guessing advantage (Attack Game 8.3), now under key establishment
- [[CS Foundations MOC]] → [[Elementary Wrapper]] — the meta-concept used in every reduction theorem
