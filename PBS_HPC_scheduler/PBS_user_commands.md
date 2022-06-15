## Run a batch scripts within HPC jobs

See for more details [R-script examples](https://github.com/ImperialCollegeLondon/RCS_UserSupport_public/tree/main/RCS_Apps_guides/R_RStudio/R_HPCjob)


### Procedure:

- make a _job-specific_ sub-folder in `${HOME}` or `${EPHEMERAL}`

  some examples :  

 `mkdir ${HOME}/myProject_01`  

 `mkdir ${EPHEMERAL}/myProject_02`  

Place into this sub-folder:

- your **Python script** (e.g. `MyAwesomeProgram.py` -- this is a python script with python instructions in it, as you will type in Jupyter Notebook Python Code cells)  

- your **job-script** (e.g. `jobscript_v1.pbs` -- this is a bash-script file with **#PBS instructions** -- scheduler directives )  

example of sub-folder content listing :
```
ls ${HOME}/myRproject_01/

jobscript_v1.pbs
MyAwesomeProgram.py
```

- submit your job **from this very _job_specific_ sub-folder** with the `qsub <job-script>` command :     

submitting from this folder means that this folder will automatically be referenced with the variable `${PBS_O_WORKDIR}`, so you can refer to it in your job-script.
<!--(see file [01_R_job_script.pbs](/RCS_Apps_guides/R_RStudio/R_HPCjob/01_R_job_script.pbs)  ## fix refs-->  

example of submission command :
```
cd ${HOME}/myRproject_01/
qsub jobscript_v1.pbs
```

---

EXAMPLE 1 :  

When the job-submission is **successful**   
the jobID of your currently submitted job is returned.

example:  
```
5626043.pbs
```

- you can check the status of all of your own submitted jobs, with the command :  

  `qstat -u $USER`

example of output :
```
pbs:
                                                            Req'd  Req'd   Elap
Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
--------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
5626041.pbs     username <qNameA> <job_name1>    --    1   1    1gb 00:01 Q   --
5626042.pbs     username <qNameB> <job_name2>    --    1   1    2gb 00:02 Q   --
5626043.pbs     username <qNameC> <job_name3>    --    1   1    3gb 00:03 Q   --
    --
```

- you can check the status of all of your own currently submitted jobs with a different table/info layout:  

`qstat`  

example:   
```
   Job ID           Class            Job Name        Status     Comment
-------------- --------------- -------------------- -------- -------------
5626041        GPU             <job_name1>         Queued   starting by Wed Jun 15 14:51
5626042        GPU             <job_name2>         Queued   starting by Thu Jun 16 03:03
5626043        v1_medium72     <job_name3>         Running  finishing today at 17:07
```


- you can check specific **NOTES from the scheduler** of your submitted jobs, with the command :  

  `qstat -s <JOBID>`

example:  
```
                                                              Req'd  Req'd   Elap
  Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
  --------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
  5645861.pbs     plc21    v1_gpu72 Analyse_Te    --    1  30  900gb 20:58 Q   --
     Not Running: Insufficient amount of resource: Qlist
```

in this case the note:

> Not Running: Insufficient amount of resource: Qlist

This means that too many resources might have been requested already by your user; and no more are currently available in the available pool.

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
