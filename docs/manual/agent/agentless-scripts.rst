
.. _manual-agentless-scripts:

.. contents::

Writing Agentless Scripts
=========================

All scripts that work with OSSEC agentless security monitoring use stdout 
for communication and reporting to the OSSEC server. This makes writing scripts 
for OSSEC simple as you do not need to do anything more then print or echo to 
stdout. The format of the output does need to meet the OSSEC specification, 
but that is a very simple thing to do.

Agentless Script Types 
----------------------

Before we move to the specification details I need to explain that OSSEC agentless 
runs to different types of scripts. Namely the following:

- **periodic_diff**

  - Scripts output data to the OSSEC agentless process that will then be compared 
    to past runs and if there are differences an OSSEC alert will be generated.

- **periodic** 

  - Scripts output controlled messages to the OSSEC agentless process that 
    will then be processed accordingly.

Periodic diff Specification 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Agentless Script: ssh_integrity_check_linux 
-------------------------------------------

Now that we have an understanding of how agentless scripts communicate with the parent 
OSSEC process, let’s move on to a working example. The OSSEC supplied script 
``ssh_integrity_check_linux`` is a great place to start, so lets open it up and see 
what is going on.

.. code-block:: console
    
    obsd46# cat /var/ossec/agentless/ssh_integrity_check_linux
     #!/usr/bin/env expect

     # @(#) $Id: ssh_integrity_check_linux,v 1.11 2009/06/24 17:06:21 dcid Exp $
     # Agentless monitoring
     #
     # Copyright (C) 2009 Trend Micro Inc.
     # All rights reserved.
     #
     # This program is a free software; you can redistribute it
     # and/or modify it under the terms of the GNU General Public
     # License (version 3) as published by the FSF - Free Software
     # Foundation.


     # Main script.
    source "agentless/main.exp"


     # SSHing to the box and passing the directories to check.
    if [catch {
        spawn ssh $hostname
    } loc_error] {
        send_user "ERROR: Opening connection: $loc_error.\n"
        exit 1;
    }


    source $sshsrc
    source $susrc

    set timeout 600
    send "echo \"INFO: Starting.\"; for i in `find $args 2>/dev/null`;do tail \$i >/dev/null 2>&1 && 
    md5=`md5sum \$i | cut -d \" \" -f 1` && sha1=`sha1sum \$i | cut -d \" \" -f
     1` && echo FWD: `stat --printf \"%s:%a:%u:%g\" \$i`:\$md5:\$sha1 \$i; done; exit\r"
    send "exit\r"

    expect {
        timeout {
            send_user "ERROR: Timeout while running commands on host: $hostname .\n"
            exit 1;
        }
        eof {
            send_user "\nINFO: Finished.\n"
            exit 0;
        }
    }

    exit 0;


The comments in the script hints to what is going on, but everything up to and 
including set timeout 600 is related to setting up the expect functions and code 
for handling the ssh subprocess and connecting to the remote host. I am not going 
to spend any time with this section, I am just going to make use of it.

The meat of what is getting processed on the remote end all happens in two lines.

.. code-block:: sh 

    send "echo \"INFO: Starting.\"; for i in `find $args 2>/dev/null`;do tail \$i >/dev/null 2>&1 && 
    md5=`md5sum \$i | cut -d \" \" -f 1` && sha1=`sha1sum \$i | cut -d \" \" -f
     1` && echo FWD: `stat --printf \"%s:%a:%u:%g\" \$i`:\$md5:\$sha1 \$i; done; exit\r"

Let's break this down to see what is happening.

The send command pushes the following string to the ssh subprocess which gets run on 
the remote end of the connection. Before the script is sent to the remote host expect internally 
processes the string. This includes searching for variables and removing any control characters.

The control characters are first taken into account, and in the case of our example all escaped 
special characters are processed. \", \r, and \$ would be replaced with ", “carriage return“, 
and & respectively. The reason the escape characters are needed so that they will not 
interfere with expects own string processing and control. We will need to handle control 
characters in this way when we begin writing our own script.
    
While special characters were being handled by expect it also looked for variables to 
replace, in this case it will find $args and replace it with what ever arguments were 
passed to the script by the OSSEC agentless process. If we specified the following in 
``/var/ossec/etc/ossec.conf`` the $args variable would be replaced with ``/bin /etc /sbin``.

.. code-block:: xml

     <agentless>
         <type>ssh_integrity_check_linux</type>
         <frequency>3600</frequency>
         <host>root@172.17.20.20</host>
         <state>periodic</state>
         <arguments>/bin /etc /sbin</arguments>
     </agentless>

Back to the commands that get run. Once expect has completed replacement we are 
left with this command.

