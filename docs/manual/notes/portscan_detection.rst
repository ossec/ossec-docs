Detecting portscans with OSSEC and iplog
----------------------------------------

iplog is a TCP/IP traffic logger. Currently, it is capable of logging TCP, UDP, and ICMP traffic. iplog is able to detect TCP port scans, TCP null scans, FIN scans, UDP and ICMP "smurf" attacks, bogus TCP flags, TCP SYN scans, TCP "Xmas" scans, ICMP ping floods, UDP scans, and IP fragment attacks. iplog is able to run in promiscuous mode and monitor traffic to all hosts on a network. iplog uses libpcap to read data from the network and can be ported to any system that supports pthreads and on which libpcap will function.

iplog.conf:
^^^^^^^^^^^

 The syslog, user, group and internal network configuration is not show (OS dependient)
 iplog can log in diferets ways depending of the configuration parameters (DNS resolv, log_dest, etc), the proposed decoders and rules 
 only work with the logs later described, this configuration file extract is functional with this requeriment, please read man iplog 
 and man iplog.conf 


#. Log the IP address as well as the hostname of packets. 

.. code-block:: console

  set log_ip true

#. Do not log the destination of packets (more presentable logs)

.. code-block:: console

  set log_dest false

#. Ignore DNS traffic from nameservers in /etc/resolv.conf.

.. code-block:: console

  set ignore_dns true

#. I dont want too many logs: ignore www, netbios, microsoft-ds loc-srv, 5900 tcp/port connections, not all the OS recognize the port alias, replace with de adecuate port number

.. code-block:: console

  ignore tcp dport 80

  ignore tcp dport netbios-ssn

  ignore tcp dport microsoft-ds

  ignore tcp dport loc-srv

  ignore tcp dport 5900


#. Port Scan Check

.. code-block:: console

  set portscan true

  set icmp true

  set frag true

  set smurf true

  set bogus true

  set fin_scan true

  set syn_scan true

  set udp_scan true

  set fool_nmap false

  set xmas_scan true

  set null_scan true

  set ping_flood true

  set traceroute true

iplog: Scan and attack responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect Scan and SYN scan
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  nmap -sT -PI -PT 10.10.160.2

iplog response:
^^^^^^^^^^^^^^^

.. code-block:: console

  Nov 14 18:09:08 TCP: domain connection attempt from 10.10.150.1:51239
  Nov 14 18:09:08 TCP: https connection attempt from 10.10.150.1:51240
  Nov 14 18:09:08 TCP: port 1723 connection attempt from 10.10.150.1:51241
  Nov 14 18:09:08 TCP: ftp connection attempt from 10.10.150.1:51242
  Nov 14 18:09:08 TCP: smtp connection attempt from 10.10.150.1:51243
  Nov 14 18:09:08 TCP: port 3389 connection attempt from 10.10.150.1:51244
  Nov 14 18:09:08 TCP: auth connection attempt from 10.10.150.1:51245
  Nov 14 18:09:08 TCP: port 636 connection attempt from 10.10.150.1:51246
  Nov 14 18:09:08 TCP: port 256 connection attempt from 10.10.150.1:51247
  Nov 14 18:09:08 TCP: port 554 connection attempt from 10.10.150.1:51248
  Nov 14 18:09:08 TCP: telnet connection attempt from 10.10.150.1:51249
  Nov 14 18:09:08 TCP: port 389 connection attempt from 10.10.150.1:51250
  Nov 14 18:09:08 TCP: ssh connection attempt from 10.10.150.1:51251
  Nov 14 18:09:08 TCP: port 486 connection attempt from 10.10.150.1:51253
  <font color="red">Nov 14 18:09:08 TCP: port scan detected [ports 53,443,1723,21,25,3389,113,636,256,554,...] from 10.10.150.1 [ports 51242,51243,...]</font>
  Nov 14 18:09:08 UDP: dgram to port 1 from 10.10.150.1:34324 (300 data bytes)
  <font color="red">Nov 14 18:09:12 TCP: SYN scan detected [ports 21,1] from 10.10.150.1 [ports 34333,34335,34325,34326,34327,...]</font>
  Nov 14 18:09:12 UDP: dgram to port 1 from 10.10.150.1:34324 (300 data bytes)
  Nov 14 18:10:02 last message repeated 1 times
  Nov 14 18:10:02 TCP: port scan mode expired for 10.10.150.1 - received a total of 1678 packets (47092 bytes).
  Nov 14 18:10:09 TCP: SYN scan mode expired for 10.10.150.1 - received a total of 24 packets (960 bytes).

