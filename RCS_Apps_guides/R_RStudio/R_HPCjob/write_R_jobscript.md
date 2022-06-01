
## write R job_scripts for the HPC to execute Rscripts

to write an R execution job script, there are various options depending on the version of R you need:

1. pre 2022 module files and SW versions  
2. 2022 module files and SW versions  
3. your own R version via anaconda installations   
<!-- 4. possibly others ? -->

---

### 1. pre 2022 module files and SW versions  

Some older SW version of R are already installed on the HPC; to display these:

[login to HPC Service] --> run `module avail R`

output example:

```
------------------------ /apps/modules/4.7.1/modulefiles ------------------------
R/2.2.1
R/2.4.1
R/2.5.1
R/2.7.0
R/2.8.1
R/2.9.1
R/2.11.1
R/2.13.0
R/2.14.2
R/2.15
R/3.0.1
R/3.1.0
R/3.1.2
R/3.2.0
R/3.2.2
R/3.2.3
R/3.2.4
R/3.3.0
R/3.3.1
R/3.3.2(default)
R/3.3.3
R/3.4.0
```

- the **default** version is the one automatically loaded if you run  
- `module load R` (without specifying the version)   
- you should run `module load R/3.4.0` and specify the version needed.

As the above software/versions may be old, incomplete or missing features and functionalities we had been asked over time, a new procedure and new software installations as well as newer versions have been built (and are going to be built).

to access the new versions keep reading below.

---

### 2. 2022 module files and SW versions  

as simple as inserting these lines into your job_scripts will give you access to the latest software builds.


```
module purge
module add tools/dev
module add R/4.1.2-foss-2021b
```

---


### 3. your own R version via anaconda installations  

To learn how to setup your R custom version/installation through anaconda  
please refer to this [R with anaconda guide](/RCS_Apps_guides/Anaconda/05_HPC_R_workflow.md)  

Please note that various users have reported difficulties installing multiple R software packages in these self-contained customized environments.

As dependencies and libraries trees can get quite complicated in these cases, issues must be solved on ad-hoc basis investigating each single case;
this could take weeks or months to sort out, according to how complex an installation or environment is or it has become over the time.

we strongly advise users to stick to the following principle:

**`K.I.S.P.` = Keep It Simple Please**


---

**IMPORTANT NOTES** :

- please do NOT run R on the login nodes but only in job-scripts.
- executing the commands above from a login node shell (instead of submitting a jobscript with the commands) will result in **running `R` on the login nodes** and we will need to action upon this. This may result in loss of time, files, work etc..

