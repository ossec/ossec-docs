.. manual-agent-dhcp-nat::

Agent systems behind NAT or with dynamic IPs (DHCP)
===================================================

If you want to install the agent on systems without a static IP address or 
behind a NAT device, you need to configure the agent using a CIDR address or 
the ip address of ``any``.



DHCP Example 
~~~~~~~~~~~~

To add an agent that can receive any IP address
in the 192.168.2.0/24 network, just provide the IP address of the agent as 
192.168.2.0/24. Example (taken from manage_agents): 

.. code-block:: console 

    Please provide the following:
    * A name for the new agent: test
    * The IP Address of the new agent: 192.168.2.0/24


NAT Example 
~~~~~~~~~~~

The same applies to systems behind a NAT device. 
The OSSEC server will see all agents behind the NAT as if they have the 
same IP address.

For example, you have systems 192.168.1.2, 192.168.1.3 and 
192.168.1.4 behind a nat server that connects to network 10.1.1.0/24 with 
the ossec server on it. 

In this case, you need to config the agents as if their IP was 10.1.1.0/24, 
because this is the IP that the server is seeing (not their original IP).
Using ``any`` instead of an IP address or range is also a valid option, allowing 
the agent to connect from any IP address.

On the :ref:`manage_agents` tool, add each one of those agents on the server using 
the following format:

.. code-block:: console 

    Please provide the following:
    * A name for the new agent: agent-1
    * The IP Address of the new agent: 10.1.1.0/24


.. code-block:: console 

    Please provide the following:
    * A name for the new agent: agent-2
    * The IP Address of the new agent: any

.. note:: 

    Make sure to use one separate key for each agent.

