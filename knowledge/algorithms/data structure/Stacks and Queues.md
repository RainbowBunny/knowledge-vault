## Stacks

> [!pseudocode]
> ```
> STACK-EMPTY(S)
> 1. if S.top == 0
> 2.     return TRUE
> 3. else return FALSE
> 
> PUSH(S, x)
> 1. S.top = S.top + 1
> 2. S[S.top] = x
> 
> POP(S)
> 1. if STACK-EMPTY(S)
> 2.     error "underflow"
> 3. else S.top = S.top - 1
> 4.     return S[S.top + 1]
> 
> MULTIPOP(S, k)
> 1. while not STACK-EMPTY(S) and k > 0
> 2.     POP(S)
> 3.     k = k - 1
> ```

## Queues

> [!pseudocode]
> ```
> QUEUE-EMPTY(Q)
> 1. if Q.head == Q.tail
> 2.     return TRUE
> 3. else return FALSE
> 
> QUEUE-FULL(Q)
> 1. if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length)
> 2.     return TRUE
> 3. else return FALSE
> 
> ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     Q[Q.tail] = x
> 5.     if Q.tail == Q.length
> 6.         Q.tail = 1
> 7.     else Q.tail = Q.tail + 1
> 
> DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     x = Q[Q.head]
> 5.     if Q.head == Q.length
> 6.         Q.head = 1
> 7.         else Q.head = Q.head + 1
> 8.         return x
> ```

## Dequeue

> [!pseudocode]
> ```
> HEAD-ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     if Q.head == 1
> 5.         Q.head = Q.length
> 6.     else Q.head = Q.head - 1
> 7.     Q[Q.head] = x
> 
> TAIL-ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     Q[Q.tail] = x
> 5.     if Q.tail == Q.length
> 6.         Q.tail = 1
> 7.     else
> 8.         Q.tail = Q.tail + 1
> 
> HEAD-DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     x = Q[Q.head]
> 5.     if Q.head == Q.length
> 6.         Q.head = 1
> 7.     else Q.head = Q.head + 1
> 8.     return x
> 
> TAIL-DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     if Q.tail == 1
> 5.         Q.tail = Q.length
> 6.     else Q.tail = Q.tail - 1
> 7.     x = Q[Q.tail]
> 8.     return x
> ```
