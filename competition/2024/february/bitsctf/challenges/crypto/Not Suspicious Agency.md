---
type: challenge
event: february
name: Not Suspicious Agency
category: crypto
note: "[[Pseudorandom Number Generators#Dual Elliptic Curve Deterministic Random Bit Generator (DUAL_EC_DRBG)|DUAL EC DRBG]]"
solved: ✅
---
```python
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from tqdm import tqdm

# =========================
# Curve: NIST P-256
# =========================
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = -3
b = int("5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B", 16)

E = EllipticCurve(GF(p), [a, b])
n = int("ffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551", 16)

# =========================
# Public points (From your challenge)
# =========================
Px, Py = (82608569474992041160607468321330734781976984380007427368012865557687600622709, 
          35069256181227824748874498744049288021402083829396944376506375002277135146766)
Qx, Qy = (73715635164746483174925677582577549814394654274863737334365964739059628583962, 
          109056745950753818921710346904416730969104963723164318521067168664927746119221)

P = E(Px, Py)
Q = E(Qx, Qy)

# =========================
# Data provided by challenge
# =========================
known_plain = b'This is a test string for debugging'
cipher_known = b'\xbd\xfe\xe5`\x1fQGU*\xcf\xc7\xde=\x068\xa6\xa7\x85.\x8a\x81\x8apF\xea\xda\xc2,\xe4\xddS\xa2U\x93\xec'
cipher_flag  = b'\xd7\x80q!X\x03\x0c\x05\x8d\xa5\xc5/MU\xffi>\xab%\xd4\xefeD\xdbYRk"\x94a\xbd\x19\x05&\xd39\x99Y'

d = 106285652031011072675634249779849270405
d_inv = inverse(d, n)

def xor(a, b):
    return bytes(x ^^ y for x, y in zip(a, b))

# Re-implementing the generator exactly as the challenge does
def generate(P, Q, s):
    while True:
        r = int((s * P).xy()[0])
        # Dual_EC yields all but the first 2 bytes of the x-coordinate
        res = long_to_bytes(int((r * Q).xy()[0]))
        # Handle padding if the x-coord is shorter than 32 bytes
        res = res.rjust(32, b'\x00')
        yield from res[2:]
        s = int((r * P).xy()[0])

# =========================
# The Attack
# =========================

# 1. Get the keystream for the first block (30 bytes)
full_keystream = xor(known_plain, cipher_known)
target_ks = full_keystream[:30]
ks_int = bytes_to_long(target_ks)

print("[*] Bruteforcing the 16 truncated bits...")

recovered_s_next = None

for hi in tqdm(range(1 << 16)):
    # Reconstruct the 256-bit candidate for (r * Q).x
    x_candidate = (hi << 240) | ks_int
    
    try:
        # Lift x to a point on the curve
        R = E.lift_x(x_candidate)
        
        # Backdoor: S_next = r * P = d_inv * (r * Q)
        S_next_point = d_inv * R
        s_next_candidate = int(S_next_point.xy()[0])
        
        # Verify against the REMAINING bytes of the known keystream (the next block)
        g = generate(P, Q, s_next_candidate)
        # The remaining known bytes start at index 30
        remaining_len = len(full_keystream) - 30
        test_bytes = bytes([next(g) for _ in range(remaining_len)])
        
        if test_bytes == full_keystream[30:]:
            print(f"[+] Match found! hi = {hi}")
            recovered_s_next = s_next_candidate
            
            # Since 'g' already consumed 'remaining_len' bytes, it is now 
            # perfectly synced to decrypt the flag.
            flag_ks = bytes([next(g) for _ in range(len(cipher_flag))])
            print(f"[+] FLAG: {xor(cipher_flag, flag_ks).decode()}")
            break
            
    except ValueError:
        # x_candidate is not a valid x-coordinate on the curve
        continue

if not recovered_s_next:
    print("[-] Failed to recover state. Check P, Q, or d.")
```

