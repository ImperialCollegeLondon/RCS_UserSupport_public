## Storing large volumes of data

The Research Data Store (RDS) is a service intended for the storage of large volumes of data.

For more information, options, costing and availability.
Please refer to the [RDS IC_webpage link](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/rds/)

All values quoted are expressed in FEC rates, that can be [costed via WorkTribe](https://www.imperial.ac.uk/research-and-innovation/research-office/preparing-and-costing-a-proposal/costing-and-pricing/costing/).  

Normally, whether our system is suitable for your purpose or what option is the best to choose from, may depend on the following:  

- Type and nature of data. (e.g. is there any personal or sensitive data ?)  
- access patterns (does the data need to be regularly accessed ?)  

A few other links to some more information and documentation to consider:  

please refer to the following pages for more info regarding **RDS** and how to use **RDS archiving facilities** for long time data **cold-storage** solution :  
(with everything that cold-storage/Archiving options entail e.g. data being read-only, slow access from tape system retrieval etc.. )

- [Archiving Data](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/rds/archiving-data-in-the-rds/)  
- [Comparing RDS to other Storage options](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/rds/comparing-rds-to-other-storage-options/)  

NOTEs:
- Archiving is a **read-only**, **sporadic access**, **cold-storage solution** (i.e. only rarely accessed, no fast IO-ops etc.).  
- If data is needed after the end of the project we may need to re-assess the scope of the request and re-quote.  

---

## Files/data transfers

When it comes to file transfers, we normally advise Users to try one (or more) of the following options and solutions currently available :

1 - using another system/tool from their workstation/laptop (e.g. by installing: Putty, WinSCP, FileZilla etc.)
you can follow these [ICT user guides](https://www.imperial.ac.uk/computing/csg/guides/file-storage/scp/)
and check [tool-chain user experience chart]((/RCS_UserSupport_public/RCS-HPC_guides/assets/images/hpc_tools.PNG)

(please note that we are not affiliated with and we do neither prefer nor endorse any of the 3rd party tools mentioned here and above.)

2 - accessing the HPC facilities using another protocol (such as [SCP](https://www.imperial.ac.uk/computing/csg/guides/file-storage/scp/)/SFTP etc..)  


3 - [locally mounting RDS](/RCS_UserSupport_public/RDS_FSmounting) on your system (laptop, lab computer etc.) the remote file-system of the HPC, in this case your RDS project folders will be presented as a network-mapped drive.  


4 - using the [Globus - client software](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/rds/globus/)  


Please bear in mind that in any case, for all options above a valid connection to IC-network must be established first:
either via IC-VPN or by using a computer physically located on campus.

Please refer to all the following guides if needed:

[Remote access](https://www.imperial.ac.uk/computing/csg/guides/remote-access/)    

[VPN-networks](https://www.imperial.ac.uk/admin-services/ict/self-service/connect-communicate/remote-access/virtual-private-network-vpn/)  

[Accessing RDS Project Allocations](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/rds/)  

---

**NOTES :**

- if you are planning to transfer a lot of files or doing big-files transfers that could take hours to complete,
I strongly suggest you to look into using either option 4 or option 2/3 above but with a terminal emulator/multiplexer running (e.g. GNU screen, Tmux for Linux/MacOs) to be able to detach from the terminals that you are performing the transfers from, thus allowing you to have the transfer window in the background.

- furthermore, if you are planning to execute these transfers from the HPC-service login nodes, please remember that these are shared resources and a very high level of I/O could cause system freezes or downtime for the whole Research community using the service.
Extreme caution must be exercised when doing these types of transfers from the login nodes or whenever using SFTP/RSYNC etc.


**IMPORTANT :**
> Planning these operations in advance and notifying the RCS Team before the execution, is normally considered a very good practice.