FIN Stealth Scan:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  nmap -sF -p- -PI -PT 10.10.150.2

iplog response:
^^^^^^^^^^^^^^^

.. code-block:: console

  <font color="red">Nov 14 18:22:51 TCP: FIN scan detected [ports 3389,1723,256,113,22,389,554,443,21,23,...] from 10.10.150.1 [port 57876]</font>
  Nov 14 18:24:05 TCP: FIN scan mode expired for 10.10.150.1 - received a total of 65535 packets (1310700 bytes)

NULL Stealth Scan:
^^^^^^^^^^^^^^^^^^

.. code-block:: console

  nmap -sN -p- -PI -PT 10.10.150.2

iplog response:
^^^^^^^^^^^^^^^

.. code-block:: console

  <font color="red">Nov 14 18:26:58 TCP: null scan detected [ports 636,53,23,3389,1723,443,113,554,25,21,...] from 10.10.150.1 [port 35444]</font>
  Nov 14 18:28:14 TCP: null scan mode expired for 10.10.150.1 - received a total of 65534 packets (1310680 bytes)

Xmas Tree Stealth Scan:
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  nmap -sX -p- -PI -PT 10.10.150.2

iplog response:
^^^^^^^^^^^^^^^

.. code-block:: console

  <font color="red">Nov 14 18:30:30 TCP: Xmas scan detected [ports 636,256,554,389,1723,53,443,21,3389,22,...] from 10.10.150.1 [port 42399]</font>
  Nov 14 18:31:48 TCP: Xmas scan mode expired for 10.10.150.1 - received a total of 65532 packets (1310640 bytes).

UDP port scan:
^^^^^^^^^^^^^^

.. code-block:: console

  nmap -sU -p- -PI -PT 10.10.150.2

iplog response:
^^^^^^^^^^^^^^^

.. code-block:: console

  Nov 14 18:34:59 UDP: dgram to port 33161 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 41107 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 63571 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 48714 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 25271 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 13612 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 41094 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 52700 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 11482 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 62794 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 28270 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 27081 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 10866 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 63494 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 28686 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 44600 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 21771 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 53283 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 44436 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 46916 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 30519 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:34:59 UDP: dgram to port 8041 from 10.10.150.1:60362 (0 data bytes)
  Nov 14 18:35:00 UDP: dgram to port 8041 from 10.10.150.1:60363 (0 data bytes)
  Nov 14 18:35:00 UDP: dgram to port 30519 from 10.10.150.1:60363 (0 data bytes)
  <font color="red">Nov 14 18:35:00 UDP: scan/flood detected [ports 33161,41107,63571,48714,25271,...] from 10.10.150.1 [ports 60362]</font>
  Nov 14 18:39:15 UDP: scan/flood mode expired for 10.10.150.1 - received a total of 356 packets (2848 bytes).

traceroute:
^^^^^^^^^^^
.. code-block:: console

  traceroute 10.10.150.1

iplog response:
^^^^^^^^^^^^^^^

  <font color="red">Nov 14 18:57:18 UDP: traceroute from 10.10.150.2</font>

Flood ping attack:
^^^^^^^^^^^^^^^^^^

.. code-block:: console

  ping -f 10.10.150.2

iplog response:
^^^^^^^^^^^^^^^

  <font color="red">Nov 14 19:09:33 ICMP: ping flood detected from 10.10.150.1</font>
  Nov 14 19:11:29 ICMP: ping flood mode expired for 10.10.150.1 - received a total of 428 packets (8416000 bytes).

IP fragment attacks:
^^^^^^^^^^^^^^^^^^^^

TODO

UDP and ICMP "smurf" attacks:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Nov 18 19:12:30 ICMP/UDP: smurf attack detected from 201.223.41.0
  <font color="red">Nov 18 19:23:30 ICMP/UDP: smurf attack detected from 201.223.41.0</font>
  Nov 18 19:28:07 ICMP/UDP: smurf attack mode expired for 201.223.41.0 - received a total of 337 packets (21568 bytes).

Another interesting logs:
^^^^^^^^^^^^^^^^^^^^^^^^^

bogus TCP flags:
^^^^^^^^^^^^^^^^
.. code-block:: console

  <font color="red">Nov 14 15:57:56 TCP: Bogus TCP flags set by 10.10.160.2:60873 (dest port 25)</font>

