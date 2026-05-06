
> [!definition] Component of a Search Problem
> - **Agent**: An entity that perceive the environment and make decisions for a specific goal.
> - **State**: An configuration of the environment.
> - **Actions**: Choices that can make in a state.
> - **Transition Model**: Consequence of an action on an state.
> - **State Space**: All valid reachable states.
> - **Goal Test**: Condition for a state to be a goal.
> - **Path Cost**: Numerical costs associated with a set of actions between two states.

> [!definition] Solution
> - **Solution**: A list of valid actions from initial state to a goal state.
> - **Optimal Solution**: Solution with minimized cost.

> [!definition] Abstraction: Node
> Node is a data structure which contains:
> - A state
> - Its parent node
> - The action that was applied to the parent node
> - Path cost from initial state to this state.

> [!algorithm] Baseline For Search Algorithm
> Repeat:
> 1. If the frontier is empty,
> 	- _Stop._ There is no solution to the problem.
> 2. Remove a node from the frontier. This is the node that will be considered.
> 3. If the node contains the goal state, return the solution. *Stop*. Else:
> 	- Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier.
> 	- Add the current node to the explored set. 

## Uninformed Search

> [!definition] Uninformed Search
> These solutions to the problem do not require prior knowledge for the problem and explored the problem on their own.
> Example: BFS, DFS

## Informed Search

### Greedy Best First Search

> [!remark]
> We now introduce a heuristic function $h(n)$ and the node we remove by step 2 is based on this heuristic function (the smaller the better).

### A* search

> [!remark]
> We now choose the node to remove by step 2 based on (cost of path until now + estimated cost).

> [!remark]
> In order for A* to be optimal, the heuristic function should be
> 1. **Admissible**, or never *overestimating* the true cost, and
> 2. **Consistent**: For every node $n$ and successor $n*$ with step cost $c$, $h(n) \leq h(n') + c$.

## Adversarial Search

