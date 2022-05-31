
# IC RCS guide to installing SW/packages using anaconda on the HPC


### 01 : Basic info, channels etc.

- Introductory concepts  
- getting started guide  
- info on channels and "basic commands"

### 02 : Some Quick Examples

basic quick commands/examples to get started with Anaconda (the `conda` program).  

1. install `app_01`
2. install `app_02` and its dependencies
3. install `app_03` and its dependencies pulling packages from a specific channel

please see the HPC prerequisites as you may need to run `anaconda-setup` first.  
(see [workflows examples](/RCS_Apps_guides/Anaconda/03_workflow_examples.md) for extensive examples)

### 03 : Workflow examples

some basic workflows :

1. New Starter Workflow
2. checking Applications availability in Anaconda Channels
3. Creating your "Application-specific" virtual environment

### 04 : HPC extended workflows

Running any SW not provided on the HPC neither as a module nor via Easy-build, by creating an "ad-hoc" virtual Environment (VEnv) using a "personal anaconda installation" and writing a "job-script" to run it as a batch-job on the cluster.

### 05 : HPC R workflow examples

Running R on the HPC via personal anaconda installation and virtual Environment;  

**IMPORTANT :**
R must be run as a batch job via job-script and NOT as a standalone App on the login node(s).

### 0X : References

