
.. _verify-agent-conf:

verify-agent-conf
==============

``verify-agent-conf`` verifies the OSSEC agent.conf configuration.
It exits silently if the configuration is correct.


verify-agent-conf example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Example 1: Running verify-agent-conf on a working agent.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/verify-agent-conf
    #


Example 2: Running verify-agent-conf on a non-working agent.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/verify-agent-conf
    2011/07/12 21:22:07 ossec-config(1226): ERROR: Error reading XML file '/var/ossec/etc/shared/agent.conf': XML ERR: Bad formed XML. Element not opened (line 13).


