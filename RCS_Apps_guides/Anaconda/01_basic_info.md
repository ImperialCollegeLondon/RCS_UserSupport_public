##  Basic info :

The following is the current "good practice guide" that we normally advise users to follow when working with anaconda on the HPC Systems :

- follow our RCS guides to install `anaconda3/personal` :
[IC RCS webpage link](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/applications/conda/)  

<!-- NDR: need to adde refs/info to future updates and versions!!! -->

- the installation step will create a **"Base" anaconda3 environment** - we normally advise to keep this base environment clean and intact, as per default installation.  

- each time you need a new App installation, please create a new Virtual Environment (wherein you will be installing the Newly requested Application);

**IMPORTANT NOTE :**  
Please absolutely avoid the urge of _modifying_ or _installing anything else_ into this **Base environment** created for you.   

Doing so, could (and it will in the medium/long run..) lead to SW dependency/library clashes and code/version issues that are practically irreversible and unfixable.  
Your anaconda installation will need at this point to be purged and re-initiated, possibly breaking all your previously built environments too.



### Channels info :

When it comes to installing software and dependencies one must take care of researching online the best sources/channels for the packages needed and what versions are compatible.  
Normally the default channels work fine unless advised differently by the RCS Team.

`conda-forge` and `bioconda` are the most used channels normally.

Care must be take by the users when selecting these, understanding their software needs, and what are the correct sources/channels and
whenever possible, please consider installing different SW in different virtual environments, in order to keep the software and their dependencies isolated.

Please do **NOT blend together the basic/default "Base" environment** (created at setup/installation) and any of the new software you want to install.

- **Check currently configured channels** in the current setup :

  `conda config --show channels`

  > example output:
```
channels:
  - defaults
  - bioconda
  - conda-forge
  - imperial-college-research-computing
```

- **Add new channels** :

  `conda config --add channels <new_channel_name>`


- **Search online for known package availability** on anaconda.org :

  (e.g. querying for vtk)  https://anaconda.org/search?q=vtk    
  
  (e.g. querying for tensorflow)  https://anaconda.org/search?q=tensorflow    

You can read more about channels and the packages they provide in [References](/RCS_Apps_guides/Anaconda/0X_references.md)