.. code-block:: sh

    echo "INFO: Starting."; for i in `find /bin /etc /sbin 2>/dev/null`;do tail $i >/dev/null 2>&1 && 
    md5=`md5sum $i | cut -d " " -f 1` && sha1=`sha1sum $i | cut -d " " -f
     1` && echo FWD: `stat --printf "%s:%a:%u:%g" $i`:$md5:$sha1 $i; done; exit
        exit


This script then goes and uses the Unix find command to locate all files in 
the specified path (from the arguments passed) and generates an OSSEC FWD: command 
for each one and prints it to stdout. Making use of the commands stat, md5sum, and 
sha1sum to generate the data needed. Here is an example of the output checking.

.. code-block:: console 

    spawn ssh root@172.17.20.20
    Last login: Wed Nov  4 11:32:51 2009 from 172.17.20.131^M
    [linux26 ~]# 
    INFO: Started.
    echo "INFO: Starting."; for i in `find {/bin /etc /sbin} 2>/dev/null`;do tail $i >/dev/null 2>&1 && 
    md5=`md5sum $i | cut -d " " -f 1` && sha1=`sh a1sum $i | cut -d " " -f
     1` && echo FWD: `stat --printf "%s:%a:%u:%g" $i`:$md5:$sha1 $i; done; exit
    INFO: Starting.
    FWD: 833:644:0:0:4148adea745af5121963f6b731b60013:60877a6f6981b16c0d53d32bcd3f07d41cfb5bd4 /etc/modprobe.d/
    glib2.sh
    [...........SNIP............]
    FWD: 1696:644:0:0:c2bd306b205ad9e81fb02ce6b225d384:5244d65815cb228a4fac7bc4c1c7774508fb7505 /etc/nsswitch.conf
    FWD: 85179:644:0:0:8db574225cd1068b47e77ceccd96f8ff:b5ef6183b35ee9d1b66ed2cefe98003c5bd99192 /etc/sensors.conf
    FWD: 49:644:0:0:52c3df2f1edf30ca3db82174be3a68d2:1934648f2429b70b1f729d343a6956fb0ea73136 /etc/php.d/imap.ini
    FWD: 873:644:0:0:04559d1fe27ecd079b69df8b319f937e:e5cab1bf1f9e4bc4386309f4e00a9b7be3e543a2 /etc/php.d/memcache.ini
    FWD: 59:644:0:0:94636ba6c4bac9d8d49d9de1a513ae0c:41d5164a2c6e332e40edf55c59a2d0df8a260964 /etc/php.d/pdo_mysql.ini
    FWD: 49:644:0:0:917dbbafbfaaa20f660063d627123dae:0e829d4ffc69f58dc258510b4b8452412e31ccc5 /etc/php.d/json.ini
    FWD: 0:644:0:0:d41d8cd98f00b204e9800998ecf8427e:da39a3ee5e6b4b0d3255bfef95601890afd80709 /etc/wvdial.conf
    logout
    Connection to 172.17.20.20 closed.

    INFO: Finished.

Modifying to make own Agentless Script: ssh_dmz_linux
----------------------------------------------------

Using the built in OSSEC agentless scripts are great, but sometimes we need more 
focused scanning and checking. So let’s modify the ssh_integrity_check_linux 
for our environment.

The goals for this new script will be to watch for changes to files based 
on the following criteria:

- All setuid and setgid files
- All files related to authentication (including .htaccess and ssh files)
- All application specific files (apache, ssh)

**Finding all setuid and setgid files**

Let’s first start by identifying a method to locate all files with their 
setuid or setgid bits enabled. To do this we will ssh to the host 172.17.20.20 
and use find to locate the files.

.. code-block:: xml

    obsd46# sudo -u ossec ssh root@172.17.20.20
    [linux26 ~]# find / -type f \( -perm -4000 -o -perm -2000 \) 
    /sbin/umount.nfs
    /sbin/netreport
    /sbin/unix_chkpwd
    /sbin/mount.nfs
    /sbin/pam_timestamp_check
    /sbin/mount.nfs4
    /sbin/umount.nfs4
    /bin/ping6
    /bin/su
    /bin/umount
    /bin/ping
    /bin/mount
    /lib/dbus-1/dbus-daemon-launch-helper
    /usr/libexec/openssh/ssh-keysign
    /usr/libexec/utempter/utempter
    /usr/sbin/usernetctl
    /usr/sbin/postqueue
    /usr/sbin/userhelper
    /usr/sbin/userisdnctl
    /usr/sbin/postdrop
    /usr/sbin/suexec
    /usr/bin/chsh
    /usr/bin/chfn
    /usr/bin/sudo
    /usr/bin/locate
    /usr/bin/wall
    /usr/bin/sudoedit
    /usr/bin/gpasswd
    /usr/bin/lockfile
    /usr/bin/newgrp
    /usr/bin/write
    /usr/bin/screen
    /usr/bin/passwd
    /usr/bin/chage
    /usr/bin/sperl5.8.8
    /usr/bin/crontab
    /usr/bin/ssh-agent

