# Upgrading Non-Interactive Shells

- __1. `cat /etc/shells` Check which shells are available in the target system__
- __2. Check for `python --version` to know python is installed or not__
  - __`python -c 'import pty; pty.spawn("/bin/bash")'`__
- __3. Check for `perl --help` installed or not__
  - __perl -e 'exec "bin/bash";'__
  - __perl: exec "/bin/bash";__
- __4. ruby: exec "bin/bash"__

- __Important__
  - __`env`__
  - __`export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`__
  - __`export TERM=xterm`__
  - __`export SHELL=bash`__
