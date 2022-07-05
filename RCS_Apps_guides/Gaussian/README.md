
[WIP: 20220705]



## Main Software

[Gaussian](https://gaussian.com/gaussian16/) : SW that provides state-of-the-art capabilities for electronic structure modeling.   

[GaussView](https://gaussian.com/gaussview6/) : GUI-based SW (graphical User interface) used with Gaussian. Features :

- It aids in the creation of Gaussian input files
- enables the user to run Gaussian calculations from a graphical interface without the need for using a command line instruction,
- it helps in the interpretation of Gaussian output (e.g., you can use it to plot properties, animate vibrations, visualize computed spectra, etc.).  

## HPC Usage

Gaussian versions can be activated loading one of the module files listed below:

- check what HPC installed versions are available:  

  `module avail gaussian`

- load `g09-e01` OR `g16-a03` :  

  `module load gaussian/g09-e01`

**TIPS:**   
Gaussian 09 command line executuable is `g09`        
Gaussian 16 command line executuable is `g16`   


### Batch jobs

Users are encouraged to write their own **batch/jobs (AKA submission scripts)**.   

See the [basic example of batch submission script](/RCS_Apps_guides/Gaussian/0x01_basic.pbs)


This is submitted by running `qsub Gaussian-jobscript.pbs`  


See for ref. [Running Gaussian](https://gaussian.com/running/)    


## Gaussian Utility Programs

[List of ALL Utility Programs](http://gaussian.com/utils/)  

---

#### File Checkpointing Utilities

[formchk](https://gaussian.com/formchk/) : converts the data in a Gaussian checkpoint file into formatted forms that are suitable for input into a variety of visualization software.

[unfchk](http://gaussian.com/unfchk) :  Convert a formatted checkpoint file back to its binary form (e.g., after moving it from a different type of computer system).  

[freqchk](http://gaussian.com/freqchk) : Prints frequency and thermochemistry data from a checkpoint file. Alternate isotopes, temperature, pressure and scale factor can be specified for the thermochemistry analysis.  

[chkchk](http://gaussian.com/chkchk) : Displays the route and title sections from a checkpoint file.  

[c8616](http://gaussian.com/c8616) : Converts checkpoint files from previous program versions to Gaussian 16 format.  

[Other info on checkpoint](http://www.ccl.net/cca/documents/dyoung/topics-orig/checkpoint.html)  

---

### Refs / LINKS

[Gaussian Online Support and Documentation](https://gaussian.com/techsupport/)  

[HPC wiki Gaussian](https://hpc-wiki.info/hpc/Gaussian)  


