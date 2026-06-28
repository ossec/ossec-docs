.. _manager_backup:

Manager backup and migration
============================

Use this guide to back up an OSSEC manager or migrate it to new hardware.
For **version upgrades** (for example 3.8 to 4.x), see :ref:`upgrade-migration`
instead — crypto and agent compatibility differ from a like-for-like host move.

When to use this guide
----------------------

* **Backup** — periodic snapshot before major changes
* **Hardware migration** — move the manager to a new server at the **same OSSEC version**
* **Disaster recovery** — restore from backup after failure

Pre-migration checklist
-----------------------

1. Record the installed OSSEC version: ``/var/ossec/bin/ossec-control info``
2. Note the agent count: ``/var/ossec/bin/agent_control -l``
3. Stop OSSEC cleanly: ``/var/ossec/bin/ossec-control stop``
4. Ensure no package upgrade is pending on the destination unless you also follow
   :ref:`upgrade-migration`

Files to copy
-------------

Agent keys and registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   /var/ossec/etc/client.keys
   /var/ossec/queue/rids/

Configuration and rules
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   /var/ossec/etc/ossec.conf
   /var/ossec/etc/internal_options.conf
   /var/ossec/etc/local_internal_options.conf
   /var/ossec/etc/shared/
   /var/ossec/rules/
   /var/ossec/etc/decoders/
   /var/ossec/etc/lists/

Agent state databases (optional but recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preserves FIM baselines, rootcheck state, and similar per-agent data:

.. code-block:: console

   /var/ossec/queue/syscheck/
   /var/ossec/queue/rootcheck/
   /var/ossec/queue/fts/
   /var/ossec/queue/agentless/
   /var/ossec/queue/agents/

Logs (optional)
^^^^^^^^^^^^^^^

.. code-block:: console

   /var/ossec/logs/

Restore procedure
-----------------

1. Install the **same OSSEC version** on the destination host (see :ref:`install`).
2. Stop OSSEC on the destination: ``/var/ossec/bin/ossec-control stop``
3. Copy backed-up files into ``/var/ossec/``, preserving ownership (``ossec:ossec``
   or your platform's equivalent).
4. If the manager IP or hostname changed, update agent ``<server-ip>`` or
   ``<server-hostname>`` on each agent, or use DNS that resolves to the new host.
5. Start OSSEC: ``/var/ossec/bin/ossec-control start``
6. Verify agents reconnect: ``/var/ossec/bin/agent_control -l`` — agents should
   show as **Active** within a few minutes.

.. note::

   You do not need to re-enroll agents if ``client.keys`` and ``queue/rids/`` were
   copied intact and the manager identity is unchanged.

Verification
------------

* ``/var/ossec/bin/ossec-control status`` — all required daemons running
* ``/var/ossec/bin/agent_control -l`` — expected agents active
* Review ``/var/ossec/logs/ossec.log`` for authentication or rule errors
