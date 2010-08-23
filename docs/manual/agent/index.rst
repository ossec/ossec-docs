.. _manual-agents:

Agents 
====== 

Their are two types of agents within OSSEC: agents/agentless.  Agents are full 
installation on many servers that report back to a central OSSEC server utlizing 
OSSEC encryped message protocol.  Agentless are process that gathers infomation 
from remote systems use any RPC method be it ssh, snmp rdp, wmi, and what ever 
can be scripted.  

**Agent**

.. toctree::
    :maxdepth: 2

    agent-management
    agent-dhcp-nat
    agent-configuration

**Agentless** 

.. toctree::
    :maxdepth: 2

    agentless-monitoring
    agentless-scripts



    

