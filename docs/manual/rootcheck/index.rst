
.. _manual-rootcheck:

Rootcheck 
=========

OSSEC HIDS will perform rootkit detection on every system where the agent is 
installed. The rootcheck (rootkit detection engine) will be executed every X minutes 
(user specified - by default every 2 hours) to detect any possible rootkit installed. 
Used with the log analysis and the integrity checking engine, it will become a very 
powerful monitoring solution.

Checks that rootcheck preforms 
------------------------------

#. Read the rootkit_files.txt which contains a big database of rootkits and files 
   used by them. It will try to stats, fopen and opendir each specified file. We 
   use all these system calls because some kernel-level rootkits hide files 
   from some system calls. The more system calls we try, the better the detection. 
   This method is more like an anti-virus rule that needs to be updated constantly. 
   The chances of false-positives are small, but false negatives can be produced 
   by modifying the rootkits.
#. Read the rootkit_trojans.txt which contains a database of signatures of files 
   trojaned by rootkits. This technique of modifying binaries with trojaned versions 
   was commonly used by most of the popular rootkits available. This detection 
   method will not find any kernel level rootkit or any unknown rootkit.
#. Scan the /dev directory looking for anomalies. The /dev should only have device 
   files and the Makedev script. A lot of rootkits use the /dev to hide files. 
   This technique can detect even non-public rootkits.
#. Scan the whole filesystem looking for unusual files and permission problems. Files 
   owned by root, with write permission to others are very dangerous, and the rootkit 
   detection will look for them. Suid files, hidden directories and files will also be 
   inspected.
#. Look for the presence of hidden processes. We use getsid() and kill() to check if 
   any pid is being used or not. If the pid is being used, but "ps" can't see it, it 
   is the indication of kernel-level rootkit or a trojaned version of "ps". We also 
   verify that the output of kill and getsid are the same.
#. Look for the presence of hidden ports. We use bind() to check every tcp and udp port 
   on the system. If we can't bind to the port (it's being used), but netstat does not 
   show it, we probably have a rootkit installed
#. Scan all interfaces on the system and look for the ones with "promisc" mode enabled. 
   If the interface is in promiscuous mode, the output of "ifconfig" should show that. 
   If not, we probably have a rootkit installed.

Configuration options
---------------------

All these configurations options can be specified in each agent ossec.conf file, except 
for the ``auto_ignore`` and ``alert_new_file`` which are manager side options. The 
``ignore`` option if specified on the manager becomes global for all agents.


.. include:: ../../syntax/ossec_config.rootcheck.trst 

