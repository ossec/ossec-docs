Log samples from PF 
-------------------

Various versions of PF currently run on OpenBSD, FreeBSD, NetBSD, DragonflyBSD, and Mac OS X 10.6. For details on how to configure it, check `the pf FAQ <http://www.openbsd.org/faq/pf/logging.html>`_ 

.. code-block:: console

  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.793256 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815379950 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.815208 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815379973 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.844763 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380002 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.867973 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380026 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.892592 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380050 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.916465 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380074 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.945039 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380102 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.966970 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2450721 win 73 <nop,nop,timestamp 1815380125 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:53:25.968177 rule 2/(match) pass in on xl0: 205.174.165.231.50425 > 192.168.2.10.22: . ack 2451361 win 73 <nop,nop,timestamp 1815380125 17589621,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:54:39.257554 rule 3/(match) pass out on xl0: 192.168.2.10.22 > 205.174.165.231.56038: . ack 53376 win 16416 <nop,nop,timestamp 4232982920 1815453138,[|tcp]> (DF) [tos 0x10]
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.265470 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 57
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.267876 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 57
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.270532 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 73
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.273141 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.275813 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.278266 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.281040 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.283846 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.286602 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 105
  Mar 30 15:55:20 enigma pf: Mar 30 15:55:14.289160 rule 3/(match) pass out on xl0: 192.168.2.10.1514 > 192.168.2.26.3875:  udp 97
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:02.810188 rule 2/(match) pass in on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo reply
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:03.688233 rule 3/(match) pass out on xl0: 192.168.2.10 > 192.168.2.1: icmp: 192.168.2.10 udp port 137 unreachable
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:03.820068 rule 3/(match) pass out on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo request
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:03.820087 rule 2/(match) pass in on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo request
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:03.820115 rule 3/(match) pass out on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo reply
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:03.820129 rule 2/(match) pass in on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo reply
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:04.830069 rule 3/(match) pass out on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo request
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:04.830088 rule 2/(match) pass in on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo request
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:04.830118 rule 3/(match) pass out on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo reply
  Mar 30 15:55:19 enigma pf: Mar 30 15:48:04.830132 rule 2/(match) pass in on lo0: 127.0.0.1 > 127.0.0.1: icmp: echo reply



