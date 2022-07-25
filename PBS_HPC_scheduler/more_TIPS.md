



TIPS for the future:

-please kindly consider NOT combining output and error logs (from the jobscript) automatically in 1 file ...
or if a job fails please rerun it with separated jobscript output/error logs so we can analyse them more easily.

how to achieve this:

removing from job-scripts the directives:
```
#PBS -o fileA
#PBS -e fileA
```
(this will combine the o and e logs into 1 fileA difficult to read for analysts.)

default bevhavior omitting these directives :

jobscript will create a `jobname.eJOBID`  errorfile `jobnam.oJOBID` outfile in the submission folder i.e. `$PBS_O_WORKDIR` .  
