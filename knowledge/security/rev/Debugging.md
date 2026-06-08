---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-05T07:31
---
# Default

## Running

| Commands   | Argument                    | Explanation                                      |
| ---------- | --------------------------- | ------------------------------------------------ |
| `gdb`      | `<program>` `[core dump]`   | Start GDB (with optional core dump).             |
| `gdb`      | `--args` `<program>` `args` | Start GDB and pass arguments                     |
| `gdb`      | `--pid` `<pid>`             | Start GDB and attach to process                  |
| `set args` | `<args...>`                 | Set arguments to pass to program to be debugged. |
| `run`      |                             | Run the program to be debugged.                  |
| `kill`     |                             | Kill the running program.                        |

## Breakpoints

| Commands  | Argument        | Explaination                 |
| --------- | --------------- | ---------------------------- |
| `break`   | `<where>`       | Set a new breakpoint.        |
| `delete`  | `<breakpoint#>` | Remove a breakpoint.         |
| `clear`   |                 | Delete all breakpoints.      |
| `enable`  | `<breakpoint#>` | Enable a disabled breakpoint |
| `disable` | `<breakpoint#>` | Disable a breakpoint.        |

## Watchpoints

| Commands  | Argument        | Explaination          |
| --------- | --------------- | --------------------- |
| `watch`   | `<where>`       | Set a new watchpoint. |
| `delete`  | `<watchpoint#>` | Delete a watchpoint.  |
| `enable`  | `<watchpoint#>` | Enable a watchpoint.  |
| `disable` | `<watchpoint#>` | Disable a watchpoint. |

## `<where>`

| Argument           | Explaination                                            |
| ------------------ | ------------------------------------------------------- |
| `function_name`    | Break/watch the named function.                         |
| `line_number`      | Break/watch the line number in the current source file. |
| `file:line_number` | Break/watch the line number in the named source file.   |

## Conditions

| Commands    | Argument                      | Explaination                                                                                                                   |
| ----------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `break`     | `<where>` `if` `<condition>`  | Break at the given location if the condition is met. Conditions may be almost any C expression that evaluate to true or false. |
| `watch`     | `<where>` `if` `<condition>`  | Watch at the given location if the condition is met. Conditions may be almost any C expression that evaluate to true or false. |
| `condition` | `<breakpoint#>` `<condition>` | Set/change the condition of an existing break- or watchpoint.                                                                  |

## Examining the stack

| Commands                        | Argument   | Explaination                                                   |
| ------------------------------- | ---------- | -------------------------------------------------------------- |
| `backtrace` / `where`           |            | Show call stack.                                               |
| `backtrace full` / `where full` |            | Show call stack, also print the local variables in each frame. |
| `frame`                         | `<frame#>` | Select the stack frame to operate on.                          |

## Stepping

| Commands   | Explaination                                                        |
| ---------- | ------------------------------------------------------------------- |
| `step`     | Go to next instruction (source line), diving into function.         |
| `next`     | Go to next instruction (source line) but donʻt dive into functions. |
| `finish`   | Continue until the current function returns.                        |
| `continue` | Continue normal execution.                                          |

## Variables and memory

| Commands             | Argument     | Explaination                                                                                                                                                                                                                                              |
| -------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `print` / `format`   | `<what>`     | Print content of variable/memory location/register.                                                                                                                                                                                                       |
| `display` / `format` | `<what>`     | Like `print`, but print the information after each stepping instruction.                                                                                                                                                                                  |
| `undisplay`          | `<display#>` | Remove the `display` with the given number.                                                                                                                                                                                                               |
| `enable display`     | `<display#>` | Enable the `display` with the given number.                                                                                                                                                                                                               |
| `disable display`    | `<display#>` | Disable the `display` with the given number.                                                                                                                                                                                                              |
| `x/nfu`              | `<address>`  | Print memory. <br>`n`: How many units to print (default 1). <br>`f`: Format character (like "print"). <br>`u`: Unit. Unit is one of: <br>- `b`: Byte, <br>- `h`: Half-word (two bytes) <br>- `w`: Word (four bytes) <br>- `g`: Giant word (eight bytes)). |

