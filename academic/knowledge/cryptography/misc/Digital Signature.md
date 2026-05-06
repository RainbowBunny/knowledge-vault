
> [!definition] Abstract Description of the Digital Signature Scheme
> - $K^{\text{Pri}}$: A private signing key.
> - $K^{\text{Pub}}$: A public verification key.
> - $\text{Sign}$: A **signing algorithm** that takes as input a digital document $D$ and a private key $K^{\text{Pri}}$ and returns a signature $D^{\text{Sig}}$ for $D$.
> - $\text{Verify}$: A **verification algorithm** that takes as input a digital document $D$, a signature $D^{\text{sig}}$, and a public key $K^{\text{Pub}}$. The algorithm returns `True` is $D^{\text{sig}}$ is a signature for $D$ associated to the private key $K^{\text{Pri}}$, and otherwise it returns `False`.

> [!remark] 
> Necessary general conditions for a secure digital signature scheme include the following:
> - Given $K^{\text{Pub}}$, an attacker cannot feasibly determine $K^{\text{Pri}}$, nor can she determine any other private key that produces the same signatures as $K^{\text{Pri}}$.
> - Given $K^{\text{Pub}}$, and a list of signed documents $D_1, \dots, D_n$ with their signatures $D_1^{\text{sig}}, \dots, D_n^{\text{sig}}$, an attacker cannot feasibly determine a valid signature on any document $D$ that is not in the list $D_1, \dots, D_n$.

## Digital Signature Scheme

- [[Digital Signature Algorithm]]
- [[GGH Public Key Cryptosystem]]
- [[ElGamal Public Key Cryptosystem]]
- [[NTRU Public Key Cryptosystem]]

