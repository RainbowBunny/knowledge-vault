---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-03T23:27
---
**Compression Ratio Info-leak Made Easy** is a security vulnerability of compression algorithm. Compression algorithm usually use two tricks:
- The most often used letters get the shortest representation.
- Any phrase that is repeated only gets stored once.

Target of the attack: 
- If a text contains both a secret and a user-controlled part, we can guess the secret by just looking at the length of the compressed result.
- If encrypt option is `compress then encrypt`.
