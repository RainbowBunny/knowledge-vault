
> [!remark] Goal 
> 1. Fast encoding of messages;
> 2. Easy transmission of encoded messages;
> 3. Fast decoding of received messages;
> 4. Maximum transfer of information per unit time;
> 5. Maximal detection or correction capability

## Communication Channel

> [!definition]
> Let $A = \{a_1, a_2, \dots, a_q\}$ be a set of size $q$, which we refer to as a **code alphabet** and whose elements are called **code symbols**.
> 1. A **q-ary word** of length $n$ over $A$ is a sequence $w = w_1 w_2 \cdots w_n$ with each $w_i \in A$ for all $i$. Equivalently, $w$ may also be regarded as the vector $(w_1, w_2, \dots, w_n)$.
> 2. A **q-ary block code** of length $n$ over $A$ is a nonempty set $C$ of q-ary words having the same length $n$.
> 3. An element of $C$ is called a **codeword** in $C$.
> 4. The number of codewords in $C$, denoted by $|C|$, is called the **size** of $C$,
> 5. The **(information) rate** of a code $C$ of length $n$ is defined to be $(\log_q |C|) / n$.
> 6. A code of length $n$ and size $M$ is called an $(n, M)$-code.

> [!definition] Communication Channel
> A **communication channel** consists of a **finite channel alphabet** $A = \{a_1, \dots, a_q\}$ as well as a set of **forward channel probabilites** $\mathcal P(a_j \text{ received} | a_i \text{ sent})$, satisfying $$\sum_{j = 1}^q \mathcal P(a_j \text{ received} | a_i \text{ sent}) = 1$$ for all $i$.

> [!definition] Memoryless
> A communication channel is said to be **memoryless** if the outcome of any one transmission is independent of the outcome of the previous transmissions; i.e., if $c = c_1 c_2 \cdots c_n$ and $x = x_1 x_2 \cdots x_n$ are words of length $n$, then $$\mathcal P(x \text{ received} | c \text{ sent}) = \prod \mathcal P(x_i \text{ received} | c_i \text{ sent})$$

> [!definition] $q$-ary symmetric channel
> A **$q$-ary symmetric channel** is a memoryless channel which has a channel alphabet of size $q$ such that
> 1. Each symbol transmitted has the same probability $p (< 1/2)$ of being received in error;
> 2. If a symbol is received in error, then each of the $q - 1$ possible errors is equally likely.

> [!example] Binary symmetric channel
> The **binary symmetric channel (BSC)** is a memoryless channel which has channel alphabet $\{0, 1\}$ and channel probabilities $$\begin{align}\mathcal P(1 \text{ received} | 0 \text{ sent}) &= \mathcal P(0 \text{ received} | 1 \text{ sent}) = p \\ \mathcal P(0 \text{ received} | 0 \text{ sent}) &= P(1 \text{ received} | 1 \text{ sent}) = 1 - p\end{align}$$
> The probability of a bit error in a BSC is $p$. This is called the **crossover probability** of the BSC.

## Decoding Rule

> [!definition] Decoding Rule
> In a communication channel with coding, only codewords are transmitted. Suppose that a word $w$ is received. If $w$ is a valid codeword, we may conclude that there is no error in the transmission. Otherwise, we know that some errors have occurred. In this case, we need a rule for finding the most likely codeword sent. Such a rule is known as a **decoding rule**.

### Maximum Likelihood Decoding

> [!definition] Maximum Likelihood Decoding
> Suppose that codewords from a code $C$ are being sent over a communication channel. If a word $x$ is received, we can compute the forward channel probabilities $$\mathcal P(x \text{ received} | c \text{ sent})$$ for all codewords $c \in C$. The **maximum likelihood decoding (MLD) rule** will conclude that $c_x$ is the most likely codeword transmitted if $c_x$ maximize the forward channel probabilities: $$\mathcal P(x \text{ received} | c_x \text{ sent}) = \max_{c \in C} \mathcal P(x \text{ received} | c \text{ sent}).$$ 
> The problem is there might be more than one $c_x$, we have two strategies:
> 1. **Complete maximum likelihood decoding (CMLD)**: Select one of them arbitrarily.
> 2. **Incomplete maximum likelihood decoding (IMLD)**: Request a retransmission.

### Nearest Neighbour/Minimum Distance Decoding

> [!definition] Nearest Neighbour/Minimum Distance Decoding
> Suppose that codewords from a code $C$ are being sent over a communication channel, if a word $x$ is received, the **nearest neighbour decoding rule** (or **minimum distance decoding rule**) will decode $x$ to $c_x$ if $d(x, c_x)$ is minimal among all the codewords in $C$, i.e, $$d(x, c_x) = \min_{c \in C} d(x, c)$$
> We can also define the complete and incomplete strategy just like the [[#Maximum Likelihood Decoding]] case as there might be more than one $x_c$.

> [!theorem]
> For a BSC with crossover probability $p < 1/2$, the maximum likelihood decoding rule is the same as the nearest neighbour decoding rule.

## Systematic Codes

> [!definition] Systematic Codes
> A systematic code produces a codeword of the form $c = (m, p)$, or the message $m$ is embedded directly and $p$ is the parity check of $m$.

## Quasi-Cyclic Codes

> [!definition] Quasi-Cyclic Codes
> We would like cyclic code as we won't need to store a large generator matrix when the code length is large.
> Quasi means that contains of multiple cyclic group.

