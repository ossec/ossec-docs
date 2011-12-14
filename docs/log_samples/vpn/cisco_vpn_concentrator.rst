Cisco VPN Concentrator Log Samples
----------------------------------


Authentication rejection (failed password):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Format:

.. code-block:: console
  MMM DD HH:MM:SS VPN.FQDN 11504 MM/DD/YYYY HH:MM:SS.780 SEV=3 AUTH/5 RPT=124 SRCIP  Authentication rejected: Reason = Unspecified handle = 805, server = AUTHSERVER.FQDN, user = USERNAME, domain = <not specified> 


Example:

.. code-block:: console
  Jan  8 09:10:37 vpn.example.com 11504 01/08/2007 09:10:37.780 SEV=3 AUTH/5 RPT=124 192.168.0.1  Authentication rejected: Reason = Unspecified handle = 805, server = auth.example.com, user = testuser, domain = <not specified>


Remote peer has failed user authentication (three password failures in a row):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Format:

.. code-block:: console
  MMM DD HH:MM:SS VPN.FQDN 562402 MM/DD/YYYY HH:NN:SSS.500 SEV=4 IKE/167 RPT=240 SRCIP  Group [GROUP] User [USERNAME] Remote peer has failed user authentication - check configured username and password


Example:


.. code-block:: console
  Jan  8 07:43:31 vpn.example.com 562402 01/19/2007 07:43:28.500 SEV=4 IKE/167 RPT=240 192.168.0.1  Group [VPNFull] User [testuser] Remote peer has failed user authentication - check configured username and password



