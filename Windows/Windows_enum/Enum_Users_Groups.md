# Enumerating Users & Groups

### In meterpreter
  - __`getuid` to get the current user__
  - __`getprivs` current privilege we have__
  - __`use post/windows/gather/enum_logged_on_users`__

### In windows
  - __`whoami` to get the current user__
  - __`whoami /priv` to get the current privilege__
  - __`query user` to get the currently logged in users__
  - __`net users` will display the all other accounts available__
  - __`net user administrator` display more details about the user__
  - __`net localgroup` to list out the all groups__
  - __`net localgroup administrators` to display the members of particular group__
