.. _ossec_config.remote: 

ossec.conf: Remote Options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

remote options are available in the the following installation types:

* server

Location 
^^^^^^^^

All remote options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <remote> 
            <!-- 
            remote options here
            --> 
        </remote> 
    </ossec_config> 

Choosing connection type
^^^^^^^^^^^^^^^^^^^^^^^^

The ``<connection>`` element selects how ``ossec-remoted`` accepts inbound events:

**secure** (default, port 1514)
    Use for **OSSEC agents**. Traffic uses the OSSEC agent protocol with optional
    encryption (AES or Blowfish). Agents authenticate with keys from ``client.keys``.

**syslog** (default port 514, UDP or TCP)
    Use for **external devices** — firewalls, routers, switches, and other syslog
    senders that are not OSSEC agents. There is no agent key exchange; restrict
    sources with ``allowed-ips`` and ``deny-ips``.

You can define multiple ``<remote>`` blocks (for example, one ``secure`` listener for
agents and one ``syslog`` listener for network gear). See also
:ref:`manual-remoted` for threading and tuning.

Options 
------- 

.. include:: ./ossec_config.remote.trst
