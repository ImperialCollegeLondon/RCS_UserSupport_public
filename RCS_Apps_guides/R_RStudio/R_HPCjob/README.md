## Run R-scripts within HPC jobs

Some example files are located in this repo folder and can be used as a "start-up template" for your workflow :

- _my_R_script.R_  (basic example of R-script)
- _01_R_job_script.pbs_  (basic example of HPC job-script - AKA. submission-script OR PBS-script)
- _02_R_job-Array_script.pbs_    (example of HPC job-script to submit an [R-script array job](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/computing/array-jobs/)) 

### Procedure:

- make a _job-specific_ sub-folder in `${HOME}` or `${EPHEMERAL}`

  some examples :  

 `mkdir ${HOME}/myRproject_01`  

 `mkdir ${EPHEMERAL}/myRproject_02`  

Place into this sub-folder:

- your **Rscript** (e.g. `Rscriptv1.R` -- this is a R-script with R instructions in it, as you will type in Rstudio R-cells - please do not insert bash code or other)  

- your **job-script** (e.g. `jobscript_v1.pbs` -- this is a bash-script file with **#PBS instructions**)  

example of sub-folder content listing :
```
ls ${HOME}/myRproject_01/

jobscript_v1.pbs
Rscriptv1.R
```

- submit your job **from this very _job_specific_ sub-folder** with the `qsub <job-script>` command :     

submitting from this folder means that this folder will automatically be referenced with the variable `${PBS_O_WORKDIR}`, so you can refer to it in your job-script. (see file [01_R_job_script.pbs](/RCS_Apps_guides/R_RStudio/R_HPCjob/01_R_job_script.pbs)

example of submission command :
```
cd ${HOME}/myRproject_01/
qsub jobscript_v1.pbs
```

---

EXAMPLE 1 :  

When the job-submission is **successful**   
the jobID of your currently submitted job is returned.

```
5626043.pbs
```

- you can check the status of all of your submitted jobs, with the command :  

  `qstat -s`

example of output :
```
pbs:
                                                            Req'd  Req'd   Elap
Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
--------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
5626043.pbs     username <qName> <job_name>    --    1   1    1gb 00:03 Q   --
    --
```

- you can check the details of a specific job with the command :

  `qstat -f <JOBID>`.


example of command and redacted output :
```
qstat -f 5626043

Job Id: 5626043.pbs
  Job_Name = <job_script_name>.pbs
  Job_Owner = username@node
  job_state = <queueing_state>
  queue = <queueName>
  server = <serverName>
  Checkpoint = u
  ctime = <timestamp>
  Error_Path = nodeName:${PBS_O_WORKDIR}/<job_script_name>.pbs.eJOBID
  group_list = your_groupName
  Hold_Types = n
  Join_Path = n
  Keep_Files = oed
  Mail_Points = n
  mtime = <timestamp>
  Output_Path = nodeName:${PBS_O_WORKDIR}/<job_script_name>.pbs.oJOBID
  Priority = 0
  qtime = <timestamp>
  Rerunable = True
  Resource_List.mem = <resource_requested>
  Resource_List.mpiprocs = <resource_requested>
  Resource_List.ncpus = <resource_requested>
  Resource_List.nodect = <resource_requested>
  Resource_List.place = <resource_requested>
  Resource_List.select = <resources_requested>
  Resource_List.walltime = <resource_requested>
  substate = 10
  Variable_List =
PBS_O_SYSTEM=...
PBS_O_HOME=...
PBS_O_LOGNAME=...
PBS_O_WORKDIR=...
PBS_O_LANG=...
PBS_O_PATH=...
PBS_O_MAIL=...
PBS_O_QUEUE=...
PBS_O_HOST=...
  etime =<timestamp>
  eligible_time = <some_value>
  Submit_arguments = ...
  project = ...

```


---

EXAMPLE 2 :  

When your job-submission is **NOT successful**  
no job is started.  
In the case of the output below, you need to fix the job-script (`#PBS` lines) and pick a correct resources combination according to the latest [job sizing guidance](https://wiki.imperial.ac.uk/display/HPC/New+Job+sizing+guidance/).

```
qsub:
 Job resource selection does not match any permitted configuration.
 Please review the job sizing guidance on:
 https://wiki.imperial.ac.uk/display/HPC/New+Job+sizing+guidance/
```

---
