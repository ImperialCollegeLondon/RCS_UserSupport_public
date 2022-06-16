
# Deleting jobs

If in doubt please consult the manual pages of the command you are trying to run, by using these [TIPS](/RCS-HPC_guides/coding/Nix-manPages.md)

in this case `man qdel`.

---

The 2 available commands to delete jobs in PBS are highlighted below, these may be tried in order of appearance.

`qdel JOBID`  
this will **schedule** a job deletion for jobs that have not yet started the provisioning phase.  

`qdel -W force JOBID`  
this will **forcibly delete** ANY job even if it has started the provisioning phase or the host has become unreachable for any reason.


Please bear in mind that both the Systems and the Scheduler, although they may have already acknowledged your job deletion command and request, they may be busy on other tasks and operations and had **scheduled your deletion request** to be handled later on or completed as soon as they become back available.  


---

**TOP TIPs :**  

- please consider using always the forced deletion command `qdel -W force JOBID` to prevent edge cases of slow job deletion.

- having a bit of patience and checking back later on the fulfilled deletion request, sometimes it helps (rather than assuming the `qdel JOBID` command is not working).  

