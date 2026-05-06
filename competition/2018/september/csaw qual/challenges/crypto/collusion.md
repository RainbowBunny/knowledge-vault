---
type: challenge
event: csaw qual
name: collusion
category: crypto
note: "[[RSA Public Key Cryptosystem]]"
solved: ✅
---
Safe prime: $p = 2 q + 1$ where $q$ is a prime.

```go
type Group struct {
  P, Q *big.Int
  X    *big.Int
}
```
$n = pq$ and even number $x < \phi(n)$. Where $p, q$ are safe prime and $x$ is an even number.


Public key/Encrypter: $\{N = pq, H = 3^x \pmod N\}$
Private key/Decrypter: $\{N = pq, d = (x + id)^{-1} \pmod {\phi(N)} \}$

Encryption with PK, `id`, `message`: 
`V = (3^id H)^r mod N = 3^{r(x + id)}`
`K = 3^r mod N`
`shared = Sum256(K)`
`nonce`: 12 bytes
`body = AES-GCM(key = shared, message, nonce)`

Challenge:
`Encryptor.json`: Given $N = pq$ and $H = 3^x$ of public key.
`message.json`: Given `V, Nonce, body`
`bobs-key.json`: Given $d_b = (x + b)^{-1} \pmod {\phi(N)}$
`carols-key.json`: Given $d_c = (x + c)^{-1} \pmod {\phi(N)}$
We want to find $x$ and factor $N$. However, we know that:
$d_b(x + b) = d_c(x + c) = 1 \pmod {\phi(N)}$
So we can find $d_b d_c x = d_c (1 - b d_b) = d_b (1 - c d_c) \pmod{\phi(N)}$ and thus have a multiple of $\phi(N)$ and factor $N$. 

```python
from Crypto.Util.number import inverse

k_phi = D_carol + D_carol*(id_carol-id_bob)*D_bob-D_bob
E_bob = inverse_mod(D_bob, k_phi)
x_k = E_bob - id_bob
D_alice = inverse_mod(x_k+id_alice, k_phi)
key = pow(V, D_alice, N)
  
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from Crypto.Utils.number import long_to_byte, byte_to_long
from hashlib import sha256
from base64 import b64decode, b64encode
  
key_bytes = long_to_bytes(key)
aes_key = sha256(key_bytes).digest()
Nonce = "2NXgQhueKbVm5Pd8"
Nonce = b64decode(Nonce)
Body = b64decode("0ZWAaAxvazGfyTJSRPkyeHU9ZUSWSoWFObggHmmfb835TWFAzA==")

aesgcm = AESGCM(aes_key)
aesgcm.decrypt(Nonce, Body, associated_data=None)
```

