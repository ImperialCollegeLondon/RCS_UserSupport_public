
[draft/WIP]

## JUPYTER HUB, LAB and NOTEBOOKS


### COMMONLY REPORTED USER ISSUES and COMPLAINTS

This is an experimental service and provided "as it is".

Due to its complex architecture and nature, users have reported multiple instances of errors and various issues that we have not been fully able to address.

These could be related to:  

- the underlying HPC hardware (known issues);   
(e.g. distributed FileSystem lock-ups and slowness or unavailability; unplanned outages; network bottlenecks etc..)

- the underlying HPC configuration (known issues):
(jobs and queues, service over-subscription, etc..)

- the Application itself - both
    - server-side (setup/config, it's proxying features and complex stack, the WebApp nature of the GUI-based tools etc..) and
    - client-side (cookies, browser compatibility, caching, not "exiting the portal" etc.)

- User dependent factors
(misconfiguration/"bloatedness" of user's environment and startup files, input/output files are too big, paths used or symlinks are not valid etc.)



---
### THINGS THAT MAY HELP

- run WebApps in browsers' incognito-mode windows ; this will make sure to:
  - "isolate" your log-in session for the time you need it
  - clear all cookies and cached Client data/settings once you're done and close the browser incognito window.

- always **use the correct log-out" procedures of the WebApp ;  
  - whenever possible search for the "LOGOUT" button or "EXIT" button of the WebApp ;  
  - sometimes if the button is not present or visible, browsing to the https://Name-of-The-Service-I-Am-using/logout page, could help logging you out - provided that page/endpoint has been setup correctly - otherwise you will see an error (most likely a 404 Error)  



---
### OTHER COMMON USER REPORTED ISSUES


1. Version Error :   
> ERROR: `this version can load notebook formats or earlier`    

  see ref: [github issue](https://github.com/ipython/ipython/issues/10174)   



2. Your Session was longer than the allowed/requested spawned job

  results in the job getting killed by the HPC scheduler.

  if by inspecting the last few lines of the file:  `$HOME/.jupyterhub.stderr`     
the output reads

  ```
=>> PBS: job killed: walltime 28828 exceeded limit 28800
```

  this means that the JHUB interface associated job was killed by the scheduler because it was longer than what we expect (i.e. for this case max 8 hour session, 28800s).

  In this case you need to start a new one; you may need to clear previous sessions/left-over files as per procedure below.


---

#### SELF TROUBLESHOOTING procedure:

things to test when things break in JHUB/JLAB (also suggested in the above link GH-thread) :  

1. please make sure to logout properly from the webApp by :

- stopping and terminating all current "jupyter notebooks or kernels" sessions/tabs

- clicking the Logout button  

- browsing to the link: https://jupyter.rcs.imperial.ac.uk/logout  


**NOTE** :   
PLEASE perform the following steps **only on Linux HPC CLI**,   
not from WINDOWS editors/CLI, otherwise strange characters will be added, breaking the script.

2. operate into your HPC `$HOME` folder to clean jupyter files:

- on the HPC terminal :
  - check your current running jobs on JupyterHub `qstat -s`   
  - kill the stale jupyterHub job: `qdel -f JOBID`  
  - wait a while for it to get acknowledged and cleared (the scheduler may take a while to clean it!)
  - when `qstat -s` does not show any longer the stale JupyterHub job proceed below


- on the HPC terminal run the command below - all in one line - this will :
  - make an executable file called `cleanJUPYTER.sh` in your `$HOME` folder,
  - open it with VIM editor, for pasting content into     

`touch ${HOME}/cleanJUPYTER.sh; chmod 0700 ${HOME}/cleanJUPYTER.sh ; vim ${HOME}/cleanJUPYTER.sh`

- at the black page of VIM editor, get into insert mode by typing the letter  `i`  
    (check the lower screen to see the insert mode active `-- INSERT --` )

    - copy from this online guide you are reading the code/snippet below : `[CTRL] + [C]`     

    - paste into Linux Vim terminal with `[SHIFT] + [CTRL] + [V]`  

  ```
  #!/usr/bin/bash

  TSTP=$(date +%Y%m%d-%H%M%S)
  DDIR=${HOME}/.local/share/jupyter
  cd $DDIR && mv nbsignatures.db nbsignatures.db._${TSTP}.bak
  rm -f ~/.ipython/profile_default/history_sqlite 2>/dev/null
  rm -f ~/.ipython/profile_default/security/nbsignatures.db 2>/dev/null
  echo DONE
  ```

  - then use the `ESC` key to exit VIM insert mode (lower screen is black now);  
  - save and exit the editor with `[SHIFT]` + `[z]` , `[z]`  
    (or alternatively type `:wq` + `[ENTER]` to exit Vim)  


- then run the script from Linux HPC CLI to clean-up jupyter files :

  `${HOME}/cleanJUPYTER.sh`



3. once that's done please try logging back into the jupyterHub website BUT this time   

- **PLEASE try using an "incognito browser" window.** to rule out other client/browser related issues.  

- sometimes saved cookies or locally cached settings in your browser prevent a smooth navigation.)

- sometimes changing/trying a different Web browser helps too - always incognito mode though, please)



#### WHEN/IF ALL THE ABOVE FAILS

- you can try with the "hard reset mode" suggested in Ref: [2]  :

`rm -rf ${HOME}/.local/share/jupyter && mkdir -pv ${HOME}/.local/share/jupyter`  


Evenutually, for what concerns furhter troubleshooting, once you tried everything above and you are still not able to run/access it :

please ask the admins to "clear your session" from the webPortal too by opening a ticket with us.

we may need to escalate further issues to whomever has installed the application for clarifications and or support and this may take a while.









Refs:  
[1] https://github.com/ipython/ipython/issues/10174  
[2] https://github.com/jupyter/notebook/issues/2923#issuecomment-335810979  

