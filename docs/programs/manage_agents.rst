
.. _manage_agents:

manage_agents
=============

manage_agents is available in two versions:

- a version for OSSEC server installations
- a version for OSSEC agent installations

The purpose of manage_agents is to provide an easy-to-use interface to handle authentication 
keys for OSSEC agents. These authentication keys are required for secure (encrypted and 
authenticated) communication between the OSSEC server and its affiliated agent instances.

manage_agents argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: manage_agents 

.. option:: -h

    Display the help message 

.. option:: -V 

    Display OSSEC Version 

.. option:: -l 

    List available agents. 

.. option:: -e <id> 

    Extracts key for an agent (Manager only).

.. option:: -i <id> 

    Import authentication key (Agent only). 

Usage 
-----

The OSSEC manual goes into details on usage of this command at :ref:`manual_agent_manage`

