## Element of Dynamic Programming

> [!remark]
> When developing a dynamic-programming algorithm, we follow a sequence of four steps:
> 1. Characterize the structure of an optimal solution.
> 2. Recursively define the value of an optimal solution.
> 3. Compute the value of an optimal solution, typically in a bottom-up fashion.
> 4. Construct an optimal solution from computed information.

> [!definition] Optimal Substructure
> A problem exhibits **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.

> [!remark]
> Common pattern in discovering optimal substructure:
> 1. Show that a solution to the problem consists of making a choice. Making this choice leaves one or more subproblems to be solved.
> 2. Suppose that for a given problem, you are given the choice that leads to an optimal solution. You do not concern yourself yet with how to determine this choice. You just assume that it has been given to you.
> 3. Given this choice, you determine which subproblems ensue and how to best characterize the resulting space of subproblems.
> 4. Show that the solutions to the subproblems used within an optimal solution to the problem must themselves be optimal by using a "cut-and-paste" technique. You do so by supposing that each of the subproblem solutions is not optimal and then deriving a contradiction.

> [!remark]
> Optimal substructure varies across problem domain in two ways:
> 1. How many subproblems an optimal solution to the original problem used, and
> 2. How many choices we have in determining which subproblem(s) to use in an optimal solution.

> [!definition] Overlapping Subproblems
> When a recursive algorithm revisits the same problem repeatedly, we say that the optimization problem has **overlapping subproblems**.

> [!remark] Reconstructing an optimal solution 
> As a practical matter, we often store which choice we made in each subproblem in a table so that we do not have to reconstruct this information from the costs that we stored.
