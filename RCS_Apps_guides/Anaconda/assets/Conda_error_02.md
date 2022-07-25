
### Anaconda version warning

trying to run a new VEnv creation

`conda create -n netcdf4`

returns the warning below:
```
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.10.3
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /rds/general/user/bbattist/home/anaconda3/envs/netcdf4



Proceed ([y]/n)? n

CondaSystemExit: Exiting.

```

Resolution:

it is safe to **press [n] here** to NOT update the base environment at this stage.

please note that if you have multiple older conda versions Venvs they may break with updates and a "porting-older-Venvs-to-newer-versions-strategy" must be implemented.

Alternatively, if you have only "testing environments" and nothing critical that you could potentially be corrupted with the update, go on and update the base installation by pressing [y].