**Finding all files related to authentication and applications specific files**

Finding all files with setuid and setgid was simple, but finding all files related to 
authentication is more involved. This of course will vary from system to system, but 
this should be good starting point.


.. code-block:: console 

    obsd46# sudo -u ossec ssh root@172.17.20.20
    [linux26 ~]# find / \( -name ".ssh" -o -name "ssh" -o -name "sshd" -o -name "httpd" -o -name ".htaccess" 
    -o -name "pam.d" \) -exec find {} \;
    /var/www/html/admin/modules/framework/var/www/html/admin/modules/.htaccess
    /etc/httpd
    /etc/httpd/conf
    /etc/httpd/conf.d
    /etc/httpd/conf.d/php.conf
    /etc/httpd/conf.d/proxy_ajp.conf
    /etc/httpd/conf.d/README
    /etc/httpd/conf.d/ssl.conf
    /etc/httpd/conf.d/welcome.conf
    /etc/httpd/conf/httpd.conf
    /etc/httpd/conf/magic
    /etc/httpd/logs
    /etc/httpd/modules
    /etc/httpd/run
    /etc/logrotate.d/httpd
    /etc/pam.d
    /etc/pam.d/authconfig
    [...................SNIP PAM Files.....................]
    /etc/pam.d/system-config-network-cmd
    /etc/pam.d/vsftpd
    /etc/rc.d/init.d/httpd
    /etc/rc.d/init.d/sshd
    /etc/ssh
    /etc/ssh/ssh_config
    /etc/ssh/sshd_config
    /etc/ssh/ssh_host_dsa_key
    /etc/ssh/ssh_host_dsa_key.pub
    /etc/ssh/ssh_host_key
    /etc/ssh/ssh_host_key.pub
    /etc/ssh/ssh_host_rsa_key
    /etc/ssh/ssh_host_rsa_key.pub
    /etc/sysconfig/httpd
    /root/.ssh
    /root/.ssh/authorized_keys
    /usr/bin/ssh
    /usr/lib/httpd
    /usr/lib/httpd/modules
    /usr/lib/httpd/modules/libphp5.so
    [...................SNIP Apache modules................]

    /usr/lib/httpd/modules/mod_vhost_alias.so
    /usr/sbin/httpd
    /usr/sbin/sshd
    /usr/src/tbm-pbxconfig-5.5.1/amp_conf/htdocs/admin/modules/framework/htdocs/admin/modules/.htaccess
    /usr/src/tbm-pbxconfig-5.5.1/amp_conf/htdocs/admin/modules/.htaccess
    /var/empty/sshd
    /var/empty/sshd/etc
    /var/empty/sshd/etc/localtime
    /var/www/html/admin/modules/framework/var/www/html/admin/modules/.htaccess
    /var/www/html/admin/modules/.htaccess

**Merging finds**

Now we have two basic find methods that identify the files we want to monitor for 
changes, but our finds were a little greedy so we should create a way to strip out 
unwanted files from the list. As this is a unix system egrep is the king for finding 
or removing items from a list. To simplify things we can use egrep with the -v 
command line argument which tells egrep NOT to print any matching items.

Just to make sure that we do not end up double processing files we can make use 
of the sort command with -u argument to remove any duplicates.

Here is how we would put together both finds, egrep, and sort to locate and 
filter what is needed.

.. code-block:: console 

    ( find / -type f \( -perm -4000 -o -perm -2000 \) && \find / \( -name ".ssh" -o -name "ssh" -o -name "sshd" 
    -o -name "httpd" -o -name ".htaccess" -o -name "pam.d" \) -exec find {} \; ) 2>/dev/null | egrep 
    -v "known_hosts|moduli|var\/log|var\/lock" | sort -u

The above command we have found all files and paths that we would like to monitor, 
but this still needs to be integrated into a script on the OSSEC server.

**Creating ssh_dmz_linux**

We don’t want to make changes to ssh_integrity_check_linux directly so we will need 
to make a copy.

.. code-block:: console

    obsd46# (cd /var/ossec/agentless && cp ssh_integrity_check_linux ssh_dmz_linux) 

Integrating our new command line into the script we must pay close attention to 
special characters that expect will process. Due to this we will need to escape 
all / and " by proceeding them with \. Once we are done escaping we just insert 
our new line in place of find $args 2>/dev/null in our new file.

Here is what the completed script will look like.