## Format

| Format | Explaination                          |
| ------ | ------------------------------------- |
| `a`    | Pointer.                              |
| `c`    | Read as integer, print as character.  |
| `d`    | Integer, signed decimal.              |
| `f`    | Floating point number.                |
| `o`    | Integer, print as octal.              |
| `s`    | Try to treat as C string.             |
| `t`    | Integer, print as binary (t = "two"). |
| `u`    | Integer, unsigned decimal.            |
| `x`    | Integer, print as hexadecimal.        |

## `<what>`

| Arguments                  | Explaination                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `expression`               | Almost any C expression, including function calls (must be prefixed with a cast to tell GDB the return value type).             |
| `file_name::variable_name` | Content of the variable defined in the named file (static variables).                                                           |
| `function::variable_name`  | Content of the variable defined in the named function (if on the stack).                                                        |
| `{type}address`            | Content at address, interpreted as being of the C type type.                                                                    |
| `$register`                | Content of named register. Interesting registers are $esp (stack pointer), $ebp (frame pointer) and $eip (instruction pointer). |

## Threads

| Commands | Arguments   | Explaination                |
| -------- | ----------- | --------------------------- |
| `thread` | `<thread#>` | Chose thread to operate on. |

## Manipulating the program

| Commands  | Arguments                     | Explaination                                                               |
| --------- | ----------------------------- | -------------------------------------------------------------------------- |
| `set var` | `<variable_name>` = `<value>` | Change the content of a variable to the given value.                       |
| `return`  | `<expression>`                | Force the current function to return immediately, passing the given value. |

## Sources

| Commands    | Arguments                  | Explaination                                                                                                                                                       |
| ----------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `directory` | `<directory>`              | Add directory to the list of directories that is searched for sources.                                                                                             |
| `list`      |                            | Shows the current or given source context. The filename may be omitted. If last is omitted the context starting at start is printed instead of centered around it. |
| `list`      | `<filename>:<function>`    | -                                                                                                                                                                  |
| `list`      | `<filename>:<line_number>` | -                                                                                                                                                                  |
| `list`      | `<first>,<last>`           | -                                                                                                                                                                  |
| `set`       | `listsize` `<count>`       | Set how many lines to show in "list".                                                                                                                              |

## Signals

| Commands | Arguments              | Explaination                                                                                                                                                                                                               |
| -------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `handle` | `<signal>` `<options>` | Set how to handle signles. Options are:<br>- (no)print: (Donʻt) print a message when signals occurs. <br>- (no)stop: (Donʻt) stop the program when signals occurs. <br>- (no)pass: (Donʻt) pass the signal to the program. |

## Informations

| Commands             | Arguments       | Explaination                                                     |
| -------------------- | --------------- | ---------------------------------------------------------------- |
| `disassemble`        |                 | Disassemble the current function or given location.              |
| `disassemble`        | `<where>`       | -                                                                |
| `info args`          |                 | Print the arguments to the function of the current stack frame.  |
| `info breakpoints`   |                 | Print informations about the break- and watchpoints.             |
| `info display`       |                 | Print informations about the "displays“.                         |
| `info locals`        |                 | Print the local variables in the currently selected stack frame. |
| `info sharedlibrary` |                 | List loaded shared libraries.                                    |
| `info signals`       |                 | List all signals and how they are currently handled.             |
| `info threads`       |                 | List all threads.                                                |
| `show directories`   |                 | Print all directories in which GDB searches for source files.    |
| `show listsize`      |                 | Print how many are shown in the "list" command.                  |
| `whatis`             | `variable_name` | Print type of named variable.                                    |

# gdb-pwndbg



# gdb-gef

