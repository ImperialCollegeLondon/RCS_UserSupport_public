###### use/install R in Venv via anaconda/personal

The recommended method to use R is by using your personal anaconda installation. (module load anaconda3/personal)
You can - and should! - create specific conda environments with the version you require of R,
**NOT installing everything in the base environment**
(the one that gets setup straight after running anaconda for the first time: this is called base environment and should be kept untouched)

Please read for reference: https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/applications/conda/

---

5. Installation/Setup of R Virtual Environment Example Workflow  

- load anaconda module personal installation:  

`module load anaconda3/personal`

- as already discussed in file: `03_workflow_examples.md`  
for anaconda first-timers or after you had purged and reset all your anaconda setup/installation you need to install it first,   
otherwise skip ahead at next point :

`anaconda-setup`  
(and follow the on-screen instructions.)

- create your "R-specific" virtual environment

(some examples below)

[A] - Create a conda-named (`-n RenvTest2`) virtual environment with R installed in it (remotely pulling a specific version: e.g.  `R v4.1`):   

`conda create -n RenvTest2 r-base=4.1 -c conda-forge`

OR:  

[B] - Create a conda-named (`-n RenvTest3`) virtual environment with R installed in it (remotely pulling the latest provided version):  

`conda create -n RenvTest3 r-base -c conda-forge`

---
**IMPORTANT NOTE :**  

- to start working into this new Venv
and/or
- If you need to install additional r packages in a specific environment

you will need to have the specific conda virtual environment with R, **ACTIVATED first !**

Please always check which conda environment is active by running:  

`conda env list`  

(and check for the `*` sign that indicates the currently active environment)

---

- start/activate your named virtual environment:

examples:  

`conda activate RenvTest2`  
OR if it errors:  
`source activate RenvTest2`  


- write a job-submission batch script containing the instructions at points above and whatever commands you need to run in batch mode on the HPC for running R-batch mode, NOT INTERACTIVE! or Rscript.

example of a generic script :

**NOTE :**   
please note that `#PBS` directives are those used by the scheduler to allocate resources to this job-script at submission time; those reported below are not realistic.  


filename :  `Rprogram_v1_jobscript.PBS`   

file content:  

```
#!/bin/bash
#PBS select=1
#PBS ...
#PBS ...

module load anaconda3/personal
source activate RenvTest2

Rscript (do something)

## OR in another way
start R >> do something
```

---

Please refer to R manual pages and IC RCS jobs scheduling and job-scripts writing guidance for more info.
