
.. _ossec-agentd:

ossec-agentd
=============

``ossec-agentd`` is the client side daemon that communicates with the server.
It runs as ossec and is chrooted to ``/var/ossec`` by default.


ossec-agentd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-agentd

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-agentd`` in the foreground.

.. option:: -u <user>

    Run ``ossec-agentd`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-agentd`` as <group>.

.. option:: -c <config>

    Run ``ossec-agentd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


