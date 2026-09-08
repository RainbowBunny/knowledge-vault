
> [!definition] Algorithm
> An **algorithm** is any well-defined computational procedure that takes some value, or set of values, as **input** and produces some value, or some set of values, as **output**. An algorithm is thus a sequence of computational steps that transform the input into the output.

## Pseudocode Conventions

> [!definition] Pseudocode Conventions
>- Indentation indicates block structure.
>- The looping constructs **while**, **for**, and **repeat-until** and the **if-else** conditional construct have interpretations similar to those in `C`, `C++`, `Java`, `Python`, and `Pascal`. Thus, immediately after a **for** loop, the loop counter's value is the value that first exceeded the **for** loop bound. Keyword **to** is used for a loop increments and **downto** is used for a loop decrements, and the amount of change follows the optional keyword **by**.
>- The symbol `//` indicates that the remainder of the line is a comment.
>- An assignment operators work from right to left.
>- Variables are local to the given procedure (unless explicit indication).
>- Array access operator is specified by square bracket.
>- Compound data is organized into **objects**, which are composed of **attributes**.
>- Parameters is passed to a procedure **by value**.
>- A **return** statement immediately transfers control back to the point of call in the calling procedure.
>- The boolean operators "and" and "or" are **short circuiting**.
>- The keyword **error** indicates that an error occurred because conditions were wrong for the procedure to have been called. 

## Loop Invariant

> [!proposition]
> To understand why an algorithm is correct, we can use loop variant and show three things:
> 1. **Initializtion**: It is true prior to the first iteration of the loop.
> 2. **Maintenance**: If it is true before an iteration of the loop, it remains true before the next iteration.
> 3. **Termination**: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.

## Analyzing algorithm

- **Input size**:
	- Number of items in the input
	- Total number of bits needed to represent the input in ordinary binary notation.
- **Running time**: The number of primitive operations or "steps" executed.

### Worst-case and average-case analysis

See [[Asymptotic Analysis]] for worst-case / average-case analysis and the $O / \Omega / \Theta$ notation.

## Designing algorithms

> [!definition] Incremental Approach
> The **incremental approach** builds the solution one element at a time: having handled the first $i$ elements, it extends the solution to element $i + 1$ (e.g. insertion sort inserting $A[i+1]$ into the sorted prefix $A[1..i]$).

### The divide-and-conquer approach

> [!definition] Divide-and-conquer approach
> The divide-and-conquer paradigm involves three steps at each level of the recursion:
> - **Divide** the problem into a number of subproblems that are smaller instances of the same problem.
> - **Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
> - **Combine** the solutions to the subproblems into the solution for the original problem.

> [!remark]
> Worked divide-and-conquer examples: merge sort in [[Sorting]], [[Order Statistics]], [[Maximum Subarray Problem]], Strassen in [[Numeric Algorithms]]. Running times of the recursions are analyzed in [[Solving Recurrences]]. The other design paradigms have their own notes: [[Dynamic Programming]] and [[Greedy Algorithms]].

