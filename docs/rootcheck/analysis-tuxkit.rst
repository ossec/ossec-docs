
.. _analysis-tuxkit:

Analysis of a rootkit: Tuxkit
===============================

By: spoonfork (spoonfork@hackinthebox.org) 


Introduction 
------------

The following is an analysis of the Tuxkit rootkit, written by a Dutch group called Tuxtendo. This rootkit was found in one of the honeypots that we set up. The honeypot was a stock installation of Redhat 7.0, with a few services running. None of the software, such as named, sendmail and the printer daemon were patched. 

There are three versions of the rootkit that are available on Tuxtendo's website. They are tuxkit.tgz, tuxkit-1.0.tgz, and tuxkit-short.tgz. Both tuxkit.tgz and tuxkit-1.0.tgz have the same contents, while tuxkit-short.tgz contains less tools. 

I've also tested some of tuxkit's binaries on Redhat 7.1, and they seemed to work fine. 

The following are the contents of each tuxkit. This analysis will focus on tuxkit-1.0.tgz, the one that was found on our honeypot. The rootkit was developed by Argv[], possibly modified from and based on the t0rn rootkit. The timestamp of the rootkit was December 2001. Googling for "tuxkit analysis" did not produce any hits, so I guess that this rootkit is pretty new. 

NOTE: chkrootkit failed to detect tuxkit. 


Packages
--------

Listing::

.. code-block:: console

    [root@angel tuxkit-1.0]# ls -l ../tuxkit  (tuxkit.tgz)
    total 2600
    -rw-------    1 sfork   sfork     502884 Dec  5 07:55 bin.tgz
    -rw-------    1 sfork   sfork        406 Dec  5 07:55 cfg.tgz
    -rw-------    1 sfork   sfork      16213 Dec  5 07:55 lib.tgz
    -rw-------    1 sfork   sfork       3684 Dec  5 07:55 README
    -rw-------    1 sfork   sfork     461892 Jan  6 00:06 sshd.tgz
    -rw-------    1 sfork   sfork    1644819 Dec  5 07:55 tools.tgz
    -rwx------    1 sfork   sfork       9489 Jan  6 00:53 tuxkit

    [root@angel tuxkit-1.0]# ls -l ../tuxkit-1.0  (tuxkit-1.0.tgz)
    total 2600
    -rw-------    1 sfork   sfork     502884 Dec  5 07:55 bin.tgz
    -rw-------    1 sfork   sfork        406 Dec  5 07:55 cfg.tgz
    -rw-------    1 sfork   sfork      16213 Dec  5 07:55 lib.tgz
    -rw-------    1 sfork   sfork       3684 Dec  5 07:55 README
    -rw-------    1 sfork   sfork     461892 Jan  6 00:06 sshd.tgz
    -rw-------    1 sfork   sfork    1644819 Dec  5 07:55 tools.tgz
    -rwx------    1 sfork   sfork       9489 Jan  6 00:53 tuxkit

    [root@angel tuxkit-1.0]# ls -l ../tuxkit-short  (tuxkit-1.0-short.tgz)
    total 1556
    -rw-------    1 1001     1001       502884 Dec  5 07:55 bin.tgz
    -rw-------    1 1001     1001          406 Dec  5 07:55 cfg.tgz
    -rw-------    1 1001     1001        16213 Dec  5 07:55 lib.tgz
    -rw-------    1 1001     1001         3684 Dec  5 07:55 README
    -rw-------    1 1001     1001       461892 Jan  6 00:06 sshd.tgz
    -rw-------    1 1001     1001       577089 Jan  6 01:12 tools.tgz
    -rwx------    1 1001     1001         9489 Jan  6 00:53 tuxkit

tuxkit-1.0.tgz 
--------------

There are six files in the tuxkit which includes a README, an installation
script, and four tarred/zipped files.

The following are the contents of the individual files in the tuxkit.

- bin.tgz 

    - contains precompiled trojan binaries

- cfg.tgz 

    - contains tuxkit's configuration files

- lib.tgz 

    - contains libproc libraries, for process hiding purposes
- sshd.tgz 

    - contains precompiled sshd, complete with sshd_config
- tools.tgz 
    - contains an arsenal of tools (duh!) for the skrip kiddie
      who don't know how to get their own tools. The tools are::

        [root@angel tools]# ls -la
        total 44
        drwxr-xr-x   11 root     root         4096 Mar  1 13:14 .
        drwxr-xr-x    4 root     root         4096 Mar  1 13:14 ..
        drwx------    2 root     root         4096 Nov 12 20:50 bitchx
        drwx------    2 root     root         4096 Dec 12 23:59 dos
        drwx------    2 root     root         4096 Nov 12 20:57 mirkforce
        drwx------    2 root     root         4096 Nov 12 20:57 nmapv
        drwx------    8 root     root         4096 Nov 12 23:05 psybnc
        drwx------    2 root     root         4096 Nov 13 01:00 sniffer
        drwx------    2 root     root         4096 Nov 12 20:58 ssh
        drwx------    2 root     root         4096 Nov 12 23:22 synscan
        drwx------    2 root     root         4096 Nov 12 20:58 utils

     The names of these tools are self-explanatory. However, they are all
     precompiled. utils contains only one utility - wget. This is to 
     enable the skripkids to easily download other tools (assuming the skripkids
     know how to use wget).

