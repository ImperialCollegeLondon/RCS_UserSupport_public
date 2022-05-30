
## HPC Services networking and connectivity


There is a possibility that "routes to the HPC Services" may be different for your system or setup; issues vary and may depend also on :

- the location where you are connecting from.  
  - **VPN** VS **on campus**;  
  - WFH ("working from home")
  - laboratory, department etc..


- the _ethernet access port_ or the _WiFI Access point_ that you are using to connect, and their underlying networking infrastructure of the building. etc..

Nonetheless, HPC services are transparent to users at present so it should not matter where you land on or where you are connecting from, as long as you are using the IC VPN connection.

Please just follow the steps below to check HPC connectivity/access and perform some first checks and troubleshooting :

**[ 1 ] - connection :**
  - if you are working remotely, (out of campus, WFH...) switch on and use **IC VPN connection** then go to step [ 2 ]
  - if you are using a network on campus go to step [ 2 ]

**[ 2 ] - check HPC Service status :**
  - if you can connect to the [HPC Service status page](https://selfservice.rcs.imperial.ac.uk/service-status)
  and successfully browse its content (you can see the page "white-blue menus", top notes, list of Services status etc..)  
  then HPC services can be reached too, and you should be able to successfully connect to it.

  PLEASE NOTE : for the following case the issue has nothing to do with HPC Services.
  - if you cannot see the page above (the page does not load -- you do not see the "white-blue menus",  or you receive an error) it means that you have networking/routing issues :
    - (if connecting over VPN) : fix your network/VPN connection first (check your local network, VPN client connection etc. get in touch with ICT Service Desk)
    - (if connecting over campus network) : please open a ticket with the service Desk and mention these issues) --
      alternatively you can try another "ethernet port" or "WiFi access point", possibly after rebooting your computer (this is particularly valid if you are using Windows-based OSs. - as connections, credentials, routes may be cached and you won't have low-level system access to modify/update them manually, but only via rebooting.)

[ 3 ] - connect to HPC following the [using SSH guide](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/getting-started/using-ssh/)

basically run from a terminal one of the following commands :

```
  ssh user@login.hpc.ic.ac.uk              ## if you need a normal common SSH session (most of the time what you need)
  ssh -X user@login.hpc.ic.ac.uk           ## if you need a X-forwarded session (works most of the time -- less secure)
  ssh -Y user@login.hpc.ic.ac.uk           ## if you need a X-forwarded secure session (more secure but sometimes you may have connection problems)
```

Furthermore,
if you are on a slow connection and requesting `-X` or `-Y`, you can also try adding the `-C` flag to the ssh command, to set a compressed stream of data when connecting

e.g.
```
ssh -XC user@login.hpc.ic.ac.uk
ssh -YC user@login.hpc.ic.ac.uk
```

please note that depending on your Operating system, the version and implementation of the SSH program in it, you many need to use different flags than those mentioned above; look at the man pages from a terminal to learn more.

`man ssh`

