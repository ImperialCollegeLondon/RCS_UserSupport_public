
**VERY IMPORTANT !**  

Please remember that :

**whenever remote drives are mounted locally**

- changing network  
- changing Wi-Fi HotSpot  
- disconnecting and reconnecting to the network  

may make your remote connection unstable, unusable or even make it fail (this may incur in data corruption or even data loss, if you have open files for instance).

For this and other reasons, we advise users to **always unmount the drives** when their workflow is finished and **remount them back** whenever they need them again.

Finally Please always make sure to

**unmount any remotely-mounted drive (HPC, RDS etc..) BEFORE changing your main IC account passwords!**

this will prevent accessibility issues and avoid any Microsoft account profile related  lockouts, due to cached passwords, expired credentials, stale connections etc.

---

### Mounting using the GUI/Graphical Desktop tools:

Please check the video


### Mounting with CLI/terminal commands:


###### Prerequisites  

YYYYY - IC HPC login username  
ZZZZZ - local OS username (retrievable with CLI command: `echo $USER`)


###### CLI commands  

**NOTEs :**

- you may need Super-user privileges on your local OS to perform some of the following commands:  

```
mkdir /media/rds 2>/dev/null  
mount -t cifs //rds.ic.ac.uk/rds/user/YYYYY -o vers=3.02,user=YYYYY,domain=ic.ac.uk,uid=ZZZZZ,file_mode=0700,dir_mode=0700 /media/rds  

```

if the mount command errors, try rerunning it with the `-v` and eventually open a support ticket quoting the received messages or errors.


