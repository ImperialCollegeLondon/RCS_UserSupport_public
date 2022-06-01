## HOW TO: run Rscript in an HPC job

example files are located in this repo folder and can be used as start-up templates for your workflows :

- my_R_script.R  
- 01_R_job_script.pbs  
- 02_R_job-Array_script.pbs    

### Procedure:

- make a `job_specific` sub-folder in `${HOME}` or `${EPHEMERAL}`

  examples:  
 `mkdir ${HOME}/myRproject_01`  
  OR  
 `mkdir ${EPHEMERAL}/myRproject_02`  

- into this sub-folder place your **Rscript** (e.g. `Rscriptv1.R` -- this is Rscript with R instructions as you will type in Rstudio R cells, no bash etc.)
- into this sub-folder place your **job-script** (e.g. `jobscript_v1.pbs` -- this is a bash file with **#PBS instructions**)  

example:
```
ls ${HOME}/myRproject_01
jobscript_v1.pbs
Rscriptv1.R
```

- submit your job **from this `job_specific` sub-folder**

example:
```
cd ${HOME}/myRproject_01/
qsub jobscript_v1.pbs
```
- example 1 of submission output:  
(i.e. job-submission **successful** and the jobID of your currently submitted job is returned).  

  ```
  5626043.pbs
  ```

  you can check the status of all jobs and the details of a specific job with the commands:
  `qstat -s` and `qstat -f <JOBID>`.



```
qstat -s

pbs:
                                                            Req'd  Req'd   Elap
Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
--------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
5626043.pbs     username <qName> <job_name>    --    1   1    1gb 00:03 Q   --
    --
```

.

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

- example 2 of submission output:  
(i.e. job-submission **UNsuccessful** no job is started; you need to fix `#PBS` lines in your jobscript and pick the correct resources).
```
qsub:
 Job resource selection does not match any permitted configuration.
 Please review the job sizing guidance on:
 https://wiki.imperial.ac.uk/display/HPC/New+Job+sizing+guidance/
```

