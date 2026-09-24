# Algorithms MOC

Hub for the algorithms domain: the CLRS side of computer science — how to solve a problem well, and with which data structure. Whether a problem can be solved at all is [[Computability MOC]]; how hard it is in the worst case is [[Complexity MOC]].

## Foundations — `foundations/`

- [[CS Foundations MOC]] — [[Algorithm]], [[Asymptotic Analysis]], [[Solving Recurrences]]

## Elsewhere in this domain

- [[Data Structures MOC]] — `data structure/`: heaps, BSTs, hashing, lists, disjoint sets, amortized analysis
- [[Graph]] — `graph/`: representations, BFS/DFS, shortest paths by BFS
- [[Problems MOC]] — `problem/`: worked algorithmic problems
- [[Setup MOC]] — `setup/`: competitive-programming tooling and snippets

## Sorting and Searching

- [[Sorting]] — insertion, selection, merge, bubble, heap, quick, counting, radix, bucket
- [[Order Statistics]] — minimum/maximum, selection in expected and worst-case linear time
- [[Searching]] — linear and binary search

## Paradigms

- [[Dynamic Programming|Dynamic Programming]] — elements + classic problems
- [[Greedy Algorithms|Greedy Algorithms]] — theory + per-problem files
- [[Randomized Algorithms]] — hiring problem, online maximum, uniform permutations, sampling

## Numeric & Tricks

- [[Numeric Algorithms]] — matrix multiplication & Strassen, complex-number multiplication, Horner's rule, Monge arrays, binary addition
- [[Optimization Trick]] — non-adjacent form, sentinels

## Subfolder: dp/

- [[Dynamic Programming|Dynamic Programming]] — elements: optimal substructure, overlapping subproblems
- [[Rod Cutting and Fibonacci]]
- [[Knapsack]] — 0/1, fractional, coin changing
- [[Matrix-Chain Multiplication]]
- [[String DP]] — printing neatly, edit distance
- [[Subsequence]] — LCS, longest palindrome subsequence
- [[Graph DP]] — optimal BST, longest path in DAG, bitonic TSP

## Subfolder: greedy/

- [[Greedy Algorithms|Greedy Algorithms]] — theory: greedy-choice property; off-line caching (Bélády)
- [[Activity Selection]] — base + multiple lecture hall + weighted variants
- [[Huffman Codes]]
- [[Matroids]] — matroid theory, weighted matroids, generic GREEDY
- [[Task Scheduling]] — unit-time with deadlines; minimize average completion time
- [[Acyclic Subgraphs]]

## Folder layout

```
algorithms/
├── Algorithms MOC.md
├── foundations/
├── dp/    greedy/
├── data structure/
├── graph/
├── problem/
└── setup/
```
