
## MKL

accessing **MKL** functionalities is done through **intel-suite** module-files or the newly added/built easy-build modules.

- using older (pre 2022) module files and SW installed on the HPC  

**workflow example :**   
(add to your job-script only the `module add/load` lines!)  

```
module avail intel
----------------------- /apps/modules/4.7.1/modulefiles ------------------------
intel-suite/2011     intel-suite/2015.3  intel-suite/2017.1
intel-suite/2013sp1  intel-suite/2016    intel-suite/2017.6(default)
intel-suite/2015     intel-suite/2016.3  intel-suite/2019.4
intel-suite/2015.1   intel-suite/2017    intel-suite/2020.2
-------------------------------------------------------------------

module add intel-suite/2019.4

```

- using newer (2022+) easy-build installations and module files    

**workflow example :**  
(add to your job-script only the `module add/load` lines!)   


```
module add tools/dev

module avail buildenv
--------------------------- /apps/sw-eb/modules/all ----------------------------
buildenv/default-foss-2019b  buildenv/default-foss-2020b
buildenv/default-foss-2020a  buildenv/default-foss-2021a
-------------------------------------------------------------------

module add buildenv/default-foss-2021a

module avail imkl
--------------------------- /apps/sw-eb/modules/all ----------------------------
imkl-FFTW/2021.4.0-iimpi-2021b  imkl/2021.2.0-iimpi-2021a  imkl/2021.4.0

module add imkl

```






---

## BLAS, LAPACK, FFTW3

**BLAS** , **LAPACK** , **FFTW3** (and others) can be accessed through **OpenBLAS** , which is an optimized version on our SW Stack deployment.  

We have a **build environment module** now available for users.  

This will give users some _pre-installed environments_ to be able to build and compile software, it does contain

- gcc  
- gfortran  
- OpenBLASS  
- fftw3  

### How to access the build environment module

#### to check what's available:

> [IC VPN] --> SSH hpc --> terminal

```
module avail tools
module show tools/dev
module add tools/dev

module avail buildenv
module show buildenv/default-foss-2021a
```

#### to use in your job-scripts/workflows

It is as simple as using the following instructions in your job-script, to access those functionalities.

```
module add tools/dev
module add buildenv/default-foss-2021a
```

these will load all their requirements too, such as
```
GCCcore
UCX
OpenMPI
OpenBLAS
FFTW
ScaLAPACK
etc...
```
