## HPC caveats and extended workflows

To be able to run your program on the HPC you need to write a "job-script" that contains the commands to execute the program.
The job-script need to be submitted as a batch job on the HPC cluster infrastructure.  

This job will be subjected to all other jobs constraints: resources available, queueing times etc..

**NOTE :**  
Please do not Run software on the Login nodes.


4. running your "Application-specific" program in an anaconda  virtual environment as a batch/remote HPC job.

- after Creating your "Application-specific" virtual environment as per workflow 3 continued example (see `03_workflow_examples.md`)

- write a job-submission batch script containing the instructions to be run as a batch job remotely.

this will need to load anaconda module, activate the correct SW Virtual Environment and then run the installed SW with all needed command-line flags, input etc..

- submit the jobscript as per IC_RCS guidance.

---

example of a generic script :

**NOTE :**   
please note that `#PBS` directives are those used by the scheduler to allocate resources to this job-script at submission time; those reported below are not realistic.  


filename :  `myprogram_v1_jobscript.PBS`   

file content:  

```
#!/bin/bash
#PBS select=1
#PBS ...
#PBS ...

module load anaconda3/personal
source activate RenvTest1

cd directory/with_my/program

my_program run -f inputfile -o outputfile

```


please consider looking at all other available resources to write job-scripts and how to perform jobs submission for IC HPC Service Infrastructure and available queues and resources.

---