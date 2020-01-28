Log Samples from Racoon VPN
---------------------------

*submited by Charles (kef_list <kef_list@ibacom.es>) to the Ossec List.



Good login:
^^^^^^^^^^^

.. code-block:: console

  2006-08-10 19:22:40: INFO: respond new phase 1 negotiation: 111.111.111.194[500]<=>83.36.51.44[500]
  2006-08-10 19:22:40: INFO: begin Aggressive mode.
  2006-08-10 19:22:40: INFO: received Vendor ID: draft-ietf-ipsec-nat-t-ike-02
  2006-08-10 19:22:41: INFO: ISAKMP-SA established 111.111.111.114[500]-83.36.51.44[500] spi:3ac2d5023f433d3e:e2d682b6f4fc4830
  2006-08-10 19:22:42: INFO: respond new phase 2 negotiation: 111.111.111.194[0]<=>83.36.51.44[0]
  2006-08-10 19:22:42: INFO: no policy found, try to generate the policy : 10.0.1.5/32[0] 10.15.13.224/27[0] proto=any dir=in
  2006-08-10 19:22:42: INFO: IPsec-SA established: ESP/Tunnel 83.36.51.44->111.111.111.194 spi=188599340(0xb3dcc2c)
  2006-08-10 19:22:42: INFO: IPsec-SA established: ESP/Tunnel 111.111.111.194->83.36.51.44 spi=19221256(0x1254b08)
  2006-08-10 19:22:42: ERROR: such policy does not already exist: 10.0.1.5/32[0] 10.15.13.224/27[0] proto=any dir=in
  2006-08-10 19:22:42: ERROR: such policy does not already exist: 10.0.1.5/32[0] 10.15.13.224/27[0] proto=any dir=fwd
  2006-08-10 19:22:42: ERROR: such policy does not already exist: 10.15.13.224/27[0] 10.0.1.5/32[0] proto=any dir=out


This line indicates that the initial phase 1 auth (pskeys or certificates) have been exchanged correctly:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2006-08-10 19:22:41: INFO: ISAKMP-SA established 111.111.111.194 [500]-83.36.51.44[500] spi:3ac2d5023f433d3e:e2d682b6f4fc4830


The other two lines to notice, and the ones that definetly say we have a new VPN established are:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2006-08-10 19:22:42: INFO: IPsec-SA established: ESP/Tunnel 83.36.51.44->111.111.111.194 spi=188599340(0xb3dcc2c)
  2006-08-10 19:22:42: INFO: IPsec-SA established: ESP/Tunnel 111.111.111.194->83.36.51.44 spi=19221256(0x1254b08)


(there are two, one for incomming traffic, another for outgoing
traffic).


Strangely enough the last 3 errror lines are NOT errors. They are
caused because I am using a "roadwarrior" configuration where
connections are allowed from variable IP addresses as opposed to the
tipical VPN between two static IPs. They simply indicate that racoon
as automatically created security policies for those IPs (and both
sides are behind NAT).


Another sample of GOOD login (in this case between two static IPs)


.. code-block:: console

  2006-02-19 11:09:25: INFO: respond new phase 1 negotiation: 80.34.246.154[500]<=>217.127.190.50[500]
  2006-02-19 11:09:25: INFO: begin Identity Protection mode.
  2006-02-19 11:09:26: WARNING: ignore INITIAL-CONTACT notification, because it is only accepted after phase1.
  2006-02-19 11:09:26: INFO: ISAKMP-SA established 80.34.246.154 [500]-217.127.190.50[500] spi:bc013ca51d1a8745:9b95e47f6705088b
  2006-02-19 11:09:26: INFO: respond new phase 2 negotiation: 80.34.246.154[0]<=>217.127.190.50[0]
  2006-02-19 11:09:27: INFO: IPsec-SA established: ESP/Tunnel 217.127.190.50->80.34.246.154 spi=87487840(0x536f560)
  2006-02-19 11:09:27: INFO: IPsec-SA established: ESP/Tunnel 80.34.246.154->217.127.190.50 spi=1290938215(0x4cf22767)


