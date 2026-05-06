---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-02T10:22
---
[z3py](https://z3prover.github.io/api/html/namespacez3py.html)

# Class

## Solver

```python
s = Solver()
```

### add

Signature: `def add(self, *args)`
Assert constraints into the solver.
```python
s.add(x > 0, x < 2)
```

### check

Signature: `def check(self, * assumptions)`
Check whether the assertions in the given solver plus the optional assumptions are consistent or not.
```python
s.check()
```

### model

Signature: `def model(self)`
Return a model for the last `check()`.
```python
s = Solver()
a = Int('a')
s.add(a + 2 == 0)
s.check()
s.model()
```

## Function



| Signature                      | Note                                                                                             | Example                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `And(*args)`                   |                                                                                                  | `p, q, r = Bools('p q r')`<br>`And(p, q, r)`                   |
| `BitVec(name, bv, ctx = None)` | Returns a bit-vector constant named `name`. `bv` may be the number of bits of a bit-vector sort. | `x = BitVec('x', 16)`                                          |
| `BitVecVal(sz, ctx = None)`    | Returns a bit-vector value with the given number of bits.                                        | `v = BitVecVal(10, 32)`                                        |
| `Bool(name, ctx = None)`       | Returns a Boolean constant named `name`.                                                         | `p = Bool('p')`                                                |
| `Bools(name, ctx = None)`      | Returns a tuple of Boolean constants.                                                            | `p, q, r = Bools('p q r')`                                     |
| `Implies(a, b, ctx = None)`    | Create a Z3 implies expression.                                                                  | `p, q = Bools('p q')`<br>`Implies(p, q)`                       |
| `z3py.LShR(a, b)`              | Create the Z3 expression logical right shift. (`a >> b`)                                         | `x, y = BitVecs('x y', 32)`<br>`LShR(x, y)`                    |
| `Or(*args)`                    |                                                                                                  | `p, q, r = Bools('p q r')`<br>`Or(p, q, r)`                    |
| `z3py.URem(a, b)`              | Create the Z3 expression (unsigned) remainder `self % other`.                                    | `x = BitVec('x', 32)`<br>`y = BitVec('y', 32)`<br>`URem(x, y)` |
