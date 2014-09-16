
.. _ossec-execd:

ossec-execd
=============

``ossec-execd`` executes active responses by running the configured scripts.
``ossec-execd`` is configured in the ossec.conf. (see :ref:`ossec_config.active-response`)

ossec-execd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-execd
i
.. option:: -c <config>

    Run ``ossec-execd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -d

    Execute ossec-execd in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-execd`` in the foreground.

.. option:: -g

    Run as ``group``.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -V

    Version and license information.



