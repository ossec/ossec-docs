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


Can OSSEC's logs be saved to a different directory?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  As a protection mechanism, OSSEC chroots most of its processes to the install directory (typically ``/var/ossec``). 
  Due to this chroot, logs must be saved to a location under ``/var/ossec``.
  OSSEC does rotate its logs, but will not be able to move them from ``/var/ossec``.

  Be sure to allocate enough space to ``/var/ossec``.


