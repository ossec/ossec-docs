.. _ossec_logic:

OSSEC Processes and Data
========================

+--------------------+--------------------------------------------------------------------------------+
| Module             | Suposition                                                                     |
+====================+================================================================================+
| ossec-analysisd    | Master program. Analyzes data from the logs, syscheck,rootcheck, etc.          |
|                    | Runs as an unprivileged (ossec) user under chroot.                             |
+--------------------+--------------------------------------------------------------------------------+
| ossec-execd        | Execute active responses by calling the configured scripts. Runs as root.      |
+--------------------+--------------------------------------------------------------------------------+
| ossec-maild        | Send e-mail alerts. Runs as an unprivileged user (ossecm) under chroot.        |
+--------------------+--------------------------------------------------------------------------------+
| ossec-remoted      | Server side socket for server/client communications.                           |
|                    | Runs as an unprivileged user (ossecr) under chroot.                            |
+--------------------+--------------------------------------------------------------------------------+
| ossec-agentd       | Agent side socket for server/client communications.                            |
|                    | Runs as an unprivileged user (ossec) under chroot.                             |
+--------------------+--------------------------------------------------------------------------------+
| ossec-logcollector | Monitor log files and windows event logs (do not use tail).                    |
+--------------------+--------------------------------------------------------------------------------+
| ossec-syscheckd    | Does integrity checking and rootkit detection (rootcheck is a module of it).   |
+--------------------+--------------------------------------------------------------------------------+
| ossec-csyslogd     | Client syslog tool to forward OSSEC alerts to remote syslog servers            |
|                    | (including SIM/SEMs and log management systems).                               |
+--------------------+--------------------------------------------------------------------------------+
| ossec-monitord     | Monitor agent connectivity and compress daily log files.                       |
+--------------------+--------------------------------------------------------------------------------+

*  ossec-logcollector on agent machine tails log file & sends to ossec-agent.
*  ossec-agent routes the information to the ossec-server (on server system).
*  ossec-remoted receives data, uncompress and unencrypt it and sends to analysisd.
*  ossec-analysisd detects an actionable issue.
*  ossec-analysisd actions:

  *  ossec-analysisd sends information to ossec-execd (if response is configured to run in the server side).
  *  ossec-analysisd sends information to ossec-remoted (if response is configured to run in the agent). 

*  ossec-maild monitors analysisd and generate e-mail alert.
*  If active response is enabled on the agent, ossec-remoted on the manager sends the active response to ossec-agent on the agent and ossec-agent sends it to ossec-execed.
*  ossec-execd calls an active response script 
