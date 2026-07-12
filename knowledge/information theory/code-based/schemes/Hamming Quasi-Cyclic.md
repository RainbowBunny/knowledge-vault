## Hamming Quasi-Cyclic (HQC)

Code-based KEM; selected by NIST (March 2025) as the backup KEM to ML-KEM. The name is literally a composition of [[Code Properties|code properties]]: security in the **Hamming** metric, keys compressed via **quasi-cyclic** structure.

## Design

> [!algorithm] HQC Framework (sketch)
> HQC uses two codes with different roles:
> - A **public, efficiently decodable code** $\mathcal C$ with a systematic generator matrix $G$ — in the NIST version a concatenation of [[Reed-Muller Codes|Reed-Muller]] and Reed–Solomon codes ([[Cyclic Codes#Reed-Solomon Code|RS]]). Its decoding capability only affects *correctness*, not security.
> - **Random quasi-cyclic codes** over $\mathbb F_2[x]/(x^n - 1)$, whose [[Syndrome Decoding|syndrome decoding]] hardness (QCSD) carries the *security*.
>
> Encryption masks $mG$ with sparse quasi-cyclic noise; decryption strips the mask and uses the decoder of $\mathcal C$ to remove the residual error. IND-CCA security is obtained via the Fujisaki–Okamoto transform (HHK).

> [!remark]
> 1. The correctness/security split is the signature design idea: the decodable code is public, so its structure costs nothing in security — the opposite of McEliece, where hiding the decodable code's structure *is* the assumption.
> 2. Decryption failure rate must be made negligible for FO/CCA security — the analysis of the residual error weight distribution is the delicate part of the spec.

## Related

- [[Code Properties]] — systematic + quasi-cyclic, and why QC compresses keys
- [[Syndrome Decoding]] — the underlying assumption (quasi-cyclic variant)
- Paper notes: RHQC (ratcheted key exchange from coding assumptions) in `academic/paper/cryptography/PQC/`
