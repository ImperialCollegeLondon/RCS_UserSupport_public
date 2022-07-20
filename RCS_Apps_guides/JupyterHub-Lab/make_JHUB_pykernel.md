

please create your jupyterHub kernels (Venvs accessible to JHUB)

by using anaconda3 and installing (only as LAST STEP!) ipykernel from the HPC command line as per this guides.

--> see [all guides on anaconda first](https://github.com/ImperialCollegeLondon/RCS_UserSupport_public/tree/main/RCS_Apps_guides/Anaconda)

```
source activate My-JHUB_kern1

(My-JHUB_kern1) user@HPC $: conda install sw_I_want_1
(My-JHUB_kern1) user@HPC $: conda install sw_I_want_2
(My-JHUB_kern1) user@HPC $: conda install sw_I_want_3
(My-JHUB_kern1) user@HPC $: conda install ipykernel
```

---
IMPORTANT NOTES:

please bear in mind :

 the more packages you install, the more complex the VEnv
 the more complex the VEnv, the more likely to fail build and dependencies resolution !

what creates issues most of the time :

 - amount of packages you are installing
 - version of these packages and their bulky dependencies

 These in fact may be conflicting, so in these complex cases, a clear understanding / listing of all the packages needed and their respective dependencies
 is needed, in order to be able to build the environments successfully.


 Sometimes "playing around with the order of the packages" may help (and you may notice which packages/dependencies are installed by others)
 navigating to the "files" links for the <MY-WANTED-PKGNAME> of choice may help in building these lists :

 `https://anaconda.org/conda-forge/\<MY-WANTED-PKGNAME\>/files`  

 e.g.  
 `https://anaconda.org/conda-forge/ipykernel/files`  
 `https://anaconda.org/conda-forge/matplotlib/files`  


---

### example Workflow of a complex installation :

1. create a list of all the tools/SW needed for the project :  

- `netcdf4` (+ dependencies)  
- `iris` (+ dependencies)  
- `matplotlib` (+ dependencies)  
- `hdf5` (+ dependencies)  

--> all these needs to be available via JHUB kernel (i.e. will need ipykernel)

2. check the web for conflicting packages/dependencies etc.  

`https://anaconda.org/conda-forge/\<MY-WANTED-PKGNAME>\/files`  

3. confirm the list is relevant:  

in this case `netcdf4` and `hdf5` were already pulled in by other tools so the final list is:

- `matplotlib` (+ dependencies)  
- `iris` (+ dependencies: including netcdf4)  
- `ipykernel` (+ dependencies)  

4. make an educated guess (based on the dependencies and requirements of the packages), of the **order of installation of packages**.
A "bad installation order" may pull in, older dependencies and making them conflicting with newer ones, of packages installed at a later stage.  

> This is achieved with experience and trial and error;  
> there is no "one-size-fits-all-guide/solution"

4. create a new (empty) Venv and activate it

5. manually install in subsequent steps the tools you need
(performing this in multiple steps may not be strictly necessary in theory, but it is very useful to make sure dependencies are resolving correctly and you can watch the installation progressing and checking the errors)

> adding a `-y` at the end of the install lines, confirms automatically the installation without the need of further manual interaction

  ```
  conda install matplotlib
  conda install iris
  conda install ipykernel
  python -m ipykernel install --user --name VenvName --display-name "name_displayed_in_JupyterNLH"
  ```


---

#### CAVEATS  

in a previous user test case of the same installation, the different order of packages below, was returning ERRORS and failures upon installation.  

  ```
  conda install ipykernel
  conda install iris
  conda install matplotlib
  ```

Iterating over steps 1. 2. 3. 4. above helped resolving the installation issues.  

> As a rule of thumb, Please consider firstly trying installing the "more core/lower-level packages and dependencies", and only at the end, the "more frontend-ones".

