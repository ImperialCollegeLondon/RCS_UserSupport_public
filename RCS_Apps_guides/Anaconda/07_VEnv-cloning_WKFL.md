#### workflow example for cloning/backing-up/restoring a conda VENV


1. list current envs:  

`conda env list`  
returns:
```
env1_TEST
env2_PROD
```
2. making a clone of `env2_PROD` and checking :  

`conda create --name env2_PROD_bkp1 --clone env2_PROD`

`conda env list`  
returns:
```
env1_TEST
env2_PROD
env2_PROD_bkp1
```

Now while operating on `env2_PROD` for some reaons this gets corrupted and I need to roll-back - provided that the backup/clone `env2_PROD_bkp1` has not been tampered with - I can now "revert/roll back" by doing:

`conda create --name env2_PROD_restored --clone env2_PROD_bkp1`

and optionally also delete the corrupted VEnv:

`conda env remove -n env2_PROD`

and checking :


`conda env list`  
returns:
```
env1_TEST
env2_PROD_bkp1
env2_PROD_restored
```