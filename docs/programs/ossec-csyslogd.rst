
.. _ossec-csyslogd:

ossec-csyslogd
=============

``ossec-csyslogd`` is a daemon that forwards the OSSEC alerts via syslog.
Configuration is done in the ``<syslog_output>`` section of the ossec.conf. (see :ref:`ossec_config.syslog_output`)


ossec-csyslogd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-csyslogd

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-csyslogd`` in the foreground.

.. option:: -u <user>

    Run ``ossec-csyslogd`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-csyslogd`` as <group>.

.. option:: -c <config>

    Run ``ossec-csyslogd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


