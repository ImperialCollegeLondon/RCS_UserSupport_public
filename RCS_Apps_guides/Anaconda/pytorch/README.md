[WIP 20220725]


Using the link [pytorch.org](https://pytorch.org/get-started/locally/) to generate the instructions to build the pytorch-based Virtual Environment :  


Example for the HPC using these values:

```
Pytorch stable: 1.12.0
Linux
Conda
Python
Cuda 10.2
```

one can use the following instructions to build a new conda VEnv with Cuda-enabled pytorch:

```
conda create -n MYenv_pytorchCUDA python==3.8 -y
source activate MYenv_pytorchCUDA
conda install pytorch torchvision -c pytorch
```

Remember to load the same exact cuda version in your jobscripts as in our example.

Submit to the GPU nodes a jobscript calling as main function/executable the file in this repo :

`python CudaTest.py`  

this will print out information on your pytorch version and capabilities.
