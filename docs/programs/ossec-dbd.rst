
.. _ossec-dbd:

ossec-dbd
=============

The ``ossec-dbd`` daemon inserts the alert logs into a database, either postgresql or mysql.
``ossec-dbd`` is configured in ossec.conf.  (see :ref:`ossec_config.database_output`)


ossec-dbd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-dbd

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-dbd`` in the foreground.

.. option:: -u <user>

    Run ``ossec-dbd`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-dbd`` as <group>.

.. option:: -c <config>

    Run ``ossec-dbd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


