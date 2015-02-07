
.. _ossec-logcollector:

ossec-logcollector
=============

The ``ossec-logcollector`` daemon monitors configured files and commands for new log messages.
``ossec-logcollector`` is configured in ossec.conf.  (see :ref:`ossec_config.localfile`)


ossec-logcollector argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-logcollector

.. option:: -c <config>

    Run ``ossec-logcollector`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -d

    Execute ossec-logcollector in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-logcollector`` in the foreground.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -V

    Version and license information.


