Microsoft ISA Server
  --------------------

Here is a sample of the firewall log from Microsoft ISA Server 2004 (in W3c extended format). Note that when the W3C extended log format is used, the times stamped on events are in Coordinated Universal Time (UTC) otherwise known as Greenwich Mean Time. So adjustments would have to be made during analysis for the particular time zone you are in.

.. code-block:: console
  #Software: Microsoft Internet Security and Acceleration Server 2004
  #Version: 2.0
  #Date: 2006-10-27 00:00:00
  #Fields: computer	date	time	IP protocol	source	destination	original client IP	source network	destination network	action	status	rule	application protocol	bytes sent	bytes sent intermediate	bytes received	bytes received intermediate	connection time	connection time intermediate	source name	destination name	username	agent	session ID	connection ID	interface	IP header	protocol payload
  ACME-PROXY	2006-10-27	00:00:00	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:00	IGMP	192.168.80.148	224.0.0.1	192.168.80.148	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:00	IGMP	192.168.80.148	224.0.0.1	192.168.80.148	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:00	UDP	192.168.100.48:138	192.168.100.255:138	192.168.100.48	Internal	Local Host	Denied	0xc004000d	-	NetBios Datagram	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:02	IGMP	192.168.70.244	224.0.0.1	192.168.70.244	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:02	IGMP	192.168.70.244	224.0.0.1	192.168.70.244	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:02	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:02	IGMP	192.168.80.240	224.0.0.1	192.168.80.240	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:02	IGMP	192.168.80.240	224.0.0.1	192.168.80.240	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:06	IGMP	192.168.80.248	224.0.0.1	192.168.80.248	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:06	IGMP	192.168.80.248	224.0.0.1	192.168.80.248	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:06	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:12	UDP	192.168.100.178:138	192.168.100.255:138	192.168.100.178	Internal	Local Host	Denied	0xc004000d	-	NetBios Datagram	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:15	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:15	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:15	UDP	192.168.100.200:127	192.168.100.255:125	192.168.100.200	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:15	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:17	UDP	192.168.70.208:138	192.168.70.255:138	192.168.70.208	Internal	Local Host	Denied	0xc004000d	-	NetBios Datagram	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:17	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:21	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:26	UDP	192.168.100.115:57135	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:26	UDP	192.168.100.115:57135	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:26	UDP	192.168.70.79:138	192.168.70.255:138	192.168.70.79	Internal	Local Host	Denied	0xc004000d	-	NetBios Datagram	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:26	UDP	192.168.100.115:57135	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	TCP	192.168.100.85:13122	192.168.100.195:135	192.168.100.85	Local Host	Internal	Intermediate	0x0	Allow RPC from ISA Server to trusted servers	RPC (all interfaces)	272	0	236	0	1799875	899844	-	-	-	-	2	233149	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	TCP	192.168.100.85:13124	192.168.100.195:1025	192.168.100.85	Local Host	Internal	Intermediate	0x0	Allow RPC from ISA Server to trusted servers	RPC (all interfaces)	0	0	0	0	1799875	899844	-	-	-	-	2	233150	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	UDP	192.168.100.43:137	192.168.100.255:137	192.168.100.43	Internal	Local Host	Denied	0xc004000d	-	NetBios Name Service	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	UDP	192.168.100.115:57135	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:29	UDP	192.168.100.43:137	192.168.100.255:137	192.168.100.43	Internal	Local Host	Denied	0xc004000d	-	NetBios Name Service	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:31	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:31	UDP	192.168.100.43:137	192.168.100.255:137	192.168.100.43	Internal	Local Host	Denied	0xc004000d	-	NetBios Name Service	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-
  ACME-PROXY	2006-10-27	00:00:31	UDP	192.168.100.115:61683	255.255.255.255:14000	192.168.100.115	Internal	Local Host	Denied	0xc004000d	-	Unidentified IP Traffic	0	0	0	0	-	-	-	-	-	-	0	0	-	-	-




Here is a sample of the web proxy log from ISA Server 2004. It is in W3C extended format.



