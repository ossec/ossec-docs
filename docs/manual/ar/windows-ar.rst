.. _manual-unix-ar: 

Windows: Active Response Configuration
======================================

To start, you need to enable active response on Windows (disabled by default).
To do that, just add the following to the agent’s ossec.conf:

.. code-block:: xml

    <active-response>
        <disabled>no</disabled>
    </active-response>

After that, you need to go to the manager and specify when to run the response.
Adding the following to ossec.conf will enable the responses for alerts above
level 6:

.. code-block:: xml

    <command>
        <name>win_nullroute</name>
        <executable>route-null.cmd</executable>
        <expect>srcip</expect>
        <timeout_allowed>yes</timeout_allowed>
    </command>

    <active-response>
        <command>win_nullroute</command>
        <location>local</location>
        <level>6</level>
        <timeout>600</timeout>
    </active-response>

With the configuration completed (and the manager restarted), you can test the
active response by running the agent-control script (in this case, I am running
it on agent id 185 to block ip 2.3.4.5):

.. code-block:: console 

    # /var/ossec/bin/agent_control -L

    OSSEC HIDS agent_control. Available active responses:

    Response name: host-deny600, command: host-deny.sh
    Response name: firewall-drop600, command: firewall-drop.sh
    Response name: win_nullroute600, command: route-null.cmd

    # /var/ossec/bin/agent_control -b 2.3.4.5 -f win_nullroute600 -u 185

    OSSEC HIDS agent_control: Running active response "win_nullroute600′ "n: 185

And looking at the agent you should see the new entry in the route table:

.. code-block:: console 

    C:\>route print
    ..
    Active Routes:
    Network Destination Netmask Gateway Interface Metric
    2.3.4.5 255.255.255.255 x.y.z x.y.z 1
    ..

If you run into any issues, look at the ossec.log file (on the agent) for any
entry for ossec-execd. If you enabled it correctly, you will see:

.. code-block:: 

    2008/08/20 11:53:49 ossec-execd: INFO: Started (pid: 3896).