- tuxkit 

    - an installation script

- README 
  
    - the obligatory README file (and greetz, of course)

The tuxkit is almost similar to the t0rn rootkit. The addition of the 
precompiled tools such as nmap, synscan and psybnc makes it a more handy 
rootkit. It is flawlessly easy to install. Tuxkit is like a pack-n-go 
kinda tool. The appendix shows the contents of each packages in tuxkit.

Installation
------------

Installation of tuxkit is very straightforward. The README says:

README::
    ./tuxkit   

             Password : This will be the password you need to login onto
                        the compromised system.
             SSD Port : This will be the port on which the SSHD will be
                        be listening on for incoming connections.
                        This port will be hidden automatically in netstat.
             bncport  : this will be the port psyBNC will listen on.
                        This port will be hidden automatically in netstat.

    The setup script does NOT have default settings, this forces you to
    provide a password, sshd and bnc ports.

    The setup script also contains a variable called EMAIL, you should edit
    this ;)


This sets tuxkit apart from t0rn - it does not use default ports. 

The default installation directory is /dev/tux. Shell script savvy skripkids
may want to change this to avoid detection.

NOTE: the tuxkit installationn script contains a variable EMAIL which has
the default value of the author. At the end of the installation, the script
will send an email which the subject "Tuxkit1.0". The e-mail contains 
information about the host, the SSH backdoor port, the psyBNC port, and
also the password. If you skripkid didn't change the EMAIL (the README
clearly states to change this), you have the risk of your server being
owned by other people.

Trojaning process
-----------------

