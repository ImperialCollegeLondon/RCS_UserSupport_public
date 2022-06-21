## HPC jobs examples and common caveats

NOTES and CONVENTIONS :   

- For the purpose of these guides the terms **job-script** and **submission-script** are used interchangeably.   
- for sake of simplicity the first line used in the example files of this Repo folder is `#!/usr/bin/bash` compatible with the new login nodes setup.    
- lines starting with `#PBS` are PBS-scheduler directives, lines starting with `### ` are just comments, the first line starting with `#!` is the "script interpreter selection" line.  

---
### Common issues:  

[Issues with the script interpreter](/PBS_HPC_scheduler/jobScripts_exmpl/gen_issues.md)  

<!-- WIP DRAFT to finish -->
jobs get killed by the scheduler

---

### HOME folder housekeeping : how to keep tidy your working environment

We normally advise users to keep their home folder tidy and easy to navigate, possibly using a "subfolder-per-project structure" to keep all input, output, job scripts self-contained and separated, to help with source control and to be able to separate also job-scripts, out/log/error files on a per-run basis in order to simplify Users' lives and allow Analysts a faster troubleshooting, whenever issues arise with User's code/job-submissions etc.  

[House-keeping example and folders structure](/PBS_HPC_scheduler/jobScripts_exmpl/houskeepStruc.md)  

---
### job-script examples


The following are simple job-scripts examples to be used as a templates and starting point for your workflow :  

[basic job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x01_basic.pbs)  

[simple job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x02_simple.pbs)  

[GPU App job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x04_GPU.pbs)  

[Job Array job-script](/PBS_HPC_scheduler/jobScripts_exmpl/0x05_jobArray.pbs)  


