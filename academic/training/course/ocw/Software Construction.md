---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-27T17:48
---
Checking:
- **Static checking**: The bug is found automatically before the program even runs
- **Dynamic checking**: The bug is found automatically when the code is executed
- **No checking**: The language doesn't help you find the error at all.

Hacking (optimism):
- Bad: writing lots of code before testing any of it
- Bad: keeping all the details in your head, assuming you'll remember them forever, instead of writing them down in your code
- Bad: assuming that bugs will be nonexistent or else easy to find and fix

Engineering (pessimists):
- Good: write a little at a time, testing as you go.
- Good: document the assumptions that your code depends on.
- Good: defend your code against stupidity 

Target: Produce software that is:
- **Safety from bugs**
- **Easy to understand**
- **Ready for change**:

Why software testing is hard:
- **Exhaustive testing** is infeasible
- **Haphazard testing** is less likely to find bugs
- **Random or statistical testing** doesn't work well

**Test first Programming**:
1. Write a specification for the function.
2. Write tests that exercise the specification.
3. Write the actual code. Once your code passes the tests you wrote, you’re done.

## Testing

**Choosing Test Cases by Partitioning**:
For all parameters:
- Divides the input space into **subdomains**
- Include Boundaries 
Test suit can be:
- Use Cartesian product for all parameters.
- Cover each part.
**Blackbox testing**: choosing test cases only from the specification.
**Whitebox testing**: choosing test cases with knowledge of how the function is actually implemented.

**Coverage**: One way to judge a test suite, three types:
- **Statement coverage**: Is every statement run by some test case
- **Branch coverage**: For every `if` or `while` statement in the program, are both the true and the false direction taken by some test case?
- **Path coverage**: Is every possible combination of branches — every path through the program — taken by some test case?

**Unit test**: Tests for an individual module.
**Integration test**: Tests a combination of modules.
**Stub**: In integration testing, if a test is failed, the problem might come from the current function or every function it called, thus, we can create mock version so that we know these functions are correct.
**Automated testing**: Running the tests and checking their results automatically.
**Regression testing**: Running all tests after every change.

## Code Review

Principle:
- Don't Repeat Yourself
- Comment Where Needed
- Fail Fast
- Avoid Magic Numbers: Use `enum` instead of number because it's not self-explanatory.
- One Purpose For Each Variable
- Use Good Names
- Use Whitespace to Help the Reader
- Don’t Use Global Variables
- Methods Should Return Results, not Print Them

## Specifications

Structure:
- **Precondition**: indicated by the keyword requires.
- **Postcondition**: indicated by the keyword effects.

Two type of exceptions:
- `RuntimeException`, `Error` and their subclasses are **unchecked** exceptions.
- All other throwables: `Throwable`, `Exception` and all of their subclasses except for those of the `RuntimeException` and `Error` lineage are **checked** exceptions.

Three dimensions of designing specifications:
- How **deterministic** it is. Does the spec define only a single possible output for a given input, or allow the implementor to choose from a set of legal outputs?
- How **declarative** it is. Does the spec just characterize what the output should be, or does it explicitly say how to compute the output?
- How **strong** it is. Does the spec have a small set of legal implementations, or a large set?

## Avoid Debugging

Defense:
- Make Bugs Impossible: 
	- **Static checking**
	- **Dynamic checking**
	- **Immutability**
- Localize Bugs: 
	- Checking preconditions
	- **Modularity** means dividing up a system into components, or modules, each of which can be designed, implemented, tested, reasoned about, and reused separately from the rest of the system.
	- **Encapsulation** means building walls around a module (a hard shell or capsule) so that the module is responsible for its own internal behavior, and bugs in other parts of the system can’t damage its integrity.

## Debugging

Reproduce the bug
Understand the Location and Cause of the Bug:
1. **Study the data**
2. **Hypothesize**
3. **Experiment**
4. **Repeat**
Tips:
- **Bug localization by binary search**
- **Prioritize your hypotheses**
- **Swap components**
- **Make sure your source code and object code are up-to-date**
- **Get help**

## Abstraction

General principle in software engineering:
- **Abstraction**
- **Modularity**
- **Encapsulation**
- **Information hiding**
- **Separation of concerns**

Operation:
- Creators: Create new objects of the type.
- Observers: Take objects of the abstract type and return objects of a different type.
- Producers: Create new objects from old objects of the type.
- Mutators: Change objects.

**Representation Invariant**: What conditions must always be true about the internal representation.

**Abstract Function**: How does the concrete representation map to the abstract value.

**Representation Exposure Problem**: Because we are passing by reference many times, it raises the threat of exposing the reference to a supposedly immutable object and accidently changing it while reading it.

ADT invariants can replace preconditions.

## Interfaces

To implement ADT, use interfaces.
Be careful when use the constructor for ADT because interface do not support constructor, however, interface does support static methods. 

**Generic interfaces**: 

Reasons to use interface:
- **Documentation for both the compiler and for humans**
- **Allowing performance trade-offs**
- **Optional methods**
- **Methods with intentionally underdetermined specification**
- **Multiple views of one class**
- **More and less trustworthy implementations**

## Equality

**For immutable types:**
- `equals`: should compare abstract values (behavioral equality).
- `hashCode`: should map the abstract value to an integer.

**For mutable types:**
- `equals`: should compare references.
- `hashcode`: should map the reference into an integer.
$\rightarrow$ Should not be overridden.

## Concurrency

### Thread Safety

**Strategy 1: Confinement**
- Not sharing data between threads.
- Avoid global variables.

**Strategy 2: Immutability**
- No mutator methods.
- All field are private and final.
- No representation exposure.
- No mutation whatsoever of mutable objects in the rep – not even beneficent mutation.

**Strategy 3: Using Thread-safe Data Types**
- Because they use synchronization.

