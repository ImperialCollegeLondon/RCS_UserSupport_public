
## R versions HPC globally installed VS own build

If you need to use R, you can achieve this in 2 ways :


###  1. Using our **HPC globally installed version of R**

which comes with tons of useful packages already pre-installed/compiled for you.

just add to your job-scripts the following, before running R Rscript :

```
module purge
module load tools/dev
module load R/4.2.1-foss-2022a
```


and test if this version of R - which is the most comprehensive and updated we have to date installed - has the packages you need; or if something missing you can install them locally in your /home path by following the
install.packages("")




### 2. Using a custom build of R, installed with anaconda

If you want to build your **own anaconda version of R** you can try navigating this very GitHub repo, and look for the following guides and examples :

`RCS_Apps_guides/Anaconda/05_HPC_R_workflow.md`  

this ["yet another online guide about R" from anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/) which is very useful.  


In a Nutshell, the command you should be using, and testing for the installation is:

```
module load anaconda3/personal
conda create -n Name-of-MY_Renv r-essentials r-base
```

this will install the anaconda packages:

- **r-essentials** ( [from r channel](https://anaconda.org/r/r-essentials)    )

  The R-Essentials bundle contains approximately 200 of the most popular R packages for data science, including the following:  `IRKernel`, `dplyr`, `shiny`, `ggplot2`, `tidyr`, `caret`, and `nnet`.

- **r-base package**  ( [from conda-forge](https://anaconda.org/conda-forge/r-base)  or [from r channel](https://anaconda.org/r/r-base)  )

  which contains the "R interpreter"
  R is the default interpreter installed into new environments;
  Unless you change the R interpreter, conda will continue to use the default interpreter in each environment.  



other [RCS official guides](https://wiki.imperial.ac.uk/display/HPC/R)




