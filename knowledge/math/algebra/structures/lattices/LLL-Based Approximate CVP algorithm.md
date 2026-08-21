### LLL-Based Approximate CVP Algorithm

> [!algorithm] LLL-Based Approximate CVP Algorithm
> **Input:**  
> - A lattice $L \subset \mathbb{R}^n$ given by a basis $(v_1, v_2, \ldots, v_n)$  
> - A target vector $w \in \mathbb{R}^n$
>
> **Output:**  
> A lattice vector $v \in L$ such that
> $$\|w - v\| \le C^n \cdot \min_{u \in L} \|w - u\|,$$
> for some absolute constant $C > 1$
>
> ---
>
> 1. Apply the LLL lattice reduction algorithm to the basis
>    $$(v_1, v_2, \ldots, v_n)$$
>    to obtain an LLL-reduced basis.
>
> 2. Using the LLL-reduced basis, apply Babai’s closest vertex algorithm
>    to compute a lattice vector $v \in L$ close to the target vector $w$.
>
> 3. Return the lattice vector $v$.

