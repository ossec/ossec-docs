
.. _ossec-execd:

ossec-execd
=============

``ossec-execd`` executes active responses by running the configured scripts.
``ossec-execd`` is configured in the ossec.conf. (see :ref:`ossec_config.active-response`)

ossec-execd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-execd

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-execd`` in the foreground.

.. option:: -u <user>

    Run ``ossec-execd`` as <user>.

    **Default:** ossecm

.. option:: -g <group>

    Run ``ossec-execd`` as <group>.

.. option:: -c <config>

    Run ``ossec-execd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


