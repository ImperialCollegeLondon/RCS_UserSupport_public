
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



### 07 : cloning/backing-up an Anaconda VEnv

to create a **clone / backup** of on of your current VEnvs use the commands below.  

If this is a **backup** (rather than a testing/development-clone) we advise keeping the clone untouched, and in the case of VEnv corruption, you can start back from this backup, creating a new working production-grade clone.

[Workflow example](/RCS_Apps_guides/Anaconda/07_VEnv-cloning_WKFL.md)  


### 08 : Deleting a conda Environment

Various options to delete anaconda environments are listed below.

common reasons for wanting to delete a Conda environment are:

-  **To free up space**  
  Conda Envs consume space and you may eventually, run out of space on your system.  
  To free space, you can delete unnecessary conda environments.

-  **Delete a corrupted environment**  
  Conda environments get corrupted easily. It is often easier to start from scratch by creating a new environment.

- **Good practice**  
  It is a good practice to delete the conda environments you do not need or that are old or not actively maintained. (python packages and libraries gets very often updated and your VEnv and code may get outdated very quickly)

---

1. `conda env remove -n <corrupted_env>`  

  OR   `conda env remove --name <corrupted_env>`  


2. `conda remove -n <corrupted_env> --all`  

  OR  `conda remove --name <corrupted_env> --all`  

3. `conda env remove --prexif /path/to/MyEnv2remove`  

  OR  `conda env remove -p /path/to/MyEnv2remove`  

  This last option implies knowledge of the path where the env is stored: (normally under `$HOME/anaconda3/envs/myenv_name` for our installation)


NOTE:  
It is not advisable to delete the conda environment directory directly but In some cases, it might be necessary.
This can be achieved like so:  

Find the path of the conda environment using:

  ```
  conda info --envs
  rm -rf /path/2/anaconda/envs/corrupted_env
  ```



### 0X : References

[managing conda envs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)  

[moving, cloning, backing up conda envs](https://www.anaconda.com/blog/moving-conda-environments)  

[deleting conda envs](https://iq.opengenus.org/delete-conda-environment/)  


