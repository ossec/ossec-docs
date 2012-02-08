ossec.conf and agent.conf
-------------------------

For agent/server installs OSSEC has some centralized configuration options available.
While a normal configuration exists in ``/var/ossec/etc/ossec.conf`` on each system, agents can also use ``/var/ossec/etc/shared/agent.conf``. 
The agent.conf exists on each system, but is distributed from the manager. 
Any changes made to the agent.conf on an agent will be overwritten the next time the file is transferred from the manager.


Configuration by Operating System:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration by Agent Name:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration by Profile:
^^^^^^^^^^^^^^^^^^^^^^^^^


