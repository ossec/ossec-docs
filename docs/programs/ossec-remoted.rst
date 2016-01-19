
.. _ossec-remoted:

ossec-remoted
=============

``ossec-remoted`` is the server side daemon that communicates with the agents.
It can listen to port 1514/udp (for OSSEC communications) and/or 514 (for syslog).
It runs as ossecr and is chrooted to ``/var/ossec`` by default.
``ossec-remoted`` is configured in the <remote> section of  ossec.conf. 
(see :ref:`ossec_config.remote`)


ossec-remoted argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-remoted

.. option:: -c <config>

    Run ``ossec-remoted`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec

.. option:: -d

    Execute ossec-remoted in debug mode. This can be used more than once to increase the verbosity of the debug messages.

.. option:: -f

    Run ossec-remoted in the foreground.

.. option:: -g <group>

    Run ``ossec-remoted`` as <group>.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -u <user>

    Run ``ossec-remoted`` as <user>.

    **Default:** ossecm

.. option:: -V

    Version and license information.


