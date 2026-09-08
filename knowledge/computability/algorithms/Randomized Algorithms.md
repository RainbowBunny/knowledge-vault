## The Hiring Problem

> [!pseudocode]
> ```
> HIRE-ASSISTANT(n)
> 1. best = 0
> 2. for i = 1 to n
> 3.     interview candidate i
> 4.     if candidate i is better than candidate best
> 5.         best = i
> 6.         hire candidate i
> ```

> [!lemma]
> Assuming that the candidates are presented in a random order, algorithm `HIRE-ASSISTANT` has an average-case total hiring cost of $O(c_h \ln n)$

> [!pseudocode]
> ```
> RANDOMIZED-HIRE-ASSISTANT(n)
> 1. randomly permute the list of candidates
> 2. best = 0 // candidate 0 is a least-qualified dummy candidate
> 3. for i = 1 to n
> 4.     interview candidate i
> 5.     if candidate i is better than candidate best
> 6.         best = i
> 7.         hire candidate i
> ```

> [!lemma]
> The expected hiring cost of the procedure `RANDOMIZED-HIRE-ASSISTANT` is $O(c_h \ln n)$

### Online Version

> [!definition] On-line hiring problem
> Suppose now that we do not wish to interview all the candidates in order to find the best one. We also do not wish to hire and fire as we find better and better applicants. Instead, we are willing to settle for a candidate who is close to the best, in exchange for hiring exactly once. We must obey one company requirement: after each interview we must either immediately offer the position to the applicant or immediately reject the applicant. What is the trade-off between minimizing the amount of interviewing and maximizing the quality of the candidate hired?

> [!pseudocode]
> ```
> ON-LINE-MAXIMUM(k, n)
> 1. for i = 1 to k
> 2.     if score(i) > bestscore
> 3.         bestscore = score(i)
> 4. for i = k + 1 to n
> 5.     if score(i) > bestscore
> 6.         return i
> 7. return n
> ```

> [!remark]
> The strategy works best when $k = \frac{n}{e}$

## Random Number Generation

> [!pseudocode]
> ```
> RANDOM(a, b)
> 1. if a == b
> 2.     return a
> 3. r = RANDOM(0, 1)
> 4. if r == 0
> 5.     return RANDOM(a, FLOOR((a + b) / 2)))
> 6. else return RANDOM(CEIL((a + b) / 2), b)   
> ```

> [!pseudocode]
> ```
> UNBIASED-RANDOM()
> 1. while TRUE
> 2.     x = BIASED-RANDOM()
> 3.     y = BIASED-RANDOM()
> 4.     if x != y
> 5.         return x
> ```

## Random Permutations

> [!pseudocode]
> ```
> PERMUTE-BY-SORTING(A)
> 1. n = A.length
> 2. let P[1..n] be a new array
> 3. for i = 1 to n
> 4.     P[i] = RANDOM(1, n ** 3)
> 5. sort A, using P as sort keys
> ```

> [!lemma]
> Procedure `PERMUTE-BY-SORTING` produces a uniform random permutation of the input, assuming that all priorities are distinct.

> [!pseudocode]
> ```
> RANDOMIZE-IN-PLACE(A)
> 1. n = A.length
> 2. for i = 1 to n
> 3.     swap A[i] with A[RANDOM(i, n)]
> ```

> [!lemma]
> Procedure `RANDOMIZE-IN-PLACE` computes a uniform random permutation.

### Random Subset of a Permutation

> [!pseudocode]
> ```
> RANDOM-SAMPLE(m, n)
> 1. if m == 0
> 2.     return EMPTYSET
> 3. else S = RANDOM-SAMPLE(m - 1, n - 1)
> 4.     i = RANDOM(1, n)
> 5.     if i in S
> 6.         S = UNION(S, {n})
> 7.     else S = UNION(S, {i})
> 8.     return S
> ```
