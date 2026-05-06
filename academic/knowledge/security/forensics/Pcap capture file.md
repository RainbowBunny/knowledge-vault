---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-27T14:17
---
[Tutorial](https://malware-traffic-analysis.net/)
## Changing Your Column Display

- Changing Date and Time to UTC: `View -> Time Display Format -> UTC Date and Time of Day (1970-01-01 01:02:03.123456)/Seconds`
- Remove `No., Protocol, Length` columns
- Add column: `Right click any column headers -> Column Preferences` and change the columns to:
	- Time - Time (format as specified)
	- Src - Src addr (unresolved)
	- Src port - Src port (unresolved)
	- Dst - Dest addr (unresolved)
	- Dst port - Dest port (unresolved)
	- Host - http.host
	- Info - Information

## Display Filter Expressions

## Common Practice


| Process             | Action                             |
| ------------------- | ---------------------------------- |
| Follow TCP Streams  |                                    |
| Check Conversations | `Statistics → Conversations → TCP` |
| Export Objects      | `File → Export Objects`            |


| Port  |                                                  |
| ----- | ------------------------------------------------ |
| 1883  | Standard reserved port for **MQTT over raw TCP** |
| 8883  | Standard reserved port for **MQTT over TLS**.    |
| 49667 | Windows ephemeral RPC port                       |
## Transport Layer Security (TLS)


| Field                                | Name                                            | Explanation                                                                                                          |
| ------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `tls.record`                         | TLS Record Layer                                |                                                                                                                      |
| `tls.record.content_type`            | Content Type                                    | `20`: `ChangeCipherSpec`<br>`21`: `Alert`<br>`22`: `Handshake`<br>`23`: `Application Data`                           |
| `tls.record.version`                 | Record Layer Version                            | For backward compatibility, not real version for interacting                                                         |
| `tls.record.length`                  | Length of TLS Record data                       | Number of bytes following this record header, helps TLS know where the record ends.                                  |
| `tls.handshake`                      | Handshake protocol message                      |                                                                                                                      |
| `tls.handshake.type`                 | Type of handshake message                       | `1`: `ClientHello`<br>`2`: `ServerHello`<br>`11`: `Certificate`<br>`16`: `ClientKeyExchange`<br>`20`: `Finished`     |
| `tls.handshake.length`               | Length of handshake message                     |                                                                                                                      |
| `tls.handshake.epms_len`             | Length of encrypted PreMaster secret            |                                                                                                                      |
| `tls.handshake.epms`                 | Encrypted PreMaster secret                      | `PreMasterSecret = client_version + 46 byte random` <br>`EncryptedPMS = encrypt(server_public_key, PreMasterSecret)` |
| `tls.handshake.version`              | Maximum version supported by client             | `03 03`: `TLS 1.2`                                                                                                   |
| `tls.handshake.random`               | Random values used for deriving keys            | `tls.handshake.random_time + tls.handshake.random_byte`                                                              |
| `tls.handshake.random_time`          | Unix time field of random structure             | Used historically to prevent replay attacks                                                                          |
| `tls.handshake.random_bytes`         | Random values used for deriving keys            | Cryptographically random that will combine with server random and pre-master secret to derive session keys           |
| `tls.handshake.session_id_length`    | Length of Session ID field                      | Client is **not resuming** a previous TLS session<br>If non-zero → session resumption attempt                        |
| `tls.handshake.cipher_suites_length` | Length of cipher suites field                   | Each cipher suite is **2 bytes**.                                                                                    |
| `tls.handshake.ciphersuite`          | Cipher Suite                                    |                                                                                                                      |
| `tls.handshake.comp_methods_length`  | List of compression methods supported by client |                                                                                                                      |
| `tls.handshake.comp_method`          | Compression method                              | Compression was removed due to **CRIME attack**                                                                      |
| `tls.handshake.extensions_length`    | Extensions                                      | TLS extensions add flexibility without breaking older versions.                                                      |
|                                      |                                                 |                                                                                                                      |




`Edit > Preferences > Protocol > TLS > Edit RSA keys list`
And add `private.key` file that derived from `.pem` file we find in certificate field (export packet byte of certificate package).

## X.509 Certificate

## HTTP

> [!remark] List HTTP objects and enpoints
> ```
> tshark -r chall.pcap -Y http \
  -T fields -e frame.number -e ip.src -e ip.dst \
  -e http.request.method -e http.host -e http.request.uri -e http.response.code
> ```

> [!remark]
> ```
> tshark -r chall.pcap --export-objects http,/tmp/pcap_http
> ```

## MQTT

Simple MQTT flow:
`CONNECT  →  CONNACK  →  PUBLISH  →  DISCONNECT`

| Field                    | Name               | Explanation                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `mqtt.hdrflags`          | Header Flags       | `msgtype + dupflag + qos + retain = 1 byte`                                                                                                                                                                                                                                    |
| `mqtt.msgtype`           | Message type       | 4 bit<br>`10`: `Connect`<br>`20`: `ConnAck`<br>`30`: `Publish`<br>`E0`: `Disconnect`                                                                                                                                                                                           |
| `mqtt.conflags`          | Connect Flags      | 1 byte: `uname + passwd + retain + qos + willflag + cleansess + 1 bit reserved`                                                                                                                                                                                                |
| `mqtt.conflag.uname`     | User Name Flag     | 1 bit: If there will be a username field                                                                                                                                                                                                                                       |
| `mqtt.conflag.passwd`    | Password Flag      | 1 bit: If authentication is needed                                                                                                                                                                                                                                             |
| `mqtt.conflag.retain`    | Will retain        | 1 bit set retail flag                                                                                                                                                                                                                                                          |
| `mqtt.conflag.qos`       | QoS Level          | 2 bit set QoS level                                                                                                                                                                                                                                                            |
| `mqtt.conflag.willflag`  | Will Flag          | 1 bit A **Last Will and Testament** message published by the broker **if the client disconnects unexpectedly**.                                                                                                                                                                |
| `mqtt.conflag.cleansess` | Clean Session Flag | 1 bit:<br>If on, Broker **forgets everything** on disconnect, no queued message and no subscriptions saved<br>If off, Broker remembers subscriptions and QoS 1/2 pending messages, need client ID and QoS                                                                      |
| `mqtt.kalive`            | Keep Alive         | 2 bytes: Times in seconds that client promises to communicate at least once.                                                                                                                                                                                                   |
| `mqtt.clientid_len`      | Client ID Length   |                                                                                                                                                                                                                                                                                |
| `mqtt.clientid`          | Client ID          | If clean session then: broker auto-assigns a client ID                                                                                                                                                                                                                         |
| `mqtt.len`               | Message Length     | 1 byte                                                                                                                                                                                                                                                                         |
| `mqtt.conack.flags`      | Acknowledge Flags  | 1 byte: `7 bit reserved + sp`                                                                                                                                                                                                                                                  |
| `mqtt.conack.flags.sp`   | Session Present    | 1 bit: On if there exists session present                                                                                                                                                                                                                                      |
| `mqtt.conack.val`        | Return Code        | 1 byte:<br>`00`: Connection Accepted<br>`01`: Unacceptable protocol version<br>`02`: Identifier rejected<br>`04`: Bad username/password                                                                                                                                        |
| `mqtt.dupflag`           | DUP Flag           | 1 bit: On if this `Publish` message **may be a retransmission** of an earlier message.                                                                                                                                                                                         |
| `mqtt.qos`               | QoS Level          | 2 bit QoS defines **delivery guarantees**:<br>`00`: At most once (fire-and-forget) - fastest but message may be lost<br>`01`: At least once - broker must ACK, retires allowed but duplicates possible<br>`10`: Exactly once - 4 step handshake with no loss and no duplicates |
| `mqtt.retain`            | Retain Flag        | 1 bit: On if broker **stores the last message** on a topic                                                                                                                                                                                                                     |
| `mqtt.topic_len`         | Topic Length       | 2 bytes                                                                                                                                                                                                                                                                        |
| `mqtt.topic`             | Topic              |                                                                                                                                                                                                                                                                                |
| `mqtt.msg`               | Message            |                                                                                                                                                                                                                                                                                |
|                          |                    |                                                                                                                                                                                                                                                                                |


## qBittorrent Web API (v2)

| Signature                 | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI Structure             | `/api/v2/sync/maindata`<br>`/api/v2/torrents/info`<br>`/api/v2/torrents/trackers`<br>`/api/v2/auth/login`<br>`/api/v2/app/preferences`<br>`/api/v2/transfer/info`                                                                                                                                                                                                                        |
| RID-based long polling    | `GET /api/v2/sync/maindata?rid=368`<br>`GET /api/v2/sync/maindata?rid=370`<br>`GET /api/v2/sync/maindata?rid=372`<br>Response `{"rid":373,"server_state":{...}}`                                                                                                                                                                                                                         |
| JSON field fingerprinting | Server-level<br>`"server_state": {`<br>  `"alltime_ul",`<br>  `"alltime_dl",`<br>  `"global_ratio",`<br>  `"up_info_speed",`<br>  `"dht_nodes"`<br>`}`<br>Torrent-level keys<br>`"torrents": {`<br>  `"<40-hex hash>": {`<br>    `"seeding_time",`<br>    `"time_active",`<br>    `"reannounce",`<br>    `"uploaded_session",`<br>    `"upspeed",`<br>    `"popularity"`<br>  `}`<br>`}` |
> [!remark]
> Extract `bittorent` packages:
> ```
> tshark -x -2 -R "bittorrent" -r evidence.pcapng -T json
> ```
> Then, merge all `bittorrent.piece.data_raw` fields.

## 802.11 (Wifi)

> [!remark]
> [cap2hashcat](https://hashcat.net/cap2hashcat/)
> To recover password hash from 802.11