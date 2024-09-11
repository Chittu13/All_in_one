# Automatic Enumeration using metasploit & JAWS

- __`use post/windows/gather/win_privs` display the current privileges__
- __`use post/windows/gather/enum_logged_on_users` display the logged users__
- __`use post/windows/gather/enum_checkvm` to chech wether the target is a virtual machine__
- __'use post/windows/gather/enum_applications` display the all installed application__
- __`use post/windows/gather/enum_computers` display the othere system connected to that network__
- __`use post/windows/gather/enum_patches` it will show hotfix ids that installed and updated__
- __`use post/windows/gather/enum_shares` it will display the shares__


# Just Another windows(Enum Script)
- __Download the script from the github ---> [JAWS](https://github.com/411Hall/JAWS)__
  - It contains only powershell script call `jaws-enum.ps1`
  - > __Create a Temp directory in target system__
  - __Upload the file in Temp using meterpreter__
    - __`upload /root/jaws-enum.ps1`__
  - __After upload the file execute the script on target system__
    - __`powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt`__
    - __or__
    - __`.\jaws-enum.ps1 -OutputFileName Jaws-Enum.txt`__
    - __you can download the file and analys it `download Jaws-Enum.txt`__
