Cisco ASA Log Samples
---------------------


Authentication rejected (failed password):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Format:

.. code-block:: console

  MMM DD HH:MM:SS ASA.FQDN %ASA-6-113005: AAA user authentication Rejected : reason = Invalid password : server =  AUTHSERVER.IP : user = USERNAME 

Example:

.. code-block:: console

  Jan  8 09:12:56 asa.example.com %ASA-6-113005: AAA user authentication Rejected : reason = Invalid password : server = 192.168.0.1 : user = testuser



Authentication Successful:
^^^^^^^^^^^^^^^^^^^^^^^^^^

Format:

.. code-block:: console

  MMM DD HH:MM:SS ASA.FQDN %ASA-6-113004: AAA user authentication Successful : server =  AUTHSERVER.IP : user = USERNAME


Example:

.. code-block:: console

  Jan  8 09:12:56 asa.example.com %ASA-6-113004: AAA user authentication Successful : server =  192.168.0.1 : user = testuser



