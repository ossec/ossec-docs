
.. _ossec-logcollector:

ossec-logcollector
=============

The ``ossec-logcollector`` daemon monitors configured files and commands for new log messages.
``ossec-logcollector`` is configured in ossec.conf.  (see :ref:`ossec_config.localfile`)


ossec-logcollector argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-logcollector

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-logcollector`` in the foreground.

.. option:: -u <user>

    Run ``ossec-logcollector`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-logcollector`` as <group>.

.. option:: -c <config>

    Run ``ossec-logcollector`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


