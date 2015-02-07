.. _ar_agent_conf_restart:


How to restart an agent after changes to the agent.conf:
========================================================

OSSEC agents require a restart after the agent.conf has been updated. 
Active response can do this automatically when it notices the file has changed.


Requirements:
^^^^^^^^^^^^^

* Active response must be enabled.
* This only works for \*nix based systems

Details:
^^^^^^^^

The idea behind this is to have active response restart the OSSEC processes when the agent.conf file changes.
A rule must be created to notice the change to that specific file, and an active response setup to react to that rule.


rules:
^^^^^^
.. code-block:: console

   <rule id="710001" level="1">
     <if_group>syscheck</if_group>
     <match>/var/ossec/etc/shared/agent.conf</match>
     <description>agent.conf was modified</description>
   </rule>


active response configuration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  <command>
    <name>restart-ossec</name>
    <executable>restart-ossec.sh</executable>
    <expect></expect>
  </command>

  <active-response>
    <command>restart-ossec</command>
    <location>local</location>
    <rules_id>710001</rules_id>
  </active-response>
