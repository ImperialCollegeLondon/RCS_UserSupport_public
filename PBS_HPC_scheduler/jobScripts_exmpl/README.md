## HPC jobs examples and common caveats

NOTES and CONVENTIONS :   

- For the purpose of these guides the terms **job-script** and **submission-script** are used interchangeably.   
- for sake of simplicity the first line used in the example files of this Repo folder is `#!/usr/bin/bash` compatible with the new login nodes setup.    
- lines starting with `#PBS` are PBS-scheduler directives, lines starting with `### ` are just comments, the first line starting with `#!` is the script interpreter selection.  

---
- issues with the script interpreter

if for any reason you receive "bash" related warning or error messages in your job output/error files this could be related to the interpreter called in your job-scripts;

Q: what to do?
A: check your job-script first line and modify accordingly.


### examples :


1st line of the job-script reads:  `#!/bin/bash`  

Q: is bash | sh | ksh | zsh or whatever else shell interpreter you need, present on the system where you are submitting the job from ?  

A: check with `which <interpreter>` and use in the job-script the path returned.

- **case 1 :**  
  `bash` is needed as a script interpreter  
  typing `which bash` in terminal  
  returns `/usr/bin/bash`  

  the job-script first line should be `#!/usr/bin/bash`  


- **case 2 :**  
  `sh` is needed as a script interpreter  
  typing `which sh` in terminal  
  returns `/bin/bash`  

  the job-script first line should be `#!/bin/sh`  


typing `which bash` in terminal could return different results when on different systems sometimes; this depends on systems setups and scripts.

e.g.

`/bin/bash`  
`/usr/bin/bash`  
etc...

alternatively as a catch all case you could try using the line below as first line of the job-script :  

`#!/usr/bin/env bash`

provided that the `env` program is located at `/usr/bin/env`  
otherwise run `which env` to locate its path and use the path returned.  


- sometimes job-scripts may run even without specifying a shell interpreter in the first line: this may be due to our custom setup and/or configuration.  

---
