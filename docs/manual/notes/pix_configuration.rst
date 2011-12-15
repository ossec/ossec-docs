How to configure PIX and OSSEC
------------------------------

by Dale Neufeld <canuck.eh ( at ) gmail.com>

This is a very basic setup and the PIX offers a lot more options for syslog configuration including using a different port.


1. Configuring syslog on the PIX


PIX 6.3 commands
http://www.cisco.com/en/US/products/sw/secursw/ps2120/products_system_message_guide_chapter09186a008051a0cc.html#wp1029066

.. code-block:: console

  logging on
  no logging device-id
  no logging timestamp
  logging trap warning (see note 1.1 below for options)
  logging host interface ipaddress


1.1 Logging Trap Options

.. code-block:: console

  Level Number
	
  Level         Keyword
  0   	 	emergency 
  1             alert
  2             critical
  3             error
  4             warning
  5             notification
  6             informational
  7             debugging 


2. Ensure your OSSEC host is seeing the PIX syslog messages

.. code-block:: console

  # tcpdump -i eth0 -A -s 0 udp port 514 and host <pix_ip>


3. Configure OSSEC to listen

Add the following to ossec.conf

.. code-block:: console

  <remote>
     <connection>syslog</connection>
     <allowed-ips>192.168.2.1</allowed-ips>  <!--ip addr of the device-->
     <port>514</port>
  </remote>


 
4. Restart the ossec service to begin listening

.. code-block:: console

  # /var/ossec/bin/ossec-control restart


