.. _manual-agents:

Agents 
====== 

There are two types of agents within OSSEC: installable agents and agentless 
agents.  Installable agents are installed on hosts, and they report back to 
a central OSSEC server via the OSSEC encrypted message protocol.  Agentless 
agents require no installation on remote hosts. They are processes initiated 
from the OSSEC manager, which gather information from remote systems, and use 
any RPC method (e.g. ssh, snmp rdp, wmi).


**Agent**

.. toctree::
    :maxdepth: 2

    agent-management
    agent-dhcp-nat
    agent-auth
    agent-configuration

**Agentless** 

.. toctree::
    :maxdepth: 2

    agentless-monitoring
    agentless-scripts



    

