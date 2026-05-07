## Greedy Algorithms

> [!definition] Greedy Algorithm
> A **greedy algorithm** is a solution of an optimization problems that always make the choice that looks best at the moment.

> [!remark]
> When developing greedy algorithm, we went through the following steps:
> 1. Cast the optimization problem as one in which we make a choice and are left with one subproblem to solve.
> 2. Prove that there is always an optimal solution to the original problem that makes the greedy choice, so that the greedy choice is always safe.
> 3. Demonstrate optimal substructure by showing that, having made the greedy choice, what remains is a subproblem with the property that if we combine an optimal solution to the subproblem with the greedy choice we have made, we arrive at an optimal solution to the original problem.

> [!definition] Greedy-Choice Property
> We can assemble a globally optimal solution by making locally optimal (greedy) choices. In other words, when we are considering which choice to make, we make the choice that looks best in the current problem, without considering results from subproblems.
