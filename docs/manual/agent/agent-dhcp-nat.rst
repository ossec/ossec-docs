.. manual-agent-dhcp-nat::

Agent systems behind NAT or with dynamic IPs (DHCP)
===================================================

If you want to install the agent on systems without a static IP address or 
behind a NAT device, you need to configure the agent using variable IP addresses. 

It means that when the :ref:`manage_agents` tool asks you for an IP, you will give the 
IP and netmask instead of a unique IP.

Setup Examples 
--------------


DHCP Example 
~~~~~~~~~~~~

For example, to add an agent that can receive any IP address (say via DHCP) 
in the 192.168.2.0/24 network, just provide the IP address of the agent as 
192.168.2.0/24. Example (taken from manage_agents): 

.. code-block:: console 

    Please provide the following:
    * A name for the new agent: test
    * The IP Address of the new agent: 192.168.2.0/24


NAT Example 
~~~~~~~~~~~

The same applies to NATed systems. Since the OSSEC server will see all devices 
behind NAT as if they had the same IP, you need to configure them with a variable 
IP address.

For example, lets say that you have systems 192.168.1.2, 192.168.1.3 and 
192.168.1.4 behind a nat server that connects to network 10.1.1.0/24 with 
the ossec server on it. 

In this case, you need to config the agents as if their IP was 10.1.1.0/24, 
because this is the IP that the server is seeing (not their original IP).

On the :ref:`manage_agents` tool, add each one of those agents on the server using 
the following format:

.. code-block:: console 

    Please provide the following:
    * A name for the new agent: agent-1
    * The IP Address of the new agent: 10.1.1.0/24


.. note:: 

    Since the ossec server is going to see them as if they were coming 
    from the nat server (10.1.1.x ip), it should work. Make sure to use one 
    separate key for each agent.
