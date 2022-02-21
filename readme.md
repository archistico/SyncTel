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
## Changelog
- 20220221 fixed error space
```
ATTENZIONE CON GLI SPAZI
QUESTI FUNZIONANO, IN UNO CI VUOLE LO SLASH NELL'ALTRO NO  
- adb shell ls "sdcard/WhatsApp/Media/WhatsApp\ Video/"
- adb pull "sdcard/WhatsApp/Media/WhatsApp Video/VID-20190304-WA0002.mp4" "./export/a.mp4"
```

## Todo
- parameter on yaml

## Flowchart

![flowchart](https://raw.githubusercontent.com/archistico/SyncTel/main/screenshot/diagramma.jpg)

