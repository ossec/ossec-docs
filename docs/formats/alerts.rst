OSSEC alert log samples
=======================


Example alert.log messages:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   ** Alert 1510376401.0: - syslog,errors,
   2017 Nov 11 00:00:01 ix->/var/log/messages
   Rule: 1005 (level 5) -> 'Syslogd restarted.'
   Nov 11 00:00:01 ix syslogd[72090]: restart

   ** Alert 1510376417.172: - syslog,smtpd,
   2017 Nov 11 00:00:17 (junction) 192.168.17.17->/var/log/maillog
   Rule: 53508 (level 5) -> 'Server TLS certificate verification failed.'
   Nov 11 00:00:16 junction smtpd[86532]: smtp-out: Server certificate verification failed on session 99fc1afc58067419

   ** Alert 1510376428.465: - syslog,sudo
   2017 Nov 11 00:00:28 ubnt->/var/log/syslog-ng/messages
   Rule: 5402 (level 3) -> 'Successful sudo to ROOT executed'
   User: root
   Nov  5 15:35:03 ubnt sudo:     root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/usr/bin/vtysh.pl -c show ip route summary json

   ** Alert 1510376428.758: - pam,syslog,authentication_success,
   2017 Nov 11 00:00:28 ubnt->/var/log/syslog-ng/messages
   Rule: 5501 (level 3) -> 'Login session opened.'
   Nov  5 15:35:03 ubnt sudo: pam_unix(sudo:session): session opened for user root by (uid=0)


Sample alerts.json messages:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

   {"rule":{"level":5,"comment":"Syslogd restarted.","sidid":1005,"group":"syslog,errors,"},"id":"1510376401.0","TimeStamp":1510376401000,"location":"/var/log/messages","full_log":"Nov 11 00:00:01 ix syslogd[72090]: restart","hostname":"ix","program_name":"syslogd"}
   {"rule":{"level":5,"comment":"Server TLS certificate verification failed.","sidid":53508,"group":"syslog,smtpd,"},"id":"1510376417.172","TimeStamp":1510376417000,"decoder":"smtpd","location":"(junction) 192.168.17.17->/var/log/maillog","full_log":"Nov 11 00:00:16 junction smtpd[86532]: smtp-out: Server certificate verification failed on session 99fc1afc58067419","hostname":"(junction) 192.168.17.17->/var/log/maillog","program_name":"smtpd"}
   {"rule":{"level":3,"comment":"Successful sudo to ROOT executed","sidid":5402,"group":"syslog,sudo"},"id":"1510376428.465","TimeStamp":1510376428000,"decoder":"sudo","srcuser":"root","dstuser":"root","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:35:03 ubnt sudo:     root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/usr/bin/vtysh.pl -c show ip route summary json","url":"/","status":"/usr/bin/vtysh.pl -c show ip route summary json","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Login session opened.","sidid":5501,"group":"pam,syslog,authentication_success,"},"id":"1510376428.758","TimeStamp":1510376428000,"decoder":"pam","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:35:03 ubnt sudo: pam_unix(sudo:session): session opened for user root by (uid=0)","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Login session closed.","sidid":5502,"group":"pam,syslog,"},"id":"1510376430.1015","TimeStamp":1510376430000,"decoder":"pam","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:35:04 ubnt sudo: pam_unix(sudo:session): session closed for user root","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Successful sudo to ROOT executed","sidid":5402,"group":"syslog,sudo"},"id":"1510376490.1239","TimeStamp":1510376490000,"deco
   der":"sudo","srcuser":"root","dstuser":"root","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:36:04 ubnt sudo:     root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/usr/bin/vtysh.pl -c show ip route summary json","url":"/","status":"/usr/bin/vtysh.pl -c show ip route summary json","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Login session opened.","sidid":5501,"group":"pam,syslog,authentication_success,"},"id":"1510376490.1533","TimeStamp":1510376490000,"decoder":"pam","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:36:04 ubnt sudo: pam_unix(sudo:session): session opened for user root by (uid=0)","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Login session closed.","sidid":5502,"group":"pam,syslog,"},"id":"1510376490.1791","TimeStamp":1510376490000,"decoder":"pam","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:36:05 ubnt sudo: pam_unix(sudo:session): session closed for user root","hostname":"ubnt","program_name":"sudo"}
   {"rule":{"level":3,"comment":"Successful sudo to ROOT executed","sidid":5402,"group":"syslog,sudo"},"id":"1510376550.2015","TimeStamp":1510376550000,"decoder":"sudo","srcuser":"root","dstuser":"root","location":"/var/log/syslog-ng/messages","full_log":"Nov  5 15:37:05 ubnt sudo:     root : TTY=unknown ; PWD=/ ; USER=root ; COMMAND=/usr/bin/vtysh.pl -c show ip route summary json","url":"/","status":"/usr/bin/vtysh.pl -c show ip route summary json","hostname":"ubnt","program_name":"sudo"}


