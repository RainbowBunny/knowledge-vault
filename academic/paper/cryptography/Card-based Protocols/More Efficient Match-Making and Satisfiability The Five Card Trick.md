---
parent: "[[Fleeting MOC]]"
tags:
  - 🪴weedy
authors: Bert den Boer
date: 2025-09-24T09:30
---

## Abstract

A two-party cryptographic protocol for evaluating any binary gate is presented. It is more efficient than previous two-party computations, and can even perform single-party (i.e. satisfiability) proofs more efficiently than known techniques. As in all earlier multiparty computations and satisfiability protocols, commitments are a fundamental building block. Each party in our approach encodes a single input bit as 2 bit commitments. These are then combined to form 5 bit commitments, which are permuted, and can then be opened to reveal the output of the gate.
## Content

This paper is creating a protocol for two-party to calculate the output of a logic gate without revealing their inputs. However, we do not consider the case where one party can deduce the other's output by using their own output and the result.

The main idea of this paper is that we can encrypt 1 bit with a 2 bit sequence then two party will concatenate their commitment with a 0 (party 1 com, 0, party 2 com) and then shuffle the sequence. Then, the final sequence is revealed and participants can see the final output.

The paper then draw an analogy from the card sequence with the binary sequence by using a group homomorphism.
