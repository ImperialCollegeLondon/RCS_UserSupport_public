
## Fortran Standards

- Fortran IV (1966)  
- Fortran 77 (old but popular version)  
- Fortran 90 (major revision to F77)  
- Fortran 95 (minor revision to F90)  
- Fortran 2003 (current standard)  
- Fortran 2008 (the next standard)   



## Release main features

- **Fortran 90**
  - major revision to Fortran
  - free format source code (convenient on modern computers)
    - up to 132 columns (<90 for readability)
  - introduced major new features (intrinsic array and functions, subroutines..)
  - dynamic memory allocation




- **Fortran 77**
  - complete sub-set of Fortran
  - fixed format source code (convenient on fixed-width punched cards)
  - only 6 chars variable names



## Notes on Compilers

Some behaviour is _"compiler-dependent"_  and not specified in standard (e.g.)

- Flags  
- Values of un-initialised variables  
- Warnings  

Resources:

https://fortranwiki.org/fortran/show/Compilers  

https://llvm.org/  


**compilers/mpi wrappers variables to use/set** :  
(defined also by the compiler modules)

```
FC=gfortran
MPIF90=mpif90
```

### Example coding guidelines

[XMM-Newton SSC (XMM-Newton Survey Science Centre) Science Analysis Software (SAS)](https://xmmssc-www.star.le.ac.uk/SAS/) --> [SAS Coding guidelines](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html)


- [Fortran-90 coding](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html#Fortran-90%20coding)  
- [Fortran-90 headers](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html#Fortran-90%20headers)  
- [C++ coding](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html#C++%20coding)  
- [C++ headers](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html#C++%20headers)  
- [Scripts](https://xmmssc-www.star.le.ac.uk/SAS/xmmsas_20121219_1645/doc/devel/coding.html#scripts)  

([OLD link](http://xmm.esa.int/sas/7.1.0/doc/devel/coding.html) for ref only -- not working )


http://www.cgd.ucar.edu/cms/ccm4/codingstandard.shtml  

[TUDELFT coding standard](https://web.archive.org/web/20081204031331/http://vlm089.citg.tudelft.nl/swan/online_doc/swanpgr/node2.html)    -- [Start here](https://web.archive.org/web/20081202133944/http://vlm089.citg.tudelft.nl/swan/online_doc/swanpgr/node1.html)  






---


##### Refs:

http://www.astro.ex.ac.uk/people/saunders/computing_tutorials/fortran.pdf