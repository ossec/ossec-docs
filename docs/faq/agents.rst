.. _faq_agents:

Agents: FAQ
-------------

.. contents:: 
    :local:


Why can't agent IDs be re-used?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When looking at historical alerts you don't want to associate alerts from one system to be attributed to another,
especially if the those alerts are from an unrelated and retired system.

ossec-logcollector(PID): ERROR: Unable to open file '/queue/ossec/.agent_info'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure there is a <server-ip> configured in the agent's /var/ossec/etc/ossec.conf, and that the IP is correct.

The OSSEC agent is unable to resolve hostnames from /etc/hosts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default OSSEC chroots many of its daemons to `/var/ossec`. When this happens the `/etc/hosts` file is unreadable.
To resolve this issue, copy `/etc/hosts` to `/var/ossec/etc/`. A hardlink to `/etc/hosts` can be used if the system
is does not have a separate `/var/` partition.

Using a hostname for the server does not work.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`ossec-agentd` chroots to `/var/ossec` by default. In order to resolve hostnames, the agent will need some support.
It could be as simple as copying `/etc/resolv.conf` to `/var/ossec/etc/resolv.conf`.

