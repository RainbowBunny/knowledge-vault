---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-12T19:12
---
## Ghidra

`Ctrl + Shift + F` for reference.

> [!remark] Copy string
> Convert the data into array type if needed, then select the section and choose copy special.

## IDA Pro

**Phase 1: The "Low Hanging Fruit" (Automated Identification)**

Before you dive into assembly, force IDA to identify as much library code as possible. Your goal is to separate the "wheat" (user code) from the "chaff" (standard library code like `glibc`, `openssl`, etc.).

### 1. Apply FLIRT Signatures

IDA ships with Fast Library Identification and Recognition Technology (FLIRT) signatures.
- **Action:** Go to the **Signatures** subview (`Shift + F5`).
- **Right-click -> Apply new signature**.
- Since you know it is 64-bit Linux (SYSV), look for signatures like `libc`, `glibc`, or `libpthread` targeted at `x86_64` (often labeled `vc` or `gcc`).
- **Why:** If you can match standard functions, IDA will rename `sub_401230` to `_printf`, saving you hours of analysis.

### 2. Leverage Lumina

IDA 9.x relies heavily on Lumina (cloud-based metadata).

- **Action:** Wait for the initial auto-analysis to finish. Then, go to **Lumina -> Pull all metadata**.
- **Why:** Lumina compares function hashes against a central database. It is surprisingly effective at identifying statically linked crypto libraries (like OpenSSL) and Golang/Rust runtime functions, even in stripped binaries.

### Python 

Error: `Can not load IDAPython`
Resolve: `idapyswitch.exe --force-path ...\python3.dll`

> [!remark]
> `Space` for text view
> `x` for reference

