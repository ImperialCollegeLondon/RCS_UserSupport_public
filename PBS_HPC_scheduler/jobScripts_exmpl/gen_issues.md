

## Issues with the script interpreter

If for any reason you receive "bash" related warning or error messages in your job output/error files this could be related to the interpreter used in your job-scripts.  

**Q :** what to do?  
**A :** check your job-script first line and modify accordingly.  


#### examples :


the 1st line of a job-script reads:  `#!/bin/bash`  

**Q :** is `bash` , `sh` , `ksh` , `zsh` (or whatever else shell-interpreter is needed) present on the system ?

(assuming the compute nodes where the job runs on have the same shell interpreters setup as the login nodes ...)

**A :** check with `which <interpreter>` and use in the job-script the path returned.

---

- **example 1 :**  
  `bash` is needed as the script interpreter  
  typing `which bash` in terminal  
  returns `/usr/bin/bash`  

  the job-script first line should be `#!/usr/bin/bash`  


- **example 2 :**  
  `sh` is needed as a script interpreter  
  typing `which sh` in terminal  
  returns `/bin/bash`  

  the job-script first line should be `#!/bin/sh`  

---

NOTES:

- Typing `which bash` in terminal could return different results when on different systems sometimes; this depends on systems setup and scripts.

> e.g.
>
>  `/bin/bash`  
>  `/usr/bin/bash`  
>  etc...
>
>  alternatively as a catch all case you could try using the line below as first line of the job-script :  
>
>  `#!/usr/bin/env bash`
>
>  provided that the `env` program is located at `/usr/bin/env`
>
>  (otherwise run `which env` to locate its path and use the path returned.)  


- sometimes job-scripts may run even without specifying a shell interpreter in the first line: this may be due to our custom setup and/or configuration.  

---
