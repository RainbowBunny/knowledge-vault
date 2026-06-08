---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-10T10:45
---
## Common

- [[linux#binwalk|binwalk]]

### file

Determine file type. More information: [https://manned.org/file](https://manned.org/file).
- Give a description of the type of the specified file. Works fine for files with no file extension:
```bash
file {{filename}}
```
- Look inside a zipped file and determine the file type(s) inside:
```bash
file -z {{foo.zip}}
```
- Allow file to work with special or device files:
```bash
file -s {{filename}}
```
- Don't stop at first file type match; keep going until the end of the file:
```bash
file -k {{filename}}
```
- Determine the mime encoding type of a file:
```bash
file -i {{filename}}
```

### foremost



### steghide

Target: [[#JPG]], [[#BMP]]
First argument

| Argument            | Explanation                            |
| ------------------- | -------------------------------------- |
| `embed`             | Embed data                             |
| `extract`           | Extract data                           |
| `info` `<filename>` | Display information about `<filename>` |
Extracting options:

| Argument            | Explanation                   |
| ------------------- | ----------------------------- |
| `-sf` `<filename>`  |                               |
| `-p` `<passphrase>` |                               |
| `-xf` `<filename>`  |                               |
| `-f`                | Overwrite existing files      |
| `-q`                | Suppress information messages |
| `-v`                | Display detailed information  |

### stegsolve


### dd

### ffmpeg

```
ffmpeg -i smt.mkv
```

```
ffmpeg -dump_attachment:t "" -i chal.mkv
```

# Image

> [!remark]
> When in doubt about LSB, just count the number of 1/number of pixel. Normally, this number should be approx 1/2.

## JPG


## PNG

- [[linux#pngcheck|pngcheck]]
- zsteg

### Other

- Frequency analysis for pixels.
- Peano sequence for permuting pixels

## BMP


## GIF

Extract frames: [https://ezgif.com/split](https://ezgif.com/split)


# Document
## PDF

### qpdf

> [!remark]
> The first step of analyzing PDF is using the `--qdf` options:
>```
 qpdf --qdf file.pdf target.pdf
>```
> In order to rewrites the PDF into a `QDF` format so that the internal structure of the PDF human-readable and diff-friendly.

- **zlib-flate** -compress | -uncompress: Hidden data might be hidden in the deleted stream in the PDF document, look for `/Filter/FlateDecode` object . The stream data begins with `78 da ec bc` .

## Microsoft Word

> [!remark]
> We can analyze the internal structure of `.docx` file by extracting the docx file as zip.

# Audio

## kt

[klystrack](https://kometbomb.github.io/klystrack/)

## midi

A MIDI file (`.mid`) is a Musical Instrument Digital Interface file that contains musical information in digital format. Unlike audio files like MP3 or WAV, MIDI files don't store actual sound recordings. Instead, they store instructions about how music should be played, including notes, timing, pitch, velocity, and instrument information.

To read this `.mid` file, we can use python package `mido`.

```python
import mido

def midi_to_text(input_mid_file, output_txt_file):
    mid = mido.MidiFile(input_mid_file)
    with open(output_txt_file, 'w', encoding='utf-8') as f:
        
        for i, track in enumerate(mid.tracks):
            f.write(f'Track {i}: {track.name}\n')
            for msg in track:
                f.write(str(msg) + '\n')
```

# Video

# Font

> [!remark]
> https://fontdrop.info/#/?darkmode=true

# Radio

> [!remark]
> [gqrx](https://www.gqrx.dk/)