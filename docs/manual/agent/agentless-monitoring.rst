
.. _manual-agentless:

Agentless Monitoring
====================

**Agentless monitoring** allows you to run integrity checking (and in the future 
log monitoring) on systems without an agent installed (including routers, firewalls, 
switches and even Linux/BSD systems). It can be executed just like our normal file 
integrity checking (alerting of checksum changes) or doing diffs and showing 
exactly what has changed.

Agentless configuration options 
-------------------------------

.. include:: ../../syntax/ossec_config.agentless.trst 

Getting started with agentless
------------------------------

After you installed OSSEC, you need to enable the agentless monitoring:

.. code-block:: console 

    # /var/ossec/bin/ossec-control enable agentless 

And provide the SSH authentication to the host you want to access. For Cisco devices 
(PIX, routers, etc), you need to provide an additional parameter for the enable password. 
The same thing applies if you want to add support for “su”, it must be the additional 
parameter. In this example, I am adding a Linux box (example.net) and a PIX firewall 
(pix.fw.local):

.. code-block:: console 

    # /var/ossec/agentless/register_host.sh add root@example.net mypass1
      *Host root@example.netl added.
    # /var/ossec/agentless/register_host.sh add pix@pix.fw.local pixpass enablepass
      *Host pix@pix.fw.local added.

    # /var/ossec/agentless/register_host.sh list
      *Available hosts:
    pix@pix.fw.local
    root@example.net

If you want to use public key authentication instead of
passwords, you need to provide NOPASS as the password and
create the public key:

.. code-block:: console 

    # sudo -u ossec ssh-keygen

It will create the public keys inside /var/ossec/.ssh .  After that, just scp the 
public key to the remote box and your password less connection should work.

Configuring agentless 
---------------------

Once you have added all your systems, you need to configure
OSSEC to monitor them. By default, we have 4 agentless types
(but we plan to add more soon):

- ssh_integrity_check_bsd
- ssh_integrity_check_linux
- ssh_generic_diff 
- ssh_pixconfig_diff

For the first two, you give a list of directories in the configuration and OSSEC
will do the integrity checking of them on the remote box. On the
ssh_generic_diff, you give a set of commands to run on the remote box and OSSEC
will alert when the output of them changes. The ssh_pixconfig_diff will alert
when a Cisco PIX/router configuration changes.

So, for my first system (root@example.net), I will monitor the /bin, /etc and /sbin
directories every 10 hours (if I was using the ssh_integrity_check_bsd, the
argument would be the directories as well):

.. code-block:: xml

    <agentless>
        <type>ssh_integrity_check_linux</type>
        <frequency>36000</frequency>
        <host>root@example.net</host>
        <state>periodic</state>
        <arguments>/bin /etc/ /sbin</arguments>
    </agentless>

For my PIX, the configuration looks like:

.. code-block:: xml 

    <agentless>
        <type>ssh_pixconfig_diff</type>
        <frequency>36000</frequency>
        <host>pix@pix.fw.local</host>
        <state>periodic_diff</state>
    </agentless>

And just to exemplify the ssh_generic_diff I will also monitor ls -la /etc; cat
/etc/passwd on the root@example.net. Note that if you want to monitor any network
firewall or switch, you can use the ssh_generic_diff and just specify the
commands in the arguments option. To use “su”, you need to set the value
“use_su” before the hostname (eg: <host>use_su root@example.net</host>).

.. code-block:: xml 

    <agentless>
        <type>ssh_generic_diff</type>
        <frequency>36000</frequency>
        <host>root@example.net</host>
        <state>periodic_diff</state>
        <arguments>ls -la /etc; cat /etc/passwd</arguments>
    </agentless>


Running the completed setup
---------------------------

Once the configuration is completed, you can restart OSSEC. You should see
something like “Started ossec-agentlessd” in the output. Before each agentless
connection is started, OSSEC will do a configuration check to make sure
everything is fine. Look at /var/ossec/logs/ossec.log for any error. If you see:

.. code-block:: 

    2008/12/12 15:20:06 ossec-agentlessd: ERROR: Expect command not found (or bad arguments) for 'ssh_integrity_check_bsd'.
    2008/12/12 15:20:06 ossec-agentlessd: ERROR: Test failed for 'ssh_integrity_check_bsd' (127). Ignoring.'

It means that you don’t have the expect library installed on the server (it is
not necessary to install anything on the agentless systems to monitor). On
Ubuntu you can do the following to install:

.. code-block:: console 

    # apt-get install expect 

After installing expect, you can restart OSSEC and you should see: 

.. code-block:: 

    2008/12/12 15:24:12 ossec-agentlessd: INFO: Test passed for 'ssh_integrity_check_bsd'.'

When it connects to the remote system, you will also see:

.. code-block:: 

    2008/12/12 15:25:19 ossec-agentlessd: INFO: ssh_integrity_check_bsd: root@example.net: Starting.
    2008/12/12 15:25:46 ossec-agentlessd: INFO: ssh_integrity_check_bsd: root@example.net: Finished.

Alerts
------

These are some of the alerts you will get:

For the ssh_generic_diff::

    OSSEC HIDS Notification.
    2008 Dec 12 01:58:30

    Received From: (ssh_generic_diff) root@example.net->agentless
    Rule: 555 fired (level 7) -> "Integrity checksum for agentless device changed."
    Portion of the log(s):

    ossec: agentless: Change detected:
    35c35
    < -rw-r-r- 1 root wheel 34 Dec 10 03:55 hosts.deny
    --
    > -rw-r-r- 1 root wheel 34 Dec 11 18:23 hosts.deny
    -END OF NOTIFICATION


For the PIX::

    OSSEC HIDS Notification.
    2008 Dec 01 15:48:03

    Received From: (ssh_pixconfig_diff) pix@pix.fw.local->agentless
    Rule: 555 fired (level 7) -> "Integrity checksum for agentless device changed."
    Portion of the log(s):

    ossec: agentless: Change detected:
    48c48
    < fixup protocol ftp 21
    --
    > no fixup protocol ftp 21
    100c100
    < ssh timeout 30
    --
    > ssh timeout 50
    More changes..

    -END OF NOTIFICATION
