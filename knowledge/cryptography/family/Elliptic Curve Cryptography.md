
Example:
- [[Diffie-Hellman Key Exchange#Elliptic Version|Elliptic Diffie-Hellman key exchange]]
- [[ElGamal Public Key Cryptosystem#Elliptic Version|Elliptic ElGamal public key cryptosystem]]
- [[Massey-Omura Three-Pass Cryptosystem#Elliptic Version|Elliptic Massey-Omura Three-Pass Cryptosystem]]


> [!remark]
> Suppose that Bob wants to send Alice the value of a point $R \in E(\mathbb F_p)$, Bob can send the $x$-coordinate of $R = (x_R, y_R)$ together with a single bit $$\beta_R = \begin{cases}0 &\text{if } 0 \leq y_R < \frac{1}{2} p \\ 1 &\text{if } \frac{1}{2} p < y_R < p \end{cases}$$
