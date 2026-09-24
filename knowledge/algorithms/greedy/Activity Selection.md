## Activity-selection problem

> [!definition] Activity-selection problem
> Suppose we have a set $S = \{a_1, a_2, \dots, a_n\}$ of $n$ proposed **activities** that wish to use a resource, such as a lecture hall, which can serve only one activity at a time. Each activity $a_i$ has a **start time** $s_i$ and a **finish time** $f_i$, where $0 \leq s_i < f_i < \infty$. If selected, activity $a_i$ takes place during the half-open time interval $[s_i, f_i)$. Activities $a_i$ and $a_j$ are **compatible** if the intervals $[s_i, f_i)$ and $[s_j, f_j)$ do not overlap. We wish to select a maximum-size subset of mutually compatible activities.

> [!pseudocode]
> ```
> RECURSIVE-ACTIVITY-SELECTOR(s, f, k, n)
> 1. m = k + 1
> 2. while m <= n and s[m] < f[k]
> 3.     m = m + 1
> 4. if m <= n
> 5.     return {a[m]} ∪ RECURSIVE-ACTIVITY-SELECTOR(s, f, m, n)
> 6. return ∅
> ```

> [!pseudocode]
> ```
> GREEDY-ACTIVITY-SELECTOR(s, f)
> 1. n = A.length
> 2. A = {a[1]}
> 3. k = 1
> 4. for m = 2 to n
> 5.     if s[m] >= f[k]
> 6.         A = A ∪ {a[m]}
> 7.         k = m
> 8. return A
> ```

### Multiple Lecture Hall Variant

> [!definition] Multiple Lecture Hall Variant
> Now we have a large number of lecture halls, where any activity can take place in any lecture hall. We wish to schedule all the activities using as few lecture halls as possible.

> [!remark] Idea
> We keep a set of unoccupied lecture halls, and sorting the events of having activity start $s_i$ and activity finish $t_i$ (If $s_i = t_j$ then activity finish will go first). Thus, we can just greedily put activity to empty lecture hall.

### Weighted Variant

> [!definition] Weighted Variant
> Now, each activity $a_i$ has an additional value $v_i$ and thus we are not maximize the number of activities scheduled but the sum of $v$ for chosen activity.

> [!remark] Idea
> We can not use greedy for this problem but dynamic programming works. Sort activities according to the ending time and calculate `c[i, j]` is the answer for all activities that start after $a_i$ and end before $a_j$.
