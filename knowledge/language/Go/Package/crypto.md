---
parent: "[[Fleeting MOC]]"
tags:
  - 🪴weedy
date: 2025-12-04T09:03
---
# aes

## Constants

### BlockSize
```go
const BlockSize = 16
```
The AES block size in bytes.

## Functions

### NewCipher
```go
func NewCipher(key [][byte]) (Cipher.Block, error)
```

NewCipher creates and returns a new [[#Block]]. The key argument must be the AES key, either 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256.

### Error
```go
func (k KeySizeError) Error() string
```

Return string by error.

## Types

### KeySizeError
```go
type KeySizeError int
```

# cipher

## Functions

### NewGCM
```go
func NewGCM(cipher Block) (AEAD, error)
```
`NewGCM` returns the given 128-bit, block cipher wrapped in Galois Counter Mode with the standard nonce length.
Example:
```go
key, _ := hex.DecodeString("6368616e676520746869732070617373776f726420746f206120736563726574")
ciphertext, _ := hex.DecodeString("c3aaa29f002ca75870806e44086700f62ce4d43e902b3888e23ceff797a7a471")
nonce, _ := hex.DecodeString("64a9433eae7ccceee2fc0eda")
block, err := aes.NewCipher(key)
aesgcm, err := cipher.NewGCM(block)
plaintext, err := aesgcm.Open(nil, nonce, ciphertext, nil)
```

### NewGCMWithNonceSize
```go
func NewGCMWithNonceSize(cipher Block, size int) (AEAD, error)
```
`NewGCMWithNonceSize` returns the given 128-bit, block cipher wrapped in Galois Counter Mode, which accepts nonces of the given length. The length must not be zero.

### NewGCMWithRandomNonce
```go
func NewGCMWithRandomNonce(cipher Block) (AEAD, error)
```

`NewGCMWithRandomNonce` returns the given cipher wrapped in Galois Counter Mode, with randomly-generated nonces. The cipher must have been created by [crypto/aes.NewCipher](https://pkg.go.dev/crypto/aes#NewCipher). It generates a random 96-bit nonce, which is prepended to the ciphertext by Seal, and is extracted from the ciphertext by Open. The NonceSize of the AEAD is zero, while the Overhead is 28 bytes (the combination of nonce size and tag size).

### NewGCMWithTagSize
```go
func NewGCMWithTagSize(cipher Block, tagSize int) (AEAD, error)
```

`NewGCMWithTagSize` returns the given 128-bit, block cipher wrapped in Galois Counter Mode, which generates `tags` with the given length (between 12-16 bytes).

### NewCBCDecrypter
```go
func NewCBCDecrypter(b Block, iv []byte) BlockMode
```
`NewCBCDecrypter` returns a `BlockMode` which decrypts in cipher block chaining mode, using the given `Block`. The length of `iv` must be the same as the Block's block size and must match the `iv` used to encrypt the data.
Example:
```go
key, _ := hex.DecodeString("6368616e676520746869732070617373")
ciphertext, _ := hex.DecodeString("73c86d43a9d700a253a96c85b0f6b03ac9792e0e757f869cca306bd3cba1c62b")
block, err := aes.NewCipher(key)
iv := ciphertext[:aes.BlockSize]
ciphertext = ciphertext[aes.BlockSize:]
mode := cipher.NewCBCDecrypter(block, iv)
mode.CryptBlocks(ciphertext, ciphertext)
```

### NewCBCEncrypter
```go
func NewCBCEncrypter(b Block, iv []byte) BlockMode
```
`NewCBCEncrypter` returns a `BlockMode` which encrypts in cipher block chaining mode, using the given `Block`. The length of `iv` must be the same as the Block's block size.

### NewCFBDecrypter (deprecated)
```go
func NewCFBDecrypter(block Block, iv []byte) Stream
```
`NewCFBDecrypter` returns a [[#Stream]] which decrypts with cipher feedback mode, using the given [[#Block]]. The iv must be the same length as the [[#Block]]'s block size.
```go
key, _ := hex.DecodeString("6368616e676520746869732070617373")
ciphertext, _ := hex.DecodeString("7dd015f06bec7f1b8f6559dad89f4131da62261786845100056b353194ad")
block, err := aes.NewCipher(key)
iv := ciphertext[:aes.BlockSize]
ciphertext = ciphertext[aes.BlockSize:]
stream := cipher.NewCFBDecrypter(block, iv)
stream.XORKeyStream(ciphertext, ciphertext)
```

### NewCFBEncrypter (deprecated)
```go
func NewCFBEncrypter(block Block, iv []byte) Stream
```
NewCFBEncrypter returns a [[#Stream]] which encrypts with cipher feedback mode, using the given [[#Block]]. The iv must be the same length as the [[#Block]]'s block size.

### NewCTR
```go
func NewCTR(block Block, iv []byte) Stream
```

NewCTR returns a [[#Stream]] which encrypts/decrypts using the given [[#Block]] in counter mode. The length of iv must be the same as the [[#Block]]'s block size.

### NewOFB
```go
func NewOFB(b Block, iv []byte) Stream
```
NewOFB returns a [[#Stream]] that encrypts or decrypts using the block cipher `b` in output feedback mode. The initialization vector iv's length must be equal to `b`'s block size.

### (StreamReader) Read
```go
func (r StreamReader) Read(dst []byte) (n int, err error)
```

### (StreamWriter) Close
```go
func (w StreamWriter) Close() error
```
`Close` closes the underlying `Writer` and returns its `Close` return value, if the `Writer` is also an `io.Closer`. Otherwise it returns `nil`.

### (StreamWriter) Write
```go
func (w StreamWriter) Write(src []byte) (n int, err error)
```

## Types

### AEAD
```go
type AEAD interface {
	NonceSize() int
	
	Overhead() int
	
	Seal(dst, nonce, plaintext, additionalData []byte) []byte
	
	Open(dst, nonce, ciphertext, additionalData []byte) ([]byte, error)
}
```
AEAD is a cipher mode providing authenticated encryption with associated data. For a description of the methodology, see [Authenticated_encryption](https://en.wikipedia.org/wiki/Authenticated_encryption).
- `NonceSize()` returns the size of the nonce that must be passed to `Seal` and `Open`.
- `Overhead()` returns the maximum difference between the lengths of a plaintext and its ciphertext.
- `Seal` encrypts and authenticates `plaintext`, authenticates the `additionalData` and appends the result to `dst`, returning the updated slice. The `nonce` must be `NonceSize()` bytes long and unique for all time, for a given key.
- `Open` decrypts and authenticates `ciphertext`, authenticates the additional data and, if successful, appends the resulting `plaintext` to `dst` , returning the updated slice. The nonce must be `NonceSize()` bytes long and both it and the `additionalData` must match the value passed to Seal.

### Block
```go
type Block interface {
	BlockSize() int
	
	Encrypt(dst, src []byte)
	
	Decrypt(dst, src []byte)
}
```
- `BlockSize` returns the cipher's block size.
- `Encrypt` encrypts the first block in `src` into `dst`. `dst` and `src` must overlap entirely or not at all. 
- `Decrypt` decrypts the first block in `src` into `dst`. `dst` and `src` must overlap entirely or not at all.
A `Block` represents an implementation of block cipher using a given key. It provides the capability to encrypt or decrypt individual blocks. The mode implementations extend that capability to streams of blocks.

### BlockMode
```go
type BlockMode interface {
	BlockSize() int
	
	CryptBlocks(dst, src, []byte)
}
```
A `BlockMode` represents a block cipher running in a block-based mode (`CBC`, `ECB` etc).
- `BlockSize` returns the mode's block size.
- `CryptBlocks` encrypts or decrypts a number of blocks.
- `src`: The plaintext we want to encrypt, length must be a multiple of `BlockSize`.
- `dst`: Where we store the ciphertext.

### Stream
```go
type Stream interface {
	XORKeyStream(dst, src []byte)
}
```
A Stream represents a stream cipher.
- `XORKeyStream` XORs each byte in the given slice with a byte from the cipher's key stream.
- `src`: The plaintext we want to encrypt.
- `dst`: Where we store the ciphertext.

### StreamReader
```go
type StreamReader struct {
	S Stream
	R io.Reader
}
```
`StreamReader` wraps a `Stream` into an `io.Reader`. It calls `XORKeyStream` to process each slice of data which passes through.

### StreamWriter
```go
type StreamWriter struct {
	S Stream
	W io.Writer
	Err error // unused
}
```

`StreamWriter` wraps a `Stream` into an `io.Writer`. It calls `XORKeyStream` to process each slice of data which passes through.

# rand

## Variables

### Reader
```go
var Reader io.Reader
```
Reader is a global, shared instance of a cryptographically secure random number generator. It is safe for concurrent use.

## Functions

### Int
```go
func Int(rand io.Reader, max *big.Int) (n *big.Int, err error)
```
`Int` returns a uniform random value in `[0, max)`. It panics if $max \leq 0$ , and returns an error if `rand.Read` returns one.
```go
a, _ := rand.Int(rand.Reader, big.NewInt(100))
fmt.Println(a.Int64())
```

### Prime
```go
func Prime(rand io.Reader, bits int) (*big.Int, error)
```
Prime returns a number of the given bit length that is prime with high probability. Prime will return error for any error returned by `rand.Read` or if bits < 2.

Example:
```go
a, _ := rand.Prime(rand.Reader, 64)
fmt.Println(a.Int64())
```

### Read
```go
func Read(b []byte) (n int, err error)
```
Read fills b with cryptographically secure random bytes. It never returns an error, and always fills b entirely.
```go
key := make([]byte, 32)
rand.Read(key)
```

### Text
```go
func Text() string
```
Text returns a cryptographically random string using the standard [RFC 4648](https://rfc-editor.org/rfc/rfc4648.html) base32 alphabet for use when a secret string, token, password, or other text is needed. The result contains at least 128 bits of randomness (26 chars), enough to prevent brute force guessing attacks and to make the likelihood of collisions vanishingly small. A future version may return longer texts as needed to maintain those properties.

# sha256

## Constants

### BlockSize
```go
const BlockSize = 64
```
The blocksize of `SHA256` and `SHA224` in bytes.

### Size
```go
const Size = 32
```
The size of a `SHA256` checksum in bytes.

### Size224
```go
const Size224 = 28
```
The size of a `SHA224` checksum in bytes.

## Functions

### New
```go
func New() hash.Hash
```
`New` returns a new [hash.Hash](https://pkg.go.dev/hash#Hash) computing the SHA256 checksum.
Example:
```go
h := sha256.New()
h.Write([]byte("hello world\n"))
fmt.Printf("%x", h.Sum(nil))
```

### New224
```go
func New224() hash.Hash
```
New224 returns a new [hash.Hash](https://pkg.go.dev/hash#Hash) computing the SHA224 checksum.

### Sum224
```go
func Sum224(data []byte) [Size224]byte
```
Sum224 returns the SHA224 checksum of the data.

### Sum256
```go
func Sum256(data []byte) [Size]byte
```
Sum256 returns the SHA256 checksum of the data.

```go
sum := sha256.Sum256([]byte("hello world\n"))
fmt.Printf("%x", sum)
```


