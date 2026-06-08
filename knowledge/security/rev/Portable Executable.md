
| DLL                            | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Kernel32.dll`                 | This is a very common DLL that contains core functionality, such as access and manipulation of memory, files, and hardware.                                                                                                                                                                                                                                                                               |
| `Advapi32.dll`                 | This DLL provides access to advanced core Windows components such as the Service Manager and Registry.                                                                                                                                                                                                                                                                                                    |
| `User32.dll`                   | This DLL contains all the user-interface components, such as buttons, scroll bars, and components for controlling and responding to user actions.                                                                                                                                                                                                                                                         |
| `Gdi32.dll`                    | This DLL contains functions for displaying and manipulating graphics.                                                                                                                                                                                                                                                                                                                                     |
| `Ntdll.dll`                    | This DLL is the interface to the Windows kernel. Executables generally do not import this file directly, although it is always imported indirectly by `Kernel32.dll`. If an executable imports this file, it means that the author intended to use functionality not normally available to Windows programs. Some tasks, such as hiding functionality or manipulating processes, will use this interface. |
| `WSock32.dll` and `Ws2_32.dll` | These are networking DLLs. A program that accesses either of these most likely connects to a network or performs network-related tasks.                                                                                                                                                                                                                                                                   |
| `Wininet.dll`                  | This DLL contains higher-level networking functions that implement protocols such as FTP, HTTP, and NTP.                                                                                                                                                                                                                                                                                                  |
> [!remark]
> The `Ex` suffix of window is when Microsoft updates the function but continue the support of the old function. The suffix `W` and `A` indicates ASCII version or wide character versions.

## PE File Headers and Sections

Sections

| Executable | Description                                                                                                                                                     |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.text`    | Contains the executable code                                                                                                                                    |
| `.rdata`   | Holds read-only data that is globally accessible within the program                                                                                             |
| `.data`    | Stores global data accessed throughout the program                                                                                                              |
| `.idata`   | Sometimes present and stores the import function information; if this section is not present, the import function information is stored in the `.rdata` section |
| `.edata`   | Sometimes present and stores the export function information; if this section is not present, the export function information is stored in the `.rdata` section |
| `.pdata`   | Present only in 64-bit executables and stores exception-handling information                                                                                    |
| `.rsrc`    | Stores resources needed by the executable                                                                                                                       |
| `.reloc`   | Contains information for relocation of library files                                                                                                            |
> [!remark]
> PEView
> PEBrowse Professional
> PE Explorer

Information

| Field           | Information Revealed                                                                |
| --------------- | ----------------------------------------------------------------------------------- |
| Imports         | Functions from other libraries that are used by the malware                         |
| Exports         | Functions in the malware that are meant to be called by other programs or libraries |
| Time Date Stamp | Time when the program was compiled                                                  |
| Sections        | Names of sections in the file and their sizes on disk and in memory                 |
| Subsystem       | Indicates whether the program is a command-line or GUI application                  |
| Resources       | Strings, icons, menus, and other information included in the file                   |
## Running Malware

> [!remark] Run dll
> ```
> rundll.exe DLLname, Export arguments
> ```
> Where `Export` is the function name in the export table or ordinal like `#1`.
> Also whenever DLL is loaded, `DLLMain` is executed

## Misc

> [!remark]
> If main looks like this:
> ```
> int __fastcall main(int argc, const char **argv, const char **envp)
{
  void *v4; // rbx
  int *v5; // rax
  _QWORD *v6; // rax
  v4 = *sub_14000F3D0();
  v5 = sub_14000F3C8();
  v6 = sub_1400078C0(*v5, (__int64)v4);
  return sub_140002A50(argc, v6);
}
> ```
> And there are some sign like `MEIPASS`, then this portable executable is generated by `pyinstaller` and can be dissect by [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor?tab=readme-ov-file)

## x32dbg/x64dbg

`Options > Preferences`

`Ctrl + G` to jump to address

`Scylla` to dump dll

