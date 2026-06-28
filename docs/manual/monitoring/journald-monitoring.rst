.. _journald-monitoring:

Journald log monitoring
=======================

On Linux systems with systemd, ``ossec-logcollector`` can read the local systemd journal
instead of (or in addition to) plain-text log files.

Requirements
------------

* OSSEC built with systemd journal support (``libsystemd-dev`` / ``systemd-devel`` at
  compile time; see :ref:`install`).
* systemd journal available on the host (typical on modern Linux distributions).

Configuration
-------------

Add a ``<localfile>`` block with ``log_format`` set to ``journald``:

.. code-block:: xml

   <localfile>
     <log_format>journald</log_format>
     <location>all</location>
   </localfile>

Filter by ``SYSLOG_IDENTIFIER`` (unit or program name):

.. code-block:: xml

   <localfile>
     <log_format>journald</log_format>
     <location>NetworkManager</location>
   </localfile>

   <localfile>
     <log_format>journald</log_format>
     <location>su</location>
   </localfile>

``location`` values
^^^^^^^^^^^^^^^^^^^

* ``all`` — every journal entry on the local host.
* *identifier* — only entries whose ``SYSLOG_IDENTIFIER`` field matches (for example a
  systemd unit name or command name).

Behavior
--------

* Journal entries are converted to a syslog-like format before being sent to
  ``ossec-analysisd``.
* Starting with OSSEC 4.1.0, journald sources are polled continuously by
  ``ossec-logcollector``, independent of ``command``-style ``frequency`` settings.
* Journal monitoring requires read access to the journal; the OSSEC user must be in the
  ``systemd-journal`` group on some distributions.

See also
--------

* :ref:`ossec_config.localfile`
* :ref:`manual_analysis`
* :ref:`ossec-logcollector`
