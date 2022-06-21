
## 2 projects house keeping example

Say I am working on 2 projects for which I have potentially - but not necessarily - separate input, output, job-scripts logs and errors files.

they are called :

- `MyProject_01`  
- `MyProject_02`  

to achieve a good structure you can run the `mkdir` command with the `-p` flag to make parent folders, like below.  
(the `-v` flag is not necessary but helpful for the beginners to show you the output of the whole list of folders created)  

`mkdir -pv $HOME/MyProject_0{1,2}/run_0{1,2}/{input/{database,models},jobScripts,output}`

this will make the following structure:

```
MyProject_01/
├── run_01
│   ├── input
│   │   ├── database
│   │   └── models
│   ├── jobScripts
│   └── output
└── run_02
    ├── input
    │   ├── database
    │   └── models
    ├── jobScripts    
    └── output



MyProject_02/
├── run_01
│   ├── input
│   │   ├── database
│   │   └── models
│   ├── jobScripts
│   └── output
└── run_02
    ├── input
    │   ├── database
    │   └── models
    ├── jobScripts
    └── output
```

you can now keep your project data and analysis separated per run and project.

example:  
Using project 1, I make 2 job-scripts to test my submissions but I only run/submit  `jobscript_1.1.pbs` with the command :

```
cd $HOME/MyProject_01/run_01/jobScripts
qsub jobscript_1.1.pbs
```
in this case my submission folder (i.e.`$HOME/MyProject_01/run_01/jobScripts` will become the variable: `$PBS_O_WORKDIR` to be referenced in jobs and job-scripts) --> [see CAVEATS \#2 , \#3]



```
  $HOME/MyProject_01/run_01/jobScripts/jobscript_1.1.pbs
  $HOME/MyProject_01/run_01/jobScripts/jobscript_1.2.pbs
  $HOME/MyProject_01/run_01/jobScripts/jobscript_1.1.pbs.eJOBID
  $HOME/MyProject_01/run_01/jobScripts/jobscript_1.1.pbs.oJOBID
```


The same goes for my test run 2: in the `run_02` folder, in this case I have submitted only `jobscript_2.2.pbs` and this has created its respective job-error and job-output log files.  

```
  $HOME/MyProject_01/run_02
  $HOME/MyProject_01/run_02/jobscript_2.1.pbs
  $HOME/MyProject_01/run_02/jobscript_2.2.pbs
  $HOME/MyProject_01/run_02/jobscript_2.2.pbs.eJOBID
  $HOME/MyProject_01/run_02/jobscript_2.2.pbs.oJOBID
```

forith this example you'll have:
```
cd $HOME/MyProject_01/run_02
qsub jobscript_2.2.pbs
```

  (and `$PBS_O_WORKDIR` now is equivalent to the new path:  `$HOME/MyProject_01/run_02/`)

---
### CAVEATS:

1.
- descend too much in folders hierarchy (especially if you are using long names) can break things. and normally is not convenient nor advised.
+ keep the names short, simple, abbreviate if possible and DO NOT use special characters, empty spaces etc. (this is a bad habbit of Windows/MacOS users)
-- I know, 2022 systems should be user-friendly compatible and UTF bla bla... but still things will break!

2. "File/folder not found" Error
you must pay careful attention to the PATHs of your files and folders; whenever using variables, binaries inside jobscripts etc..

the errors:
"File/folder not found" most likely indicates you have mis-referenced the path to your files and care must be taken to double-check this.

3. job-script output/error logs

as you can see in the example above, my first run has produced job output and error log files  `*.oJOBID` and `*.eJOBID`

this is controlled automatically!  

if you have in your job-script the directive `#PBS -j oe`   (or   `#PBS -j eo`) this instruction will override the automatic behaviour and combine job-output and job-error log files in 1 single file.)  
