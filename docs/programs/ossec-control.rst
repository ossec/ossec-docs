
.. _ossec-control:

ossec-control
=============

``ossec-control`` is a script to start, stop, configure, or check on the status of OSSEC processes.
``ossc-control`` can enable or disable client-syslog, database logging, agentless configurations, and debug mode.

ossec-control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-control

.. option:: start

    Start the OSSEC processes.

.. option:: stop

    Stop the OSSEC processes.

.. option:: restart

    Restart the OSSEC processes.

.. option:: status

    Determine which OSSEC processes are running.

.. option:: enable

    Enable OSSEC functionality.

    .. option:: database

        Enable the ``ossec-dbd`` daemon for logging to a database.
        **Available:** Server and local installs only.

        .. note::
            Database support must be compiled in at install time.

    .. option:: client-syslog

        Enable ``ossec-csyslogd`` for logging to remote syslog.
        **Available:** Server and local installs only.

    .. option:: agentless

        Enable ``ossec-agentlessd`` for running commands on systems without OSSEC agents.
        **Available:** Server and local installs only.

    .. option:: debug

        Run all OSSEC daemons in debug mode.


.. option:: disable

    Disable OSSEC functionality.

    .. option:: database

        Disable the ``ossec-dbd`` daemon for logging to a database.
        **Available:** Server and local installs only.

        .. note::
            Database support must be compiled in at install time.

    .. option:: client-syslog

        Disable ``ossec-csyslogd`` for logging to remote syslog.
        **Available:** Server and local installs only.

    .. option:: agentless

        Disable ``ossec-agentlessd`` for running commands on systems without OSSEC agents.
        **Available:** Server and local installs only.

    .. option:: debug

        Turn off debug mode.



ossec-control example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example: Running ossec-control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/ossec-control

    Usage: /var/ossec/bin/ossec-control {start|stop|restart|status|enable|disable}


