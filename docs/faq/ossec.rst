.. _faq_ossec:

OSSEC: FAQ
-------------

.. contents:: 
    :local:


Can an OSSEC manager have more than 256 agents?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  By default OSSEC limits the number of agents to 256 per manager. This limitation is set in the code, but can be modified at compile time.
  Depending on the event load, a manager running on modern hardware can handle many more agents.
  Some users have more than 1000 agents on a single manager.
  To change the maximum number of agents, cd into the src directory and run the following command:

  .. code-block:: console

      make setmaxagents


  You should be prompted for the number of agents to allow.

  One issue you may face after changing this setting is the number of files allowed to be open for a single user.
  The users ``ossec`` and ``ossecr`` both open at least 1 file (syscheck database and rids file) per agent.
  Raising this limit is operating system specific.

  Some Linux distributions support a ``/etc/security/limits.conf``. Set the limits to be at least a few files above what the max agents is set to.

  .. code-block:: console

     ossec            soft    nofile          2048
     ossec            hard    nofile          2048
     ossecr           soft    nofile          2048
     ossecr           hard    nofile          2048



Where are OSSEC's logs stored?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  On OSSEC server and local installs there are several classes of OSSEC logs. 
  There are the logs created by the OSSEC daemons, the log messages from the agents, and the alerts.
  Agent installs do not have logs from other agents or alerts, but do have logs created by the OSSEC processes.

  All logs are stored in subdirectories of ``/var/ossec/logs``. 
  OSSEC's log messages are stored in ``/var/ossec/logs/ossec.log``.

  Log messages from the agents are not stored by default. After analysis they are deleted unless the <logall> option is included in the manager's ossec.conf. 
  If set all log messages sent to the manager are stored in ``/var/ossec/logs/archives/archives.log`` and rotated daily.

  Alerts are stored in ``/var/ossec/logs/alerts/alerts.log``, and rotated daily.


Where can I view the logs sent to an OSSEC manager (or on a local install)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  OSSEC does not store the logs sent to it by default. If a log does not trigger an alert it is discarded, and logs that do trigger alerts are stored with the alerts in ``/var/ossec/logs/alerts``.

  The ``<log-all>`` option can be added to the ``<global>`` section (see: :ref:`ossec_config.global`) of the manager's ossec.conf. The manager's OSSEC processes should be restarted.
  The raw logs will then be saved to files, organized by date, in ``/var/ossec/logs/archives``.

  The headers attached to these log messages are in the format of ``"YYYY Month dd HH:MM:ss agent_name->/path/to/log/file "``.

  .. code-block:: console

      2011 Aug 04 00:00:01 server->/var/log/local7 Aug  4 00:00:26 server named[29909]: client 192.168.1.7#39323: query: fake.example.net IN AAAA +


Can OSSEC's logs be saved to a different directory?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  As a protection mechanism, OSSEC chroots most of its processes to the install directory (typically ``/var/ossec``). 
  Due to this chroot, logs must be saved to a location under ``/var/ossec``.
  OSSEC does rotate its logs, but will not be able to move them from ``/var/ossec``.

  Be sure to allocate enough space to ``/var/ossec``.



I'm getting an error when starting OSSEC: "OSSEC analysisd: Testing rules failed. Configuration error. Exiting." Why?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  There was a small bug in the ossec-control script that was not caught in time for 2.6.
  The error comes from the script trying to run ossec-logtest from the wrong directory.
  The solution is to change the line where ossec-logtest is running to look like this:

  .. code-block:: console

      echo | ${DIR}/bin/ossec-logtest > /dev/null 2>&1;


Do the rules get pushed to the agents automatically?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  The rules only exist on the manager. All analysis is done on the manager.
  Agents do not send alerts to the manager, they only send the raw logs.


How can I get ossec.log to rotate daily?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Use logrotate.d or newsyslog. XXX

