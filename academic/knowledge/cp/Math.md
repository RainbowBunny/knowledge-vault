
## Matrix

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
