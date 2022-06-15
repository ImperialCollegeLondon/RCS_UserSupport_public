
[preliminary draft - WIP]

---

## Connect to HPC from Windows OSs

DISCLAIMER :  
neither the authors of these guides nor IC / ICT / RCS endorse in any way or with any preference :

- the installation or use of any 3rd party software from any Software house.  
- the use of one proposed method over the other.  

you could potentially use the following tools and guides to connect from Windows OSs to the HPC Services :  

- `WSL and WSL2`  
(windows subsystem for Linux version 2 latest alternatively still could use the legacy version 1 -- not advised this last one)
this will allow you to run a Linux terminal emulator on Windows OSs fully integrated with Windows OS.
you can connect to the linux-based HPC Service in a faster and better way than with the commonly used GUI-based IDEs.

**how to setup WSL2 :**  

[Web-guide_01](https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/)  (easy)  
[Web-guide_02](https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577) (Advanced)  

- `cmd.exe`  
the standard/MS DOS-like terminal available on Windows OSs; by default it should have nowadays the ssh program installed to be able to use the SSH protocol; you will need to install it if it is not available on your installation.
you can then use this tool to ssh to the HPC login node.

[Web-guide_01](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh)  (easy -- using ssh in cmd.exe when already installed)  
[Web-guide_02](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/)  (easy -- Enable and use win10 SSH when not available)  

- `powershell`
the standard windows world terminal to interface with your Windows OS.
this should provide SSH protocol out of the box otherwise SSH program/protocol support must need to be installed/enabled.

[Web-guide_02](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) (openssh install firstuse, if not available in powershell)  

- `mobaXterm`  
[mobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html) is yet another terminal emulator on windows  

- `PuTTY`  
(older tool not really advised for modern client OS systems)


---

for smaller / average-sized file transfers you can use any of the following tools :  

- [winSCP](https://winscp.net/eng/index.php)    
- [fileZilla](https://filezilla-project.org/)
- any other tool (GUIbased or not) that support SFTP


for big file transfers probably using GLobus is the best idea in this case.  



You can also mount remotely the RDS and your HPC `${HOME}` and `${EPHEMERAL}` folders and work on these over a remote connection, as if they were mounted on your local workstation, but please bear in mind that this will come with some caveats :

- changing network (especially wifi hotspots could interrupt connectivity and even "break" the mapped network connection)

- you may face some other issues (more or less difficult to troubleshoot) when the remote File system gets too busy to cope with the high load
(for instance experiencing slow-downs, sluggish file explorer windows, file transfers hanging or even file corruption when transferring data etc..)



### other Refs:

[run-linux-gui-apps-wsl-windows-10](https://pureinfotech.com/run-linux-gui-apps-wsl-windows-10/)  

---
[preliminary draft - WIP]



