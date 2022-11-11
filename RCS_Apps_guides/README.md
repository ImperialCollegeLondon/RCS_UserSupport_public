### IC RCS guides for Running software on the HPC Services

NOTES :

- always check first if a software is already available and installed on the HPC Systems' environment  
  - most likely SW comes in various versions via module-files. (old SW-stack, new SW-stack, easybuild SW-stack)


- all SW installation requests need to go through [RCS - Help](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/get-support/contact-us/) --> requests to install software in the HPC systems


Refs:   

[RCS HPC wiki: getting started](https://wiki.imperial.ac.uk/display/HPC/Getting+started)     
[RCS HPC wiki: applications](https://wiki.imperial.ac.uk/display/HPC/Applications)    


#### currently HPC provided module files

- production grade module files

```
module load tools/prod
```

- development grade module files (may break)

```
module load tools/dev
```


---

### Anaconda

indicated to run your software versions by using [Anaconda](/RCS_Apps_guides/Anaconda/README.md) and virtual environments where you can easily install software.


### Julia  


### Matlab  


###  MKL, BLAS, LAPACK, FFTW3

some commonly used libraries and how to access them [libs and Features](/RCS_Apps_guides/libs_and_features.md)  


### Build environment


```
$ module add tools/dev
$ module avail build
$ module add buildenv/default-foss-2021a
```


### Compilation of Software

[Ref. to extended guidance](/RCS_Apps_guides/SW_compilation.md)





---

#### NOTES  

Please remember that you will need to incorporate the above commands (their "slimmed down versions" or similar) into your **job-scripts** ;  

running software or compilations on **login nodes** is NOT allowed and available _ONLY_ in some particular cases.  

(i.e. tasks that do NOT require intensive calculations and/or extensive usage of the underlying HW resources of the node, as well as tasks that will NOT run for a prolonged time - ideally not more than 10-30 minutes).  

**Long running compilation tasks, executables and programs** will be NOT allowed to run on login nodes and once spotted, instantly killed both automatically by the Systems, and manually by the system administrators, resulting in **users' loss of time and work** and possibly a **penalty** for future job runs when correctly submitting to the queues (batch system).  



































