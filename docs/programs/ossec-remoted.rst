
.. _ossec-remoted:

ossec-remoted
=============

``ossec-remoted`` is the server side daemon that communicates with the agents.
It can listen to port 1514/udp (for OSSEC communications) and/or 514 (for syslog).
``ossec-remoted`` is configured in ossec.conf.  (see :ref:`ossec_config.remote`)


ossec-remoted argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-remoted

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-remoted`` in the foreground.

.. option:: -u <user>

    Run ``ossec-remoted`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-remoted`` as <group>.

.. option:: -c <config>

    Run ``ossec-remoted`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


