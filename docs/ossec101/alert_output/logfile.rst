.. _ossec_101_output_logfile:



OSSEC 101: logfile output
-------------------------

By default OSSEC will output alerts to a logfile located at ``/var/ossec/logs/alerts/alerts.log``.
The alert format is multi-line, and the exact information will vary based on the alert.

The alerts.log file rotates every day at midnight, and is saved to ``/var/ossec/logs/alerts/YYYY/mm/ossec-alerts-dd.log.gz``.
The MD5 of the logfile is stored in ``/var/ossec/logs/alerts/YYYY/mm/ossec-alerts-dd.log.sum``.


Options:
^^^^^^^^

There are currently no options associated with the alerts.log


Log sample:
^^^^^^^^^^^

.. code-block:: console

   ** Alert 1345225879.4882: - syslog,sudo
   2012 Aug 17 13:51:19 arrakis->/var/log/secure
   Rule: 5402 (level 3) -> 'Successful sudo to ROOT executed'
   User: ddp
   2012-08-17T13:51:19.415746-04:00 arrakis sudo:      ddp : TTY=ttyp3 ; PWD=/home/ddp ; USER=root ; COMMAND=/usr/sbin/pkg_add -ui

   ** Alert 1345226469.5197: - ossec,
   2012 Aug 17 14:01:09 arrakis->ossec-logcollector
   Rule: 591 (level 3) -> 'Log file rotated.'
   ossec: File rotated (inode changed): '/var/log/messages'.






