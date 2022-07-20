### Common Errors


`CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`  

to resolve this Error received when running `conda activate My_Venv` , you can check out the 3 options below;

(I suggest using them in the "practical order" 3,2,1 not the logical one below.)

---

1. Follow the instructions given at screen (it may not work sometimes)  

```
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```


2.  manually patch your anaconda installation with this file:

- download from this repo the file : [conda.sh](/RCS_Apps_guides/Anaconda/assets/files/conda.sh)  

- save it in `~/anaconda3/etc/profile.d/`

- add to your `.bashrc` (or `.bash_profile` file - depending on which one your shell is using) - the line:  

  `source ~/anaconda3/etc/profile.d/conda.sh`

- use normally the command  

  `conda activate My_Venv`


3. Just use the commands below :)  

  `source activate My_Venv` to "activate" the VEnv   
  and   
  `conda deactivate` to deactivate.


---
