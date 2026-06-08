---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-27T20:11
---
## javax.crypto.Cipher

A `Cipher` object performs these tasks:
1. **Encryption**
2. **Decryption**
3. **Key wrapping/unwrapping** (encrypting keys)
4. **Generating IV/nonce automatically**
5. **Padding data**
6. **Combining an algorithm + mode + padding**

Operation modes: `opmode` parameters that use in telling Cipher the **type of operation**:

| Constant                  | Meaning              |
| ------------------------- | -------------------- |
| `Cipher.ENCRYPT_MODE` = 1 | Encrypt data         |
| `Cipher.DECRYPT_MODE` = 2 | Decrypt data         |
| `Cipher.WRAP_MODE` = 3    | Wrap a key           |
| `Cipher.UNWRAP_MODE` = 4  | Unwrap a wrapped key |
Usage:
```java
cipher.init(opmode, key);
cipher.init(opmode, key, iv);
cipher.init(opmode, key, secureRandom);
```

| Parameters   |                                                                            |
| ------------ | -------------------------------------------------------------------------- |
| Key          | - `SecretKey` (AES, DES)<br>- `PrivateKey` / `PublicKey` (RSA)             |
| IV/Nonce     | Required for:<br>- `AES/CBC`<br>- `AES/CTR`<br>- `AES/GCM`<br>- `ChaCha20` |
| SecureRandom | Used for:<br>- RSA padding<br>- automatic IV generation                    |
**Cipher Operation Flow**

**Encrypting**:
```java
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, key, iv);
byte[] ciphertext = cipher.doFinal(plaintext);
```

**Decrypting**:
```java
cipher.init(Cipher.DECRYPT_MODE, key, iv);
byte[] plaintext = cipher.doFinal(ciphertext);
```

**Encryption with update()**:
```java
cipher.update(buffer);
cipher.update(buffer2);
cipher.doFinal();
```

