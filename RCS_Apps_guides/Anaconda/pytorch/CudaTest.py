import torch

# check if pytorch is CUDA enabled

def print_cuda_Info():
    f = open('CUDAavail_test.log','w')
    f.write("checking code CUDA capabilities" + '\n')
    f.write("-------------------------------" + '\n')
    f.write("cuda available is : " + str(torch.cuda.is_available()) + '\n')
    f.write("cuda device count is : " + str(torch.cuda.device_count()) + '\n')
    f.write("cuda current device is : " + str(torch.cuda.current_device()) + '\n')
    GPU_id=torch.cuda.current_device()
    f.write("cuda device name is : " + str(torch.cuda.get_device_name(GPU_id)) + '\n')
    f.write("cuda device info is : " + str(torch.cuda.device(GPU_id)) + '\n')
    f.close()


print_cuda_Info()

