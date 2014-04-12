
.. _agent-auth:

agent-auth
=============

The agent-auth program is the client application used with :ref:`ossec-authd` to automatically add agents to an OSSEC manager.

.. warning:

    There is no authentication or authorization involved in this transaction, so it is recommended that 
    this daemon only be run when a new agent is being added.

agent-auth argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: agent-auth

.. option:: -h

    Display the help message 

.. option:: -m <manager_ip>

    IP address of the manager.

.. option:: -p <port>

    Port ossec-authd is running on.
    **Default** 1515

.. option:: -A <agent_name>

    Agent name to be used.
    **Default** hostname

.. option:: -D

    Directory where OSSEC is installed.
    **Default** /var/ossec


agent-auth example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example: Adding an agent with a hostname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/agent-auth -m 192.168.1.1 -p 1515 -A example-agent
    INFO: Connected to 192.168.1.1:1515
    INFO: Using agent name as: melancia
    INFO: Send request to manager. Waiting for reply.
    INFO: Received response with agent key
    INFO: Valid key created. Finished.
    INFO: Connection closed. 



