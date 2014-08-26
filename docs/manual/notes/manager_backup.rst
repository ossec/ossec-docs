Migrating/backing up the manager
--------------------------------

If you need to migrate the manager to another system (or just want to backup the current setup), these are the files you need:

These are the two locations where the keys are saved for all the agents.

.. code-block:: console

  /var/ossec/etc/client.keys
  /var/ossec/queue/rids/ 

These are the configuration files you may want to keep 

.. code-block:: console

  /var/ossec/etc/*.conf
  /var/ossec/rules
  /var/ossec/etc/*.xml
  /var/ossec/etc/shared/agent.conf


These are the databases where we store data for the agents.

.. code-block:: console

  /var/ossec/queue/syscheck
  /var/ossec/queue/rootcheck
  /var/ossec/queue/fts
  /var/ossec/queue/agentless

Logs stored if they are needed.

.. code-block:: console

  /var/ossec/logs
