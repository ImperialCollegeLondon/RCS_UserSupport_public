## HPC jobs examples and common caveats

NOTES and CONVENTIONS :   

- For the purpose of these guides the terms **job-script** and **submission-script** are used interchangeably.   
- for sake of simplicity the first line used in the example files of this Repo folder is `#!/usr/bin/bash` compatible with the new login nodes setup.    
- lines starting with `#PBS` are PBS-scheduler directives, lines starting with `### ` are just comments, the first line starting with `#!` is the "script interpreter selection" line.  

---



[Issues with the script interpreter](/PBS_HPC_scheduler/jobScripts_exmpl/gen_issues.md)  

---

#### job-script examples


The following are simple job-scripts examples to be used as a templates and starting point for your workflow :  

[basic job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x01_basic.pbs)  

[simple job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x02_simple.pbs)  

[GPU App job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x04_GPU.pbs)  

[Job Array job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x05_jobArray.pbs)  


