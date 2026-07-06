# Computer Science MOC

Top-level index for `knowledge/cs/`. This domain merges what was previously in `cp/`, `algorithm/`, and `computation theory/`. Cryptographic algorithms (DLP, LLL, LWE, SIS, Pollard's ρ) live in [[Cryptography MOC|cryptography/]]. **Complexity theory has been promoted to its own top-level domain at [[Complexity MOC|knowledge/complexity/]]** — it's no longer nested under `cs/`.

Each section below points to a sub-MOC that lists the files in that folder.

## Sub-MOCs

- [[knowledge/cs/foundations/Foundations MOC]] — what algorithms are, asymptotic analysis, recurrences, formal languages, computability
- [[Algorithms MOC]] — sorting, searching, DP (`dp/`), greedy (`greedy/`), randomized, numeric
- [[Data Structures MOC]] — heaps, BSTs, hashing, lists, disjoint sets, amortized analysis
- [[Problems MOC]] — Max subarray, Subset-Sum, SAT, submodular welfare, AI search
- [[Setup MOC]] — competitive-programming tooling and snippets

For complexity theory (P, NP, BPP, IP, hierarchy theorems, …) see the standalone [[Complexity MOC|`complexity/` domain]].

## Single-file folders

- [[Graph]] — representations, BFS/DFS theory, shortest paths by BFS; trees/connectivity/flows still to write

## Folder Layout

```
cs/
├── CS MOC.md
├── foundations/
│   ├── Foundations MOC.md
│   ├── Algorithm.md
│   ├── Asymptotic Analysis.md
│   ├── Solving Recurrences.md
│   ├── Languages.md
│   └── Computability Theory.md
├── algorithms/
│   ├── Algorithms MOC.md
│   ├── Sorting.md
│   ├── Order Statistics.md
│   ├── Searching.md
│   ├── Randomized Algorithms.md
│   ├── Numeric Algorithms.md
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
│       ├── Greedy Algorithms.md   (incl. off-line caching)
│       ├── Activity Selection.md
│       ├── Huffman Codes.md
│       ├── Matroids.md
│       ├── Task Scheduling.md
│       └── Acyclic Subgraphs.md
├── data-structures/
│   ├── Data Structures MOC.md
│   ├── Heap.md
│   ├── B-Trees.md
│   ├── Priority Queues.md
│   ├── Stacks and Queues.md
│   ├── Linked Lists.md
│   ├── Hash Tables.md
│   ├── Binary Search Tree.md
│   ├── Red-Black Trees.md
│   ├── Disjoint Sets.md
│   ├── Memory.md
│   └── Amortized Analysis.md   (incl. dynamic table)
├── graph/
│   └── Graph.md
├── problems/
│   ├── Problems MOC.md
│   ├── Maximum Subarray Problem.md
│   ├── Subset-Sum Problem.md
│   ├── Satisfiability Problem.md
│   ├── Submodular Welfare Problem.md
│   └── Search Problem.md
└── setup/
    ├── Setup MOC.md
    ├── CP Setup.md
    └── Snippet Reference.md
```
