
# Autopsy

## fls

`fls` is a **file-listing tool in The Sleuth Kit (TSK)**. It reads directory structures **directly from a disk image or block device**.
**Basic invocation**:
```bash
fls [options] image [images] [inode]
```
Where:
- `image`: Disk image or block device (e.g. `disk.dd`, `/dev/loop0p1`)
- `images`: Additional image segments (for split images)
- `inode` _(optional)_: Directory inode to start from (if omitted then root directory is used)
**Option**:
- **File selection filters**:
	- `-a`: show `.` and `..`
	- `-d`: deleted entries only
	- `-u`: undeleted entries only
	- `-D`: directories only
	- `-F`: files only
- **Output format options**:
	- `-l`: long format (like `ls -l`)
	- `-p`: full path
	- `-m dir/`: mactime format for `/dir` in CSV compatible format.
	- `-h`: MD5 hash
- **Filesystem & image handling**:
	- `-f fstype`: manually specify file system (`ntfs`, `fat`, `ext4`, `apfs`, ...)
	- `-i imgtype`: specifies image container type (`raw`, `ewf`, `vmdk`, ...)
	- `-b dev_sector_size`: sector size in byte (commonly `512` or `4096`), important for advanced format drives and some RAID / embedded devices.
	- `-o imgoffset`: offset (in sectors) to the file system start, used when images contain a partition table or targeting a specific partition.
- **Pool / snap support (modern filesystems)**:
	- `-P pooltype`: Pool container type (`LVM`, `APFS`, `ZFS`)
	- `-B pool_volume_block`: specify which pool to access
	- `-S snap_id`: 
	- `-k password`: for encrypted pools
- **Traversal and verbosity**:
	- `-r`: recursive
	- `-v`: verbose
	- `-V`: version
- **Time handling**:
	- `-z ZONE`:
	- `-s seconds`:
`*`: Unallocated

## icat

`icat` (“inode cat”) extracts the **raw contents of a file** from a filesystem inside a disk image—**even if the file is deleted**, even if the OS cannot mount it, and even if it comes from a snapshot or pool container.
**Basic invocation**:
```bash
icat [options] image inum[-typ[-id]]
```
Different option:
- `-h`: Do not display holes in sparse files
- `-r`: Recover deleted file
- `-R`: Recover deleted and suppress errors
- `-s`: Display slack space

# V2


# Volatility 3

[volatility3](https://github.com/volatilityfoundation/volatility3)

## Windows

## Image Info

```bash
vol -f <file> windows.info
```

## Process Information

### PSList

```bash
vol -f <file> windows.pslist
vol -f <file> windows.psscan
vol -f <file> windows.pstree
```

Common process (expected)

| Type                   | Process                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| Core OS                | `System`, `smss.exe`, `csrss.exe`, `wininit.exe`, `services.exe`, `lsass.exe`, `winlogon.exe` |
| GUI / UX               | `explorer.exe`, `dwm.exe`, `ctfmon.exe`, `taskhostw.exe`                                      |
| Browsers               | `msedge.exe`, `firefox.exe`                                                                   |
| Defender / Security    | `MsMpEng.exe`, `MpDefenderCore.exe`, `SecurityHealth*.exe`                                    |
| Search / Cortana stack | `SearchIndexer.exe`, `SearchApp.exe`, `SearchProtocolHost.exe`                                |
| VM artifacts           | `VBoxService.exe`, `VBoxTray.exe`                                                             |
### Procdump



## Command Line

```bash
vol -f <file> windows.cmdline
```

## Hash dump

```
vol -f <file> windows.hashdump
```

## Linux disk

```
.bash_history
.ssh
```

