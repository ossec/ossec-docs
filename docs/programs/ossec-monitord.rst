
.. _ossec-monitord:

ossec-monitord
=============

The ``ossec-monitord`` daemon monitors agent connectivity and compress daily log files.
``ossec-monitord`` is configured in ossec.conf.  (see :ref:`ossec_config.localfile`)


ossec-monitord argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-monitord

.. option:: -c <config>

    Run ``ossec-monitord`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec

.. option:: -d

    Execute ossec-monitord in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-monitord`` in the foreground.

.. option:: -g <group>

    Run ``ossec-monitord`` as <group>.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -u <user>

    Run ``ossec-monitord`` as <user>.

    **Default:** ossecm

.. option:: -V

    Version and license information.


