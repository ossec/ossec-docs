
.. _manual_agent_manage:

Managing Agents 
===============

To add an agent to an OSSEC manager with :ref:`manage_agents` you need to follow the steps below.

1. Run manage_agents on the OSSEC server.
2. Add an agent.
3. Extract the key for the agent.
4. Copy that key to the agent.
5. Run manage_agents on the agent.
6. Import the key copied from the manager.
7. Restart the manager's OSSEC processes.
8. Start the agent.


manage_agents on the OSSEC server
---------------------------------

The server version of manage_agents provides an interface to:

- add an OSSEC agent to the OSSEC server
- extract the key for an agent already added to the OSSEC server
- remove an agent from the OSSEC server
- list all agents already added to the OSSEC server.


Running manage_agents and start screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``manage_agents`` should be run as a user with 
the appropriate privileges (e.g. root).

Run ``manage_agents``:

.. code-block:: console

    # /var/ossec/bin/manage_agents

The manage_agents menu:

.. code-block:: console

    ****************************************
    * OSSEC HIDS v2.5-SNP-100809 Agent manager.     *
    * The following options are available: *
    ****************************************
       (A)dd an agent (A).
       (E)xtract key for an agent (E).
       (L)ist already added agents (L).
       (R)emove an agent (R).
       (Q)uit.
    Choose your action: A,E,L,R or Q:

Typing the appropriate letter and hitting enter will initiate that function.

Adding an agent
^^^^^^^^^^^^^^^

To add an agent type ``a`` in the start screen:

.. code-block:: console

    Choose your action: A,E,L,R or Q: a

You are then prompted to provide a name for the new agent.
This can be the hostname or another string to identify the system. 
In this example the agent name will be agent1.

.. code-block:: console

    - Adding a new agent (use '\q' to return to the main menu).
      Please provide the following:
       * A name for the new agent: agent1

After that you have to specify the IP address for the agent. This can either be a single 
IP address (e.g. 192.168.1.25), a range of IPs (e.g. 192.168.2.0/24), or ``any``. Using a 
network range or ``any`` is preferable when the IP of the agent may change frequently  
(DHCP), or multiple systems will appear to come from the same IP address (NAT).

.. code-block:: console

       * The IP Address of the new agent: 192.168.2.0/24

.. warning::

   If you use a specific IP address it **must** be unique. Duplicate IP addresses will cause issues.
   Multiple systems can use the same IP range or ``any``.


The last information you will be asked for is the ID you want to assign to the agent. 
:ref:`manage_agents` will suggest a value for the ID. This value should be the lowest positive 
number that is not already assigned to another agent. The ID 000 is assigned to the 
OSSEC server. To accept the suggestion, simply press ENTER. To choose another value, 
type it in and press ENTER.

.. code-block:: console

       * An ID for the new agent[001]:

As the final step in creating an agent, you have to confirm adding the agent:

.. code-block:: console

    Agent information:
       ID:002
       Name:agent1
       IP Address:192.168.2.0/24

    Confirm adding it?(y/n): y
    Agent added.

After that :ref:`manage_agents` appends the agent information to /var/ossec/etc/client.keys 
and goes back to the start screen.

.. warning::

   If this is the first agent added to this server, the server's OSSEC processes should be restarted using ``/var/ossec/bin/ossec-control restart``.


Extracting the key for an agent
-------------------------------

After adding an agent, a key is created. This key must be copied to the agent. 
To extract the key, use the ``e`` option in the manage_agents start screen. You will be 
given a list of all agents on the server. To extract the key for an agent, 
simply type in the agent ID. It is important to note that you have 
to enter all digits of the ID.

.. code-block:: console

    Choose your action: A,E,L,R or Q: e

    Available agents: 
       ID: 001, Name: agent1, IP: 192.168.2.0/24
    Provide the ID of the agent to extract the key (or '\q' to quit): 001

    Agent key information for '001' is: 
    MDAyIGFnZW50MSAxOTIuMTY4LjIuMC8yNCBlNmY3N2RiMTdmMTJjZGRmZjg5YzA4ZDk5m

    ** Press ENTER to return to the main menu.

The key is encoded in the string (shortened for this example)
``MDAyIGFnZW50MSAxOTIuMTY4LjIuMC8yNCBlNmY3N2RiMTdmMTJjZGRmZjg5YzA4ZDk5Mm`` 
and includes information about the agent. This string can be added to the agent through the agent version of 
``manage_agents``.

Removing an agent
-----------------

If you want to remove an OSSEC agent from the server, use the ``r`` option in the :ref:`manage_agents`
start screen. You will be given a list of all agents already added to the server. To remove 
an agent, simply type in the ID of the agent, press enter, and finally confirm the deletion. 
It is important to note that you have to enter all digits of the ID.

.. code-block:: console

    Choose your action: A,E,L,R or Q: e

    Available agents: 
       ID: 001, Name: agent1, IP: 192.168.2.0/24
    Provide the ID of the agent to extract the key (or '\q' to quit): 001
    Confirm deleting it?(y/n): y
    Agent '001' removed.

``manage_agents`` then invalidates the agent information in 
``/var/ossec/etc/client.keys``. Only the values for ID and the key are kept to 
avoid conflicts when adding agents. The deleted agent can no longer 
communicate with the OSSEC server.


manage_agents on OSSEC agents
------------------------------

The agent version provides an interface for importing authentication keys.

.. code-block:: console

    ****************************************
    * OSSEC HIDS v2.5-SNP-100809 Agent manager.     *
    * The following options are available: *
    ****************************************
       (I)mport key from the server (I).
       (Q)uit.
    Choose your action: I or Q: i

    * Provide the Key generated by the server.
    * The best approach is to cut and paste it.
    *** OBS: Do not include spaces or new lines.

    Paste it here (or '\q' to quit): [key extracted via manage_agents on the server]

    Agent information:
       ID:001
       Name:agent1
       IP Address:192.168.2.0/24

    Confirm adding it?(y/n): y
    Added.
    ** Press ENTER to return to the main menu.


For the changes to be in effect you have to 
restart the server and start the agent.