.. code-block:: console
  #Software: Microsoft Internet Security and Acceleration Server 2004
  #Version: 2.0
  #Date: 2006-11-12 00:00:00
  #Fields: c-ip	cs-username	c-agent	sc-authenticated	date	time	s-svcname	s-computername	cs-referred	r-host	r-ip	r-port	time-taken	cs-bytes	sc-bytes	cs-protocol	cs-transport	s-operation	cs-uri	cs-mime-type	s-object-source	sc-status	s-cache-info	rule	FilterInfo	cs-Network	sc-Network	error-info	action
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	78	489	5591	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323133-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	438	488	6862	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-031002301331132331-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	94	489	7007	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323200-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	94	489	8363	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323201-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	93	488	1254	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133120101-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	78	488	1253	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133120100-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	78	488	1253	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133120110-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	78	488	10757	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-031002301331132323-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:00	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	219	488	10017	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-031002301331132332-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:01	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	78	480	308	http	TCP	GET	http://gt.shaffle.com/newstyle?q2-0310023013312001	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:01	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	78	486	6199	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-031002301331200-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	172	485	8286	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-031002301331133-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	94	485	8241	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-031002301331200-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	157	486	7906	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311332-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	109	486	9036	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013312001-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.100.202	anonymous	Acrobat Messages Updater	N	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	rms.adobe.com	10.25.100.85	8080	1	224	4574	http	TCP	GET	http://rms.adobe.com/read/0600/win_/ENU/read0600win_ENUadbe0000.xml	-	-	12209	0x6	Deny Internet Access	-	Internal	External	0x800	Denied
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	62	488	1250	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133113322-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	250	486	11002	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013312010-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.80.234	anonymous	Acrobat Messages Updater	N	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	rms.adobe.com	10.25.100.85	8080	1	224	4574	http	TCP	GET	http://rms.adobe.com/read/0600/win_/ENU/read0600win_ENUadbe0000.xml	-	-	12209	0x6	Deny Internet Access	-	Internal	External	0x800	Denied
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	78	488	1230	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133113321-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:02	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	63	488	1339	http	TCP	GET	http://gt.shaffle.com/newstyle?f1c-03100230133120011-t.124	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	203	489	7906	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323302-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.48.32	anonymous	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	N	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	283	4574	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/installprecisiontime.exe	-	-	12209	0x2	Deny Internet Access	-	Internal	External	0x800	Denied
  10.25.48.32	anonymous	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	N	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	392	504	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/installprecisiontime.exe	-	-	5	0x2	Deny Internet Access	-	Internal	External	0x880	Failed
  10.25.48.32	ACME\bgrimm	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	Y	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	544	4313	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/installprecisiontime.exe	-	-	12202	0x2	Block Spyware and Adware sites	-	Internal	External	0x880	Denied
  10.25.48.32	anonymous	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	N	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	276	4574	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/precisiontime.ini	-	-	12209	0x2	Deny Internet Access	-	Internal	External	0x800	Denied
  10.25.48.32	anonymous	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	N	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	385	504	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/precisiontime.ini	-	-	5	0x2	Deny Internet Access	-	Internal	External	0x880	Failed
  10.25.48.32	ACME\bgrimm	Gator/1.0 Precision Time {782E4A69-C75A-491B-B314-9569B3765C65}	Y	2006-11-12	00:00:03	w3proxy	ACME-PROXY	-	gatorcme.gator.com	10.25.100.85	8080	1	537	4313	http	TCP	GET	http://gatorcme.gator.com/gatorcme/autoupdate/precisiontime.ini	-	-	12202	0x2	Block Spyware and Adware sites	-	Internal	External	0x880	Denied
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:04	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	93	489	5827	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311332223-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:04	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	140	489	8105	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323330-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:04	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	94	489	6965	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311332222-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.80.219	ACME\gcurry	Mozilla/4.0 (compatible; MSIE 5.0; Win32)	Y	2006-11-12	00:00:04	w3proxy	ACME-PROXY	-	www.msn2go.com	64.92.173.122	8080	5141	560	102	http	TCP	GET	http://www.msn2go.com:8080/msn2goproxy	-	Inet	204	0x40000005	Allow Web Access	-	Internal	External	0x480	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:05	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	157	489	8284	http	TCP	GET	http://gt.shaffle.com/newstyle?f1-0310023013311323333-i.109	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:06	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	62	480	308	http	TCP	GET	http://gt.shaffle.com/newstyle?q2-0310023013312002	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:06	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.91	80	63	480	308	http	TCP	GET	http://gt.shaffle.com/newstyle?q2-0310023013312013	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.70.185	ACME\rrichards	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Windows Live Messenger 8.0.0792)	Y	2006-11-12	00:00:08	w3proxy	ACME-PROXY	-	207.46.109.14	207.46.109.14	80	110	299	285	http	TCP	POST	http://207.46.109.14/gateway/gateway.dll?Action=poll&SessionID=785192002.25263	application/x-msn-messenger	Inet	200	0x40000004	Allow Web Access	-	Internal	External	0xd80	Allowed
  10.25.80.219	ACME\gcurry	Mozilla/4.0 (compatible; MSIE 5.0; Win32)	Y	2006-11-12	00:00:15	w3proxy	ACME-PROXY	-	www.msn2go.com	64.92.173.122	8080	5296	307	102	http	TCP	GET	http://www.msn2go.com:8080/msn2goproxy	-	Inet	204	0x40000005	Allow Web Access	-	Internal	External	0x480	Allowed
  10.25.34.65	ACME\sstorm	kh_lt/LT3.0.0762	Y	2006-11-12	00:00:21	w3proxy	ACME-PROXY	-	gt.shaffle.com	57.145.187.93	80	63	480	308	http	TCP	GET	http://gt.shaffle.com/newstyle?q2-0310023013311331	application/octet-stream	Inet	200	0x40000005	Allow Web Access	-	Internal	External	0xd80	Allowed



Here are log samples from ISA Server 2000

IP Packet Filter log in W3C Extended format

.. code-block:: console
  #Software: Microsoft(R) Internet Security and Acceleration Server 2000
  #Version: 1.0
  #Date: 2006-11-16 00:04:45
  #Fields: date	time	source-ip	destination-ip	protocol	param#1	param#2	tcp-flags	filter-rule	interface	ip-header	payload
