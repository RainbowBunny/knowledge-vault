---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-14T22:39
---
# Language Basics

Naming convention 
- For variable and method: `camelCase`.
- For constant: `UPPER_SNAKE_CASE`.
- For class: `camelCase` but the first letter is also upper-case.
- For method: the first word should be a verb.
- For package: lowercase separate by dots.

## Variable

Different types of variables:
- **Instance Variables (Non-Static Fields)**: Value that are bound by each _instance_ of a class. 
- **Class Variables (Static Fields)**: Initialize only once for a class.
- **Local Variables**: 
- **Parameters**: 

| Data Type | Definition                               | Default Values |
| --------- | ---------------------------------------- | -------------- |
| `byte`    | `8`-bit signed two's complement integer  | `0`            |
| `short`   | `16`-bit signed two's complement integer | `0`            |
| `int`     | `32`-bit signed two's complement integer | `0`            |
| `long`    | `64`-bit signed two's complement integer | `0`            |
| `float`   | `32`-bit IEEE 754 floating point         | `0.0f`         |
| `double`  | `64`-bit IEEE 754 floating point         | `0.0d`         |
| `char`    | `16`-bit Unicode character.              | `'\u0000'`     |
| `boolean` | Only two values: `true` and `false`      | `false`        |
| `Object`  |                                          | `null`         |
## Operators

**Precedence:** `posfix > unary > multiplicative > additive > shift > relational > equality > bitwise AND > bitwise XOR > bitwise OR > logical AND > logical OR > ternary > assignment`

## Expressions, Statements, and Blocks

Type of statements:
- Expression Statement
- Declaration Statement
- Control Flow Statement
	- If-then Statement
	- Switch Statement
	- Do-while Statement

## Control Flow Statements

`switch` works with:
- `byte, short, char, int`
- Enumerated types
- `String`
- Special classes wrap certain primitive types: `Character, Byte, Short, Integer`

`break`:
- Unlabeled `break`: The statement `break;`, breaking the innermost loop.
- Labeled `break`: We can label a `loop` statement, breaking the labeled `loop` instead of the innermost loop.

`continue`:
- Unlabeled `continue`: The statement `continue;`, continue the innermost loop.
- Labeled `continue`: We can label a `continue` statement, continue the labeled `loop` instead of the innermost loop.

# Classes and Objects

## Classes

**Access modifier**:
- `public` – accessible from all classes.
- `protected` – accessible from subclasses.
- No modifier – accessible from package.
- `private` – accessible only within its own class.
Overloading Methods: Method with the same name but different parameters.
The class doesn't have to have a constructor, then the compiler automatically provided a no-argument which will call the no-argument constructor of the superclass.
**Arbitrary Number of Arguments**: The last argument can be followed by ... to have a arbitrary number of arguments.
**Passing Primitive Data Type Arguments**
**Passing Reference Data Type Arguments** = **Passing Classes**
Special:
```java
static {

}
```
**Final method**: Method can not be overridden.

## Objects

**The Garbage Collector**: 

## Nested Classes

**Nested classes** are divided into:
- **Inner classes**
- **Static nested classes**
Outer class can be `public` or `private`.
Inner class can be `private`, `public`, `protected` or *package private*.
Usage for nested class:
- **It is a way of logically grouping classes that are only used in one place**
- **It increases encapsulation**
- **It can lead to more readable and maintainable code**
Local classes: Class defined in the body of a method.
Local classes and inner classes cannot define or declare any static members.
Anonymous classes

# Interfaces and Inheritance


# Number and Strings

## Numbers

## Characters

**Escape Sequences**:
- `\t`: tab
- `\b`: backspace
- `\n`: newline
- `\r`: carriage return
- `\f`: form feed
- `\'`: 
- `\"`:
- `\\`: 

## Autoboxing and Unboxing

`Autoboxing`: Automatic conversion from primitive types to corresponding object wrapper classes.
`Unboxing`: Conversion goes other way.

# Packages

## Create and Using Packages

