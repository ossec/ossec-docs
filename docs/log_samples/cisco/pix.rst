Cisco PIX Logs
--------------



Log Samples from the Cisco PIX:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Cisco PIX logs are very well formatted and easy to parse. Every message starts with a unique
ID of the event, which is in the following format: <b>%PIX-severity-eventID. A complete
list with all event IDS can be found at the :
[http://www.cisco.com/en/US/products/sw/secursw/ps2120/products_system_message_guide_chapter09186a008051a0ca.html cisco site].
[http://www.cisco.com/univercd/cc/td/doc/product/iaabu/pix/pix_v53/syslog/pixemsgs.htm Cisco Pix Specific].


Full log samples:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sep  7 06:25:17 PIXName %PIX-7-710005: UDP request discarded from 0.0.0.0/68 to outside:255.255.255.255/67
  Sep  7 06:25:23 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:23 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:23 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:24 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:24 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:24 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:25 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:25 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:25 PIXName %PIX-7-710005: UDP request discarded from 1.1.1.1/137 to outside:1.1.1.255/137
  Sep  7 06:25:28 PIXName %PIX-7-609001: Built local-host db:10.0.0.1
  Sep  7 06:25:28 PIXName %PIX-6-302013: Built inbound TCP connection 141968 for db:10.0.0.1/60749 (10.0.0.1/60749) to NP Identity Ifc: 10.0.0.2/22 (10.0.0.2/22)
  Sep  7 06:25:28 PIXName %PIX-7-710002: TCP access permitted from 10.0.0.1/60749 to db:10.0.0.2/ssh
  Sep  7 06:26:20 PIXName %PIX-5-304001: 203.87.123.139 Accessed URL 10.0.0.10:/Home/index.cfm
  Sep  7 06:26:20 PIXName %PIX-5-304001: 203.87.123.139 Accessed URL 10.0.0.10:/aboutus/volunteers.cfm
  Sep  7 06:26:49 PIXName %PIX-4-106023: Deny udp src outside:204.16.208.49/58939 dst dmz:10.0.0.158/1026 by access-group "acl_outside" [0x0, 0x0]
  Sep  7 06:26:49 PIXName %PIX-4-106023: Deny udp src outside: 204.16.208.49/58940 dst dmz:10.0.0.158/1027 by access-group "acl_outside" [0x0, 0x0]
  Sep  7 06:31:26 PIXName %PIX-7-711002: Task ran for 330 msec, Process= ssh_init, PC = fddd93, Traceback =   0x00FF1E6B  0x00FE1890 0x00FE0D3C  0x00FD326A  0x00FC0BFC 0x00FDBB8E  0x00FDBA4D  0x00FCD846  0x00FBF09C  0x001C76AE 0x00A01512  0x009CF6B5  0x00BDB9CE  0x00BDA502
  Sep  7 06:31:32 PIXName %PIX-6-315011: SSH session from 10.0.0.254 on interface db for user "" disconnected by SSH server, reason: "TCP connection closed" (0x03)

  %PIX-7-710001: TCP access requested from 192.168.2.10/13269 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/13528 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/14154 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/19067 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/21532 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/27167 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/29488 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/32597 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/40654 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/48798 to outside:192.168.2.14/ssh
  %PIX-7-710001: TCP access requested from 192.168.2.10/7180 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/13269 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/13528 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/14154 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/19067 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/21532 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/27167 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/29488 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/32597 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/40654 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/48798 to outside:192.168.2.14/ssh
  %PIX-7-710002: TCP access permitted from 192.168.2.10/7180 to outside:192.168.2.14/ssh
  %PIX-7-710005: UDP request discarded from 0.0.0.0/68 to outside:255.255.255.255/bootps
  %PIX-7-710005: UDP request discarded from 192.168.1.2/137 to inside:192.168.1.255/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.1.2/138 to inside:192.168.1.255/netbios-dgm
  %PIX-7-710005: UDP request discarded from 192.168.1.2/3935 to inside:192.168.1.1/1900
  %PIX-7-710005: UDP request discarded from 192.168.2.1/137 to outside:192.168.2.11/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.2.1/137 to outside:192.168.2.14/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.2.11/137 to outside:192.168.2.255/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.2.11/138 to outside:192.168.2.255/netbios-dgm
  %PIX-7-710005: UDP request discarded from 192.168.2.11/68 to outside:255.255.255.255/bootps
  %PIX-7-710005: UDP request discarded from 192.168.2.12/137 to outside:192.168.2.255/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.2.12/138 to outside:192.168.2.255/netbios-dgm
  %PIX-7-710005: UDP request discarded from 192.168.2.12/68 to outside:255.255.255.255/bootps
  %PIX-7-710005: UDP request discarded from 192.168.2.13/137 to outside:192.168.2.255/netbios-ns
  %PIX-7-710005: UDP request discarded from 192.168.2.13/138 to outside:192.168.2.255/netbios-dgm
  %PIX-7-710005: UDP request discarded from 192.168.2.13/68 to outside:255.255.255.255/bootps
  %PIX-7-710005: UDP request discarded from 192.168.2.190/137 to outside:192.168.2.255/netbios-ns
  %PIX-6-315011: SSH session from 192.168.2.10 on interface outside for user "roo" disconnected by SSH server, reason: "TCP connection closed" (0x03)
  %PIX-6-604101: DHCP client interface outside: Allocated ip = 192.168.2.11, mask = 255.255.255.0, gw = 192.168.2.1
  %PIX-6-604101: DHCP client interface outside: Allocated ip = 192.168.2.14, mask = 255.255.255.0, gw = 192.168.2.1
  %PIX-6-604103: DHCP daemon interface inside:  address granted 000c.29e4.ebc3 (12.168.1.3)
  %PIX-6-604103: DHCP daemon interface inside:  address granted 000c.29e4.ebc3 (12.168.1.4)
  %PIX-6-604103: DHCP daemon interface inside:  address granted 0100.0d9d.8283.ec(192.168.1.2)
  %PIX-6-605004: Login denied from 192.168.2.10/13269 to outside:192.168.2.14/ssh for user "root"
  %PIX-6-605004: Login denied from 192.168.2.10/13528 to outside:192.168.2.14/ssh for user "dcid"
  %PIX-6-605004: Login denied from 192.168.2.10/14154 to outside:192.168.2.14/ssh for user "root"
  %PIX-3-305006: portmap translation creation failed for tcp src inside:192.168.1.2/2893 dst outside:192.168.2.99/3128
  %PIX-3-305006: portmap translation creation failed for tcp src inside:192.168.1.2/2892 dst outside:192.168.2.99/3128
  %PIX-3-201008: The PIX is disallowing new connections.
  %PIX-3-106011: Deny inbound (No xlate) udp src outside:192.168.2.1/137 dst outside:192.168.2.14/137
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:63.245.209.21/80 dst outside:192.168.2.14/1823
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:195.27.11.150/80 dst outside:192.168.2.14/1717
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:195.27.11.150/80 dst outside:192.168.2.14/1716
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:195.27.11.143/80 dst outside:192.168.2.14/1721
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:195.27.11.142/80 dst outside:192.168.2.14/1720

  %PIX-3-106011: Deny inbound (No xlate) tcp src inside:10.100.7.43/80 dst inside:10.100.4.71/2285
  %PIX-3-106011: Deny inbound (No xlate) tcp src inside:10.100.5.43/80 dst inside:10.100.4.71/2285
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:213.98.202.19/3959 dst outside:213.58.100.132/139
  %PIX-3-106011: Deny inbound (No xlate) tcp src outside:213.98.202.19/3959 dst outside:213.58.100.132/139
  %PIX-3-106011: Deny inbound (No xlate) udp src outside:192.168.2.1/137 dst outside:192.168.2.14/137
  %PIX-3-106010: Deny inbound tcp src outside:213.98.79.233/2620 dst dmz:213.98.254.145/135
  %PIX-3-106010: Deny inbound tcp src outside:213.91.69.233/2620 dst dmz:213.98.254.145/145

  Jan 28 02:04:30 pix-inside %PIX-3-106010: Deny inbound tcp src outside:67.200.184.237/1262 dst inside:10.107.96.170/80
  Jan 28 02:01:08 pix-inside %PIX-3-106010: Deny inbound udp src outside:216.143.1.229/1321 dst inside:10.107.96.213/1434
  Jan 28 06:17:47 pix-inside %PIX-3-106010: Deny inbound icmp src outside:80.181.210.80 dst inside:10.107.96.229 (type 8, code 0)
  Jan 28 00:21:50 pix-inside %PIX-3-106011: Deny inbound (No xlate) tcp src outside:217.228.221.121/1233 dst outside:10.47.243.45/80
  Jan 28 00:01:38 pix-inside %PIX-4-106023: Deny tcp src outside:213.22.40.190/1381 dst inside:10.107.8.6/445 by access-group "ACL-FROM-OUTSIDE"
  Jan 28 00:01:38 pix-inside %PIX-4-106023: Deny udp src outside:24.200.88.234/1025 dst inside:10.107.31.183/137 by access-group "ACL-FROM-OUTSIDE"
  Jan 28 00:41:42 pix-inside %PIX-4-106023: Deny icmp src outside:128.9.160.165 dst inside:10.107.19.103 (type 8, code 0) by access-group "ACL-FROM-OUTSIDE"
  Jan 28 01:48:01 pix-inside %PIX-4-106023: Deny protocol 4 src outside:131.119.0.197 dst inside:10.107.16.135 by access-group "ACL-FROM-OUTSIDE"

  <164>Jul 05 2004 00:58:00: %PIX-4-400011: IDS:2001 ICMP unreachable from 172.54.32.18 to 192.168.54.23 on interface outside
  <162>Jul 05 2004 00:56:23: %PIX-2-109011: Authen Session Start: user 'Graffe', sid 55
  <164>Jul 05 2004 00:56:26: %PIX-4-500004: Invalid transport field for protocol=17, from 10.34.55.198/50230 to 192.168.64.23/0
  <164>Dec 05 2006 12:06:59: %PIX-4-405001: Received ARP request collision from 10.54.100.218/007e.0cfe.b3a4 on interface inside




Alert Messages, Severity 1:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Critical Messages, Severity 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-2-106006: Deny inbound UDP from ***/20031 to ***/20031 on  interface vpn
  %PIX-2-106006: Deny inbound UDP from ***/20031 to ***/20031 on  interface vpn
  %PIX-2-106006: Deny inbound UDP from ***/54481 to ***/1026 on  interface vpn
  %PIX-2-106006: Deny inbound UDP from ***9/20031 to ***/20031 on interface vpn
  %PIX-2-106006: Deny inbound UDP from ***/20031 to ***/20031 on  interface vpn


Error Messages, Severity 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-3-313001: Denied ICMP type=11, code=0 from 192.168.30.2 on interface 2


Warning Messages, Severity 4:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-4-410001: Dropped UDP DNS reply from os-to-dmz:192.168.30.2 to outside:192.168.100.2/53; packet length 560 bytes exceeds configured limit of 512 bytes


Notification Messages, Severity 5:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-5-304001: 192.168.20.50 Accessed URL x.y.z.a:/test/xx/yy.html

Informational Messages, Severity 6:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-6-302016: Teardown UDP connection 1042068 for outside:192.168.20.45/53 to inside:192.168.20.208/37989 duration 0:02:10 bytes 185
  %PIX-6-106015: Deny TCP (no connection) from 192.168.2.50/443 to 192.168.20/65 flags RST on interface outside


Debugging Messages, Severity 7:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  %PIX-7-710005: UDP request discarded from  192.168.20.45/53 to outside:192.168.20.208/37989



