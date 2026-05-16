# Computer Science MOC

Top-level index for `academic/knowledge/cs/`. This domain merges what was previously in `cp/`, `algorithm/`, and `computation theory/`. Cryptographic algorithms (DLP, LLL, LWE, SIS, Pollard's ρ) live in [[Cryptography MOC|cryptography/]].

Each section below points to a sub-MOC that lists the files in that folder.

## Sub-MOCs

- [[Foundations MOC]] — what algorithms are, asymptotic analysis, recurrences, formal languages
- [[Algorithms MOC]] — sorting, searching, DP (`dp/`), greedy (`greedy/`), randomized
- [[Data Structures MOC]] — heaps, BSTs, hashing, lists, disjoint sets, amortized analysis
- [[Complexity MOC]] — complexity classes, intractability, advanced topics, probabilistic
- [[Problems MOC]] — Max subarray, Subset-Sum, SAT, AI search
- [[Setup MOC]] — competitive-programming tooling and snippets

## Single-file folders

These folders contain only one file each, so they don't have a sub-MOC:

- [[Computability Theory]] — Turing machines, decidability, undecidability, reducibility, recursion theorem
- [[Math]] — matrix multiplication & Strassen, complex numbers, Horner's rule, Monge arrays, binary addition
- [[Graph]] — representations, traversal, shortest paths, MST, flows (stub)

## Folder Layout

```
cs/
├── CS MOC.md
├── foundations/
│   ├── Foundations MOC.md
│   ├── Algorithm.md
│   ├── Asymptotic Analysis.md
│   ├── Solving Recurrences.md
│   └── Languages.md
├── algorithms/
│   ├── Algorithms MOC.md
│   ├── Sorting.md
│   ├── Order Statistics.md
│   ├── Searching.md
│   ├── Randomized Algorithms.md
│   ├── Optimization Trick.md
│   ├── dp/
│   │   ├── Dynamic Programming.md
│   │   ├── Rod Cutting and Fibonacci.md
│   │   ├── Knapsack.md
│   │   ├── Matrix-Chain Multiplication.md
│   │   ├── String DP.md
│   │   ├── Subsequence.md
│   │   └── Graph DP.md
│   └── greedy/
│       ├── Greedy Algorithms.md
│       ├── Activity Selection.md
│       ├── Huffman Codes.md
│       ├── Matroids.md
│       ├── Task Scheduling.md
│       ├── Acyclic Subgraphs.md
│       └── Off-line Caching.md
├── data-structures/
│   ├── Data Structures MOC.md
│   ├── Heap.md
│   ├── B-Trees.md
│   ├── Priority Queues.md
│   ├── Stacks and Queues.md
│   ├── Linked Lists.md
│   ├── Dynamic Table.md
│   ├── Hash Tables.md
│   ├── Binary Search Tree.md
│   ├── Red-Black Trees.md
│   ├── Disjoint Sets.md
│   ├── Memory.md
│   └── Amortized Analysis.md
├── computability/
│   └── Computability Theory.md
├── complexity/
│   ├── Complexity MOC.md
│   ├── Complexity Class.md
│   ├── Complexity Theory.md
│   ├── Intractable.md
│   ├── Advanced Complexity.md
│   ├── Complexity Notes.md
│   └── Probabilistic Algorithms.md
├── math/
│   └── Math.md
├── graph/
│   └── Graph.md
├── problems/
│   ├── Problems MOC.md
│   ├── Maximum Subarray Problem.md
│   ├── Subset-Sum Problem.md
│   ├── Satisfiability Problem.md
│   └── Search Problem.md
└── setup/
    ├── Setup MOC.md
    ├── CP Setup.md
    └── Snippet Reference.md
```
