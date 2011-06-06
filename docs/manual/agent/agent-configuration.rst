
.. _manual-syscheck:

Centralized agent configuration
===============================

If you ever wanted to be able to configure your agents remotely, you will be
happy to know that starting on version 2.1 you will be able to do so. We allow
centralized configuration for file integrity checking (syscheckd), rootkit
detection (rootcheck) and log analysis.

This is how it works.

Create agent configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

First Create the file /var/ossec/etc/shared/agent.conf.

Inside the file you can configure the agent just as you would normally at
ossec.conf

.. code-block:: xml 

    <agent_config>
        <localfile>
            <location>/var/log/my.log</location>
            <log_format>syslog</log_format>
        </localfile>
    </agent_config>


But you have a few more options. You can restrict the config by agent name or by
operating system:

.. code-block:: xml 

    <agent_config name="agent1">
        <localfile>
            <location>/var/log/my.log</location>
            <log_format>syslog</log_format>
        </localfile>
    </agent_config>

    <agent_config os="Linux">
        <localfile>
            <location>/var/log/my.log2</location>
            <log_format>syslog</log_format>
        </localfile>
    </agent_config>

    <agent_config os="Windows">
        <localfile>
            <location>C:\myapp\my.log</location>
            <log_format>syslog</log_format>
        </localfile>
    </agent_config>

And only the proper agent will read them, giving us great granularity to push
the configuration to all your agents.

After you configured, the manager will push it to the agents. Note that it can
take a while for it to complete (since the manager caches the shared files and
only re-reads them every few hours). If you restart the manager the
configuration will be pushed much quicker.

Restart the agent 
^^^^^^^^^^^^^^^^^

Once the configuration file is pushed, you can run the command :ref:`agent_control` to
see if the agent received the config and restart the agent remotely.

.. code-block:: console 

    # md5 /var/ossec/etc/shared/agent.conf
    MD5 (/var/ossec/etc/shared/agent.conf) = ee1882236893df851bd9e4842007e7e7
    # /var/ossec/bin/agent_control -i 200

    OSSEC HIDS agent_control. Agent information:
    Agent ID: 200
    Agent Name: ourhome
    IP address: 192.168.0.0/16
    Status: Active

    Operating system: Linux ourhome 2.6.24-23-generic #1 SMP Mon Jan 26 00..
    Client version: OSSEC HIDS v2.1 / ee1882236893df851bd9e4842007e7e7
    Last keep alive: Tue Jun 30 08:29:17 2009

    Syscheck last started at: Tue Jun 30 04:29:32 2009
    Rootcheck last started at: Tue Jun 30 06:03:08 2009

When the agent received the configuration, the “Client Version” field will have
the md5sum of the agent.conf file.

To restart the agent:

.. code-block:: console 

    # /var/ossec/bin/agent_control -R 200 (where 200 is the agent id)

    OSSEC HIDS agent_control: Restarting agent: 200
