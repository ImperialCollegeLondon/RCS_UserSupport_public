
## Connect to HPC Service using OpenVPN client on Linux/Nix OSs


**NOTE :**
If you suddenly start having issues after this tested method was previously working this could be due to:
1. your updated credentials  
2. VPN server configuration changes  
3. other issues.

To resolve, (1) Please remember to keep your credentials updated and (2) check the link [IC ICT VPN](https://www.imperial.ac.uk/admin-services/ict/self-service/connect-communicate/remote-access/virtual-private-network-vpn/).  


In case of updates to configurations or should ICT have changed parameters or decided to update the config file for any reason (improvements, security fixes etc.)
you will need to re-download it from this [configuration file](https://openvpn.ic.ac.uk/ic.ovpn).  

### Instructions :


- **download** the ovpn IC connection profile (only needed the first time, if program is not already installed)



- **install** the openvpn client  
(only needed the first time, if program is not already installed)    

-  For debian based Systems (e.g. Ubuntu and the likes)  

  `sudo apt-get install openvpn -y`  

- to **connect** to the VPN  :  
  you will need to execute the following command every time you want to use VPN.  
  (note the double dash `-` before config)  

  `sudo openvpn --config /path/to/file/ic.ovpn`  


> **NOTE :**  
please remember to leave the terminal with `openvpn` process open, as closing it will result in termination of your VPN network connection.   
> Leaving the terminal with the openvpn process open is also a good practice and a useful way to check your VPN logs, to spot connectivity issues etc.


- type in your IC username and password at the prompt by following the prompted instructions  

- when the process reaches the stage: _Initialization Squence Completed_ , you are good to connect to the HPC service.  

- from another terminal run the following to connect to the HPC Service

`ssh yourICusername@locing.hpc.ac.uk`  


- to terminate the connection in the openvpn terminal press:

`[CTRL]` + `[C]`



