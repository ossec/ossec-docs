
.. _list_agents:

list_agents
===========

OSSEC HIDS list_agents: List available agents.

list_agents is only available on OSSEC servers or local mode installations. 
It can be used to retrieve

- a list of all OSSEC agents that successfully connected to the server in the past
- a list of all OSSEC agents currently connected to the server
- a list of all OSSEC agents that were connected to the server in the past but are currently not connected.

If an agent was added via the :ref:`manage_agents` tool but has not yet been connected to the server, it will not show up in the output of list_agents.

list_agents argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: manage_agents 

.. option:: -h

    Display the help message.

.. option:: -a

    List all agents.

.. option:: -c

    List the connected (active) agents.

.. option:: -n

    List the not connected (active) agents.
