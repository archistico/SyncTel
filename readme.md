# SyncTel

Synchronize and merge your photos on Android smartphone to pc folder with ADB

## Info

- download ADB and unzip in favorite folder [Link google last release ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
- Set develop mode on your smartphone
- Set on "usb debug" on advanced features
- Copy syntel.py on folder adb
- ./adb.exe devices
- if see your device is ok
- Set on python file:
  - CARTELLA_TELEFONO
  - CARTELLA_EXPORT
  - Files extension do you want

```
python syntel.py
```

## Todo
- choise if erase after copy image on smarphone  
  ```adb shell rm sdcard/download/file.ext```
- parameter on cli
- fix: filename with space

## Flowchart

![flowchart](https://raw.githubusercontent.com/archistico/SyncTel/main/screenshot/diagramma.jpg)

