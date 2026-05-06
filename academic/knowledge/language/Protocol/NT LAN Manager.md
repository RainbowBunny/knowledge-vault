---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-27T15:47
---

| Step | Message    | Name              | Who Sends       | Purpose                                                         |
| ---- | ---------- | ----------------- | --------------- | --------------------------------------------------------------- |
| 1    | **Type 1** | NTLMSSP_NEGOTIATE | Client → Server | Client says: “I want to use NTLM and here are my capabilities.” |
| 2    | **Type 2** | NTLMSSP_CHALLENGE | Server → Client | Server sends a random challenge.                                |
| 3    | **Type 3** | NTLMSSP_AUTH      | Client → Server | Client proves identity by sending encrypted responses.          |
