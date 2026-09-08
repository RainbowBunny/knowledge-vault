## Printing Neatly

> [!definition] Printing Neatly
> Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of $n$ words of length $l_1, l_2, \dots, l_n$, measured in characters. We want to print this paragraph neatly on a number of lines that hold a maximum of $M$ characters each. Our criterion of "neatness" is as follows. If a given line contains words $i$ through $j$, where $i \leq j$, and we leave exactly one space between words, the number of extra space characters at the end of the line is $M - j + i - \sum_{k = i}^j l_k$, which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. Give a dynamic-programming algorithm to print a paragraph of $n$ words neatly on a printer.

> [!pseudocode]
> ```
> PRINT-NEATLY(l, n, M)
>  1. let extras[1..n, 1..n], lc[1..n, 1..n], and c[0..n] be new arrays
>  2. for i = 1 to n
>  3.     extras[i, j] = M - l[i]
>  4.     for j = i + 1 to n
>  5.         extras[i, j] = extras[i, j - 1] - l[j] - 1
>  6. for i = 1 to n
>  7.     for j = i to n
>  8.         if extras[i, j] < 0
>  9.             lc[i, j] = INF
> 10.         else if j == n and extras[i, j] >= 0
> 11.             lc[i, j] = 0
> 12.         else lc[i, j] = (extras[i, j]) ** 3
> 13. c[0] = 0
> 14. for j = 1 to n
> 15.     c[j] = INF
> 16.     for i = 1 to j
> 17.         if c[i - 1] + lc[i, j] < c[i]
> 18.             c[j] = c[i - 1] + lc[i, j]
> 19.             p[j] = i
> 20. return (c, p)
> 
> GIVE-LINES(p, j)
> 1. i = p[j]
> 2. if i == 1
> 3.     k = 1
> 4. else k = GIVE-LINES(p, i - 1) + 1
> 5. print (k, i, j)
> 6. return k
> ```

## Edit Distance


