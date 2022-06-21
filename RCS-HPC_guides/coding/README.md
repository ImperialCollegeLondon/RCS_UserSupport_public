
# HOW TO: code on the HPC

if you want to avoid issues with :

- loss of code and data  
- the desperate need to restore files (etc..)  

the following list of simple RULES and HINTS is for you.

1. **rule number one :** simply put  
PLEASE **DON'T CODE ON THE HPC SERVICE !**  

  **reason :** the HPC is a complex set of intertwined Systems (Compute, Storage and networks); as such many things could go wrong on many different levels and subsystems, and impact your code and workflows, jeopardize your analysis and results etc.

  Data losses occur when :
  - the FS locks-up and it is not responsive
  - the Systems are overloaded - you will notice slow downs in your terminal etc.. -  
  - the network is congested or expeeriencing issues  


  all the above are very difficult to troubleshoot and revert from, and despite being able to provide a limited amount of data recovery and snapshotting features,
  you should not blindly rely on these features, but clearly understand and assess the risks that **"directly coding on the HPC"** poses in light of what's been exposed above.  

  **alternative :** you should be coding on your local workstation and then synch over the files when the code is ready/mature to be tested/run on the HPC.  

  This is especially valid if your code/sw is getting more than 10 lines long and complex.

2. **pay attention to Microsoft Windows-OS editors "shenanigans"** :  
when using this OS and its custom editing tools, please remember that "weird" control characters may be introduced in your scripts (this is - simply put - due to "different OSs paradigms which are not fully cross-compatible") so you may want to sanitize your code.

  **reason :**  MS windows control codes and line terminators, will most likely break your scripts on Linux based OS, such as the ones we run on the HPC.  
  (e.g. removing `^M` characters and similar; please note on this topic, that some characters may be hidden to the users)

  **alternative :** for short pieces of code and scripts (e.g. HPC job-scripts) coding directly on a Linux OS based system may help.
  also checking your script with the linux editors `vi` or `vim` may help spotting these characters.  

  See on this topic: [tricks on vi/vim editor](/RCS-HPC_guides/coding/vim_tricks_01.md)  

3. if you - for whatever reason - can not avoid at all costs to "code on the HPC" we always advise users to use `git` to **keep code source-controlled** and commit changes very often.
(`git`  should be always available on the HPC  
  you can check this from a terminal with:  
  `$ which git`   
  otherwise, you can always import it as a "module" by running  
  ```
  $ module load git
  $ which git
  ```

Please note that **GIT is NOT GITHUB* !** ;    
you do not need to subscribe to online cloud Microsoft based services (such as github) to be able to source control locally your code; neither you need to publish it online on that named platform; all you need is a .gitconfig in your repo and some basic instructions to get you started with source controlled software.

gitHub in fact is a totally different tool (a 3rd party Microsoft cloud service) for a different scope and it is not needed for your scope.


