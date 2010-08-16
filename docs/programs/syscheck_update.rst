
.. _syscheck_update:

syscheck_update
===============

syscheck_update: Updates the integrity check database. This means that all information about files that were added to the integrity check database will be dismissed and leave an empty database which will be populated again the next time the syscheck daemon runs on agents or the server.

It does the same thing as :option:`syscheck_control -u`(cf. :ref:`syscheck_control`).

syscheck_update argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: syscheck_update

.. option:: -h

    Display the help message.

.. option:: -l 

    List available agents. 

.. option:: -a 

    Updates the database for all agents.

.. option:: -u <agent_id>

    Updates the database for the agent.

.. option:: -u local

    Updates the local database.