2006-11-16	00:04:45	10.45.1.1	10.45.2.4	Udp	1675	137	-	BLOCKED	10.45.1.1	23 44 44 4e yu bf 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8b 44 89 44 3a 82 37
2006-11-16	00:04:46	10.45.1.1	10.45.2.4	Udp	1675	137	-	BLOCKED	10.45.1.1	23 44 44 4e yu c1 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8b 44 89 44 3a 82 35
2006-11-16	00:04:48	10.45.1.1	10.45.2.4	Udp	1675	137	-	BLOCKED	10.45.1.1	23 44 44 4e yu c2 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8b 44 89 44 3a 82 33
2006-11-16	00:04:49	10.45.1.1	10.45.2.4	Udp	1675	137	-	BLOCKED	10.45.1.1	23 44 44 4e yu ce 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8b 44 89 44 3a 82 31
2006-11-16	00:04:51	10.45.1.1	10.45.2.4	Udp	1675	137	-	BLOCKED	10.45.1.1	23 44 44 4e yu cf 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8b 44 89 44 3a 82 2f
2006-11-16	00:08:51	10.45.1.1	10.45.2.4	Udp	1676	137	-	BLOCKED	10.45.1.1	23 44 44 4e e6 61 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 4g 44 89 44 3a 82 26
2006-11-16	00:08:52	10.45.1.1	10.45.2.4	Udp	1676	137	-	BLOCKED	10.45.1.1	23 44 44 4e e7 97 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 4g 44 89 44 3a 82 24
2006-11-16	00:08:54	10.45.1.1	10.45.2.4	Udp	1676	137	-	BLOCKED	10.45.1.1	23 44 44 4e e8 4f 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 4g 44 89 44 3a 82 22
2006-11-16	00:08:55	10.45.1.1	10.45.2.4	Udp	1676	137	-	BLOCKED	10.45.1.1	23 44 44 4e e9 d1 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 4g 44 89 44 3a 82 20
2006-11-16	00:08:57	10.45.1.1	10.45.2.4	Udp	1676	137	-	BLOCKED	10.45.1.1	23 44 44 4e eb 4c 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 4g 44 89 44 3a 82 1e
2006-11-16	00:12:27	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 bd eb 40 44 74 06 51 ac 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:12:28	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 uj 0e 40 44 74 06 20 89 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:12:31	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 11 61 40 44 74 06 fe 36 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:12:37	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 57 15 40 44 74 06 b8 82 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:12:49	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 b5 69 40 44 74 06 5a 2e 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:13:12	41.56.41.15	10.45.1.1	Tcp	80	24820	SYN ACK 	BLOCKED	10.45.1.1	23 44 44 30 58 ea 40 44 74 06 h9 yu 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 84 h9 7d 10 a3 70 12 18 44 62 51 44 44 02 04 05 64 04 02 01 01
2006-11-16	00:13:21	41.56.41.15	10.45.1.1	Tcp	80	24820	RST ACK 	BLOCKED	10.45.1.1	23 44 44 28 0f ca 40 44 74 06 ff d5 0c 78 29 0f c0 a8 01 01	44 50 60 f4 ec f3 fc 85 h9 7d 10 a3 50 14 44 44 a6 c1 44 00
2006-11-16	01:08:33	10.45.1.1	10.45.2.4	Udp	1677	137	-	BLOCKED	10.45.1.1	23 44 44 4e 5c 5c 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8d 44 89 44 3a 81 9a
2006-11-16	01:08:34	10.45.1.1	10.45.2.4	Udp	1677	137	-	BLOCKED	10.45.1.1	23 44 44 4e 5c 7e 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8d 44 89 44 3a 81 98
2006-11-16	01:08:36	10.45.1.1	10.45.2.4	Udp	1677	137	-	BLOCKED	10.45.1.1	23 44 44 4e 5c f7 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8d 44 89 44 3a 81 96
2006-11-16	01:08:37	10.45.1.1	10.45.2.4	Udp	1677	137	-	BLOCKED	10.45.1.1	23 44 44 4e 5d 75 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8d 44 89 44 3a 81 94
2006-11-16	01:08:39	10.45.1.1	10.45.2.4	Udp	1677	137	-	BLOCKED	10.45.1.1	23 44 44 4e 5d bc 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8d 44 89 44 3a 81 92
2006-11-16	01:12:06	10.45.1.1	10.45.2.4	Udp	1678	137	-	BLOCKED	10.45.1.1	23 44 44 4e 8f bc 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8e 44 89 44 3a 81 87
2006-11-16	01:12:08	10.45.1.1	10.45.2.4	Udp	1678	137	-	BLOCKED	10.45.1.1	23 44 44 4e 90 96 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8e 44 89 44 3a 81 85
2006-11-16	01:12:09	10.45.1.1	10.45.2.4	Udp	1678	137	-	BLOCKED	10.45.1.1	23 44 44 4e 91 bd 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8e 44 89 44 3a 81 83
2006-11-16	01:12:11	10.45.1.1	10.45.2.4	Udp	1678	137	-	BLOCKED	10.45.1.1	23 44 44 4e 91 e0 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8e 44 89 44 3a 81 81
2006-11-16	01:12:12	10.45.1.1	10.45.2.4	Udp	1678	137	-	BLOCKED	10.45.1.1	23 44 44 4e 92 11 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8e 44 89 44 3a 81 7f
2006-11-16	02:12:43	10.45.1.1	10.45.2.4	Udp	1679	137	-	BLOCKED	10.45.1.1	23 44 44 4e 63 b5 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8f 44 89 44 3a 80 f6
2006-11-16	02:12:45	10.45.1.1	10.45.2.4	Udp	1679	137	-	BLOCKED	10.45.1.1	23 44 44 4e 63 e0 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8f 44 89 44 3a 80 f4
2006-11-16	02:12:46	10.45.1.1	10.45.2.4	Udp	1679	137	-	BLOCKED	10.45.1.1	23 44 44 4e 64 17 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8f 44 89 44 3a 80 f2
2006-11-16	02:12:48	10.45.1.1	10.45.2.4	Udp	1679	137	-	BLOCKED	10.45.1.1	23 44 44 4e 64 5d 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8f 44 89 44 3a 80 f0
2006-11-16	02:12:49	10.45.1.1	10.45.2.4	Udp	1679	137	-	BLOCKED	10.45.1.1	23 44 44 4e 64 73 44 44 80 11 44 44 c0 a8 01 01 c0 a8 02 04	06 8f 44 89 44 3a 80 ee



