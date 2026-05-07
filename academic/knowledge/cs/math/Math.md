## Matrix Multiplication

### General Matrix Multiplication

> [!pseudocode]
> ```
> MATRIX-MULTIPLY(A, B)
> 1. if A.columns != B.rows
> 2.     error "incompatible dimensions"
> 3. else let C be a new A.rows * B.columns matrix
> 4.     for i = 1 to A.rows
> 5.         for j = 1 to B.columns
> 6.             c[i][j] = 0
> 7.             for k = 1 to A.columns
> 8.                 c[i][j] = c[i][j] + a[i][k] * b[k][j]
> 9. return C
> ```

### Square Matrix Multiplication

> [!definition] Square Matrix Multiplication
> **Input**: Two $n \times n$ square matrices $A = (a_{i, j})$ and $B = (b_{i, j})$ 
> **Output**: The product $C = A \cdot B$, with each entry $c_{i, j} = \sum_{k = 1}^n a_{i, k} \cdot b_{k, j}$

> [!pseudocode]
> ```
> SQUARE-MATRIX-MULTIPLY(A, B)
> 1. n = A.rows
> 2. let C be a new n * n matrix
> 3. for i = 1 to n
> 4.     for j = 1 to n
> 5.         c[i][j] = 0
> 6.         for k = 1 to n
> 7.             c[i][j] = c[i][j] + a[i][k] * b[k][j]
> 8. return C
> ```

### Strassen's Algorithm

> [!proposition]
> Partition:
> $$A = \begin{pmatrix}A_{1,1} & A_{1,2} \\ A_{2, 1} & A_{2, 2}\end{pmatrix}, \quad B = \begin{pmatrix}B_{1,1} & B_{1,2} \\ B_{2, 1} & B_{2, 2}\end{pmatrix}, \quad C = \begin{pmatrix}C_{1,1} & C_{1,2} \\ C_{2, 1} & C_{2, 2}\end{pmatrix}$$

> [!pseudocode]
> ```
> SQUARE-MATRIX-MULTIPLY-RECURSIVE(A, B)
>  1. n = A.rows
>  2. let C be a new n * n matrix
>  3. if n == 1
>  4.     return c[1][1] = a[1][1] * b[1][1]
>  5. else partition A, B, and C 
>  6.     C[1][1] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][1], B[1][1])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][2], B[2][1])
>  7.     C[1][2] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][1], B[1][2])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][2], B[2][2])
>  8.     C[2][1] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][1], B[1][1])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][2], B[2][1])
>  9.     C[2][2] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][1], B[1][2])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][2], B[2][2])
> 10. return C
> ```

> [!pseudocode]
> ```
> STRASSEN(A, B)
>  1. n = A.rows
>  2. let C be a new n * n matrix
>  3. if n == 1
>  4.     return c[1][1] = a[1][1] * b[1][1]
>  5. else partition A, B, and C
>  6.     M[1] = STRASSEN(A[1][1] + A[2][2], B[1][1] + B[2][2])
>  7.     M[2] = STRASSEN(A[2][1] + A[2][2], B[1][1])
>  8.     M[3] = STRASSEN(A[1][1], B[1][2] - B[2][2])
>  9.     M[4] = STRASSEN(A[2][2], B[2][1] - B[1][1])
> 10.     M[5] = STRASSEN(A[1][1] + A[1][2], B[2][2])
> 11.     M[6] = STRASSEN(A[2][1] - A[1][1], B[1][1] + B[1][2])
> 12.     M[7] = STRASSEN(A[1][2] - A[2][2], B[2][1] + B[2][2])
> 13.     C[1][1] = M[1] + M[4] - M[5] + M[7]
> 14.     C[1][2] = M[3] + M[5]
> 15.     C[2][1] = M[2] + M[4]
> 16.     C[2][2] = M[1] - M[2] + M[3] + M[6]
> 17. return C
> ```

## Complex Numbers

### Multiplying Complex Numbers

> [!definition] Multiplying Complex Numbers
> **Input**: Two complex numbers $\langle a, b \rangle$ and $\langle c, d \rangle$.
> **Output**: The multiplication of two complex numbers $\langle ac - bd, ad + bc \rangle$

> [!proposition] Idea
> Calculate $M_1 = ac, M_2 = bd, M_3 = (a + b)(c + d)$, then:
> **Real Part**: $ac - bd = M_1 - M_2$.
> **Imaginary Part**: $ad + bc = M_3 - M_1 - M_2$.

## Polynomials

### Horner's Rule

> [!definition] Horner's Rule
> For a polynomial $P(x) = \sum_{k = 0}^n a_k x^k$, given the coefficients $a_0, a_1, \dots, a_n$ and a value $x$: $$P(x) = a_0 + x(a_1 + x(a_2 + \cdots + x(a_{n - 1} + x a_n)\cdots)),$$ and thus we can calculate this by the code segment:
> ```
> 1. y = 0
> 2. for i = n downto 0
> 3.     y = ai + x * y
> ```

## Monge Arrays

> [!definition] Monge Array
> An $m \times n$ array $A$ of real numbers is a **Monge array** if for all $i, j, k$ and $l$ such that $1 \leq i < k \leq m$ and $1 \leq j < l \leq n$, we have $$A[i, j] + A[k, l] \leq A[i, l] + A[k, j].$$

> [!proposition]
> 1. An array is Monge if and only if for all $i = 1, 2, \dots, m - 1$ and $j = 1, 2, \dots, n - 1$, we have $$A[i, j] + A[i + 1, j + 1] \leq A[i, j + 1] + A[i + 1, j].$$
> 2. Let $f(i)$ be the index of column containing the leftmost minimum element of row $i$, then $f(1) \leq f(2) \leq \cdots \leq f(m)$ for any $m \times n$ Monge array.

## Binary Arithmetic

### Adding Two n-bit Binary Integers

> [!definition] Adding two $n$-bit binary integers
> **Input**: Two sequences of $n$-bit binary integers $A = \langle a_1, a_2, \dots, a_n \rangle$ and $B = \langle b_1, b_2, \dots, b_n \rangle$.
> **Output**: The sum of the two integers stored in binary form in an $(n + 1)$-element array $C = \langle c_1, c_2, \dots, c_{n + 1} \rangle$.