The trojaning process is straightforward. syslogd is killed first. Then
all the files that came with tuxkit-1.0.tgz are untarred and upzipped.
The installation directory is created. The default installation directory
is /dev/tux, and even though this is kept as the variable RDIR, the tuxkit
install script hardcoded "mkdir /dev/tux", thus changing RDIR, but forgetting
to change the line above will cause your installation to skew a bit (most 
skripkids won't bother to do this anyway). In fact, /dev/tux is hardcoded 
almost everywhere in the installation script.

The hidden files .addr, .cron, .file, .log and .proc are copied to /dev/tux/

The library files are copied to lib, and /sbin/ldconfig is executed.

This step is followed by copying files to be trojaned to /dev/tux/backup, and
replacing these files with the trojaned version. A script "sz", which is part
of the bin.tgz is run against each trojaned binaries so that the size matches
that of the original binaries. "sz" basically pads the trojan with zeros
(from /dev/zero).

Backdooring process
-------------------

The backdoored SSH is installed in /usr/bin/xsf. The trojaned sshcheck is 
installed in /usr/bin/xchk. Both are invoked the following way::

	/usr/bin/xsf -q 1>/dev/null 2>/dev/null
	/usr/bin/xchk -q 1>/dev/null 2>/dev/null

The /etc/rc.d/rc.sysinit is also edited to include the following lines::

	echo "# Running Xsf ..." >> /etc/rc.d/rc.sysinit
 	echo "/usr/bin/xsf -q 1>/dev/null 2>/dev/null" >> /etc/rc.d/rc.sysinit
 	echo "# Running Xchk ..." >> /etc/rc.d/rc.sysinit
 	echo "/usr/bin/xchk 1>/dev/null 2>/dev/null" >> /etc/rc.d/rc.sysinit

If you string xsf, you will be able to get the passwords that the skripkid
used.

The tuxkit configuration files
------------------------------

The tuxkit config files follows that of the original Linux rootkit. There are
.addr, .cron, .file, .log and .proc. The filenames are self-explanatory. These
files follow the convention of the original Linux rootkit. In forensic, what
you will be interested in most is the .addr files, because it contains the
IP that netstat is supposed to hide.

Detecting tuxkit
----------------

Detecting tuxkit is fairly simple. 

# Look for the existence of /dev/tux
# Run lsof -i +M | grep xsf 

Hey, why wasn't lsof trojaned? t0rn has a trojaned lsof :)

Detecting tuxkit - trojans
--------------------------

.. code-block:: console

   #  md5sums - if you've keep an md5sum of the virgin state of your
      installation, detecting trojans should be a walk in the park. Every
      system administrator should use file integrity checker to monitor 
      critical file change.
   #  Look for /usr/bin/xsf and /usr/bin/xchk
   #  Look for extra lines in /etc/rc.sysinit
   #  cd /etc/ssh; ls -l. The trojaned ls will return nothing, when in 
      fact your ssh config files are still there.

The following are the size difference between tuxkit and Redhat 7.1 binaries.
(before installation)::

.. code-block:: console

    files        tuxkit        Redhat 7.1
    ------------------------------------------
    crontab      29052               21280
    df           27112               26812
    dir          42952               45948
    dmesg         3640                4252
    du           25592               25788
    find         55220               47516
    ifconfig     36356               51164
    killall      14400               12096
    locate        9144               25020 (symlink to slocate)
    login         3980               17740
    ls           42952               45948
    netstat      58228               83132
    ps           62748               63180
    pstree       14532               12284 
    sshcheck     89828               - (my test machine don't have this)
    sshdconfig  451260               - (my test machine don't have this)
    syslogd      28324               26972
    tcpd         18660               24844
    top          37844               34924
    updatedb      4394               25020 (symlink to slocate)
    vdir         42952               45948

This result is quite interesting. Trojans are not supposed to be bigger that
the original binaries!

Detecting tuxkit - if you are lucky
-----------------------------------

On our honeypot, the trojaned 'ps' still shows xsf, even though xsf was in
the list of processes to be hidden. However, 'ls' seems to work very well
in hiding files.

Recommendations
---------------

For tuxkit developers 

- Add trojaned lsof. Borrow one from t0rn :) Also, fix ps. 
- tools.tgz is probably not needed. A skripkid who is able to crack a Linux
  machine (duh) should be able to download and compile his/her own tools. 
  Furthermore, tools.tgz adds unnecessary extra bytes to the tuxkit - not
  really convenient for downloading.
- Add a self-deleting script, i.e. delete the tar files and installation
  directory after installation. skripkids seems incapable of doing this.
  The config files should be kept somewhere else other than /dev/tux.

For skripkidz - vi tuxkit, type the following::

     :%s//dev/tux/installation_dir_of_your_choice/g

where installation_dir_of_your_choice is, uh, the installation directory
of your choice. (However, this won't work, since /dev/tux/.{addr,proc}, etc
are already hardcoded to the binaries - so hehe, just run ./tuxkit and pray
that the stupid system administrators won't notice :)

For system administrators - run file integrity checker after each fresh
install.

Conclusion
----------

The world of forensic analysis ain't fun without rootkits.

Appendix - Contents of each packages
------------------------------------

Contents::

.. code-block:: console

    [root@angel tuxkit-1.0]# less bin.tgz 
    -rwx------ root/root     29052 2001-12-26 21:37:57 bin/crontab
    -rwx------ root/root     27112 2001-12-26 21:37:57 bin/df
    -rwx------ root/root     42952 2001-12-26 21:37:57 bin/dir
    -rwx------ root/root      3640 2001-12-26 21:37:57 bin/dmesg
    -rwx------ root/root     25592 2001-12-26 21:37:57 bin/du
    -rwx------ root/root     55220 2001-12-26 21:37:57 bin/find
    -rwx------ root/root     36356 2001-12-26 21:37:57 bin/ifconfig
    -rwx------ root/root     14400 2001-12-26 21:37:57 bin/killall
    -rwx------ root/root      9144 2001-12-26 21:37:57 bin/locate
    -rwx------ root/root      3980 2001-12-26 21:37:57 bin/login
    -rwx------ root/root     42952 2001-12-26 21:37:57 bin/ls
    -rwx------ root/root     58228 2001-12-26 21:37:57 bin/netstat
    -rwx------ root/root     62748 2001-12-26 21:37:57 bin/ps
    -rwx------ root/root     14532 2001-12-26 21:37:57 bin/pstree
    -rwx------ root/root     89828 2001-12-26 21:37:57 bin/sshcheck
    -rwx------ root/root    451260 2001-12-26 21:37:57 bin/sshdconfig
    -rwx------ root/root     28324 2001-12-26 21:37:57 bin/syslogd
    -rwx------ root/root      1522 2001-12-26 21:37:57 bin/sz
    -rwx------ root/root     18660 2001-12-26 21:37:57 bin/tcpd
    -rwx------ root/root     37844 2001-12-26 21:37:57 bin/top
    -rwx------ root/root      4394 2001-12-26 21:37:57 bin/updatedb
    -rwx------ root/root     42952 2001-12-26 21:37:57 bin/vdir

    [root@angel tuxkit-1.0]# less cfg.tgz 
    -rw------- root/root        17 2001-11-11 19:12:19 cfg/.addr
    -rw------- root/root        69 2001-11-12 23:06:32 cfg/.cron
    -rw------- root/root        67 2001-12-27 20:54:23 cfg/.file
    -rw------- root/root        13 2001-12-27 20:54:47 cfg/.log
    -rw------- root/root       116 2001-12-27 20:55:29 cfg/.proc

    [root@angel tuxkit-1.0]# less sshd.tgz
    -rw------- virus/virus     828 2001-12-13 00:22:12 ssh2/hostkey
    -rw------- virus/virus     697 2001-12-13 00:22:12 ssh2/hostkey.pub
    -rw------- virus/virus     503 2001-12-27 20:43:12 ssh2/logo
    -rw------- virus/virus     512 2001-12-13 23:51:33 ssh2/random_seed
    -rwx------ virus/virus 1040220 2002-01-06 00:05:58 ssh2/sshd
    -rw------- virus/virus     647 2001-12-27 22:42:20 ssh2/sshd2_config

    [root@angel tuxkit-1.0]# less lib.tgz 
    lrwxrwxrwx root/root         0 2001-11-11 02:49:02 lib/libproc.so -> libproc.so.
    2.0.7


 
