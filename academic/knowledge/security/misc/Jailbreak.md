---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-15T10:08
---
## Bash

`${IFS}` can replace ` `
`regex` replace filename

## Pyjail

Warning: In some situation, some extra installed library like `numpy` can mess up with the challenge, so creating a new minimal environment with [[Conda]] is advised.

Every function object in Python has a `__call__` method:

```
x() <> x.__call__()
```

We can pass an integer `fd` to `open()` function thus:
- `open(0)`: Open `stdin` stream.
- `open(1)`: Open `stdout` stream.
- `open(2)`: Open `stderr` stream.
However, `open(0)` reading will not strip newline character.

Combine `next` and `open`:
`next(open(0))`: Read 1 line but not stripped.

Create False:
- `() in ()`

### popshell

```python
__import__('os').system('bash')
```

### print

```python
print("%s" % exp)
```
`-> eval(exp)` 

[https://gynvael.coldwind.pl/n/](https://gynvael.coldwind.pl/n/)