## Version Control

- **Repository**: a local or remote store of the versions in our project
- **Working copy**: a local, editable copy of our project that we can work on
- **File**: a single file in our project
- **Version** or **revision**: a record of the contents of our project at a point in time
- **Change** or **diff**: the difference between two versions
- **Head**: the current version

## Features of a version control system

- **Reliable**: 
- **Multiple files**:
- **Meaningful versions**:
- **Revert**:
- **Compare versions**:
- **Review history**:
- **Not just for code**:
Allow multiple people to work together:
- **Merge**
- **Track responsibility**
- **Work in parallel**
- **Work-in-progress**

```bash
git restore file
```
Restore a file to the last commit.

```bash
git fsck --lost-found --full
```
_FSCK = File System Check_
- Verifies the **integrity of the Git object database**
- Walks all objects: commits, trees, blobs, tags
- Finds **broken**, **missing**, or **unreachable** objects

```bash
git show hash
```

Git to sparse clone to get a specific folder instead of all repositories.
```shell
git clone --filter=blob:none --sparse <REPO>
```

```shell
git sparse-checkout add <folder>
```

## Git forensics

https://github.com/robisonsantos/packfile_reader