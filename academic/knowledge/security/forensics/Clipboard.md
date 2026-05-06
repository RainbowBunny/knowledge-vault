---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-27T10:23
---
# Window

## Detection Method 1: ActivitiesCache.db

Prerequisite for clipboard data to be logged:
- Clipboard history enabled
- Clipboard sync across devices

The location for the artefact is in the following directory: `%AppData%\Local\ConnectedDevicesPlatform\<UserProfile>\`

File can be analyzed:
- `ActivitiesCache.db` (the database file that we can analyse)
- `ActivitiesCache.db-shm`
- `ActivitiesCache.db-wal` (the write-ahead log which can also be analysed for data)

Table: `SmartLookup`
- **StartTime** (epoch time) - When the data was first copied to the clipboard
- **ExpirationTime** (epoch time) - When the data will be deleted from the `ActivitiesCache.db` (roughly 12 hours)
- **ClipboardPayload** - Base64 encoded string of the clipboard contents
- **Payload** - This field tells you where the clipboard data was copied from
- **ActivityType** - Type 10 means data resides in clipboard, Type 16 shows if data was copied or pasted


## Detection Method 2: Memory Forensics



## Detection Method 3: Clipboard History Folder

Additionally, if clipboard history is enabled a folder path will be created storing clipboard data. The location for this is: `%AppData%\Local\Microsoft\Windows\Clipboard`

