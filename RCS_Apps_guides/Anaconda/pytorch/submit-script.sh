#!/bin/bash
#PBS -N CUDAtest
#PBS -l select=1 ... (with GPU specifications as per sizing guidance)
#PBS -l walltime=00:15:00

cd ${PBS_O_WORKDIR}

module purge
module load cuda/10.2
module load cudnn/8.2.4

module load anaconda3/personal

## Remember to change this value yo the name of your VEnv with pytorch
source activate YOUR_NAMED_pytorch

echo "testing pytorch build CUDA capabilities at $(date)"

python CudaTest.py

echo "... Run finished $(date)"
