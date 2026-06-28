.. _manual-ar-scripts:

Bundled active-response scripts
===============================

Scripts are installed to ``/var/ossec/active-response/bin/``. Each must be
referenced from a ``<command>`` block in ``ossec.conf`` before use. Most blocking
scripts expect ``srcip`` in ``<expect>``.

Firewall and network blocking
-----------------------------

+-------------------+----------+-----------------------------------------------+
| Script            | Expect   | Notes                                         |
+===================+==========+===============================================+
| host-deny.sh      | srcip    | Adds IP to ``/etc/hosts.deny`` (tcp wrappers) |
| firewall-drop.sh  | srcip    | iptables, ipfilter, or AIX IPSec (auto-detect)|
| firewalld-drop.sh | srcip    | Linux with firewalld; enable manually         |
| nftables-drop.sh  | srcip    | Linux nftables; requires pre-configured sets  |
| pf.sh             | srcip    | OpenBSD/FreeBSD PF table ``ossec_fwtable``    |
| ipfw.sh           | srcip    | FreeBSD IPFW table 1                          |
| ipfw_mac.sh       | srcip    | macOS IPFW                                    |
| npf.sh            | srcip    | NetBSD NPF                                    |
| route-null.sh     | srcip    | Null-route the source IP                      |
| ip-customblock.sh | srcip    | Template for custom block actions             |
| firewall-drop.cmd | srcip    | Windows firewall block                        |
| netsh.cmd         | srcip    | Windows ``netsh`` firewall block              |
| route-null.cmd    | srcip    | Windows null route                            |
+-------------------+----------+-----------------------------------------------+

Account and service actions
---------------------------

+-------------------+----------+-----------------------------------------------+
| Script            | Expect   | Notes                                         |
+===================+==========+===============================================+
| disable-account.sh| username | Locks account via ``passwd -l`` or AIX chuser |
| restart-ossec.sh  | (none)   | Restarts OSSEC on the target host             |
| restart-ossec.cmd | (none)   | Windows agent restart                         |
+-------------------+----------+-----------------------------------------------+

Notifications and integrations
------------------------------

These scripts require API keys or credentials edited inside the script before use.

+-------------------+----------+-----------------------------------------------+
| Script            | Expect   | Notes                                         |
+===================+==========+===============================================+
| ossec-slack.sh    | (none)   | Posts alert to Slack via incoming webhook     |
| ossec-pagerduty.sh| (none)   | Creates PagerDuty incident via API key        |
| ossec-tweeter.sh  | (none)   | Posts alert text to Twitter/X                 |
| cloudflare-ban.sh | srcip    | Adds IP to Cloudflare block list (API token)  |
| ossec-aws-waf.sh  | srcip    | Adds IP to AWS WAF IP set (requires AWS CLI)  |
+-------------------+----------+-----------------------------------------------+

Configuration example
---------------------

.. code-block:: xml

   <command>
     <name>slack-notify</name>
     <executable>ossec-slack.sh</executable>
     <expect></expect>
     <timeout_allowed>no</timeout_allowed>
   </command>

   <active-response>
     <command>slack-notify</command>
     <location>server</location>
     <level>10</level>
   </active-response>

See :ref:`manual-ar-unix` for command and active-response syntax.