Here is the ISA Server 2000 Firewall Log in ISA Server format


.. code-block:: console
  10.45.100.201, -, -, N, 11/8/2006, 0:00:05, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1169, 12515, 814, 22813, 25, TCP, Accept, -, -, -, 20000, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:13, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1172, 16, 0, 0, 25, TCP, Accept, -, -, -, 0, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:16, fwsrv, ACME-PROXY, -, -, 172.16.2.3, 3962, 15, 0, 0, 25, TCP, Accept, -, -, -, 0, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:19, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1172, 5875, 460, 26032, 25, TCP, Accept, -, -, -, 20000, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:23, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1174, 15, 0, 0, 25, TCP, Accept, -, -, -, 0, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:24, fwsrv, ACME-PROXY, -, -, 172.16.2.3, 3962, 7406, 641, 49956, 25, TCP, Accept, -, -, -, 20000, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:28, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 25, 9000, 0, 0, 25, TCP, Connect, -, -, -, 0, 0, Outbound SMTP, Allow Internal Mail Servers to Connect to DMZ Servers, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:28, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 25, 9156, 32392, 304, 25, TCP, Connect, -, -, -, 20000, 0, Outbound SMTP, Allow Internal Mail Servers to Connect to DMZ Servers, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:29, fwsrv, ACME-PROXY, -, -, 172.16.2.3, 3970, -, 0, 0, 25, TCP, Accept, -, -, -, 0, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.1.37, andone, webshots.scr:3:5.1, Y, 11/8/2006, 0:00:33, fwsrv, ACME-PROXY, -, webshots.com, 216.239.124.149, 0, -, 0, 0, -, -, GHBN, -, -, -, 0, 0, Publish SSH on ACMESG1, Grant Access to all destinations, -, -
  10.45.1.37, andone, webshots.scr:3:5.1, Y, 11/8/2006, 0:00:33, fwsrv, ACME-PROXY, -, -, 216.239.124.149, 80, -, 0, 0, 80, TCP, Connect, -, -, -, 13301, 0, Internet Access, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:35, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1174, 11015, 613, 17385, 25, TCP, Accept, -, -, -, 20000, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:37, fwsrv, ACME-PROXY, -, -, 172.16.2.3, 3970, 7781, 456, 20647, 25, TCP, Accept, -, -, -, 20000, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:37, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 1176, -, 0, 0, 25, TCP, Accept, -, -, -, 0, 0, Publish Internal SMTP Email Server, -, -, -
  10.45.100.201, -, -, N, 11/8/2006, 0:00:39, fwsrv, ACME-PROXY, -, -, 172.16.2.2, 25, 9000, 0, 0, 25, TCP, Connect, -, -, -, 0, 0, Outbound SMTP, Allow Internal Mail Servers to Connect to DMZ Servers, -, -
  10.45.1.37, SYSTEM, CLMLService.exe:3:5.1, Y, 11/8/2006, 0:00:40, fwsrv, ACME-PROXY, -, -, -, 51233, 180109, 0, 0, 51233, TCP, Bind, -, -, -, 20000, 0, -, -, -, -
  10.45.1.37, SYSTEM, CLMLService.exe:3:5.1, Y, 11/8/2006, 0:00:41, fwsrv, ACME-PROXY, -, -, -, 51824, -, 0, 0, 51824, TCP, Bind, -, -, -, 0, 0, -, -, -, -
  10.45.1.37, SYSTEM, CLMLService.exe:3:5.1, Y, 11/8/2006, 0:00:41, fwsrv, ACME-PROXY, -, -, -, 54333, -, 0, 0, 54333, UDP, Bind, -, -, -, 0, 0, -, -, -, -
  10.45.1.37, SYSTEM, CLMLService.exe:3:5.1, Y, 11/8/2006, 0:00:41, fwsrv, ACME-PROXY, -, -, -, 57543, 7063719, 0, 0, 57543, UDP, Bind, -, -, -, 20001, 0, -, -, -, -
  10.45.1.37, SYSTEM, CLMLService.exe:3:5.1, Y, 11/8/2006, 0:00:41, fwsrv, ACME-PROXY, -, -, -, 51824, -, 0, 0, 51824, TCP, Listen, -, -, -, 0, 0, -, -, -, -
  10.45.70.31, sstorch, aim.exe:3:5.0, Y, 11/8/2006, 0:55:49, fwsrv, ACME-PROXY, -, aim-charts.pf.aol.com, 64.12.185.119, 0, -, 0, 0, -, -, GHBN, -, -, -, 0, 0, Publish SSH on ACMESG1, Grant Access to all destinations, -, -
  10.45.70.31, sstorch, aim.exe:3:5.0, Y, 11/8/2006, 0:55:49, fwsrv, ACME-PROXY, -, -, 64.12.185.119, 80, -, 0, 0, 80, TCP, Connect, -, -, -, 13301, 0, Internet Access, -, -, -
  10.45.80.238, lstath, IEXPLORE.EXE:3:5.0, Y, 11/8/2006, 14:28:46, fwsrv, ACME-PROXY, -, www.searchalot.com, 64.14.40.138, 0, -, 0, 0, -, -, GHBN, -, -, -, 0, 0, Publish SSH on ACMESG1, Grant Access to all destinations, -, -
  10.45.80.238, lstath, IEXPLORE.EXE:3:5.0, Y, 11/8/2006, 14:28:46, fwsrv, ACME-PROXY, -, -, 64.14.40.138, 80, -, 0, 0, 80, TCP, Connect, -, -, -, 13301, 0, Internet Access, -, -, -
  10.45.1.58, dmesg, FileZilla.exe:3:5.1, Y, 11/8/2006, 19:00:59, fwsrv, ACME-PROXY, -, -, 172.16.2.4, 2332, 9000, 0, 0, 2332, TCP, Connect, -, -, -, 0, 0, Internet Access, Grant Access to all destinations, -, -
  10.45.1.58, dmesg, FileZilla.exe:3:5.1, Y, 11/8/2006, 19:00:59, fwsrv, ACME-PROXY, -, -, 172.16.2.4, 2332, 9000, 0, 355, 2332, TCP, Connect, -, -, -, 20000, 0, Internet Access, Grant Access to all destinations, -, -
  10.45.1.68, Dlicious, mstsc.exe:3:5.1, Y, 11/8/2006, 19:02:16, fwsrv, ACME-PROXY, -, -, 172.16.2.3, 3389, 166219, 30240, 129171, 3389, TCP, Connect, -, -, -, 20000, 0, Terminal Services Access to DMZ Server, Grant Access to all destinations, -, -
  10.45.1.68, Dlicious, mstsc.exe:3:5.1, Y, 11/8/2006, 19:02:16, fwsrv, ACME-PROXY, -, -, -, 0, 164110, 0, 0, 0, UDP, Bind, -, -, -, 20000, 0, -, -, -, -



