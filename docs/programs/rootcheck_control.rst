
.. _rootcheck_control:

rootcheck_control
=================

The rootcheck_control tool allows you to manage the policy monitoring and system auditing database that is stored on the server (manager) side. You can list anomalies detected by the rootcheck functionality, categorized into resolved and outstanding issues. Moreover you can find out when ossec-rootcheck was run the last time.

rootcheck_control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: rootcheck_control 

.. option:: -h

    Display the help message.

.. option:: -l 

    List available agents. 

.. option:: -lc 

    List only currently connected agents. 

.. option:: -u <id>

    Updates (clear) the database for the agent.

.. option:: -u all 

    Updates (clear) the database for all agents.

.. option:: -i <agent_id>

    Prints database for the agent.

.. option:: -r

    Used with -i, prints all the resolved issues.

.. option:: -q

    Used with -i, prints all the outstanding issues.

.. option:: -L

    Used with -i, prints the last scan.

.. option:: -s

    Changes the output to CSV (comma delimited).


rootcheck_control example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Getting a list of system auditing/policy monitoring events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get a list of all auditing/policy monitoring events for a specific agent, you can run `rootcheck_control -i <agent_id>`. To retrieve the agent id you can use any of the following commands:

- :option:`rootcheck_control -l`,
- :option:`agent_control -l` 
- :option:`syscheck_control -l`
- :option:`syscheck_update -l`
- :option:`manage_agents -l`

.. code-block:: console 

    # /var/ossec/bin/rootcheck_control -i 002

    Policy and auditing events for agent 'ossecagent (002) - 192.168.1.86':

    Resolved events: 

    2010 Jun 15 13:01:22 (first time detected: 2009 Dec 10 18:48:43)
    System Audit: System Audit: CIS - Debian Linux 8.8 - GRUB Password not set. File: /boot/grub/menu.lst. Reference: http://www.ossec.net/wiki/index.php/CIS_DebianLinux .


    Outstanding events: 

    2010 Jun 17 17:34:37 (first time detected: 2009 Dec 10 18:48:43)
    System Audit: System Audit: CIS - Testing against the CIS Debian Linux Benchmark v1.0. File: /etc/debian_version. Reference: http://www.ossec.net/wiki/index.php/CIS_DebianLinux .

    2010 Jun 17 17:34:37 (first time detected: 2009 Dec 10 18:48:43)
    System Audit: System Audit: CIS - Debian Linux 1.4 - Robust partition scheme - /tmp is not on its own partition. File: /etc/fstab. Reference: http://www.ossec.net/wiki/index.php/CIS_DebianLinux .

    2010 Jun 17 17:34:37 (first time detected: 2009 Dec 10 18:48:43)
    System Audit: System Audit: CIS - Debian Linux 2.3 - SSH Configuration - Root login allowed. File: /etc/ssh/sshd_config. Reference: http://www.ossec.net/wiki/index.php/CIS_DebianLinux .

As you can see the detected events are shown in two categories, resolved events and outstanding event. To only show resolved events, run :option:`rootcheck_control -ri <agent_id>`.
To only show outstanding events, run :option:`rootcheck_control -qi <agent_id>`.
To only show the results of the last scan and time of that scan, run :option:`rootcheck_control -Li <agent_id>`.

To gain that kind of information for the OSSEC server, run :option:`rootcheck_control -i 000`.

Example 2: Clearing the system auditing/policy database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To clear the system auditing/policy monitoring database for a certain agent run the following command:

.. code-block:: console

    # /var/ossec/bin/rootcheck_control -u 002

    ** Policy and auditing database updated.

To clear the database for all agents and the server run the following command:

.. code-block:: console

    # /var/ossec/bin/rootcheck_control -u all

    ** Policy and auditing database updated.

The next time rootcheck is run, the database will be populated again.