OSSEC (HIDS) + iplog (sensor) implementation:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Work in progress
* TODO: improve regex, decoders and rules. p0f complementation?
* Configuration tested in FreeBSD 6.1 and archlinux gimmick
* Last modification 14/Nov/2006

iplog decoder:
^^^^^^^^^^^^^^

For this logs:
^^^^^^^^^^^^^^

  Nov 14 18:09:12 TCP: SYN scan detected [ports 21,1] from 10.10.150.1 [ports 34333,34335,34325,34326,34327,...]
  Nov 14 18:09:08 TCP: port scan detected [ports 53,443,1723,21,25,3389,113,636,256,554,...] from 10.10.150.1 [ports 51242,51243,...]
  Nov 14 18:22:51 TCP: FIN scan detected [ports 3389,1723,256,113,22,389,554,443,21,23,...] from 10.10.150.1 [port 57876]
  Nov 14 18:26:58 TCP: null scan detected [ports 636,53,23,3389,1723,443,113,554,25,21,...] from 10.10.150.1 [port 35444]
  Nov 14 18:30:30 TCP: Xmas scan detected [ports 636,256,554,389,1723,53,443,21,3389,22,...] from 10.10.150.1 [port 42399]

a working decoder is:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console


 <decoder name="iplog-scan">
  <prematch>\S+ scan detected</prematch>
  <regex offset="after_prematch">\S+ \S+ from (\S+)</regex>
  <order>srcip</order>
 </decoder>


For this log:
^^^^^^^^^^^^^

.. code-block:: console

  Nov 14 18:35:00 UDP: scan/flood detected [ports 33161,41107,63571,48714,25271,...] from 10.10.150.1 [ports 60362]

a proppossed decoder is (not tested):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

 <decoder name="iplog-flood">
  <prematch>scan/flood detected</prematch>
  <regex offset="after_prematch">\S+ \S+ from (\S+)</regex>
  <order>srcip</order>
 </decoder>

For this log:
^^^^^^^^^^^^^

.. code-block:: console

  Nov 14 19:09:33 ICMP: ping flood detected from 10.10.150.1

a proppossed decoder is (not tested):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

 <decoder name="iplog-pingflood">
  <prematch>ping flood detected from</prematch>
  <regex offset="after_prematch">(\S+)</regex>
  <order>srcip</order>
 </decoder>

For this log:
^^^^^^^^^^^^^

(necesary to include???????) i Think no (very paranoid)

.. code-block:: console

  Nov 14 18:57:18 UDP: traceroute from 10.10.150.2

a proppossed decoder is (not tested):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

 <decoder name="iplog-traceroute">
  <prematch>pingtraceroute from</prematch>
  <regex offset="after_prematch">(\S+)</regex>
  <order>srcip</order>
 </decoder>

 

For this log:
^^^^^^^^^^^^^

(necesary to include???????) i Think no (very paranoic)

.. code-block:: console

  Nov 14 15:57:56 TCP: Bogus TCP flags set by 10.10.160.2:60873 (dest port 25)

a proppossed decoder is (not tested):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 <decoder name="iplog-bogustcp">
  <prematch>Bogus TCP flags set by</prematch>
  <regex offset="after_prematch">(\S+):\d+</regex>
  <order>srcip</order>
 </decoder>

iplog rules:
^^^^^^^^^^^^

Only for working decoders:

.. code-block:: console

  cd /var/ossec/rules
  touch iplog_rules.xml
  chown root:ossec iplog_rules.xml
  chmod 550 iplog_rules.xml

in iplog_rules.xml include:

.. code-block:: console

 <group name="syslog,errors,">
  <rule id="99990" level="6">
    <decoded_as>iplog-scan</decoded_as>
    <description>iplog scan detect</description>
  </rule>
 </group>

ossec.conf'

.. code-block:: console

  cd /var/ossec/etc
  vi  ossec.conf

include in the correct place:

.. code-block:: console

  <include>iplog_rules.xml</include>

and

.. code-block:: console

  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/iplog</location>
  </localfile>

or wherever you put your iplog logs

start iplog

.. code-block:: console

 iplog -d 

restart ossec
.. code-block:: console

  /var/ossec/bin/ossec-control restart

test with nmap (see before)

OSSEC active-response:
^^^^^^^^^^^^^^^^^^^^^^

