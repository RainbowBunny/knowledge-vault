---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-15T15:54
---
`PyQT6` is a python library to create desktop application with python.
[https://doc.qt.io/qtforpython-6/api.html](https://doc.qt.io/qtforpython-6/api.html)

# QtWidgets

## ItemFlag

| Constant                  | Descriptions                                           |
| ------------------------- | ------------------------------------------------------ |
| `Qt.NoItemFlags`          |                                                        |
| `Qt.ItemIsSelectable`     |                                                        |
| `Qt.ItemIsEditable`       |                                                        |
| `Qt.ItemIsDragEnabled`    |                                                        |
| `Qt.ItemIsDropEnabled`    |                                                        |
| `Qt.ItemIsUserCheckable`  |                                                        |
| `Qt.ItemIsEnabled`        |                                                        |
| `Qt.ItemIsAutoTristate`   | The item’s state depends on the state of its children. |
| `Qt.ItemNeverHasChildren` |                                                        |
| `Qt.ItemIsUserTristate`   |                                                        |


## QModelIndex
## QListWidgetItem

| Method     | Parameter | Returns | Note |
| ---------- | --------- | ------- | ---- |
| `setFlags` |           |         |      |

## QListWidget

| Method               | Parameter                                                             | Returns              | Note                                |
| -------------------- | --------------------------------------------------------------------- | -------------------- | ----------------------------------- |
| `addItem`            | `item` – [[#QListWidgetItem]]                                         |                      |                                     |
| `addItem`            | `label` – `str`                                                       |                      |                                     |
| `addItems`           | `labels` – `list[str]`                                                |                      |                                     |
| `clear`              |                                                                       |                      | Delete all items                    |
| `currentItem`        |                                                                       | [[#QListWidgetItem]] |                                     |
| `currentItemChanged` | `current` – [[#QListWidgetItem]]<br>`previous` – [[#QListWidgetItem]] |                      | Signal emitted whenever item change |
| `currentRow`         |                                                                       | `int`                |                                     |
| `item`               | `row` – `int`                                                         | [[#QListWidgetItem]] | Get item by row                     |
| `itemFromIndex`      | `index` – [[#QModelIndex]]                                            |                      |                                     |
| `takeItem`           | `row` – `int`                                                         | [[#QListWidgetItem]] | Removes and returns item in row     |
|                      |                                                                       |                      |                                     |

# QtMultimedia

## QAudioFormat

### SampleFormat

**Constant**: `Unknown`, `Uint8`, `Uint16`, `Uint32`, `Float`

### AudioChannelPosition

You need it **only if channel order or physical meaning matters**.

### ChannelConfig

|     |     |
| --- | --- |
|     |     |

## QAudioDevice


| Method | Parameter | Returns | Note |
| ------ | --------- | ------- | ---- |
|        |           |         |      |


## QAudioOutput

| Property | Types             |
| -------- | ----------------- |
| `device` | [[#QAudioDevice]] |
| `muted`  | `bool`            |
| `volume` | `float`           |
⇾ Slots + Signals

## QMediaPlayer

| Method           | Parameter                    | Returns | Note |
| ---------------- | ---------------------------- | ------- | ---- |
| `setAudioOutput` | `output` – [[#QAudioOutput]] |         |      |

