
## ioctl.h

Function: `int ioctl(int fd, unsigned long request, void *arg)`

| Parameter | Meaning                                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `fd`      | File descriptor of the device (e.g., `/dev/kvm`, `/dev/sda`)                                                                     |
| `request` | The command code is a **32-bit encoded number** that uniquely identifies _which ioctl operation_ you want the kernel to perform. |
| `arg`     | Pointer to data needed for that command (input/output)                                                                           |
Returns value: 0 on success, -1 on error.

## mman.h

| Signature                                                                                                | Explanation | Returns                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `void *mmap(size_t length; void addr[length], size_t length, int prot, int flags, int fd, off_t offset)` |             | On success, returns a pointer to the mapped area.  <br>On error, the value `MAP_FAILED` is returned, and `errno` is set to indicate the error. |
| `int munmap(size_t length; void addr[length], size_t length)`                                            |             | On success, returns `0`.<br>On failure, it returns `-1`, and `errno` is set to indicate the error.                                             |
### prot

| Constant     | Value  | Explanation           |
| ------------ | ------ | --------------------- |
| `PROT_NONE`  | `0x00` | No permissions        |
| `PROT_READ`  | `0x01` | Pages can be read     |
| `PROT_WRITE` | `0x02` | Pages can be written  |
| `PROT_EXEC`  | `0x04` | Pages can be executed |
Protections are chosen from these bits, or-ed together

## flags

| Constant                      | Value          | Explanation                              |
| ----------------------------- | -------------- | ---------------------------------------- |
| `MAP_SHARED`                  | `0x0001`       | Share changes                            |
| `MAP_PRIVATE`                 | `0x0002`       | Changes are private                      |
| `MAP_FIXED`                   | `0x0010`       | Map address must be exactly as requestes |
| `__MAP_NOREPLACE`             | `0x0800`       | Fail if address not available            |
| `MAP_ANON`<br>`MAP_ANONYMOUS` | `0x1000`       | Allocated from memory, swap space        |
| `__MAP_NOFAULT`               | `0x2000`       |                                          |
| `MAP_STACK`                   | `0x4000`       | Mapping is used for a stack              |
| `MAP_CONCEAL`                 | `0x8000`       | Omit from dumps                          |
| `MAP_FAILED`                  | `((void *)-1)` | Error return from `mmap()`               |
Flags contain sharing type and options.
Sharing types; choose one.

## types.h

| Type     | Explanation                                      |
| -------- | ------------------------------------------------ |
| `off_t`  | Signed `64-bit`: standard POSIX file offset type |
| `loff_t` | Signed `64-bit`: Linux kernel type               |

## socket.h


| Constants        | Value | Explanation |
| ---------------- | ----- | ----------- |
| `SOCK_STREAM`    | `1`   |             |
| `SOCK_DGRAM`     | `2`   |             |
| `SOCK_SEQPACKET` | `5`   |             |
| `SOCK_RAW`       | `3`   |             |
| `SOCK_RDM`       | `4`   |             |

| Constants    | Value | Explanation |
| ------------ | ----- | ----------- |
| `AF_UNSPEC`  | `0`   |             |
| `AF_UNIX`    | `1`   |             |
| `AF_LOCAL`   | `1`   |             |
| `AF_INET`    | `2`   |             |
| `AF_IMPLINK` | `3`   |             |
| `AF_PUP`     | `4`   |             |
| `AF_CHAOS`   | `5`   |             |
| `AF_NS`      | `6`   |             |
| `AF_ISO`     | `7`   |             |
| `AF_OSI`     | `7`   |             |
| `AF_ECMA`    | `8`   |             |
| `AF_DATAKIT` | `9`   |             |
|              |       |             |



| Signature                                        | Explanation | Returns |
| ------------------------------------------------ | ----------- | ------- |
| `int socket(int domain, int type, int protocol)` |             |         |
