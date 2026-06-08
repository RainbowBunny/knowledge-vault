---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-28T16:07
---
## Ports

| Protocol         | Port     | Description                                             |
| ---------------- | -------- | ------------------------------------------------------- |
| HTTP             | 5985     | WinRM over HTTP                                         |
| HTTPS            | 5986     | WinRM over HTTPS                                        |
| WS-Management    | 80 / 443 | When proxies or via IIS (Internet Information Services) |
| WinRM inside SMB | 47001    | Windows Remote Shell                                    |

## Signatures

**HTTP headers**:

```
User-Agent: Microsoft WinRM Client
Content-Type: application/soap+xml;charset=UTF-8
Authorization: NTLM TlRM...
```

## Decyption

- [winrm_decrypt.py](https://gist.github.com/jborean93/d6ff5e87f8a9f5cb215cd49826523045/)

