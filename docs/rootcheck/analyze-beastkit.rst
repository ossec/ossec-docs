
.. _analyze_beastkit:

Analysis of a rootkit: Beastkit 
===============================

by: unknown


Analysis of a rootkit found on a RedHat 7.2 System in 01/2002. The rootkit setup 
script includes the line "#Beastkit 7.0 - X-Org edition". Due to this fact, we 
call the rootkit "Beastkit 7.0" in this document. The compromise was done 
through an crc32 compensation attack against SSH-1.5-1.2.27. 

Detecting Beastkit
------------------

To ensure unmodified results of common programs (like ps) we used a mounted 
Stand-alone shell (sash) and static binaries. 

results of unmodified netstat shows following interesting connections: 

.. code-block:: console 

    Proto Recv-Q Send-Q Local Address           Foreign Address         State
    tcp        0      0 0.0.0.0:56493           0.0.0.0:*               LISTEN

    results of unmodified ps shows following interesting proceses: 
    USER       PID %CPU %MEM  SIZE   RSS TTY STAT START   TIME COMMAND
    root     17081  0.0  0.0  1880     4  ?  S   03:42   0:00 /usr/sbin/arobia -q -p 56493 
    root     17097  0.0  0.0  1528   160  ?  S   03:42   0:00 lpsched  /usr/local/bin/bin/..././
    root     17109  0.0  0.0  1524   156  ?  S   03:42   0:00 lpsched  /idrun
    root     17300  0.0  0.0  1528   160  ?  S   03:45   0:00 lpsched

    results of unmodified lsof (LiSt Open Files) shows following interesting open files: 
    COMMAND     PID    USER   FD   TYPE     DEVICE     SIZE       NODE NAME
    arobia    17081    root  cwd    DIR        3,2     1024          2 /
    arobia    17081    root  rtd    DIR        3,2     1024          2 /
    arobia    17081    root  txt    REG        3,5   206760     306925 /usr/sbin/arobia
    arobia    17081    root  mem    REG        3,2   485171      34370 /lib/ld-2.2.4.so
    arobia    17081    root  mem    REG        3,2   436784      34380 /lib/libnsl-2.2.4.so
    arobia    17081    root  mem    REG        3,2    85115      34282 /lib/libcrypt-2.2.4.so
    arobia    17081    root  mem    REG        3,2    47872      34327 /lib/libutil-2.2.4.so
    arobia    17081    root  mem    REG        3,2  5772268      60578 /lib/i686/libc-2.2.4.so
    arobia    17081    root    0u   CHR        1,3               22868 /dev/null
    arobia    17081    root    1u   CHR        1,3               22868 /dev/null
    arobia    17081    root    2u   CHR        1,3               22868 /dev/null
    arobia    17081    root    3u  IPv4     110686                 TCP *:56493 (LISTEN)*
    arobia    17081    root    5u  sock        0,0              110290 can't identify protocol
    idrun     17109    root  cwd    DIR        3,5        0     306921 /usr/man/.man10/bk7 (deleted)
    idrun     17109    root  rtd    DIR        3,2     1024          2 /
    idrun     17109    root  txt    REG        3,5    89828     306945 /usr/sbin/idrun
    idrun     17109    root  mem    REG        3,2   485171      34370 /lib/ld-2.2.4.so
    idrun     17109    root  mem    REG        3,2  5772268      60578 /lib/i686/libc-2.2.4.so
    idrun     17109    root  mem    REG        3,2   261460      34311 /lib/libnss_files-2.2.4.so
    idrun     17109    root    0u   raw                         263594 00000000:0001->00000000:0000 st=07
    idrun     17109    root    3u   raw                         111231 00000000:0001->00000000:0000 st=07
    idrun     17109    root    5u  sock        0,0              110290 can't identify protocol
    bktd      17097    root  cwd    DIR        3,5        0     306921 /usr/man/.man10/bk7 (deleted)
    bktd      17097    root  rtd    DIR        3,2     1024          2 /
    bktd      17097    root  txt    REG        3,5    93924     306924 /usr/local/bin/.../bktd
    bktd      17097    root  mem    REG        3,2   485171      34370 /lib/ld-2.2.4.so
    bktd      17097    root  mem    REG        3,2  5772268      60578 /lib/i686/libc-2.2.4.so
    bktd      17097    root  mem    REG        3,2   261460      34311 /lib/libnss_files-2.2.4.so
    bktd      17097    root    0u   raw                         263598 00000000:0001->00000000:0000 st=07
    bktd      17097    root    3u   raw                         110971 00000000:0001->00000000:0000 st=07
    bktd      17097    root    5u  sock        0,0              110290 can't identify protocol

Beastkit properties
-------------------


