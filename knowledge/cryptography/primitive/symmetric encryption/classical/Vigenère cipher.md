
## Cryptanalysis of the Vigenère cipher

> [!remark] Frequency of Letters in English Text
> The following table shows the approximate frequency of each letter
> in typical English text. This information is commonly used in
> frequency analysis attacks on classical ciphers.
>
> ### By decreasing frequency
>
> | Letter | Frequency | Letter | Frequency |
> |------|----------|------|----------|
> | E | 13.11% | M | 2.54% |
> | T | 10.47% | U | 2.46% |
> | A | 8.15% | G | 1.99% |
> | O | 8.00% | Y | 1.98% |
> | N | 7.10% | P | 1.98% |
> | R | 6.83% | W | 1.54% |
> | I | 6.35% | B | 1.44% |
> | S | 6.10% | V | 0.92% |
> | H | 5.26% | K | 0.42% |
> | D | 3.79% | X | 0.17% |
> | L | 3.39% | J | 0.13% |
> | F | 2.92% | Q | 0.12% |
> | C | 2.76% | Z | 0.08% |
>
> ---
>
> ### Alphabetical order
>
> | Letter | Frequency | Letter | Frequency |
> |------|----------|------|----------|
> | A | 8.15% | N | 7.10% |
> | B | 1.44% | O | 8.00% |
> | C | 2.76% | P | 1.98% |
> | D | 3.79% | Q | 0.12% |
> | E | 13.11% | R | 6.83% |
> | F | 2.92% | S | 6.10% |
> | G | 1.99% | T | 10.47% |
> | H | 5.26% | U | 2.46% |
> | I | 6.35% | V | 0.92% |
> | J | 0.13% | W | 1.54% |
> | K | 0.42% | X | 0.17% |
> | L | 3.39% | Y | 1.98% |
> | M | 2.54% | Z | 0.08% |

> [!definition] Index of Coincidence
> Let $s = c_1 c_2 c_3 \cdots c_n$ be a string of $n$ alphabetic characters. The **index of coincidence** of $s$, denoted by $\text{IndCo}(s)$, is the probability that two randomly chosen characters in the string $s$ are identical.
> 
> For each $i = 0, 1, 2, \dots, 25$, let $F_i$ be the frequency with which letter $i$ appears in the string $s$. Then, $$\text{IndCo}(s) = \frac{1}{n(n - 1)} \sum_{i = 0}^{25} F_i (F_i - 1)$$

> [!question]
> How can we quantify the following two statements so as to be able to distinguish between them?
> - String 1 has letter frequencies similar to those in table above.
> - String 2 has letter frequencies that look more or less random.

> [!remark] Answer
> - If $\text{IndCo}(s) \approx 0.068$, then $s$ looks like simple substitution English.
> - If $\text{IndCo}(s) \approx 0.038$, then $s$ looks like random letters. 

> [!definition] Mutual Index of Coincidence
> Let $$s = c_1 c_2 c_3 \dots c_n \quad \text{and} \quad t = d_1 d_2 d_3 \dots d_m$$
> be strings of alphabetic characters. The **mutual index of coincidence** of $s$ and $t$, denoted by $\text{MutIndCo}(s, t)$, is the probability that a randomly chosen character from $s$ and a randomly chosen character from $t$ will be the same.
> 
> If we let $F_i(s)$ denote the number of times the $i^{th}$ letter of the alphabet appears in the string $s$, and similarly for $F_i(t)$, then the probability of choosing the $i^{th}$ letter from both is the product of the probabilities $\frac{F_i(s)}{n}$ and $\frac{F_i(t)}{m}$. In order to obtain a formula for the mutual index of coincidence of $s$ and $t$, we add these probabilities over all possible letters, $$\text{MulIndCo}(s, t) = \frac{1}{nm} \sum_{i = 0}^{25} F_i(s) F_i(t).$$
 