## Workflow examples


1. New Starter Workflow :

- First time running Anaconda or
- running Anaconda after a "System Reset" of the Anaconda installation  

If This is the first time running anaconda, or after you had purged/reset your anaconda setup/installation.  
(for example: because you installed wrong packages in the base environment or you've been asked to run `rm -rf ~/anaconda3` to purge the installation)

- login to HPC Services

- load anaconda module personal installation :

`module load anaconda3/personal`

- run anaconda setup, and follow the on-screen instructions :

`anaconda-setup`



---

2. checking Applications availability in Anaconda Channels :

check if an App named *Plink* or *Plink2* is available on the Anaconda channels for installation.

- browse to https://anaconda.org/search and enter your search query.  

- select the Application you are interested in

example 1 :
 _bioconda/plink 1.90b6.21_ clicking on the link, browse to: https://anaconda.org/bioconda/plink
inspect but DO NOT RUN the detailed command on how to run this installation:
`conda install -c bioconda plink`


example 2 :
_bioconda/plink2 2.00a2.3_ clicking on the link, browse to: https://anaconda.org/bioconda/plink2
inspect but DO NOT RUN the detailed command on how to run this installation:
`conda install -c bioconda plink2`

**NOTE :**   
these are 2 different software versions from 2 different channels.
Blindly running the above "install commands" will effectively install the respective App in the currently selected Virtual Environment (which normally is the base one! you do NOT want to do this!)

---

3. Creating your "Application-specific" virtual environment :

- login to HPC Services  

- load anaconda module personal installation :  

`module load anaconda3/personal`

- Create a conda-named (-n RenvTest1) virtual environment installing *app_01* in it - pulling it from the default channels(a) :

`conda create -n RenvTest1 app_01`  

- list all your available environments:  

`conda env list`  

- Start working in the newly created Environment with *app_01* installed:
start/activate your named virtual environment:

`conda activate RenvTest1` or if this errors  

`source activate RenvTest1`  

- now for HPC extended workflows see file `04_HPC_extd_workflow.md`


---

**NOTES :**  

(a) pulling from default Anaconda channels means that your App is already available/bundled in Anaconda.
please check the online anaconda website for packages/bundles providing your application.
Refer to the `01_basic_info.md` file and links in `0X_references.md` for more info on channels etc..