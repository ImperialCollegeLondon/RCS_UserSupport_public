
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

if the mount command errors, try rerunning it with the `-v`

