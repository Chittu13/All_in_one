# Alternate Data Streams

- `type payload.exe > nothing.txt:windows.exe`
  - __`payload.exe` is a backdoor__
  - __storing the `payload.exe` code in `nothing.txt:windows.exe`__
- making simbalic link
  - `mklink wupdate.exe c:\Temp\nothing.txt:windows.exe`
- type `wupdate` it will start running
