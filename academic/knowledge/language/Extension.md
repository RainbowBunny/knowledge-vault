## Debian binary package

A Debian binary package is a file with a `.deb` extension that contains pre-compiled, ready-to-run software for a Debian system. It is a self-contained archive that holds all the necessary files to install an application, including executables, libraries, configuration files, and documentation. These packages simplify software management by automating installation, upgrading, and removal, allowing users to bypass the need for manual compilation.

Extraction:

```bash
dpkg-deb -x package.deb extracted/
```

## PEM

In cryptography, **PEM** stands for Privacy-Enhanced Mail, and it's a common text-based file format for storing and sending cryptographic keys, certificates, and other data. A PEM file contains data encoded in Base64 ASCII and is enclosed by plain-text headers like `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`. This format is widely used for exchanging keys and certificates for public key infrastructure (PKI) and is often used with SSL/TLS, as seen in files with extensions like .pem, .cer, .crt, or .key.

Import/Export:
[[pycryptodome#crypto.PublicKey]]

## NTDS.dit

This is the **Active Directory database**, stored using the **ESE (Extensible Storage Engine)** format. It contains:
- Domain user accounts
- Password hashes (NT hashes)
- Kerberos keys
- Groups, OUs, policies
- Domain trust info
- AD schema/configuration
- Replication metadata

With the assistance of `SYSTEM` hive provides the BOOTKEY, we can decrypt `NTDS.dit` file with [[Impacket]]: 

```
python secretsdump.py -ntds ntds.dit -system SYSTEM LOCAL
```

Account format:
```
username:RID:LM_hash:NTLM_hash::: 
```

Where:
- `username`: Account name
- `RID`: Relative user ID
- `LM_hash`:
- `NTLM_hash`: 

Kerberos keys:
- `username`: Account name
- `enctype`: Encryption type
- `key`: Password hash
