In meterpreter 

  - __`run autoroute -s <targetip>.0/20`__

__now we are scanning for the ports__
  - __`search portscan`__
```
use auxiliary/scanner/portscan/tcp
set ports 1-100
exploit
```

portforwarding to find the what service is running on that port 
  - __`portfwd add -l 1234 -p 80 -r <target2>`__
  - > __And scan the port in your localhost__
  - __`db_nmap -sV -sS -p 1234 localhost`__
