
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

.. option:: -V

    Display OSSEC Version.

.. option:: -h

    Display the help message.

.. option:: -l

    List available agents.

.. option:: -e <agent_id>

    Extracts key for an agent (Manager only).

.. option:: -r <agent_id>

    Remove an agent (Manager only).

.. option:: -i <key>

    Import authentication key (Agent only).

.. option:: -f  <file>

    Generate clients in bulk from <file> (Manager only). The file is a comma delimited file containing the IP addresses and agent names to be added.
    This file should be located within ``/var/ossec``, and referenced by its path relative to ``/var/ossec``.

**Example:**

.. code-block:: console

   # cat /var/ossec/k
   192.168.1.2,host02
   192.168.1.3,host03

   # /var/ossec/bin/manage_agents -f /k
   Bulk load file: /k
   Opening: [/k]
   Agent information:
      ID:002
      Name:host02
      IP Address:192.168.1.2

   Agent added.
   Agent information:
      ID:003
      Name:host03
      IP Address:192.168.1.3

   Agent added.


Usage
-----

The OSSEC manual goes into details on usage of this command at :ref:`manual_agent_manage`
