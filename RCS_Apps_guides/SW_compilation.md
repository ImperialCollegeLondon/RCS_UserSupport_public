
# Compilation of Software

## Intel CPU and chipset

Users are advised to use the Intel compilers and MKL performance libraries on Intel-based architecture Chipsets, since they usually give the best performance.




## AMD CPUs and chipset

Users are advised to use AMD compilers and related libraries on AMD-based architecture Chipsets, since they usually give the best performance.

### compilers Resources and references

[AMD Optimizing C/C++ and Fortran Compilers (AOCC)](https://developer.amd.com/amd-aocc/) -- [Download](https://developer.amd.com/amd-aocc/#downloads)

https://fortranwiki.org/fortran/show/Compilers

[The LLVM Compiler Infrastructure](https://llvm.org/)  


[generic info on Intel compilers for HPC etc.](https://www.aspsys.com/solutions/software-solutions/hpc-compilers/)  

[NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk)  
[NVIDIA HPC compilers User Guide](https://docs.nvidia.com/hpc-sdk/compilers/hpc-compilers-user-guide/)  

#### to compile Fortran code

[Fortran wiki compilers](https://fortranwiki.org/fortran/show/Compilers)

We normally advise users in need to compile on our HPC infrastructure Fortran based code, to use a flavor of the `gfortran` compiler.
This can be achieved in different ways, depending on your needs and level with the HPC.  

- by using the default module for GCC (which provides `gfortran` too)

```
$ module avail gcc
$ module load gcc
$ which gfortran
```

- by using the latest installed (May 2022) "Build environment" -- see above paragraph

```
$ module add tools/dev
$ module avail build
$ module add buildenv/default-foss-2021a
$ which gfortran
$ gfortran --version
```

**NOTE :**  
Please remember that in order to run compilation jobs you will need to incorporate the above commands (their "slimmed down versions" or similar) into your **job-scripts** ;
compilation on **login nodes** is available _ONLY_ for "light and short" compilation tasks.    
(i.e. tasks that do NOT require intensive calculations and/or extensive usage of the underlying HW resources of the node, as well as tasks that will NOT run for a prolonged time - ideally not more than 10-30 minutes).  

**Long running compilation tasks** will be not allowed on login nodes and when spotted, instantly killed both automatically by the Systems, and manually by the system administrators, resulting in **users' loss of time and work** and possibly a **penalty** for future job runs when correctly submitting to the queues (batch system).  

