# MPC MOC

Index for `cryptography/secure computation/` — several parties jointly compute on private inputs while revealing only what they are meant to learn.

- [[Secure Multi-party Computation]] — definitions, semi-honest vs. malicious adversaries, classic protocols (garbled circuits, GMW, BGW, …)
- [[Multi-Party Computation]] — check against the note above for overlap
- [[Oblivious Transfer]] — 1-out-of-2 OT, the workhorse primitive under many MPC constructions
- [[Private Information Retrieval]] — query a database without revealing which entry

Properties (`property/`): [[Correctness]] · [[t-Privacy]]

## Related

- [[Threshold MOC]] — secret sharing, the other underlying primitive
- [[Verifiable Computing MOC]] — ZK is used inside MPC compilers to handle malicious parties; in the other direction, [[Multi-Party Computation-in-the-Head]] turns an MPC protocol into a ZK proof