[https://hugsy.github.io/gef/](https://hugsy.github.io/gef/)

| Commands                             | Arguments                                                        | Usage                                                                                                                                                                                                                                             |
| ------------------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases`                            | `add` `[alias]` `[command]`                                      | Create an alias for command                                                                                                                                                                                                                       |
| `aliases`                            | `rm` `[alias]`                                                   | Remove an alias                                                                                                                                                                                                                                   |
| `aliases`                            | `ls`                                                             | Listing aliases                                                                                                                                                                                                                                   |
| `aslr`                               |                                                                  | Check if `aslr` is on                                                                                                                                                                                                                             |
| `aslr`                               | `on`                                                             | Enable `aslr`                                                                                                                                                                                                                                     |
| `aslr`                               | `off`                                                            | Disable `aslr`                                                                                                                                                                                                                                    |
| `canary`                             |                                                                  | If the currently debugged process was compiled with the Smash Stack Protector (SSP), display the value of the canary                                                                                                                              |
| `checksec`                           |                                                                  | Determine which security protections are enabled                                                                                                                                                                                                  |
| `dereference`                        | `[start_address]` `[-l n_address]` `[-r base_location]`          | Dereferencing an address, default `start_address=$sp`, for `n_address=10` consecutive address and show relative to `base_location`                                                                                                                |
| `flags/edit-flags`                   | `[(+\|-\|~) FLAGNAME]`                                           | Set, unset or toggle flag                                                                                                                                                                                                                         |
| `elf/elf-info`                       | `[--filename /path]`                                             | Provides some basic information on the currently loaded ELF binary.                                                                                                                                                                               |
| `entry-break/start`                  |                                                                  | Set a temporary breakpoint at `main` or `__libc_start_main` or start of ELF.                                                                                                                                                                      |
| `format-string-helper/fmtstr-helper` |                                                                  | Create breakpoint against serval insecure format string targets.                                                                                                                                                                                  |
| `functions`                          |                                                                  | List all convenience functions provided by GEF.                                                                                                                                                                                                   |
| `got`                                | `[--all]` `[filers]`                                             | Display current state of `GOT table`                                                                                                                                                                                                              |
| `nop`                                | `[LOCATION]` `[--i ITEMS]` `[--f]` `[--n]` `[--b]`               | Patch instructions with `nops`<br>`LOCATION` Address<br>`--i ITEMS` Number of items to insert<br>`--f` Force patch even if overwriting partial instruction<br>`--n` Insert exactly `ITEMS` `nop` instruction<br>`--b` Fill `ITEM` bytes with nops |
| `pattern`                            | `create` `[-h]` `[-n N]` `[length]`                              | Create cyclic sequence for `length` byte with unique subsequence length `N`                                                                                                                                                                       |
| `pattern`                            | `search` `[-h]` `[-n N]` `[--max-length MAX_LENGTH]` `[pattern]` |                                                                                                                                                                                                                                                   |
| `pie breakpoint`                     |                                                                  |                                                                                                                                                                                                                                                   |
| `pie info`                           |                                                                  |                                                                                                                                                                                                                                                   |
| `pie delete`                         |                                                                  |                                                                                                                                                                                                                                                   |
| `pie attach`                         |                                                                  |                                                                                                                                                                                                                                                   |
| `pie run`                            |                                                                  |                                                                                                                                                                                                                                                   |
| `registers/reg`                      |                                                                  | Print all the registers and dereference any pointers.                                                                                                                                                                                             |
| `stepover`                           |                                                                  | Step 1 instruction.                                                                                                                                                                                                                               |
| `skipi`                              | `[LOCATION] [--n NUM_INSTRUCTIONS]`                              | `[LOCATION]`: From where to skip (default `$PC`)<br>`[--n NUM_INSTRUCTIONS]`: how many instruction to skip                                                                                                                                        |
| `vmmap`                              |                                                                  | Displays the target process's entire memory space mapping.                                                                                                                                                                                        |

# radare2

[Link](https://r2wiki.readthedocs.io/en/latest/options/p/pd-sz/)

**Start analyze with `radare2`**
```bash
r2 -A ./binary
```

**List function:**
```bash
afl
```

**Go to a function:**
```bash
s FUNCTION_NAME
```

## Disassembly

**Disassemble current function**:
```bash
pdf
```

**Disassemble N instructions**:
```bash
pd N
```

**Disassemble N instructions backward:**
```bash
pd -N
```

**Disassemble N bytes:**
```bash
pD N
```

