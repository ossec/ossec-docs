
.. _agent_control:

agent_control
=============

The agent_control tool allows you to query and get information from any agent you have configured 
on your server and it also allows you to restart (run now) the syscheck/rootcheck scan on any agent.

Enabling `active response <../manual/ar/index.html>`_ will be necessary to start scans remotely and possibly other functions.

agent_control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: agent_control 

.. option:: -h

    Display the help message 

.. option:: -l 

    List available (active or not) agents 

.. option:: -lc

    List active agents 

.. option:: -i <agent_id>

    Extracts information from an agent 

.. option:: -R <agent_id>

    Restarts the OSSEC processes on the agent

    .. note::
       Requires active response to be enabled.

.. option:: -r 

    Run the integrity/rootcheck checking on agents.  Must be utilized 
    with :option:`agent_control -a` or :option:`agent_control -u`

    .. note::
       Requires active response to be enabled.

.. option:: -a

    Utilizes all agents.

.. option:: -u <agent_id>

    <agent_id> that will perform the requested action. 


agent_control example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Listing all active agents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first interesting argument is :option:`agent_control -lc`, to list the connected (active agents). To list 
all of them, use :option:`agent_control -l` only.

.. code-block:: console 

    # /var/ossec/bin/agent_control -lc
    OSSEC HIDS agent_control. List of available agents:
    ID: 000, Name: enigma.ossec.net (server), IP: 127.0.0.1, Active/Local
    ID: 002, Name: winhome, IP: 192.168.2.190, Active
    ID: 005, Name: jul, IP: 192.168.2.0/24, Active
    ID: 165, Name: esqueleto2, IP: 192.168.2.99, Active
    ID: 174, Name: lili3win, IP: 192.168.2.0/24, Active 

Example 2: Querying information from agent 002 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To query an agent, just use the :option:`agent_control -i` option followed by the agent id.

.. code-block:: console 

    # /var/ossec/bin/agent_control -i 002

    OSSEC HIDS agent_control. Agent information:
    Agent ID: 002
    Agent Name: winhome
    IP address: 192.168.2.190
    Status: Active

    Operating system: Microsoft Windows XP Professional (Build 2600)
    Client version: OSSEC HIDS v1.5-SNP-080412
    Last keep alive: Fri Apr 25 14:33:03 2008

    Syscheck last started at: Fri Apr 25 05:07:13 2008
    Rootcheck last started at: Fri Apr 25 09:04:12 2008

Example 3: Executing syscheck and rootcheck scan immediately
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To execute the syscheck/rootcheck scan immediately, use the :option:`agent_control -r` 
option followed by the :option:`agent_control -u` with the agent id.

.. code-block:: console 

    # /var/ossec/bin/agent_control -r -u 000

    OSSEC HIDS agent_control: Restarting Syscheck/Rootcheck locally.