.. code-block:: console 

    obsd56# cat /var/ossec/agentless/ssh_dmz_linux
     #!/usr/bin/env expect

     # @(#) $Id: ssh_integrity_check_linux,v 1.11 2009/06/24 17:06:21 dcid Exp $
     # Agentless monitoring
     #
     # Copyright (C) 2009 Trend Micro Inc.
     # All rights reserved.
     # 
     # This program is a free software; you can redistribute it
     # and/or modify it under the terms of the GNU General Public
     # License (version 3) as published by the FSF - Free Software
     # Foundation.


     # Main script.
    source "agentless/main.exp"


     # SSHing to the box and passing the directories to check.
    if [catch {
        spawn ssh $hostname
    } loc_error] {
        send_user "ERROR: Opening connection: $loc_error.\n"
        exit 1;
    }


    source $sshsrc
    source $susrc

    set timeout 600
    send "echo \"INFO: Starting.\"; for i in `(find / \\( -name \".ssh\" -o -name \"ssh\" -o -name \"sshd\" 
    -o -name \"httpd\" -o -name \".htaccess\" -o -name \"pam.d\" \\) -exec find {} \\; && find / -type f 
    \\( -perm -4000 -o -perm -2000 \\); ) 2>/dev/null | egrep -v \"known_hosts|moduli|var\\/log|var\\/lock\" | sort -u`;
    do tail \$i >/dev/null 2>&1 && md5=`md5sum \$i | cut -d \" \" -f 1` && sha1=`sha1sum \$i | cut -d \" \" 
    -f 1` && echo FWD: `stat --printf \"%s:%a:%u:%g\" \$i`:\$md5:\$sha1 \$i; done; exit\r"
    send "exit\r"

    expect {
        timeout {
            send_user "ERROR: Timeout while running commands on host: $hostname .\n"
            exit 1;
        }
        eof {
            send_user "\nINFO: Finished.\n"
            exit 0;
        }
    }

    exit 0;

**Testing** 

Before we add this new script to OSSEC configuration we need to test it. 

.. code-block:: console 

    obsd46# (cd /var/ossec && sudo -u ossec ./agentless/ssh_dmz_linux root@172.17.20.20 )

    ERROR: ssh_integrity_check <hostname> <arguments>


Due to not making use of the of the $arg variable in the way that ssh_integrity_check_linux 
wants use too, this caused this the problem above. Solving this problem would require 
making changes to files that will effect other built in scripts. So a quick solution is 
to just pass anything as an argument to the script. This will have no effect on our 
script as we do not make use of the $arg variable.

.. code-block:: console 

    obsd46# (cd /var/ossec && sudo -u ossec ./agentless/ssh_dmz_linux root@172.17.20.20 NOTUSED)
    spawn ssh root@172.17.20.20
    Last login: Wed Nov  4 13:46:32 2009 from 172.17.20.131^M
    [linux26 ~]#  
    INFO: Started.
    echo "INFO: Starting."; for i in `(find / \( -name ".ssh" -o -name "ssh" -o -name "sshd" -o -name "httpd" 
    -o -name ".htaccess" -o -name "pam.d" \)  -exec find {} \; && find / -type f \( -perm -4000 -o -perm -2000 
    \); ) 2>/dev/null | egrep -v "known_hosts|moduli|var\/log|var\/lock"`;do tail $i >/dev/null 2>&1 &&
     md5=`md5s ^Mum $i | cut -d " " -f 1` && sha1=`sha1sum $i | cut -d " " -f 1` && echo FWD: `stat --printf 
    "%s:%a:%u:%g" $i`:$md5:$sha1 $i; done; exit
    INFO: Starting.
    FWD: 14:775:100:101:3bc0a3e92f8170084dd102eda9a474b1:25a1783a3c6bdd9745ec245ec1bfa0414ee05d23 /var/www/html/admin/modules/.htaccessmodules/.htaccess
    FWD: 3519:644:0:0:e4ca381035a34b7a852184cc0dd89baa:6e43d0b5a46ed5ba78da5c7e9dcf319b27d769e7 /var/empty/sshd/etc/localtime
    FWD: 560:644:0:0:58370830ecfa056421ad21aff9c18905:d115bb5aeefaab97c53fbbd5df84ebcb9170d796 /etc/httpd/conf.d/php.conf
    [...................SNIP.............................]
    FWD: 392:644:0:0:e92bea7e9d70a9ecdc61edd7c0a2f59a:d77b61dac010c60589b4d8a2039e3b8a5bed18b2 /etc/httpd/conf.d/README
    FWD: 70888:4711:0:0:9046bd13339e7ef22266067b633e601a:3fc41029ddb14fe4ed613f479fa9e89c944f04dd /usr/bin/sperl5.8.8
    FWD: 315416:6755:0:0:4c63a9709fb7f0f97c30aa29d204859c:c379efa658de72866b8f6de5767906ff78d127b0 /usr/bin/crontab
    FWD: 88964:2755:0:99:baf3ebef6377d6ef42858776c33621b0:62394bf57d18c3fd49adeb39a1da61661cabc3c8 /usr/bin/ssh-agent
    logout
    Connection to 172.17.20.20 closed.

    INFO: Finished.




