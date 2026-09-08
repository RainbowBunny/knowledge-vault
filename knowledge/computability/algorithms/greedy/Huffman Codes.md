## Huffman Codes

> [!definition] Variable-Length Code
> Considering the problem of designing a **binary character code** (or **code**) in which each character is represented by a unique binary string (**codeword**). If every codeword has the same length then it is called **fixed-length code**, else, it is called **variable-length code**.

> [!definition] Prefix Code
> The codes such that no codeword in it is also a prefix of some other codeword is called **prefix codes**.

> [!definition] Optimal Code Problem
> Given a tree $T$ corresponding to a prefix code, we can easily compute the number of bits required to encode a file (**cost**) by the formula: $$B(T) = \sum_{c \in C} c.\text{freq} \cdot d_T(c).$$ Where, $c.\text{freq}$ is frequency of character $c$ and $d_T(c)$ is the length of the codeword for character $c$.

> [!pseudocode]
> ```
> HUFFMAN(C)
> 1. n = |C|
> 2. Q = C
> 3. for i = 1 to n - 1
> 4.     allocate a new node z
> 5.     z.left = x = EXTRACT-MIN(Q)
> 6.     z.right = y = EXTRACT-MIN(Q)
> 7.     z.freq = x.freq + y.freq
> 8.     INSERT(Q, z)
> 9. return EXTRACT-MIN(Q)
> ```
