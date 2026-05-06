---
parent: "[[Foundational Math for Zero Knowledge Proofs]]"
tags: []
date: 2025-07-09T21:31
---
## Explaining the P vs NP problem

Problems in P are problems that are both easy to solve (in polynomial time) and easy to verify solutions for (in polynomial time).

A *witness* in computer science is proof that you solved the problem correctly.

Problems in PSPACE: Might take exponential time to solve but don't necessarily require exponential memory space to run the search.
**Important**: Many researchers believe no efficient algorithm to solve these problems exists at all. If an efficient solution to these problems could be discovered, it would also be possible to reuse the algorithm to break all modern encryption and fundamentally alter computing as we know it.

Problems in NP are problems that easy to verify solutions but hard to solve (require exponential resources). 

| Category | Compute Time                 | Verification Time            |
| -------- | ---------------------------- | ---------------------------- |
| P        | Must be polynomial or better | Must be polynomial or better |
| NP       | No Requirement               | Must be polynomial or better |
| PSPACE   | No Requirement               | No Requirement               |
## Expressing problems and solutions as Boolean formulas

All problems in P and NP can be expressed as a Boolean formula that outputs true if we know the corresponding variable assignment (witness), which encodes a correct solution to the original problem.

## P vs NP and ZK Proofs

The “knowledge” in Zero Knowledge Proofs refers to knowledge of the witness.
All problems with solutions that can be quickly verified can be converted into a Boolean formula.
In ZK literature, we often refer to Boolean formulas as Boolean circuits.
