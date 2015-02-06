
.. _ossec-analysisd:

ossec-analysisd
===============

``ossec-analysisd`` recveives the log messages and compares them to the rules. It will create alerts when a log message matches an applicable rule.


ossec-analysisd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-analysisd

.. option:: -c <config>

    Configuration file ossec-analysisd should use.

.. option:: -D <dir>

    Chroot to ``<dir>``.

.. option:: -d

    Execute ossec-analysisd in debug mode. This can be used more than once to increase the verbosity of the debug messages.

.. option:: -f

    Run ossec-agentlessd in the foreground.

.. option:: -g <group>

    Run as ``group``.

.. option:: -h

    Display a help message.

.. option:: -t

    Test the configuration.

.. option:: -u

    Run as ``user``.

.. option:: -V

    Display the version and license information.


