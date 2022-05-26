[preliminary draft]

### MAIN ISSUES SEEN SO FAR

1. due to the current system setup and how jobs are spawned you can't run both "user beloved GUIs", concurrently :

- jupyterhub  
- OOD/Rstudio  

if you do so, they will clash and behave unexpectedly.

> TOP-TIP: PLEASE either use one Service or the other.

if/when updates are made these will be communicated to the users by the Team via the wiki pages.

2. there may be some **time constraints and limitations** to your spawned sessions. (i.e. they cannot be left running/idling forever or they will hang and/or possibly behave unexpectedly)   
(time constraints are normally mentioned at spawn-time, and they "will be converted into equivalent walltime" for the underlying jobs that power your calculations on the HPC "behind the scenes of the GUI".)

> TOP-TIP: PLEASE be careful not to exceed this "usage time";  
 you may incur in random errors and issues.



### THINGS THAT HELP

- run WebApps in browsers' incognito-mode windows

  this will make sure to "isolate" your log-in session for the time you need it and clear all cookies and cached Client data/settings once you're done

- always **use the correct log-out" procedure

  whenever possible search for the "LOGOUT" button or "EXIT" button of the WebApp ;
  sometimes if the button is not present or visible,
  hitting the https://Name-of-The-Service-I-Am-using/logout  can help logging you out, - provided that page/endpoint is setup correctly - otherwise you will see an error (most likely 404 Errors)  

...



### REPORTED USER ISSUES

This is an experimental service and provided "as it is".

Due to its complex architecture and nature, users have reported multiple instances of errors and various issues that we have not been fully able to address nor timely support.

These could be related to:  

- the underlying HPC hardware (known issues);   
(e.g. distributed FileSystem lock-ups and slowness or unavailability; unplanned outages; network bottlenecks etc..)

- the underlying HPC configuration (known issues):
(jobs and queues, service over-subscription, etc..)

- the Application itself - both
    - server-side (setup/config, it's proxying features and complex stack, the WebApp nature of the GUI-based tools etc..) and
    - client-side (cookies, browser compatibility, caching, not "exiting the portal" etc.)

- User dependent factors
(startup files misconfiguration/"bloatedness", input/output files, paths used etc.)




### SELF-TROUBLESHOOTING - SITUATION:1

Some users' issues reported:


`'RStudio initialisation error: status code 502 returned by RStudio server when executing 'client_init'.`


possible solution proposed by STeam member:

[IC-VPN|campus Netowkr] --> login to HPC:

once at the Server prompt, run the following commands to clean possible stale files:


```
rm -rf $HOME/.local/share/rstudio/persistent-state
rm -rf $HOME/.local/share/rstudio/client-state
rm -rf $HOME/.local/share/rstudio/sessions/active/*
rm -rf $HOME/.local/share/rstudio/profiles-cache
```




### SELF-TROUBLESHOOTING - SITUATION:2

if you experience the following situation:

- unable to log in to RStudio using OpenOnDemand.
- job could be alreayd started
- connecting to RStudio yields ERROR MESSAGE: `"Error: Temporary server error, please try again"` with a sign-in page.
- signing in at this point could return an: `incorrect username or password error.`

this is most likely due to a "backend connectivity issue" between OOD Server and the HPC infrastructure.

how to resolve:

- check the [ IC_VPN | Campus Network ] --> [HPC Service status page](https://selfservice.rcs.imperial.ac.uk/service-status)

  for the following keywords / issues mentions either

  - queues
  - authentication
  - downtime
  - or File-System issues (most importantly)


  these have been seen to be most likely the culprits for the issues with
  OOD Service Portal.

- PLEASE kindly bear with us as there may be some underlying issue with the infrastructure;

- checking back at a later time could help;

- eventually if nothing improves kindly raise a ticket following the [procedure](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/support/help/) for

  > _"For support relating to jobs, problems with submission scripts, applications, and issues with HPC software in general:"_

  quoting:  **OOD/RStudio issues**

  in the first line and/or in the title/short description.




