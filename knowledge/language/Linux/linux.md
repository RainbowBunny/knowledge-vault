---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-05T11:10
---
## binwalk

Firmware Analysis Tool. More information: [https://github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk).
- Scan a binary file: 
```bash
binwalk {{path/to/binary}}
```
- Extract files from a binary, specifying the output directory:
```bash
binwalk --extract --directory {{output_directory}} {{path/to/binary}}
```
- Recursively extract files from a binary limiting the recursion depth to 2:
```bash
binwalk --extract --matryoshka --depth {{2}} {{path/to/binary}}
```
- Extract files from a binary with the specified file signature:
```bash
binwalk --dd '{{png image:png}}' {{path/to/binary}}
```
- Analyze the entropy of a binary, saving the plot with the same name as the binary and `.png` extension appended:
```bash
binwalk --entropy --save {{path/to/binary}}
```
- Combine entropy, signature and opcodes analysis in a single command:
```bash
binwalk --entropy --signature --opcodes {{path/to/binary}}
```

## dig

[Link](https://www.ibm.com/docs/en/aix/7.3.0?topic=d-dig-command)

## exiftool

Read and write meta information in files. More information: [https://exiftool.org](https://exiftool.org/).
- Remove all EXIF metadata from the given files:
```bash
exiftool -All= {{file1 file2 ...}}
```
- Move the date at which all photos in a directory were taken 1 hour forward:
```bash
exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}
```
- Move the date at which all JPEG photos in the current directory were taken 1 day and 2 hours backward:
```bash
exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg
```
- Only change the `DateTimeOriginal` field subtracting 1.5 hours, without keeping backups:
```bash
exiftool -DateTimeOriginal-=1.5 -overwrite_original
```
- Recursively rename all JPEG photos in a directory based on the `DateTimeOriginal` field:
```bash
exiftool '-filename
```

## gpg


| Argument          | Explanation                  |
| ----------------- | ---------------------------- |
| `-d` `<filename>` | Decrypt data                 |
| `-o` `<filename>` | Write output to `<filename>` |
## find

`find [path] -name "filename"`

## ltrace

Display dynamic library calls of a process. More information: [https://manned.org/ltrace](https://manned.org/ltrace).
- Print (trace) library calls of a program binary:
```bash
ltrace ./{{program}}
```
- Count library calls. Print a handy summary at the bottom:
```bash
ltrace -c {{path/to/program}}
```
- Trace calls to malloc and free, omit those done by libc:
```bash
ltrace -e malloc+free-@libc.so* {{path/to/program}}
```
- Write to file instead of terminal:
```bash
ltrace -o {{file}} {{path/to/program}}
```

## ldd

## nm


## nslookup

Query name server(s) for various domain records. More information: [https://manned.org/nslookup](https://manned.org/nslookup).

- Query your system's default name server for an IP address (A record) of the domain:
```bash
nslookup {{example.com}}
```
- Query a given name server for a NS record of the domain:
```bash
nslookup -type=NS {{example.com}} {{8.8.8.8}}
```
- Query for a reverse lookup (PTR record) of an IP address:
```bash
nslookup -type=PTR {{54.240.162.118}}
```
- Query for ANY available records using TCP protocol:
```bash
nslookup -vc -type=ANY {{example.com}}
```
- Query a given name server for the whole zone file (zone transfer) of the domain using TCP protocol:
```bash
nslookup -vc -type=AXFR {{example.com}} {{name_server}}
```
- Query for a mail server (MX record) of the domain, showing details of the transaction:
```bash
nslookup -type=MX -debug {{example.com}}
```
- Query a given name server on a specific port number for a TXT record of the domain:
```bash
nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}
```

## pngcheck

Print detailed information about and verify PNG, JNG, and MNG files. More information: [http://www.libpng.org/pub/png/apps/pngcheck.html](http://www.libpng.org/pub/png/apps/pngcheck.html).

- Print a summary for an image (width, height, and color depth):
```bash
pngcheck {{image.png}}
```
- Print information for an image with colorized output:
```bash
pngcheck -c {{image.png}}
```
- Print verbose information for an image:
```bash
pngcheck -cvt {{image.png}}
```
- Receive an image from stdin and display detailed information:
```bash
cat {{path/to/image.png}} | pngcheck -cvt
```
- search for PNGs within a specific file and display information about them:
```bash
pngcheck -s {{image.png}}
```
- Search for PNGs within another file and extract them:
```bash
pngcheck -x {{image.png}}
```

## readelf 

Displays information about ELF files. More information: [http://man7.org/linux/man-pages/man1/readelf.1.html](http://man7.org/linux/man-pages/man1/readelf.1.html).
- Display all information about the ELF file:
```bash
readelf -all {{path/to/binary}}
```
- Display all the headers present in the ELF file:
```bash
readelf --headers {{path/to/binary}}
```
- Display the entries in symbol table section of the ELF file, if it has one:
```bash
readelf --symbols {{path/to/binary}}
```
- Display the information contained in the ELF header at the start of the file:
```bash
readelf --file-header {{path/to/binary}}
```

## steghide

Steganography tool for JPEG, BMP, WAV and AU file formats. More information: [https://github.com/StefanoDeVuono/steghide](https://github.com/StefanoDeVuono/steghide).
- Embed data in a PNG, prompting for a passphrase:
```bash
steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}
```
- Extract data from a WAV audio file:
```bash
steghide extract --stegofile {{path/to/sound.wav}}
```
- Display file information, trying to detect an embedded file:
```bash
steghide info {{path/to/file.jpg}}
```
- Embed data in a JPEG image, using maximum compression:
```bash
steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}
```
- Get the list of supported encryption algorithms and modes:
```bash
steghide encinfo
```
- Embed encrypted data in a JPEG image, e.g. with Blowfish in CBC mode:
```bash
steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}
```

## strace

Troubleshooting tool for tracing system calls. More information: [https://manned.org/strace](https://manned.org/strace).

- Start tracing a specific process by its PID:
```bash
strace -p {{pid}}
```
- Trace a process and filter output by system call:
```bash
strace -p {{pid}} -e {{system_call_name}}
```
- Count time, calls, and errors for each system call and report a summary on program exit:
```bash
strace -p {{pid}} -c
```
- Show the time spent in every system call:
```bash
strace -p {{pid}} -T
```
- Start tracing a program by executing it:
```bash
strace {{program}}
```
- Start tracing file operations of a program:
```bash
strace -e trace=file {{program}}
```
