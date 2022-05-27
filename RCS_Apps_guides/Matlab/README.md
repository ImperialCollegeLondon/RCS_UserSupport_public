
## MATLAB

**NOTES** :

-   All releases newer than R2013b can utilize up to 512 workers (CPU cores) on a local machine through the Parallel Computing Toolbox.  
-   Parallel Computing Toolbox will attempt to use 12 cores by default  
-   Parallel Computing Toolbox will attempt to use a number of workers equal to the physical cores of the computer.  


### Running matlab on the HPC via CLI (batch mode)

#### example of workflow

### **workflow_1**

**NOTES** :

- Matlab must **NOT be run on LOGIN NODES** but in appropriate **JOB-SCRIPTS!**  
- see notes below and documents on job-scripts.  


load Matlab module file from cluster SW installation:

```
$ module avail matlab

$ module load matlab/R2021a

$ which matlab
```


**IMPORTANT:**  

please note that following **workflow_1** above will result in user **running the software on the login node** (i.e. the node where they land when connecting to the HPC.) and this is normally not allowed.

Please refer to **job-sizing guidance** and submission of proper job-scripts that runs your software of choice on the compute nodes.


example of a submission script (AKA job-script) for Matlab :  
(see job-sizing guides for `#PBS` directives to request appropriately cluster resources).

in the code snipped below:  
`<-- bla bla` : these are just comments and cannot be put in the jobscript.

```
#!/usr/bin/bash       <-- note that this interpreter may need to be changed!

#PBS ...              <-- omitting selections for sake of example
#PBS ...              <-- omitting selections for sake of example

module load matlab/R2021a     <-- loading this modfile that I know it exists

cd $PBS_O_WORKDIR             <-- starting from my submission folder

## execution of program
matlab -nosplash -nodisplay -nojvm -batch myMfile.m -logfile myTestRun_output.log

```


other commands to try once you are familiar with the flags and their meaning:

examples:

1. achieving `single core execution`

- using in your code the function: `maxNumCompThreads(1)`

  > ref:
 https://uk.mathworks.com/help/matlab/ref/maxnumcompthreads.html  


- running `matlab` from Linux command line with the flag :   `-singleCompThread`  

  something like the following for instance:

  (i.e. place the following commands in your job-script above after the
  `## execution of program`  line, replacing what's there).

`matlab -nosplash -nodisplay -nojvm -singleCompThread -batch myMfile.m -logfile myTestRun_output.log`  

OR:   

`matlab -nosplash -nodisplay -nodesktop -nojvm -singleCompThread -logfile myTestRun_output.log -r myMfile.m`  




---

#### LINKS and references:

  https://www.mathworks.com/help/matlab/startup-and-shutdown.html?s_tid=CRUX_topnav

  https://www.mathworks.com/help/matlab/ref/matlablinux.html
  https://www.mathworks.com/help/matlab/matlab_env/commonly-used-startup-options.html

- Single-thread :

  https://www.mathworks.com/help/mps/server/usesinglecompthread.html#responsive_offcanvas

- Multi-thread :

  https://www.mathworks.com/help/mps/server/numthreads.html


#### may be useful to some users:

https://www.mathworks.com/matlabcentral/answers/340040-how-to-limit-cores-cpu-dedicated-to-matlab  

https://www.mathworks.com/matlabcentral/answers/334118-what-is-the-maximum-numbers-of-workers-i-can-use-with-matlab-parallel-computing-toolbox


#### for windows users:
(may be not best advice on HPC!)

https://www.mathworks.com/help/matlab/ref/matlabwindows.html  

https://www.mathworks.com/matlabcentral/answers/341799-how-to-run-matlab-files-in-batch-mode-or-as-a-batch-process#toggle-comments  

https://www.mathworks.com/matlabcentral/answers/102082-how-do-i-call-matlab-from-the-dos-prompt  

https://www.mathworks.com/matlabcentral/answers/97204-how-can-i-pass-input-parameters-when-running-matlab-in-batch-mode-in-windows  


