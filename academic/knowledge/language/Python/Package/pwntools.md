# Class

## ELF

### got



### plt


Function: `read(address, count)`

Explanation: Read `count` bytes label by `address`.


| Function | Argument                                                                                                                                                 | Returns                                                   | Explanation |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------- |
| `read`   | `address: int`<br>Virtual address to read<br>`count: int`<br>Number of bytes to read                                                                     | `A`: `byte`                                               |             |
| `search` | `needle: bytes`<br>String to search for.<br>`writable: bool`<br>Search only writable sections.<br>`executable: bool`<br>Search only executable sections. | `out`: An iterator for each virtual address that matches. |             |


