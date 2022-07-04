#!/usr/bin/bash

#PBS -l select=1:ncpus=6:mpiprocs=6:mem=32gb
#PBS -l walltime=00:15:0
#PBS -N testName

### make sure no other modules are loaded

module purge

### Load modules for the needed application (if already installed on the HPC)

module load lammps/19Mar2020

### Change directory to the submission folder (where my script is located in this example)

cd ${PBS_O_WORKDIR}

#------------------------------------------------------------------------------------------------------------
### saving some useful job debugging info
### edit TSTMP to tweak timestamp/date formatting output (man date)

LINE="-----------------------------------------------------------"
TSTMP1=$(date +%Y%m%d-%H%M%S)
echo -e "\n${LINE}\nJobID: ${PBS_JOBID}\nStart time: ${TSTMP1}\n${LINE}\n" >> debug.log
#------------------------------------------------------------------------------------------------------------

### Run a python3 script (located in the submission folder)
### and save output and error files into the submission folder itself.

python3 myPythonScript.py

#------------------------------------------------------------------------------------------------------------
### saving some useful job debugging info
### edit TSTMP to tweak timestamp/date formatting output (man date)

TSTMP2=$(date +%Y%m%d-%H%M%S)
echo -e "\n${LINE}\nJob ${PBS_JOBID} has completed \nEnd time: ${TSTMP2}\n${LINE}\n" >> debug.log
#------------------------------------------------------------------------------------------------------------