
[draft/WIP]

### JUPYTER HUB, LAB and NOTEBOOKS



#### COMMON USER REPORTED ISSUES


ERROR: `thise version can load notebook formats or earlier`    

see ref:
https://github.com/ipython/ipython/issues/10174   






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

    - copy from this online guide you are reading the code/snipped below : `[CTRL] + [C]`     

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

