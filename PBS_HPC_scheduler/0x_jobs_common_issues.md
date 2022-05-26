[preliminary draft]

#### common reasons for jobs not running.

Non-exhaustive list of possible job-issues and errors;

look for these and/or similar comments in the output of :

`qstat -f JOBID`  
OR   
`qstat -f JOBID.pbs`

---

`Not Running: Insufficient amount of resource: ncpus`   

There may not be enough CPU cores available to start this job.  
Nothing is wrong: the job is simply waiting for its turn to run.  


`Not Running: Insufficient amount of resource: mem `  

There may not be enough memory available to start this job.  .
Nothing is wrong: the job is simply waiting for its turn to run.  


`Not Running: Job would conflict with reservation or top job  `

The job is waiting for another job to finish, before it will have available resources to run.  
Nothing is wrong: the job is simply waiting for its turn to run.  


`Not Running: PBS Error: Could not reserve allocation from project “<prj>” to run job.`  `

This comment can be temporary for a job during the period that the job scheduler reconsiders to run it. When it is not transient, similar to the example shown above, it suggests that the project has not enough SU in the `Avail` account. Jobs with this comment might be able to run when the `Reserved` SUs returns to `Avail` depending on the actual usage of the just-finished jobs.

**Not Running: Job would cross dedicated time boundary**  

Jobs with a wall time limit that would extend into a scheduled downtime will not be started until the scheduled maintenance finishes.
If you know the job won't use all the requested wall time, please request it as close to the actual usage as possible.  
If it is not possible to reduce the walltime limit to allow zero overlap between the job's potential execution time and the scheduled downtime, the job has to wait to be started after the downtime window.