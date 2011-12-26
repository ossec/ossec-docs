.. _ossec_101_install_agent_linux:


OSSEC 101: Installing a Linux Agent
-----------------------------------

Things to keep in mind:
^^^^^^^^^^^^^^^^^^^^^^^

Just like the server installation most of the agent OSSEC processes chroot themselves to ``/var/ossec``. Unlike the server version, an agent installation does not store as many logs. The main logs are ``/var/ossec/logs/ossec.log`` and ``/var/ossec/logs/active-responses.log`` if you are using active response. Be sure to allow ample space for these log files.


Installation process:
^^^^^^^^^^^^^^^^^^^^^



Importing the agent key:
^^^^^^^^^^^^^^^^^^^^^^^^






