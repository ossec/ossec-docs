
.. _ossec-control:

ossec-control
=============

``ossec-control`` is a script to start, stop, configure, or check on the status of OSSEC processes.
``ossc-control`` can enable or disable client-syslog, database logging, agentless configurations, and debug mode.

ossec-control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    .. _ossec-control-start:

    **start**
      Start the OSSEC processes.

    .. _ossec-control-stop:

    **stop**
      Stop the OSSEC processes.

    .. _ossec-control-restart:

    **restart**
      Restart the OSSEC processes.

    .. _ossec-control-reload:

    **reload**
      Restart all OSSEC processes except ``ossec-execd``. This allows an agent to reload without losing active response status.

      .. note::

         This is only available on an OSSEC agent.

    .. _ossec-control-status:

    **status**
      Determine which OSSEC processes are running.

    .. _ossec-control-enable:

    **enable**
      Enable OSSEC functionality.

        .. _ossec-control-enable-database:

        **database**
          Enable the ``ossec-dbd`` daemon for logging to a database.

          **Available:** Server and local installs only.

          .. note::

              Database support must be compiled in at install time.

        .. _ossec-control-enable-client-syslog:

        **client-syslog**
          Enable ``ossec-csyslogd`` for logging to remote syslog.

          **Available:** Server and local installs only.

        .. _ossec-control-enable-agentless:

        **agentless**
          Enable ``ossec-agentlessd`` for running commands on systems without OSSEC agents.

          **Available:** Server and local installs only.

        .. _ossec-control-enable-debug:

        **debug**
          Run all OSSEC daemons in debug mode.


    .. _ossec-control-disable:

    **disable**
      Disable OSSEC functionality.

        .. _ossec-control-disable-database:

        **database**
          Disable the ``ossec-dbd`` daemon for logging to a database.

          **Available:** Server and local installs only.

          .. note::

              Database support must be compiled in at install time.

        .. _ossec-control-disable-client-syslog:

        **client-syslog**
          Disable ``ossec-csyslogd`` for logging to remote syslog.

         **Available:** Server and local installs only.

        .. _ossec-control-disable-agentless:

        **agentless**
          Disable ``ossec-agentlessd`` for running commands on systems without OSSEC agents.

          **Available:** Server and local installs only.

        .. _ossec-control-disable-debug:

        **debug**
          Turn off debug mode.



ossec-control example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example: Running ossec-control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/ossec-control

    Usage: /var/ossec/bin/ossec-control {start|stop|restart|status|enable|disable}


