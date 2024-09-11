# Enumerating Users & Groups

- __`whoami` Display the name of current user__
- __`groups <user>` to chech the user to which group user is belongs to__
- __`cat /etc/passwd` display other users on the linux system __
  - > __It will display both service account and user account__
    - __For user account it will be /bin/bash or /bin/sh for the born shell__
    - __For service account it will be /usr/sbin/nologin__
  - __`cat /etc/passwd | grep -v /nologin` display only user account__
```
root:x:0:0:root:/root:/bin/bash
 |     | |
 |     | |
 |     | | 
 |     | group id
 |   user id
user name
```
- __`useradd -m bob -s /bin/bash` creating a user__
- __`groups` display the groups__
- __`groups bob` checking the user to which group belongs to__
- __`usermod -aG root bob` Add the bob user to the root group__
- __`last` it will display only last user logged__
- __`lastlog` it will display the history of logged user__
