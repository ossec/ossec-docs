How to configure ossec to never block some IPs in the active response
---------------------------------------------------------------------

OSSEC by default white lists localhost and your name servers. 
To add more IPs to the white list, so they will never be blocked, just 
add a new ``white_list`` entry inside the ``global`` section. 


White list an IP and a network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, the 10.1.0.0/16 network and IP 1.2.3.4 will not be blocked:

.. code-block:: console
  <global>
    <white_list>127.0.0.1</white_list>
    <white_list>10.1.0.0/16</white_list>
    <white_list>1.2.3.4</white_list>
  </global>



CIDR addresses can also be used to white list whole networks:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  <global>
    <white_list>192.168.2.0/24</white_list>
    <white_list>10.0.0.0/8</white_list>
  </global>



For DNS servers
^^^^^^^^^^^^^^^

For some DNS servers it might be a good idea to ignore all the DNS root servers, so they are never blocked:

.. code-block:: console
  <white_list>198.41.0.4</white_list>
  <white_list>192.228.79.201</white_list>
  <white_list>192.33.4.12</white_list>
  <white_list>128.8.10.90</white_list>
  <white_list>192.203.230.10</white_list>
  <white_list>192.5.5.241</white_list>
  <white_list>192.112.36.4</white_list>
  <white_list>128.63.2.53</white_list>
  <white_list>192.36.148.17</white_list>
  <white_list>192.58.128.30</white_list>
  <white_list>193.0.14.129</white_list>
  <white_list>198.32.64.12</white_list>
  <white_list>202.12.27.33</white_list>