As you can see the last two lines are identical as the first case.


WARNING: in both samples they represent a "tunnel" configuration. I
do not know what they would look like in "transport" mode....



Now here are some samples of FAILLED logins from hackers trying to get in:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2006-08-08 01:42:08: INFO: respond new phase 1 negotiation: 111.111.111.194[500]<=>222.155.15.88[500]
  2006-08-08 01:42:08: INFO: begin Identity Protection mode.
  2006-08-08 01:42:08: INFO: received Vendor ID: MS NT5 ISAKMPOAKLEY
  2006-08-08 01:42:09: ERROR: couldn't find the pskey for 222.155.15.88.
  2006-08-08 01:42:09: ERROR: failed to process packet.
  2006-08-08 01:42:09: ERROR: phase1 negotiation failed.
  2006-08-08 01:43:12: ERROR: unknown Informational exchange received.

The interesting line is:

.. code-block:: console

  2006-08-08 01:42:09: ERROR: couldn't find the pskey for 222.155.15.88. 

Also, there is no INFO: ISAKMP-SA established... line because phase 1
has failed.



Here is another case of invalid login, this time the errors are
caused because the hacker has used different settings for the many
options that need to be set the same way on both sides to establish a
VPN

.. code-block:: console

  2006-07-22 08:19:43: INFO: respond new phase 1 negotiation: 
  2006-07-22 08:19:43: INFO: begin Identity Protection mode.
  2006-07-22 08:19:43: INFO: received Vendor ID: MS NT5 ISAKMPOAKLEY
  2006-07-22 08:19:43: ERROR: invalid attribute type 32001.
  2006-07-22 08:19:43: ERROR: invalid attribute type 32001.
  2006-07-22 08:19:43: ERROR: invalid attribute type 32001.
  2006-07-22 08:19:43: ERROR: invalid attribute type 32001.
  2006-07-22 08:19:43: ERROR: rejected authmethod: DB (prop#1:trns#1):Peer(prop#1:trns#2) = pre-shared key:GSS-API on Kerberos 5
  2006-07-22 08:19:43: ERROR: rejected authmethod: DB (prop#1:trns#1):Peer(prop#1:trns#4) = pre-shared key:GSS-API on Kerberos 5
  2006-07-22 08:19:43: ERROR: rejected hashtype: DB(prop#1:trns#1):Peer (prop#1:trns#4) = SHA:MD5
  2006-07-22 08:19:43: ERROR: rejected enctype: DB(prop#1:trns#1):Peer (prop#1:trns#6) = 3DES-CBC:DES-CBC
  2006-07-22 08:19:43: ERROR: rejected authmethod: DB (prop#1:trns#1):Peer(prop#1:trns#6) = pre-shared key:GSS-API on Kerberos 5
  2006-07-22 08:19:43: ERROR: rejected dh_group: DB(prop#1:trns#1):Peer (prop#1:trns#6) = 1024-bit MODP group:768-bit MODP group
  2006-07-22 08:19:43: ERROR: rejected enctype: DB(prop#1:trns#1):Peer (prop#1:trns#8) = 3DES-CBC:DES-CBC
  2006-07-22 08:19:43: ERROR: rejected authmethod: DB (prop#1:trns#1):Peer(prop#1:trns#8) = pre-shared key:GSS-API on Kerberos 5
  2006-07-22 08:19:43: ERROR: rejected hashtype: DB(prop#1:trns#1):Peer (prop#1:trns#8) = SHA:MD5
  2006-07-22 08:19:43: ERROR: rejected dh_group: DB(prop#1:trns#1):Peer (prop#1:trns#8) = 1024-bit MODP group:768-bit MODP group
  2006-07-22 08:19:43: ERROR: no suitable proposal found.
  2006-07-22 08:19:43: ERROR: failed to get valid proposal.
  2006-07-22 08:19:43: ERROR: failed to process packet.


