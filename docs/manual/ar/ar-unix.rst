.. _manual-ar-unix:

UNIX: Active Response Configuration
===================================

The Active response configuration is divided into two parts. In the first one you
configure the commands you want to execute. In the second one, you bind the
commands to rules or events.

Commands Configuration
^^^^^^^^^^^^^^^^^^^^^^

In the commands configuration you create new “commands” to be used as responses.
You can have as many commands as you want. Each one should be inside their own
“command” element. For further information please see the `examples <../../syntax/head_ossec_config.active-response.html#example-active-response-configurations>`_.

.. code-block:: xml

    <command>
        <name>The name (A-Za-Z0-9)</name>
        <executable>The command to execute (A-Za-z0-9.-)</executable>
        <expect>Comma separated list of arguments (A-Za-z0-9)</expect>
        <timeout_allowed>yes/no</timeout_allowed>
    </command>

- **name**: Used to link the command to the response.
- **executable**: It must be a file (with exec permissions) inside
  “/var/ossec/active-response/bin”.

  You don’t need to provide the whole path.
- **expect**: The arguments this command is expecting (options are srcip and
  username).
- **timeout_allowed**: Specifies if this command supports timeout.


Responses Configuration
^^^^^^^^^^^^^^^^^^^^^^^

In the active-response configuration, you bind the commands (created) to events.
You can have as many responses as you want. Each one should be inside their own
“active-response” element. For further information please see the ` <../../syntax/head_ossec_config.active-response.html#example-active-response-con
figurations>`_.

.. code-block:: xml

    <active-response>
        <disabled>Completely disables active response if "yes"</disabled>
        <command>The name of any command already created</command>
        <location>Location to execute the command</location>
        <agent_id>ID of an agent (when using a defined agent)</agent_id>
        <level>The lower level to execute it (0-9)</level>
        <rules_id>Comma separated list of rules id (0-9)</rules_id>
        <rules_group>Comma separated list of groups (A-Za-z0-9)</rules_group>
        <timeout>Time to block</timeout>
    </active-response>


- **disabled**: Disables the active response capabilities if set to yes. If this is set, active response will not work.
- **command**: Used to link the response to the command
- **location**: Where the command should be executed. You have four options:

    - **local**: on the agent that generated the event
    - **server**: on the OSSEC server
    - **defined-agent**: on a specific agent (when using this option, you need to set the agent_id to use)
    - **all**: or everywhere.

- **agent_id**: The ID of the agent to execute the response (when defined-agent is set).
- **level**: The response will be executed on any event with this level or higher.
- **timeout**: How long until the reverse command is executed (IP unblocked,
  for example).


Active Response Tools
^^^^^^^^^^^^^^^^^^^^^

By default, the ossec hids comes with the following pre-configured
active-response tools:

- **host-deny.sh**: Adds an IP to the /etc/hosts.deny file (most Unix systems).
- **firewall-drop.sh** (iptables): Adds an IP to the iptables deny list (Linux 2.4 and 2.6).
- **firewall-drop.sh** (ipfilter): Adds an IP to the ipfilter deny list (FreeBSD, NetBSD and Solaris).
- **firewall-drop.sh** (ipfw): Adds an IP to the ipfw deny table (FreeBSD).

    .. note::

        On IPFW we use the table 1 to add the IPs to be blocked. We also
        set this table as deny in the beginning of the firewall list. If you use the
        table 1 for anything else, please change the script to use a different
        table id.

- **firewall-drop.sh** (ipsec): Adds an IP to the ipsec drop table (AIX).
- **pf.sh** (pf): Adds an IP to a pre-configured pf deny table (OpenBSD and FreeBSD).

    .. note::

        On PF, you need to create a table in your config and deny all the
        traffic to it. Add the following lines at the beginning of your
        rules and reload pf (pfctl -F all && pfctl -f /etc/pf.conf):
        table <ossec_fwtable> persist #ossec_fwtable

        block in quick from <ossec_fwtable> to any
        block out quick from any to <ossec_fwtable>

- **firewalld-drop.sh** (firewalld): Adds a rich-rule to block an IP to firewalld (Linux with firewalld enabled).

    .. note::

        You must manually enable this script in ossec.conf if you have firewalld
        enabled. The script will add (and remove) a rich-rule that drops all
        incoming communication from the supplied srcip.

- **nftables-drop.sh** (nftables): Adds an IP to a pre-configured set (Linux with nftables enabled).

    .. note::

        You must manually enable this script in ossec.conf if you have nftables
        enabled. The script will add (and remove) IPs to a pre-configured set that
        should drop all incoming communication from the supplied srcip.
        The necessary nftables sets and rules need to already exist. An example configuration would be:

    .. code-block:: none

    table inet filter {
            set ossec_ar4 {
                    type ipv4_addr
                    comment "ossec active response"
            }

            set ossec_ar6 {
                    type ipv6_addr
                    comment "ossec active response"
            }

            chain INPUT {
                    type filter hook input priority filter; policy drop;
                    ct state invalid counter packets 71 bytes 3416 drop
                    ip saddr @ossec_ar4 drop
                    ip6 saddr @ossec_ar6 drop
                    ct state established,related counter packets 4969 bytes 1764628 accept
                    ip protocol icmp counter packets 0 bytes 0 accept
                    ip6 nexthdr ipv6-icmp counter packets 0 bytes 0 accept
                    iifname "lo" counter packets 63 bytes 4432 accept
                    # more accept rules
            }

            chain FORWARD {
                    type filter hook forward priority filter; policy drop;
                    meta nfproto ipv4 counter packets 0 bytes 0 reject with icmp type host-prohibited
            }

            chain OUTPUT {
                    type filter hook output priority filter; policy accept;
            }
        }