[https://godbolt.org/](https://godbolt.org/)

## Memory layout

> [!definition] Memory Layout
> - **Data**: This term can be used to refer to a specific section of memory called the data section, which contains values that are put in place when a program is initially loaded. These values are sometimes called static values because they may not change while the program is running, or they may be called global values because they are available to any part of the program. 
> - **Code**: Code includes the instructions fetched by the CPU to execute the program’s tasks. The code controls what the program does and how the program’s tasks will be orchestrated. 
> - **Heap**: The heap is used for dynamic memory during program execution, to create (allocate) new values and eliminate (free) values that the program no longer needs. The heap is referred to as dynamic memory because its contents can change frequently while the program is running. 
> - **Stack**: The stack is used for local variables and parameters for functions, and to help control program flow. We will cover the stack in depth later in this chapter.

## Secure Computing (SECCOMP)

> [!remark]
> [seccomp-tools](https://github.com/david942j/seccomp-tools)

## Virtual Machine

> [!remark]
> One important thing about virtual machine is that we need to determine the opcode.

> [!example]
> `Magic Number + Function Count + Address + Function Name Length + Function name`

## Techniques

### Packing

https://github.com/upx/upx

```
upx -d <file>
```

### Control Flow Obfuscation

> [!proposition]
> The trap `UD2` which stands for **undefined instruction** is an opcode designed by Intel to be guaranteed-invalid, and CPU will raise an **Illegal Instruction Exception (Signal 4/SIGILL)**. This signal can be caught with `sigaction` to add a trap handler. After the handler finished, the execution would be continued.

> [!proposition]
> Be careful with functions that can be put in the init array section.


## Android Mobile App

> [!remark]
> Sometimes, the app is just a wrapper for something else, so you might want to check the assets.

## Unity

### CSharp

> [!remark] Reverse Enginner
> Tool that we can use: https://github.com/dnSpy/dnSpy
> Usually, control flow of the game is `Assembly-CSharp.dll`.
> To get all assets of the Unity game, we can use [UnityPy](https://pypi.org/project/UnityPy/).

Example:
```python
import os
import UnityPy
from PIL import Image

# -----------------------
# Helpers
# -----------------------

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def safe_name(name, fallback):
    return name if name else fallback

# -----------------------
# Sprite extraction
# -----------------------

def export_sprite(obj, out_dir, sprite_cache):
    data = obj.parse_as_object()
    name = safe_name(data.m_Name, f"Sprite_{obj.path_id}")

    img = data.image
    if not img:
        return

    path = os.path.join(out_dir, f"{name}.png")
    ensure_dir(out_dir)
    img.save(path, "PNG")

    sprite_cache[obj.path_id] = img

# -----------------------
# Texture2D extraction
# -----------------------

def export_texture(obj, out_dir):
    data = obj.parse_as_object()
    name = safe_name(data.m_Name, f"Texture_{obj.path_id}")

    img = data.image
    if not img:
        return

    path = os.path.join(out_dir, f"{name}.png")
    ensure_dir(out_dir)
    img.save(path, "PNG")

# -----------------------
# Animation extraction
# -----------------------

def extract_sprite_animation(clip, sprite_cache):
    frames = []

    for curve in clip.m_ObjectReferenceCurves:
        if curve.attribute != "m_Sprite":
            continue

        for key in curve.keyframes:
            sprite_ptr = key.value
            if not sprite_ptr:
                continue

            sprite_obj = sprite_ptr.read()
            if not sprite_obj:
                continue

            sprite_id = sprite_obj.path_id
            img = sprite_cache.get(sprite_id)

            # If sprite wasn’t exported yet, extract on demand
            if img is None and sprite_obj.image:
                img = sprite_obj.image
                sprite_cache[sprite_id] = img

            if img:
                frames.append((key.time, img))

    # Sort by time
    frames.sort(key=lambda x: x[0])
    return [img for _, img in frames]

def export_animation(obj, out_dir, sprite_cache):
    clip = obj.parse_as_object()
    name = safe_name(clip.m_Name, f"Animation_{obj.path_id}")

    frames = extract_sprite_animation(clip, sprite_cache)
    if not frames:
        return

    anim_dir = os.path.join(out_dir, name)
    ensure_dir(anim_dir)

    # Export PNG sequence
    for i, img in enumerate(frames):
        img.save(os.path.join(anim_dir, f"{i:03}.png"), "PNG")

    # Export GIF preview
    gif_path = os.path.join(out_dir, f"{name}.gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )

# -----------------------
# Main unpacker
# -----------------------

def unpack_all_assets(source_folder: str, destination_folder: str):
    sprite_cache = {}

    for root, _, files in os.walk(source_folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                env = UnityPy.load(path)
            except Exception:
                continue

            for obj in env.objects:
                try:
                    if obj.type.name == "Sprite":
                        export_sprite(obj, os.path.join(destination_folder, "sprites"), sprite_cache)

                    elif obj.type.name == "Texture2D":
                        export_texture(obj, os.path.join(destination_folder, "textures"))

                    elif obj.type.name == "AnimationClip":
                        export_animation(obj, os.path.join(destination_folder, "animations"), sprite_cache)

                except Exception as e:
                    print(f"Failed {obj.type.name} {obj.path_id}: {e}")

# -----------------------
# Run
# -----------------------

unpack_all_assets("Data", "assets")
```

### IL2CPP

> [!remark]
> Target:
> `lib/arm64-v8a/libil2cpp.so`
> `assets/bin/Data/Managed/Metadata/global-metadata.dat`
> Can use [ll2CppDumper](https://github.com/Perfare/Il2CppDumper) to analyze:
> ```
> il2cppdumper <>
> ```

> [!remark]
> If there are `lib/arm64-v8a` and `lib/armeabi-v7a` then we prefer analyzing the `arm64-v8a` (`64 bit`).
> - `libil2cpp.so`: game logic.
> - `libunity.so`: game engine (usually no game logic here so no need to analyze)
> - `libmain.so`: android bootstrap.


## Egret/HTML5 Game

> [!remark]
> For this type of game, the server will be referee and client will send the action that they want to make. Then, the server will decide what will happen. In this architecture, it is hard to do client side tampering.

## RPG Maker VX Ace

> [!remark]
> To extract the resource of the game, try:
> [rgssad](https://aur.archlinux.org/packages/rgssad)

## Cocos2d

> [!definition] Structure
> `Game.exe` = host + glue -> helper.
> `Cocos2d-x` = engine + main loop -> game logic.

## Fusion

> [!remark]
> When seeing something like `mmfs2.dll`
> https://github.com/AITYunivers/NebulaFD
> - AMGI
> - ANM
> - APK
> - CCN
> - EXE
> - IPA
> - KNP
> - MFA

## xp3

[xp3-tool](https://github.com/storycraft/xp3-tool)
`/mnt/c/Users/vmc15/Documents/Projects/xp3-tool/target/release/xp3-unpacker`