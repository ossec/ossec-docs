
.. _ossec-maild:

ossec-maild
=============

The ``ossec-maild`` daemon sends OSSEC alerts via email.
``ossec-maild`` is started by ossec-control.
Configuration for ossec-maild is handled in the ossec.conf. (see :ref:`ossec_config.global`)

ossec-maild argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-maild

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-maild`` in the foreground.

.. option:: -u <user>

    Run ``ossec-maild`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-maild`` as <group>.

.. option:: -c <config>

    Run ``ossec-maild`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


