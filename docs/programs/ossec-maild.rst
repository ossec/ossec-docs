
.. _ossec-maild:

ossec-maild
=============

The ``ossec-maild`` daemon sends OSSEC alerts via email.
``ossec-maild`` is started by ossec-control.
Configuration for ossec-maild is handled in the ossec.conf. (see :ref:`ossec_config.global`)

ossec-maild argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-maild

.. option:: -c <config>

    Run ``ossec-maild`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec

.. option:: -d

    Execute ossec-maild in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-maild`` in the foreground.

.. option:: -g <group>

    Run ``ossec-maild`` as <group>.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -u <user>

    Run ``ossec-maild`` as <user>.

    **Default:** ossecm

.. option:: -V

    Version and license information.

