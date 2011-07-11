
.. _ossec-authd:

ossec-authd
=============

The ossec-authd daemon will automatically add an agent to an OSSEC manager and provide the key to the agent.
The :ref:`agent-auth` application is the client application used with ossec-authd.

There is no authentication involved in this transaction, so it is recommended that this daemon only be run when a new agent is being added.

agent_control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-authd

.. option:: -d

    Run in debug mode.

.. option:: -p <port>

   Listen on port.
   **Default** 1515


ossec-authd example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example: Running ossec-authd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/ossec-authd -p 1515 >/dev/null 2>&1 &

And the logs when an agent is added:

.. code-block:: console

    2011/01/19 15:04:40 ossec-authd: INFO: New connection from 192.168.10.5
    2011/01/19 15:04:41 ossec-authd: INFO: Received request for a new agent (example-agent) from: 192.168.10.5
    2011/01/19 15:04:41 ossec-authd: INFO: Agent key generated for example-agent (requested by 192.168.10.5)
    2011/01/19 15:04:41 ossec-authd: INFO: Agent key created for example-agent (requested by 192.168.10.5) 


