.. _agent_auth:



Adding an agent with ossec-authd
================================

It is possible to add a key to a system via an automated method. 
`ossec-authd <../../programs/ossec-authd.html>`_ and `agent-auth <../../programs/agent-auth.html>`_ provide this functionality.


ossec-authd
^^^^^^^^^^^

``ossec-authd`` will run on the server adding agents and distributing authentication keys. 
There is currently no authentication, so any host that can cannot to the port ossec-authd listens to can obtain an OSSEC agent key.
It is recommended that the OSSEC manager's firewall be used to help limit connections.


Run ossec-authd, listening on port 1515:

.. code-block:: console

   /var/ossec/bin/ossec-authd -p 1515 > /dev/null 2>&1&



agent-auth

