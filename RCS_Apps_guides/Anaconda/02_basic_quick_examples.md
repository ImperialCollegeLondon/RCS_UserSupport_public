######  Basic Quick Examples:

Requirements:
- Access to HPC services
- module anaconda3/personal must be loaded in your current shell environment  

---

1. install *app_01* (already available from _default anaconda3 channel(s)_(a)) into a new Virtual Environment called _ENV01_ :  

`conda create -n ENV01 app_01`  

2. install *app_02* and its dependencies "dependency_A", "dependency_B" etc.. into a new Virtual Environment called _ENV02_ :  

`conda create -n ENV02 app_02 dependency_A dependency_B`  

--- 

**NOTE :**   
We always advise users to keep at a minimum the number of packages/dependencies installed in each Virtual Environment, to avoid future conflicts in packages installation/resolution.  

The reason behind this is that you want to keep as much separated as possible each Virtual Environment for each package/App you install as these may need different (sometimes even conflicting?!) libraries and dependencies.


3. install *app_03* and its dependencies "dependency_C" .. into a new Virtual Environment called _ENV03_ , pulling packages from _conda-forge_ channel :

`conda create -n ENV03 app_03 dependency_C -c conda-forge`  


---

**PLEASE REMEMBER :**  

If you install multiple different Apps all in the same "base" environment (**NOT ADVISED!**)
all their dependencies- will end up in the same installation causing conflicts and issues.
If not now, surely in the future your environment will NOT be able to "resolve" dependencies anymore and it WILL BREAK and FAIL!

This is due to:
 - the way anaconda3 works by isolating apps  
 - the overall complexity that your base Env has reached due to multiple Apps installation.  


 ---

