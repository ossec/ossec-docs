.. _faq_ossec:

OSSEC: FAQ
-------------

.. contents:: 
    :local:


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




