
.. _ossec-syscheckd:

ossec-syscheckd
===============

The ``ossec-syscheckd`` daemon checks configured files for changes to the checksums, permissions or ownership.
``ossec-syscheckd`` is started by ossec-control.
Configuration for ossec-syscheckd is handled in the ossec.conf. 

See :ref:`manual-syscheck` for more detailed configuration information.

ossec-syscheckd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-syscheckd

.. option:: -c <config>

    Run ``ossec-syscheckd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -d

    Execute ossec-syscheckd in debug mode. This can be used more than once to increase the verbosity of the debug messages.

.. option:: -f

    Run ``ossec-syscheckd`` in the foreground.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -V

    Version and license information.


