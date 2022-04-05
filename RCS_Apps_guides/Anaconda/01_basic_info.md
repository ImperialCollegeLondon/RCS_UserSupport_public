######  Basic info :

The following is the current "good practice guide" that we normally advise users to follow when working with anaconda on the HPC Systems :

- follow our RCS guides to install anaconda3/personal
(main link: https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/applications/conda/ )  

- this installation will create a "base" anaconda3 environment - we normally advise to keep this base environment clean and intact, as per default installation.  

- each time you need a new App installation, please create a new Virtual Environment (wherein you will be installing the Newly requested Application).



###### Channels info :

When it comes to installing software and dependencies one must take care of researching online the best sources/channels for the packages needed and what versions are compatible.
Normally the default channels work fine unless advised differently by the RCS Team.

`conda-forge` and `bioconda` are the most used channels normally, but again, care must be take by the users, understanding their software needs, selecting the correct sources/channels and
whenever possible, please consider installing different SW in different virtual environments, in order to keep the software and their dependencies isolated and not all blended together into the basic/default Base environment, created at setup/installation.

To check the currently loaded/configured channels in the current setup run :

`conda config --show channels`

(example output:)

channels:
  - defaults
  - bioconda
  - conda-forge
  - imperial-college-research-computing

you can add new channels with the command:

`conda config --add channels <new_channel_name>`

you can read more about channels and the packages they provide in `0X_references.md`.



