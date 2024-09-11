# Enumerating Processes & Services


### In meterpreter 
  - __`ps` it will display the list of running process__
    - __`pgrep explorer.exe`__
    - __`migrate <PID>`__


### In windows
  - __`net start` diplay the services started__
  - __`wmic service list brief` display the running services__ 
  - __`tasklist /SVC` displays list of process running and services that runs under process__
  - __`schtasks /query /fo LIST` Display the list of schedule tasks__
    