Here is a sample of the ISA Server 2000 web proxy log in W3C Extended format

.. code-block:: console

  #Software: Microsoft(R) Internet Security and Acceleration Server 2000
  #Version: 1.0
  #Date: 2006-11-16 00:00:01
  #Fields: c-ip	cs-username	c-agent	sc-authenticated	date	time	s-svcname	s-computername	cs-referred	r-host	r-ip	r-port	time-taken	cs-bytes	sc-bytes	cs-protocol	cs-transport	s-operation	cs-uri	cs-mime-type	s-object-source	sc-status	s-cache-info	rule#1	rule#2
  10.54.80.151	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:01	w3proxy	ACME-PROXY	-	web.freemail.com	-	80	-	992	3292	http	TCP	POST	http://web.freemail.com/mail/channel/bind?at=3fed1555f6851887-10ee843eb7e&VER=2&SID=ABDB48E0D064E6E7&RID=83189&zx=f5lvq4-uftwvt&t=1	-	-	407	-	-	-
  10.54.80.151	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:01	w3proxy	ACME-PROXY	-	web.freemail.com	-	80	-	52	1980	http	TCP	POST	http://web.freemail.com/mail/channel/bind?at=3fed1555f6851887-10ee843eb7e&VER=2&SID=ABDB48E0D064E6E7&RID=83189&zx=f5lvq4-uftwvt&t=1	-	-	407	-	-	-
  10.54.29.65	ACME\clmantock	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Windows Live Messenger 8.0.0812)	Y	2006-11-16	00:00:02	w3proxy	ACME-PROXY	-	207.46.107.35	207.46.107.35	80	719	339	572	http	TCP	POST	http://207.46.107.35/gateway/gateway.dll?Action=poll&SessionID=1035492081.13530	application/x-msn-messenger	Inet	200	0x40000004	Internet Access	Grant Access to all destinations
  10.54.29.65	ACME\clmantock	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Windows Live Messenger 8.0.0812)	Y	2006-11-16	00:00:03	w3proxy	ACME-PROXY	-	207.46.107.35	207.46.107.35	80	703	338	290	http	TCP	POST	http://207.46.107.35/gateway/gateway.dll?Action=poll&SessionID=1035492081.1247	application/x-msn-messenger	Inet	200	0x40000004	Internet Access	Grant Access to all destinations
  10.54.80.151	ACME\eflynn	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:03	w3proxy	ACME-PROXY	-	web.freemail.com	72.14.205.17	80	2329	1666	342	http	TCP	POST	http://web.freemail.com/mail/channel/bind?at=3fed1555f6851887-10ee843eb7e&VER=2&SID=ABDB48E0D064E6E7&RID=83189&zx=f5lvq4-uftwvt&t=1	text/html; charset=utf-8	Inet	200	0x42040004	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	414	155	http	TCP	GET	http://www.c-spline.com/styles/style.css	text/css	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	422	155	http	TCP	GET	http://www.c-spline.com/images/searchcooper2.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	421	155	http	TCP	GET	http://www.c-spline.com/images/searchcooper.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	420	155	http	TCP	GET	http://www.c-spline.com/images/cooperhome2.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	418	155	http	TCP	GET	http://www.c-spline.com/images/cooperhome.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	428	155	http	TCP	GET	http://www.c-spline.com/images/cooper-connection_02.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	429	155	http	TCP	GET	http://www.c-spline.com/images/cooper-connection_01.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	416	155	http	TCP	GET	http://www.c-spline.com/images/logo_sm.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	44.231.209.19	80	2453	271	16042	http	TCP	GET	http://www.c-spline.com/euserc.asp	text/html	Inet	200	0x42020000	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	428	155	http	TCP	GET	http://www.c-spline.com/images/Metering/Meterheader.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	433	155	http	TCP	GET	http://www.c-spline.com/images/Cooperc-spline/cprbline211.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	432	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/milonic_src.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	430	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/mmenudom.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:04	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	423	155	http	TCP	GET	http://www.c-spline.com/images/textbox_shadow.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:05	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	430	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/menu_data.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:05	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	417	155	http	TCP	GET	http://www.c-spline.com/images/whitend3.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:05	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	416	155	http	TCP	GET	http://www.c-spline.com/images/bee-gray.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:05	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	415	155	http	TCP	GET	http://www.c-spline.com/images/euserc.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.20.97	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Win32)	N	2006-11-16	00:00:07	w3proxy	ACME-PROXY	-	updaterservice.wildtangent.com	-	80	-	1480	2846	http	TCP	POST	http://updaterservice.wildtangent.com/updater/updatecheckin.wss	-	-	407	-	-	-
  10.54.20.97	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Win32)	N	2006-11-16	00:00:07	w3proxy	ACME-PROXY	-	updaterservice.wildtangent.com	-	80	-	1187	887	http	TCP	POST	http://updaterservice.wildtangent.com/updater/updatecheckin.wss	-	-	407	-	-	-
  10.54.20.97	ACME\capadonna	Mozilla/4.0 (compatible; MSIE 6.0; Win32)	Y	2006-11-16	00:00:07	w3proxy	ACME-PROXY	-	-	-	-	-	1716	-	-	TCP	POST	http://updaterservice.wildtangent.com/updater/updatecheckin.wss	-	-	12209	0x4	Internet Access	Block unproductive websites
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:09	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	6453	4587	14623	http	TCP	POST	http://145.27.59.156/campaign	text/html	Inet	200	0x40000004	Internet Access	Grant Access to all destinations
  10.54.70.45	anonymous	Acrobat Messages Updater	N	2006-11-16	00:00:09	w3proxy	ACME-PROXY	-	rms.adobe.com	-	80	-	224	2792	http	TCP	GET	http://rms.adobe.com/read/0600/win_/ENU/read0600win_ENUadbe0000.xml	-	-	407	-	-	-
  10.54.80.133	ACME\rgordon	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:10	w3proxy	ACME-PROXY	-	b.web.freemail.com	66.102.11.189	80	241844	1483	1410	http	TCP	GET	http://b.web.freemail.com/mail/channel/bind?at=d125f6cdf3da8331-10eebce9ebc&RID=rpc&SID=4E672078DDD815A7&CI=0&AID=1442&TYPE=html&zx=lr71ql-cphr5q&DOMAIN=web.freemail.com&t=1	text/html; charset=utf-8	Inet	200	0x42040001	Internet Access	Grant Access to all destinations
  10.54.80.133	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:10	w3proxy	ACME-PROXY	-	b.web.freemail.com	-	80	-	992	3093	http	TCP	GET	http://b.web.freemail.com/mail/channel/bind?at=d125f6cdf3da8331-10eebce9ebc&RID=rpc&SID=4E672078DDD815A7&CI=0&AID=1451&TYPE=html&zx=3ie2qj-xmlylo&DOMAIN=web.freemail.com&t=1	-	-	407	-	-	-
  10.54.80.133	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:10	w3proxy	ACME-PROXY	-	b.web.freemail.com	-	80	-	-	1837	http	TCP	GET	http://b.web.freemail.com/mail/channel/bind?at=d125f6cdf3da8331-10eebce9ebc&RID=rpc&SID=4E672078DDD815A7&CI=0&AID=1451&TYPE=html&zx=3ie2qj-xmlylo&DOMAIN=web.freemail.com&t=1	-	-	407	-	-	-
  10.54.70.99	anonymous	Acrobat Messages Updater	N	2006-11-16	00:00:12	w3proxy	ACME-PROXY	-	rms.adobe.com	-	80	-	224	2792	http	TCP	GET	http://rms.adobe.com/read/0600/win_/ENU/read0600win_ENUadbe0000.xml	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:12	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	700	2846	http	TCP	GET	http://145.27.59.156/campaign?jcid=1163599178318&redir=index.xxx?aid=campaign&&HH1=34&gg2=45&dd1=15&mm1=23&re1=2006&HH2=19&MM2=15&dd2=15&mm2=23&re2=2006&rcp=&name=Hope+6-510&desc=Hope+6-510&rtype=2&val=1&msg=Hope+6-510+return+to+service+%40+6%3A43pm+after+relay+disabled	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:12	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	1302	http	TCP	GET	http://145.27.59.156/campaign?jcid=1163599178318&redir=index.xxx?aid=campaign&&HH1=34&gg2=45&dd1=15&mm1=23&re1=2006&HH2=19&MM2=15&dd2=15&mm2=23&re2=2006&rcp=&name=Hope+6-510&desc=Hope+6-510&rtype=2&val=1&msg=Hope+6-510+return+to+service+%40+6%3A43pm+after+relay+disabled	-	-	407	-	-	-
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:12	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	172	956	259	http	TCP	GET	http://145.27.59.156/campaign?jcid=1163599178318&redir=index.xxx?aid=campaign&&HH1=34&gg2=45&dd1=15&mm1=23&re1=2006&HH2=19&MM2=15&dd2=15&mm2=23&re2=2006&rcp=&name=Hope+6-510&desc=Hope+6-510&rtype=2&val=1&msg=Hope+6-510+return+to+service+%40+6%3A43pm+aft	-	Inet	302	0x40000005	Internet Access	Grant Access to all destinations
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:13	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	465	2846	http	TCP	GET	http://145.27.59.156/campaign/web/MCstyle.css	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:13	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	1067	http	TCP	GET	http://145.27.59.156/campaign/web/MCstyle.css	-	-	407	-	-	-
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:13	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	422	721	172	http	TCP	GET	http://145.27.59.156/campaign/web/MCstyle.css	text/css	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:13	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	703	480	21834	http	TCP	GET	http://145.27.59.156/index.xxx?aid=campaign&pg=2.0	text/html	Inet	200	0x42000005	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:13	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	360	457	172	http	TCP	GET	http://145.27.59.156/clientscripts.js	text/javascript	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	442	155	http	TCP	GET	http://www.c-spline.com/styles/style.css	text/css	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	15	450	155	http	TCP	GET	http://www.c-spline.com/images/searchcooper2.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	449	155	http	TCP	GET	http://www.c-spline.com/images/searchcooper.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	20081.6-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	448	155	http	TCP	GET	http://www.c-spline.com/images/cooperhome2.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	446	155	http	TCP	GET	http://www.c-spline.com/images/cooperhome.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	456	155	http	TCP	GET	http://www.c-spline.com/images/cooper-connection_02.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	457	155	http	TCP	GET	http://www.c-spline.com/images/cooper-connection_01.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	444	155	http	TCP	GET	http://www.c-spline.com/images/logo_sm.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	445	155	http	TCP	GET	http://www.c-spline.com/images/products.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	461	155	http	TCP	GET	http://www.c-spline.com/images/Cooperc-spline/cprbline211.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	15	460	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/milonic_src.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	451	155	http	TCP	GET	http://www.c-spline.com/images/textbox_shadow.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	458	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/mmenudom.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	44.231.209.19	80	2641	347	24328	http	TCP	GET	http://www.c-spline.com/product/SearchProduct/search.asp?id=11	text/html	Inet	200	0x40020001	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	734	453	172	http	TCP	GET	http://145.27.59.156/scriptLib.js	text/javascript	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:14	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	458	155	http	TCP	GET	http://www.c-spline.com/Include/headers/menu/menu_data.js	application/x-javascript	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	445	155	http	TCP	GET	http://www.c-spline.com/images/whitend3.gif	image/gif	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	-	444	155	http	TCP	GET	http://www.c-spline.com/images/bee-gray.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.30.132	ACME\rross	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322)	Y	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	www.c-spline.com	-	80	16	446	155	http	TCP	GET	http://www.c-spline.com/images/blinelogo.jpg	image/jpeg	NotModified	0	0x1002	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	609	450	172	http	TCP	GET	http://145.27.59.156/common.js	text/javascript	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	360	452	172	http	TCP	GET	http://145.27.59.156/cssarrays.js	text/javascript	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	456	2846	http	TCP	GET	http://145.27.59.156/printstyles.css	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	3319	http	TCP	GET	http://145.27.59.156/images/Top_closed_arrow_down.gif	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	3304	http	TCP	GET	http://145.27.59.156/images/nav_02l.gif	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	3304	http	TCP	GET	http://145.27.59.156/images/nav_03l.gif	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	3304	http	TCP	GET	http://145.27.59.156/images/cleardot.gif	-	-	407	-	-	-
  10.54.35.2	anonymous	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	N	2006-11-16	00:00:15	w3proxy	ACME-PROXY	-	145.27.59.156	-	80	-	-	1058	http	TCP	GET	http://145.27.59.156/printstyles.css	-	-	407	-	-	-
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	437	450	172	http	TCP	GET	http://145.27.59.156/navpad.css	text/css	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	546	712	172	http	TCP	GET	http://145.27.59.156/printstyles.css	text/css	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	156	456	172	http	TCP	GET	http://145.27.59.156/images/nav_06.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	282	456	172	http	TCP	GET	http://145.27.59.156/images/navgo.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	266	456	172	http	TCP	GET	http://145.27.59.156/images/nav_13.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	453	456	172	http	TCP	GET	http://145.27.59.156/images/nav_14.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:16	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	453	577	172	http	TCP	GET	http://145.27.59.156/images/Top_closed_arrow_down.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	453	458	172	http	TCP	GET	http://145.27.59.156/images/nav_01.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  10.54.35.2	ACME\hizzo	Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)	Y	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	145.27.59.156	145.27.59.156	80	484	458	172	http	TCP	GET	http://145.27.59.156/images/cw_logo.gif	image/gif	VCache	304	0x1006	Internet Access	Grant Access to all destinations
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	890	160	-	http	TCP	GET	http://i.framp.com/images/global/brand/icons/viewlarger.gif	image/gif	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	906	160	-	http	TCP	GET	http://i.framp.com/images/global/brand/title/fragsolid2.gif	image/gif	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	891	155	-	http	TCP	GET	http://i.framp.com/images/global/masthead/nav_down.gif	image/gif	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	906	158	-	http	TCP	GET	http://i.framp.com/images/global/masthead/activetabbg.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	906	170	-	http	TCP	GET	http://i.framp.com/images/global/masthead/inactivetab_rightcorner.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	906	168	-	http	TCP	GET	http://i.framp.com/images/global/masthead/activetab_rightcorner.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	921	148	-	http	TCP	GET	http://i.framp.com/images/global/general/oo.gif	image/gif	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	921	160	-	http	TCP	GET	http://i.framp.com/images/global/masthead/inactivetabbg.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	921	155	-	http	TCP	GET	http://i.framp.com/images/global/masthead/mdabarbg.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.177	80	906	169	-	http	TCP	GET	http://i.framp.com/images/global/masthead/inactivetab_leftcorner.jpg	image/jpeg	VCache	304	0xa00000	-	-
  -	-	Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) Active Cache Request	N	2006-11-16	00:00:17	w3proxy	ACME-PROXY	-	i.framp.com	67.45.248.182	80	921	158	-	http	TCP	GET	http://i.framp.com/images/global/masthead/smlflags/jm.gif	image/gif	VCache	304	0xa00000	-	-