Beastkit 7.0 replaces common binaries that can be used to monitor system operation (like ps). 
List of programs included in the rootkit (bin.tgz)::

    md5sum                            Filename             Size
    98bf3bd30914773e50060a7f56eda4f4  encrypt             14808
    ae060f54e8f3a8e79dc95867171811ef  pg                   3552
    f2e3b130a937af92ff507315406589b1  sz                   1382
    0a07cf554c1a74ad974416f60916b78d  /bin/ls             39696
    195075782a2f7853731bf3e0c62e6925  /bin/netstat        54152
    ced323b51dc984f66c2695d8fd6a2368  /bin/ps             62920
    e4738d828b366ac21572e6a17f7ecba4  /sbin/ifconfig      31504
    753d5e7af271c12e0803956dd8c2b8e6  /sbin/syslogd       26496
    0a07cf554c1a74ad974416f60916b78d  /usr/bin/dir        39696
    98596eaad65b9f748fca2dcf48a9b3ef  /usr/bin/find       59536
    a1931a396d9a7ffbcd0c7612627073ba  /usr/bin/pstree     12340
    3fc77d2a3ae361c86ef4629c0f5e380e  /usr/bin/slocate    23560
    fd319aa8e6f56a32c0cb8fc6e9a69195  /usr/bin/top        33992
    f7acbc61f8715bdda41989683bc8e8a8  /usr/bin/md5sum     31452
    0c1411a47e58bcbef33abdaf53ede4e6  /usr/sbin/idrun     89828
    56b863dcfacadf6d66d859e2ee59517e  /usr/sbin/lsof      82628

The original programs got replaced by the rootkit. The timestamps doesn't 
change, because the rootkit use touch -acmr to transmit the timestamp to the 
rootkit files. 


Beastkit contains some tools (bktools) (placed at /lib/ldd.so/bktools)::

    md5sum                            Filename             Size
    b0812b62c9c3307161c5400870d7d230  bkget               25664
    926784667fa921b38fceb124644f6568  bkp                  7578
    63c6a53e779c06923344b15a0e8f1799  bks                 16070
    12e8748c19abe7a44e67196c22738e9b  bksb                 1345
    5dba380b431418f1d15a014472268b65  bkscan               9556
    d536271d4c13a2cf71c0e74d09839f27  bktd                90788
    2f6957ee2b2c29259225c6b0f271539b  patch                1875
    0bb5cb28717d1a36c2a871a1dd713666  prl                  1854
    e2384d85534272ba46baa6979cefc634  prw                  1831

    bkget - SynScan Daemon (by psychoid/tCl) 
    bkp - hdlp2 version 2.05 
    bks - Sniffer 
    bksb - "sauber"-Script (see duarawkz-rootkit), cleans up some of the intruders traces 
    bkscan - SynScan (by psychoid/tCl) 
    bktd 
    patch - SSHd-Patchscript (update to ssh-1.2.32 using ftp) 
    prl - SSHd-Patchscript (update to ssh-1.2.32 using http) 
    prw - SSHd-Patchscript (update to ssh-1.2.32) 


A SSHd backdoor named "arobia" was installed. The config files were 
found in /usr/lib/elm/arobia/. A new password for the backdoor was generated 
with the command ``sed s/08e7592e361de6fd59d4d126b29fe6ea/`md5sum --string=$1|awk '{print $1}'`/g elm\ > arobia``, 
which replaces the default password (08e7592e361de6fd59d4d126b29fe6ea=arobia) 
of the original backdoor "elm" and generates the new backdoor "arobia". 
After that, "arobia" was moved to /usr/sbin. The backdoor start-up is done 
by /usr/sbin/arobia -q -p 56493, whereby "56493" is the portnumber. ::

    md5sum                            Filename                              Size
    f7820a858bceee09246f4454e3c24e95  /usr/sbin/arobia                    206760
    f78fa4c346287a3af35656a9ac33e733  /usr/lib/elm/arobia/elm             206760
    a5d7227117841d0518a6be3510dabb57  /usr/lib/elm/arobia/elm/hk             529
    eb1929cdeb8c4abe428540a58adfa7a2  /usr/lib/elm/arobia/elm/hk.pub         333
    5fd2ce512e0eba4d090191e8a1518808  /usr/lib/elm/arobia/elm/sc             880
    563b9fb9877beb3b33428acdfba1a571  /usr/lib/elm/arobia/elm/sd.pp            6
    82ff57cdc95b9b01d88ef5dca721981d  /usr/lib/elm/arobia/elm/sdco           480
    a604bd841806dd5abe543a3281eb5a78  /usr/lib/elm/arobia/elm/srsd           512



More rootkit properties:
~~~~~~~~~~~~~~~~~~~~~~~~

The program bktd was placed at /usr/local/bin/.../, furthermore some libraries at /lib/::

    md5sum                            Filename                      Size
    00846ffcc2ed7fa23b42089e92273964  bktd                         93924
    2aed58986303584c96edd16f6195e797  /lib/libproc.a               33848
    8581544643145cd159e93df986539ce8  /lib/libproc.so.2.0.6        37984
    dcf6a1cb6fd162461195294904c078f8  /lib/lidps1.so                   9
    6efdfd44c0b1e197dae1b10e994f7721  /usr/include/file.h             56
    1791784f079870739ecc707add37aafe  /usr/include/hosts.h            19
    64bdd72e707ba4680cc7d7a58e8aac07  /usr/include/log.h              43
    1534580c14b3b70d29d000f3691d1c25  /usr/include/proc.h             47

The following lines were added in /etc/rc.d/rc.sysinit to start a backdoor at 
port 33333 at system startup: 

.. code-block:: console 

    # Arobia daemon startup..
    /usr/sbin/xntps -q -p 33333


