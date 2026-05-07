## Task-scheduling Problem as a Matroid

> [!definition] Scheduling Unit-time Tasks with Deadlines and Penalties for a Single Processor
> **Input**:
> - A set $S = \{a_1, a_2, \dots, a_n\}$ of $n$ unit-time tasks;
> - A set of $n$ integer **deadlines** $d_1, d_2, \dots, d_n$, such that each $d_i$ satisfies $1 \leq d_i \leq n$ and task $a_i$ is supposed to finish by time $d_i$; and
> - A set of $n$ nonnegative weights or **penalties** $w_1, w_2, \dots, w_n$, such that we incur a penalty of $w_i$ if task $a_i$ is not finished by time $d_i$, and we incur no penalty if a task finishes by its deadline.
> 
> Find a schedule for $S$ that minimizes the total penalty incurred for missed deadlines.

> [!definition] Canonical Form
> We can always transform an arbitrary schedule into **canonical form**, in which the early tasks precede the late tasks and we schedule the early tasks in order of monotonically increasing deadlines.

> [!theorem]
> We say a set $A$ of tasks is **independent** if there exists a schedule for these tasks such that no tasks are late. Then set $S$ is a set of unit-time tasks with deadlines, and $\mathcal I$ is the set of all independent sets of tasks form a matroid.

> [!pseudocode]
> ```
> SCHEDULING-VARIATIONS(A)
>  1. let D[1..n] be a new array
>  2. for i = 1 to n
>  3.     a[i].time = a[i].deadline
>  4.     if D[a[i].deadline] != NIL
>  5.         y = FIND-SET(D[a[i].deadline])
>  6.         a[i].time = y.low - 1
>  7.     x = MAKE-SET(a[i])
>  8.     D[a[i].time] = x
>  9.     x.low = x.high = a[i].time
> 10.     if D[a[i].time - 1] != NIL
> 11.         UNION(D[a[i].time - 1], D[a[i].time])
> 12.     if D[a[i].time + 1] != NIL
> 13.         UNION(D[a[i].time + 1], D[a[i].time])
> ```

## Task scheduling to Minimize Average Completion Time

> [!definition] Task scheduling to minimize average completion time
> Suppose you are given a set $S = \{a_1, a_2, \cdots, a_n\}$ of tasks, where task $a_i$ requires $p_i$ units of processing time to complete. You have one computer on which to run these tasks, and the computer can run only one task at a time. Let $c_i$ be the **completion time** of task $a_i$, that is, the time at which task $a_i$ complete processing. Minimize the average completion time: $$\frac{1}{n} \sum_{i = 1}^n c_i.$$

### Non-preemptive Variant

> [!definition] Non-preemtive
> Once task $a_i$ starts, it must run continuously for $p_i$ units of time.

> [!proposition] 
> Greedy algorithm by sorting task by length works.

### Preemptive Variant with Release Time

> [!definition]
> Now, tasks are not all available at once. That is, each task cannot start until its **release time** $r_i$. Also, we now allow **preemption**, so that a task can be suspended and restarted at a later time.

> [!proposition]
> Now greedy need to run for every unit of time (we can reduce to only consider release time).