A description of the fields in the ISA Server 2000 version log files can be found `at this site. <http://msdn2.microsoft.com/en-us/library/ms813182.aspx>`_

A description of the fields in the ISA Server 2004 log files can be found `at this site.http://msdn2.microsoft.com/en-us/library/aa503237.aspx>`_ 

Other general information about ISA Server and ISA Server logs can be found at the following links:

`Official Microsoft site for ISA Server 2000 <http://www.microsoft.com/isaserver/prodinfo/previousversions/2000.mspx>`_

`Official Microsoft site for ISA Server 2004 <http://www.microsoft.com/isaserver/prodinfo/previousversions/2004.mspx>`_ 

`Official Microsoft site for ISA Server 2006 <http://www.microsoft.com/isaserver/default.mspx>`_

`Microsoft ISA Server Firewall Resource Site: Articles and Tutorials <http://www.isaserver.org>`_

` ISA Server 2000 Alerts, Reports and Logs FAQ <http://www.microsoft.com/technet/isa/2000/maintain/isafaqra.mspx>`_

`Configuring ISA Server 2000 log files <http://www.isaserver.org/tutorials/Configuring_ISA_Server_Log_Files.html>`_

`How to Configure Logging in ISA Server 2000 <http://support.microsoft.com/default.aspx?scid=kb;en-us;302372>`_

