
.. _ossec-syscheckd:

ossec-syscheckd
=============

The ``ossec-syscheckd`` daemon checks configured files for changes to the checksums, permissions or ownership.
``ossec-syscheckd`` is started by ossec-control.
Configuration for ossec-syscheckd is handled in the ossec.conf. 

See :ref:`manual-syscheck` for more detailed configuration information.

ossec-syscheckd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-syscheckd

.. option:: -d

    Run in debug mode.

.. option:: -V

    Version and license information.

.. option:: -h

    Display the help message.

.. option:: -t

    Test configuration.

.. option:: -f

    Run ``ossec-syscheckd`` in the foreground.

.. option:: -c <config>

    Run ``ossec-syscheckd`` using <config> as the configuration file.

    **Default:** /var/ossec/etc/ossec.conf

.. option:: -D <dir>

    Chroot to <dir>.

    **Default:** /var/ossec


