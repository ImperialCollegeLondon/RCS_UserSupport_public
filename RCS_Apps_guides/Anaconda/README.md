
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

### 02a : Re-initialize your current anaconda personal installation

To **purge** your currently installed anaconda-personal installation and **Re-initialize** it  

you need to remove the `anaconda3` folder in your `/home` directory and re-install from scratch.

**IMPORTANT :**  

please bear in mind that this operation will **remove also all the virtual environments** that you have created so far because they are stored in `${HOME}/anaconda3/envs`.

**backing these up** may be possible, but I have not personally tested yet a fast and effective way to do so and most importantly, an easy/quick way to restore them after re-initialization.

`rm -rf ${HOME}/anaconda3/`


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

### 06 : Export / Import Anaconda Virtual Environments

Anaconda allows you to export a virtual environment into a YAML file.  
It’s simple to understand data serialization language often used to create configuration files.  
YAML is similar to JSON, but without brackets.  

- Use the following command to export the environment.  
remember to modify the export path of the command, here set to `/tmp`:  


`conda env export > /tmp/test_env.yaml`

NOTE:  
In the generated YAML/YML file, both :
- The **environment name** (displayed on the first line)
- The **prefix** line

must be changed manually because prefix path may not be valid/useful and you may already have such named environment (no duplicates!)

find the lines to change :  

`grep -E "name:|prefix: " /tmp/test_env.yaml`

then change them according to your needs.

- You can now use the following command to create a virtual environment from the YAML file:  

`conda env create -f /tmp/test_env.yaml`


### 0X : References