Firewall Drop: FreeBSD-IPFW:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add to your ipfw script the follow lines, if you are using the 00001 rule number disoccupying:

.. code-block:: console

  /sbin/ipfw add 00001 deny ip from table\(00002\) to any
  /sbin/ipfw add 00001 deny ip from any to table\(00002\)

Change  /var/ossec/active-response/bin/firewall-drop.sh to adjust to the red lines

.. code-block:: console

  #!/bin/sh
  # Adds an IP to the IPFW drop list.
  # Only works with IPFW.
  # We use TABLE 00001. If you use this table for anything else,
  # please change it here.
  # Expect: srcip
  # Author: Rafael Capovilla - under @ ( at ) underlinux.com.br
  # Author: Daniel B. Cid - dcid @ ( at ) ossec.net
  # Last modified: May 07, 2006
  UNAME=`uname`
  IPFW="/sbin/ipfw"
  ARG1=""
  ARG2=""
  ACTION=$1
  USER=$2
  IP=$3
  <font color="red">TABLE_ID=00002</font>
  LOCAL=`dirname $0`;
  cd $LOCAL
  cd ../
  PWD=`pwd`
  echo "`date` $0 $1 $2 $3" >> ${PWD}/ossec-hids-responses.log
  # Checking for an IP
  if [ "x${IP}" = "x" ]; then
    echo "$0: <action> <username> <ip>" 
    exit 1;
  fi
  #  Blocking IP
  if [ "x${ACTION}" != "xadd" -a "x${ACTION}" != "xdelete" ]; then
     echo "$0: Invalid action: ${ACTION}"
     exit 1;
  fi
  # We should run on FreeBSD
  # We always use table 00001 and rule id 00001.
  if [ "X${UNAME}" = "XFreeBSD" ]; then
    ls ${IPFW} >> /dev/null 2>&1
    if [ $? != 0 ]; then
        exit 0;
    fi
    # Check if our table is set
    <font color="red"> ${IPFW} show | grep "^00001" | grep "table(2)" >/dev/null 2>&1</font>
    if [ ! $? = 0 ]; then
         # We need to add the table
         ${IPFW} -q 00001 add deny ip from table\(${TABLE_ID}\) to any
         ${IPFW} -q 00001 add deny ip from any to table\(${TABLE_ID}\)
    fi    
    # Executing and exiting
    ${IPFW} -q table ${TABLE_ID} ${ACTION} ${IP}
    exit 0;
  fi
  # Not FreeBSD
  exit 1;

Include in ``/var/ossec/etc/ossec.conf``:

.. code-block:: console

  <command>
    <name>firewall-drop</name>
    <executable>firewall-drop.sh</executable>
    <expect>srcip</expect>
  </command>

  <active-response>
    <disabled>no</disabled>
    <command>firewall-drop</command>
    <location>local</location>
       <rules_id>99990</rules_id>
  </active-response>

restart ossec:

.. code-block:: console

  /var/ossec/bin/ossec-control restart

Scan your machine (caution OSSEC will block the scanner IP) from online scanner server like: http://www.derkeiler.com/Service/PortScan/, or from a remote machine with: 

.. code-block:: console

  nmap -sT -PI -PT 1.2.3.4

look if the active-response works with:

.. code-block:: console

  /sbin/ipfw table 2 list

or

.. code-block:: console

  tail -f /var/ossec/active-response/ossec-hids-responses.log

if you want to flush the banned IPs in the table

.. code-block:: console

  /sbin/ipfw table 2 flush

or want to remove a specific IP in the table

.. code-block:: console

  /sbin/ipfw table 2 delete 1.2.3.4

if you want to flush the table every 24 Hrs:

.. code-block:: console

  vi /etc/crontab

and include
.. code-block:: console

  0    */24       *       *       *  root /sbin/ipfw table 2 flush > /dev/null 2>&1

More restrictions:
^^^^^^^^^^^^^^^^^^

iplog.conf:
^^^^^^^^^^^
To Enable or disable a mechanism that attempts to fool programs, such as nmap and queso, that perform remote OS detection, add the follow line to iplog.conf

.. code-block:: console

 set fool_nmap true

As a side effect, enabling this option will also cause most of nmap's stealth" scans to fail.

BSD's sysctl (some FreeBSD especific):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  tcp_drop_synfin
  net.inet.tcp.blackhole
  net.inet.udp.blackhole



