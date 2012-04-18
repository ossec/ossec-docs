ossec.conf and agent.conf
-------------------------

For agent/server installs OSSEC has some centralized configuration options available.
While a normal configuration exists in ``/var/ossec/etc/ossec.conf`` on each system, agents can also use ``/var/ossec/etc/shared/agent.conf``. 
The agent.conf exists on each system, but is distributed from the manager. 
Any changes made to the agent.conf on an agent will be overwritten the next time the file is transferred from the manager.

The ``agent.conf`` is not distributed immediately after a change, in fact the transfer can take several hours. Also the agents have to be restarted after receiving a new ``agent.conf``.

Configuration by Operating System:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to configure systems based on the operating system they run. This can be useful when monitoring log files that are in one location on one OS, and either absent or in a different location on another OS.

For instance OpenBSD has a logfile named ``/var/log/daemon`` that is not present on most other systems. To make sure the file is monitored we can add the following to ``/var/ossec/etc/shared/agent.conf`` on the manager:

.. code-block:: console

  <agent_config os="OpenBSD">
    <localfile>
      <log_format>syslog</log_format>
      <location>/var/log/daemon</location>
    </localfile>



Configuration by Agent Name:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These same changes can reference a system by agent name as well. In this instance I want to monitor ``/var/log/nmap-out.log`` on agent99, but don't want to modify agent99's ``ossec.conf``. Adding the following to the ``agent.conf`` accomplishes this:

.. code-block:: console

  <agent_config name="agent99">
    <localfile>
      <log_format>nmapg</log_format>
      <location>/var/log/nmap-out.log</location>
    </localfile>
  </agent_config>


Configuration by Profile:
^^^^^^^^^^^^^^^^^^^^^^^^^

Profiles are the newest option for the ``agent.conf``. A popular way to use this option is to create profiles based on purpose, for instance a "webserver" profile. This allows you to modify the settings for all webservers, without affecting other systems sharing an OS or duplicating information by creating multiple entries with different names.

.. code-block:: console

  <agent_config profile="webserver">
    <localfile>
      <log_format>apache</log_format>
      <location>/var/log/apache/error_log</location>
    </localfile>
  </agent_config>

This option does require modification of the agent's ``ossec.conf``. i
The ``<client>`` section of the agent's ``ossec.conf`` will need to include a ``<config-profile>`` option with all desired profiles (comma separated).

.. code-block:: console

  <ossec_config>
    <client>
      <server-ip>192.168.1.100</server-ip>
      <config-profile>webserver</config-profile>
    </client>
  </ossec_config>




Automatically restarting the agent processes when agent.conf is updated:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To help solve the problem of restarting the agents every time the ``agent.conf`` changes, you can use the following active response configuration. This assumes that you have active response enabled on the agents and manager.

This is the command and active response definition enabling the restart:

.. code-block:: console

    <command>
      <name>restart-ossec</name>
      <executable>restart-ossec.sh</executable>
      <expect></expect>
    </command>

    <active-response>
      <command>restart-ossec</command>
      <location>local</location>
      <rules_id>510010</rules_id>
    </active-response>


This is the rule referenced in the ``<active-response>`` above:

.. code-block:: console

    <rule id="510010" level="10">
      <if_sid>550</if_sid>
      <match>/var/ossec/etc/shared/agent.conf</match>
      <description>agent.conf has been modified.</description>
    </rule>


When syscheck finds a modified ``agent.conf`` rule 510010 is triggered, which triggers the restart-ossec active response.
