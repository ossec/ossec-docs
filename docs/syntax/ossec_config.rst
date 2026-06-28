.. _syntax_ossec_config:

ossec.conf: syntax and options
==============================

``ossec.conf`` is the main configuration file for OSSEC. Options are grouped into XML
sections inside ``<ossec_config>``. Each section below documents supported elements,
attributes, and defaults.

Configuration quick reference
-----------------------------

+----------------------+----------------------------------------------------------+
| Section              | Purpose                                                  |
+======================+==========================================================+
| :ref:`ossec_config.global` | Email, logging, GeoIP, IP allow lists, alert output |
| :ref:`ossec_config.rules` | Rule file includes                                    |
| :ref:`ossec_config.syscheck` | File integrity monitoring (FIM)                    |
| :ref:`ossec_config.rootcheck` | Rootkit and policy checks                         |
| :ref:`ossec_config.alerts` | Alert log and email level thresholds               |
| :ref:`ossec_config.email_alerts` | Per-rule email routing                         |
| :ref:`ossec_config.localfile` | Log sources and formats                           |
| :ref:`ossec_config.remote` | Agent and syslog listeners on the manager          |
| :ref:`ossec_config.client` | Agent connection and crypto settings               |
| :ref:`ossec_config.command` | Active response command definitions               |
| :ref:`ossec_config.active-response` | Active response rules and triggers          |
| :ref:`ossec_config.database_output` | MySQL/PostgreSQL alert output               |
| :ref:`ossec_config.syslog_output` | Forward alerts to remote syslog               |
| :ref:`ossec_config.agentless` | SSH-based monitoring without an agent            |
| :ref:`ossec_config.reports` | Scheduled report definitions                       |
+----------------------+----------------------------------------------------------+

.. toctree::
    :maxdepth: 2
    :glob:

    head_ossec_config*
