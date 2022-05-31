

### Common issues: files with mixed ownership/permissions etc.

If you notice files with mixed ownership in your folders, this could be for various reasons that range from bad practices of account/passwords sharing to more technical issues.

Most of the times this is due to the fact that you may have used (or you may still be using) some tools/lab-equipment etc.   
to create these files and/or some non-conventional method "which may be NOT fully synched and updated with your account/profile".  

This may be due also to some "stale/cached information" on the systems you are working on (most likely the credentials of "your mountings" etc.)  

before proceeding further by creating even more files with mixed ownership, please try the following:   

**Troubleshooting procedure :**

NOTE:  
[ALT] steps may need to be performed in reverse order depending on your systems..

- [ALT] try to enumerate the systems/tools/lab-equipment where you are still logged in and, wherever/whenever possible, try to **log-out** from these tools/software/etc..

- [ALT] make sure to unmount all previously mounted instances of the RDS/staorage/HPC folders from any device.

- restart the device if possible (especially if it's based on MS Windows OS)

- finally remount the mounted paths to sync back your newly acquired/updated credentials. (guides are provided)


Unfortunately, We cannot guarantee that if you keep your current setup on various systems/lab-equipment etc. without unmounting the storage first, and then trying remounting it -- to sync ownership/permissions -- you will not be ending up again in the same exact position of recreating files with the wrong/mixed user/group ownership.


on Linux based systems we can always back-up and diff these discrepancies by cross-referencing your data ACLs;

Ask an HPC admins for assistance if you need this task to be performed for you.


