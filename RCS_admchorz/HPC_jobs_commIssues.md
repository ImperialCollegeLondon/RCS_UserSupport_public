

### SELF TROUBLESHOOTING TIPS and STEPS

The following is a list of commonly encountered issues, that will prevent users to run jobs or make them incur into issues, whenever running/submitting jobs to the HPC.

Please consider  

**using this checklist before opening a ticket with RCS Tech Support**  

as a first troubleshooting step, to make sure everything has been thoroughly checked on the client-side first.



---


#### 1) Quota and storage space limits

**Reason:**  
when your quota is reached, you and your jobs will not be able to create/save any more files; everything that is based on this operation will fail or not start.

**How to Check:**  
- at every subsequent login to the HPC CLI you will be presented with a recap summary of your quota.  
- you can run the "quota" command from HPC CLI to confirm you are NOT "OVERQUOTA" or reaching 100%  

**How to Fix:**  
- use common sense when creating and storing files  
- come up with a useful storage-management solution (**)  
- archive, compress (tar, tgz, zip etc.) or delete files to restore quota availability.(**)  

(**) = especially useful and indicated for older projects and files.

**Caveats:**   
- 2 are the thresholds to keep in mind with quota:
you can reach both MAX files numbers quota or MAX disk space quota;

(example 1:  
  2 millions small files will make you reach the _MAX files number quota_ (if this is set to 1 million files per user, for instance,) even if you still have disk space quota available)

(example 2:  
  if you have 2TB of quota and you save just 4 very big files of 500GB each, this will make you reach the _MAX disk space quota_, regardless the fact that you still have 900k more files you could potentially save to reach the MAX files number threshold)

- please note that for the system to report the "exact quota values",
15-30 mins may be needed to sync back metadata from the storage systems.

This means that e.g. if you are at 99% and very recently you/your job has created even more files (reaching for instance 100%),
in order for you to be able to see this, you need to wait 15-30 mins before the output of the quota command is updated.


#### 2) Amount of resources requested  

**Reason:**  
when you submit many jobs all the resources requested sum up to the total amount of resources you are using, and there may be a maximum on your user, project,


**How to Check:**  
- use the "availability" command to check availability resources
- contact the PBS admin if the online documentation is not clear or the data reported is not realistic; they will help you understanding and possibly checking this.
- use (but do NOT automate with "watch" or iterative scripts, rather run manually and sparingly) the "qstat" command to check on the status of your jobs. (see below...)


**How to Fix:**  
- use common sense when submitting jobs (especially job arrays with a lot of sub-jobs)
- understand the sizing of jobs and translate common concepts to your specific job requirements, to come up with ad-hoc sensible sizing.
- size your jobs in a wise fashion
- use resources wisely and sparingly, do not OVERSIZE jobs
- understand that : the more resources you request, the longer your job will queue up for and unluckily it may not even run if not enough resources are available at one single time.
- understand the correct flags to use when issuing the "qstat" command to check upon different things:
```
qstat -answ1
qstat -t 1234[]
qstat -as 123
```

**Caveats:**   
- there may be limitations in place decided by the system or the system administrator :
- there may be the need




#### 3) SOFTWARE RELATED ISSUES (NOT RCS/HPC APPLICATIONS!)  


**Reason:**  
there may be issues with the software you are trying to run, that not necessarily are Applications related (i.e. they have little to do with the HPC installed SW and applications);
these issues are most likely seen as bugs in the code you run or compile, in the logic steps of your jobscripts etc..


**How to Check:**  
- make sure to inspect failed jobs error and output logs as well as
- make sure to inspect the main program (run by the jobscript) output/errors


**How to Fix:**  
- make sure to follow our latest guidance and examples:
    - when running jobscripts
    - when creating your own SW virtual environments with anaconda


**Caveats:**   
 most of the time users are able to spot straight away after inspection of the above, small issues and typos made from their end;
 sometimes more advanced SW development skills are required to troubleshoot and debug issues; for these cases please make sure to open a ticket with the RCS Support
 - using the latest guidance when providing information on the failed jobs
 - using your OS-clipboard copy/paste features when creating tickets, PLEASE DO NOT attach pictures (especially when long paths, jobIDs and details that are prone to typos are involved and need to be checked.)

