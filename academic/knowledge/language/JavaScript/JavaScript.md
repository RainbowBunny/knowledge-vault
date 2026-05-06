---
parent: "[[Fleeting MOC]]"
tags:
date: 2025-11-24T15:49
---
## Prototypes and inheritance

A JavaScript object is a collection of properties (pairs of `key:value`) where `value` can be either data or function.

Prototype in JavaScript is like the constructor of the object, where an object inherits all the properties of its prototype unless it has a key with the same name.

When a `key` is accessed, if the object does not have the `key`, its prototype and its parent's prototype will be lookup in that order.

The prototype of an object can be access by the `__proto__` key, and `prototype` of an object can be modified, but it is not recommended.

## Instance of

The `instanceof` operator checks if the `prototype` of the object appears anywhere in its prototype chain.

