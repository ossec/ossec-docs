
.. _manual-agentless-scripts:

Agentless Scripts
=================

All scripts that work with OSSEC agentless security monitoring use stdout 
for communication and reporting to the OSSEC server. This makes writing scripts 
for OSSEC simple as you do not need to do anything more then print or echo to 
stdout. The format of the output does need to meet the OSSEC specification, 
but that is a very simple thing to do.

Before we move to the specification details I need to explain that OSSEC agentless 
runs to different types of scripts. Namely the following:

- **periodic_diff**

  - Scripts output data to the OSSEC agentless process that will then be compared 
    to past runs and if there are differences an OSSEC alert will be generated.

- **periodic** 

  - Scripts output controlled messages to the OSSEC agentless process that 
    will then be processed accordingly.

Periodic diff Specification 
---------------------------

The output for periodic_diff is very simple, any and all output after the agentless 
command :samp:`STORE: now` and before the next OSSEC Command will be stored and compared 
for differences. This type of script is mostly used for hardware devices such as 
Cisco IOS, Juniper JunOS, and other products.

Scripts that use the periodic_diff make use of the following commands:

- **INFO:**

  - The string following INFO will be logged to /var/ossec/logs/ossec.log by OSSEC for debugging. 

- **ERROR:** 

  - Error needs to be reported. The string following this command is forwarded to the 
    OSSEC manager, and the OSSEC process closes down the script.

- **STORE:** 

  - All the lines that follows this command will be added stored and compared to 
    previous runs of the script

Here is an example of a periodic_diff script that comes with OSSEC. (Please note 
with all agentless scripts you must be in the root of the OSSEC install for them 
to function correctly.)

.. code-block:: console 

    obsd46#( cd /var/ossec && ./agentless/ssh_pixconfig_diff cisco@172.17.0.1 'show hardware' )
    spawn ssh -c des cisco@172.17.0.1
    No valid ciphers for protocol version 2 given, using defaults.
    Password: 

    a.zfw.tss>INFO: Starting.
    enable
    Password: 
    a.zfw.tss#ok on enable pass

    STORE: now
    no pager
                 ^
    % Invalid input detected at '^' marker.

    a.zfw.tss#term len 0
    a.zfw.tss#terminal pager 0
                         ^
    % Invalid input detected at '^' marker.

    a.zfw.tss#show version | grep -v Configuration last| up
                             ^
    % Invalid input detected at '^' marker.

    a.zfw.tss#show running-config
    Building configuration...


    Current configuration : 14631 bytes
    !
    version 12.4

    [................SNIP CONFIG.................]

    a.zfw.tss#show hardware
    Cisco IOS Software, 3800 Software (C3845-ADVENTERPRISEK9-M), Version 12.4(24)T1, RELEASE SOFTWARE (fc3)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2009 by Cisco Systems, Inc.
    Compiled Fri 19-Jun-09 19:21 by prod_rel_team

    ROM: System Bootstrap, Version 12.3(11r)T2, RELEASE SOFTWARE (fc1)

    a.zfw.tss uptime is 1 week, 5 days, 7 hours, 29 minutes
    System returned to ROM by reload at 13:34:26 UTC Thu Oct 22 2009
    System image file is "flash:c3845-adventerprisek9-mz.124-24.T1.bin"


    This product contains cryptographic features and is subject to United
    States and local country laws governing import, export, transfer and
    use. Delivery of Cisco cryptographic products does not imply
    third-party authority to import, export, distribute or use encryption.
    Importers, exporters, distributors and users are responsible for
    compliance with U.S. and local country laws. By using this product you
    agree to comply with applicable laws and regulations. If you are unable
    to comply with U.S. and local laws, return this product immediately.

    A summary of U.S. laws governing Cisco cryptographic products may be found at:
    http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

    If you require further assistance please contact us by sending email to
    export@cisco.com.

    Cisco 3845 (revision 1.0) with 1007615K/40960K bytes of memory.
    Processor board ID FTX1043A2CR
    2 Gigabit Ethernet interfaces
    1 ATM interface
    1 Virtual Private Network (VPN) Module
    4 CEM T1/E1 ports
    DRAM configuration is 64 bits wide with parity enabled.
    479K bytes of NVRAM.
    492015K bytes of USB Flash usbflash0 (Read/Write)
    62720K bytes of ATA System CompactFlash (Read/Write)

    Configuration register is 0x2102


    a.zfw.tss#exit
    Connection to 172.17.0.1 closed by remote host.
    Connection to 172.17.0.1 closed.

    INFO: Finished.


In this example above the script would store the contents between :samp:`STORE: now` 
and :samp:`INFO: Finished.`. If this is the first time that OSSEC agentless has run 
this command no alerts would be generated and the contents would have been saved for 
later comparisons. If OSSEC agentless has a stored copy from a previous execution it 
will compare the files and if there are any differences it will generate an alert.

Periodic Specification 
----------------------

The periodic specification has more options and gives more control to the script 
writer on what actions OSSEC will take. Once again stdout is used for communication 
so script writing is easy.

- **INFO:** 

  - The string following INFO will be logged to /var/ossec/logs/ossec.log by OSSEC for 
    debugging.

- **ERROR:**

  - Error needs to be reported. The string following this command is forwarded to the 
    OSSEC manager, and the OSSEC process closes down the script.

- **FWD:**

  - The string following FWD is a colon delimited list of stats on a given file.

- **LOG:** 

  - The string following LOG: will be passed into ossec-analysisd and processed like 
    all other log messages.
    
Example of real FWD: command.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console 

    FWD: 19419:600:0:0:fb30de5b02029950ae05885a3d407c8c:017cd6118cdc166ee8eba8af1b7fdad6763203d3 ./.bash_history 

The Fields break down in to the following:

- FWD:

  -  The OSSEC Command

- 19419 

  - Total size of file, in bytes 

- 600 

  - Access rights of file in octal

- 0 

  - User ID of file owner

- 0 

  - Group ID of file owner 

- fb30de5b02029950ae05885a3d407c8c 

  - MD5 Hash of file 

- 017cd6118cdc166ee8eba8af1b7fdad6763203d3 

  - SHA1 Hash of file 

- ./.bash_history 

  - Path and name of file


Using this format OSSEC can store the information about a file and then in the future run 
compare that they are the same. If for some reason they are not the same an alert will be 
generated. Here is an example of a password change on a linux system: ::

    OSSEC HIDS Notification.
    2009 Sep 21 15:19:00

    Received From: (ssh_integrity_check_linux) root@172.17.20.20->syscheck
    Rule: 550 fired (level 7) -> "Integrity checksum changed."
    Portion of the log(s):

    Integrity checksum changed for: '/etc/shadow'
    Old md5sum was: '0d92e12c92f3edcf9d8876ea57c5f677'
    New md5sum is : '2bd51b61dea17c5682fb2c0cf4f92c63'
    Old sha1sum was: '2270c03a920ef8dd50e11cefdef046a8660f7a29'
    New sha1sum is : 'd9518ea9022b10d07f81925c6d7f2abb4364b548'
     
    --END OF NOTIFICATION

