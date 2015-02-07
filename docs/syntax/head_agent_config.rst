
.. _agent_config: 

agent.conf
==========

Overview 
--------

More information on using the agent.conf can be found `here <../manual/agent/agent-configuration.html>`_


Supported types
^^^^^^^^^^^^^^^

The agent.conf is valid on the server install only.

Location 
^^^^^^^^

The ``agent.conf`` exists in ``/var/ossec/etc/shared``.
It should be readable by the ossec user.

.. code-block:: console

    -r-xr-x---  1 root  ossec  10908 Aug 12 16:06 /var/ossec/etc/shared/agent.conf


XML excerpt to show location:

.. code-block:: xml 

    <agent_config>
        ...
    </agent_config>



Options
-------

.. include:: agent_config.trst





