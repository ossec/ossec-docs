
.. _ossec-makelists:

ossec-makelists
=============

The ``ossec-makelists`` utility to compile cdb databases.
``ossec-makelists`` will scan ossec.conf for database files, check the mtime, and recompile all out of date databases.

See :ref:`manual-rule-lists` for more information.

ossec-makelists argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-makelists 

.. option:: -c <config>

    Run with configuration file of <config>.

    **Default** /var/ossec/etc/ossec.conf

.. option:: -d

    Execute ossec-makelists in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -F

    Force the rebuild of all configured databases.

.. option:: -g <group>

    Run as <group>.

.. option:: -h

    Display the help message. 

.. option:: -t

    Test the configuration.

.. option:: -u <user>

    Run as <user>.

.. option:: -V

    Diplay the version and license information.



ossec-makelists example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~



Example: Running ossec-makelists and an update is necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/ossec-makelists
     * File lists/blocked.txt.cdb need to be updated


Example: Running ossec-makelists when no update is necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console 

    # /var/ossec/bin/ossec-makelists
     * File lists/blocked.txt.cdb does not need to be compiled

