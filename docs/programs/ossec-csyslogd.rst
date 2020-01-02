
.. _ossec-csyslogd:

ossec-csyslogd
==============

``ossec-csyslogd`` is a daemon that forwards the OSSEC alerts via syslog.
Configuration is done in the ``<syslog_output>`` section of the ossec.conf. (see :ref:`ossec_config.syslog_output`)


ossec-csyslogd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-csyslogd

.. option:: -c <config>

    Run ``ossec-csyslogd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec

.. option:: -d

    Execute ossec-csyslogd in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-csyslogd`` in the foreground.

.. option:: -g <group>

    Run ``ossec-csyslogd`` as <group>.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -u <user>

    Run ``ossec-csyslogd`` as <user>.

    **Default:** ossecm

.. option:: -V

    Version and license information.


