## java.security.MessageDigest

Algorithm:
- **SHA-256**
- **SHA-512**
- **SHA-1** (deprecated for security)
- **MD5** (broken — do NOT use)
- **SHA-3** (since Java 9)

`getInstance`: To get a `MessageDigest` object 
`digest`: To get hash of the byte string. 
`update`: To add a byte string to get the hash.