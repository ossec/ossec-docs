Log entries in asl.log on OSX
-----------------------------

*Note: user's name changed to "username" and host's name changed to "Hostname" to protect the innocent.*

Sudo:
^^^^^

.. code-block:: console

  [Time 2006.12.28 15:54:03 UTC] [Facility local2] [Sender sudo] [PID -1] [Message   username : TTY=ttyp1 ; PWD=/Users/username ; USER=root ; COMMAND=/usr/bin/su -] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 22:10:45 UTC] [Facility local2] [Sender sudo] [PID -1] [Message   username : TTY=ttyp1 ; PWD=/sw/src/fink.build ; USER=postgres ; COMMAND=/sw/bin/initdb-8.2 -D /sw/var/postgresql-8.2/data] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 22:11:19 UTC] [Facility local2] [Sender sudo] [PID -1] [Message   username : TTY=ttyp1 ; PWD=/sw/src/fink.build ; USER=postgres ; COMMAND=/sw/bin/pg_ctl-8.2 start -D /sw/var/postgresql-8.2/data -l /sw/var/postgresql-8.2/pgsql.log] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 22:11:30 UTC] [Facility local2] [Sender sudo] [PID -1] [Message   username : TTY=ttyp1 ; PWD=/sw/src/fink.build ; USER=postgres ; COMMAND=/sw/bin/pg_ctl-8.2 stop -D /sw/var/postgresql-8.2/data -m fast] [Level 5] [UID -2] [GID -2] [Host Hostname]


sshd:
^^^^^^^
.. code-block:: console

  [Time 2006.12.28 15:53:55 UTC] [Facility auth] [Sender sshd] [PID 483] [Message error: PAM: Authentication failure for username from 192.168.0.2] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.11.02 11:41:44 UTC] [Facility auth] [Sender sshd] [PID 800] [Message refused connect from 59.124.44.34] [Level 4] [UID -2] [GID -2] [Host test-emac]


Cron:
^^^^^

.. code-block:: console

  [Time 2006.12.28 14:15:00 UTC] [Facility cron] [Sender anacron] [PID 459] [Message Updated timestamp for job `cron.daily' to 2006-12-28] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 14:18:00 UTC] [Facility cron] [Sender anacron] [PID 455] [Message Job `cron.daily' terminated] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 14:18:00 UTC] [Facility cron] [Sender anacron] [PID 455] [Message Normal exit (1 jobs run)] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 15:10:00 UTC] [Facility cron] [Sender anacron] [PID 481] [Message Anacron 2.3 started on 2006-12-28] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 15:10:00 UTC] [Facility cron] [Sender anacron] [PID 481] [Message Normal exit (0 jobs run)] [Level 5] [UID -2] [GID -2] [Host Hostname]


Software Update:
^^^^^^^^^^^^^^^^

.. code-block:: console

  [Time 2006.12.28 01:59:49 UTC] [Facility install] [Sender Software Update] [PID 353] [Message JavaScript error "Undefined value" while running "__choice_su_visible"] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:49 UTC] [Facility install] [Sender Software Update] [PID 353] [Message __choice_su_visible returned error: Undefined value] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:52 UTC] [Facility install] [Sender Software Update] [PID 353] [Message Package Authoring Error: installation-check results requires a message] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:52 UTC] [Facility install] [Sender Software Update] [PID 353] [Message Package Authoring Error: installation-check results requires a message] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:52 UTC] [Facility install] [Sender Software Update] [PID 353] [Message Package Authoring Error: installation-check results requires a message] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:55 UTC] [Facility install] [Sender Software Update] [PID 353] [Message JavaScript error "Undefined value" while running "__choice_su_visible"] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.28 01:59:55 UTC] [Facility install] [Sender Software Update] [PID 353] [Message __choice_su_visible returned error: Undefined value] [Level 3] [UID -2] [GID -2] [Host Hostname]


Postfix:
^^^^^^^^

.. code-block:: console

  [Time 2006.12.24 17:15:01 UTC] [Facility mail] [Sender postfix/postqueue] [PID 265] [Message warning: Mail system is down -- accessing queue directly] [Level 4] [UID -2] [GID -2] [Host Hostname]


Configd:
^^^^^^^^

.. code-block:: console

  [Time 2006.12.23 17:44:48 UTC] [Facility daemon] [Sender configd] [PID 40] [Message AppleTalk shutdown] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:44:48 UTC] [Facility daemon] [Sender configd] [PID 40] [Message AppleTalk shutdown complete] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:44:52 UTC] [Facility daemon] [Sender configd] [PID 40] [Message posting notification com.apple.system.config.network_change] [Level 5] [UID -2] [GID -2] [Host Hostname]


Crashdump:
^^^^^^^^^^

.. code-block:: console

  [Time 2006.12.23 17:30:23 UTC] [Facility daemon] [Sender crashdump] [PID 5546] [Message dummy-5507 crashed] [Level 3] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:30:23 UTC] [Facility daemon] [Sender crashdump] [PID 5546] [Message crash report written to: /Library/Logs/CrashReporter/dummy-5507.crash.log] [Level 3] [UID -2] [GID -2] [Host Hostname]


Launchd:
^^^^^^^^

.. code-block:: console

  [Time 2006.12.23 17:20:00 UTC] [Facility launchd] [Sender launchd] [PID -1] [Message Server 0 in bootstrap 1103 uid 0: "/usr/sbin/lookupd"[935\]: exited abnormally: Hangup] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:20:00 UTC] [Facility daemon] [Sender configd] [PID 40] [Message AppleTalk startup] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:20:01 UTC] [Facility netinfo] [Sender lookupd] [PID 3126] [Message lookupd (version 369.5) starting - Sat Dec 23 10:20:01 2006] [Level 5] [UID -2] [GID -2] [Host Hostname]
  [Time 2006.12.23 17:20:03 UTC] [Facility launchd] [Sender launchd] [PID -1] [Message Server 0 in bootstrap 1103 uid 0: "/usr/sbin/lookupd"[3126\]: exited abnormally: Hangup] [Level 5] [UID -2] [GID -2] [Host Hostname]


