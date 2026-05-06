
[https://github.com/vsajip/python-gnupg/blob/master/gnupg.py](https://github.com/vsajip/python-gnupg/blob/master/gnupg.py)
## `GPG`

Signature: `class gnupg.GPG(gpgbinary='gpg', gnupghome=None, verbose=False, use_agent=False, keyring=None, options=None, secret_keyring=None, env=None)`
Parameters:
- `gpgbinary` – The path to the `gpg` executable
- `verbose` (default: `False`) – Print information (e.g. the gpg command lines, and status messages returned by gpg) to the console.
- `use_agent` (default: `False`) – If specified as True, the `--use-agent` parameter is passed to `gpg`, asking it to use any in-memory GPG agent (which remembers your credentials).
- `keyring` (default: `None`) – If specified, the value is used as the name of the keyring file. The default keyring is not used. A list of paths to keyring files can also be specified.
- `options` (default: `None`) – If specified, the value should be a list of additional command-line options to pass to `gpg`.
- `secret_keyring` (default: `None`) – If specified, the value is used as the name of the secret keyring file. A list of paths to secret keyring files can also be specified. _Note that these files are not used by GnuPG >= 2.1._
- `env` (default: `None`) – If specified, the value is used as the environment variables used when calling the GPG executable.

### `encrypt_file`

Signature: `def encrypt_file(fileobj_or_path, recipients, sign=None, always_trust=False, passphrase=None, armor=True, output=None, symmetric=False, extra_args=None)`
Parameters:
- `fileobj_or_path` (`str`|`file`) – A path to a file or a file-like object containing the data to be encrypted.
- `recipients` (`str` | `list`) – A key id of a recipient of the encrypted data, or a list of such key ids.
- `sign` (`str`) – If specified, the key id of a signer to sign the encrypted data.
- `always_trust` (`bool`) – Whether to always trust keys.
- `passphrase` (`str`) – The passphrase to use for a signature.
- `armor` (`bool`) – Whether to ASCII-armor the output.
- `output` (`str`) – A path to write the encrypted output to.
- `symmetric` (`bool`) – Whether to use symmetric encryption.
- `extra_args` (`list[str]`) – A list of additional arguments to pass to `gpg`.

### `encrypt`

Signature: `def encrypt(data, recipients, **kwargs)`
Parameters:
- `data` (`str`|`bytes`): The data to encrypt.
- `recipients` (`str|list[str]`): A key id of a recipient of the encrypted data, or a list of such key ids.
- `kwargs` (`dict`): Keywords arguments, which are passed to `encrypt_file()`.