`ISA Server 2000 Monitoring Concepts: Logging <http://www.microsoft.com/technet/isa/2000/proddocs/isadocs/cmt_logintro.mspx>`_

`ISA Server 2000 Packet Filtering <http://www.microsoft.com/technet/isa/2000/proddocs/isadocs/m_p_c_allowblock.mspx>`_

`About the ISA Server 2000 Firewall <http://msdn2.microsoft.com/en-us/library/ms811785.aspx>`_ 

`ISA Server 2004 best practices: Logging <http://www.microsoft.com/technet/isa/2004/plan/logging-best-practices.mspx>`_

`Description of the time format used in ISA Server 2004 logs <http://support.microsoft.com/kb/887005>`_

`ISA Server 2004 Monitoring Concepts:Logs <http://www.microsoft.com/technet/isa/2004/help/FW_LogOver.mspx>`_

`ISA Server 2004 Log Code Values <http://www.microsoft.com/technet/isa/2004/help/FW_LogCodeHead.mspx>`_

`Understanding ISA Server 2004 Monitoring <http://www.isaserver.org/tutorials/Understanding-ISA-2004-Monitoring-Part1.html>`_

`ISA Server 2006 Logging Fields and Values <http://www.microsoft.com/technet/isa/2006/Logging_Reference.mspx>`_ 

