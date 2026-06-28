.. _systemd-deployment:

systemd deployment
==================

OSSEC ships systemd unit files for server, agent, hybrid, and agent-enrollment installs.

Main service
------------

``ossec-hids.service`` wraps ``ossec-control start|stop`` for standard server, local,
and agent installs:

.. code-block:: ini

   [Service]
   Type=forking
   EnvironmentFile=/etc/ossec-init.conf
   Environment=DIRECTORY=/var/ossec
   ExecStart=/usr/bin/env ${DIRECTORY}/bin/ossec-control start
   ExecStop=/usr/bin/env ${DIRECTORY}/bin/ossec-control stop

Enable after install:

.. code-block:: console

   systemctl enable ossec-hids
   systemctl start ossec-hids

Hybrid install
--------------

A **hybrid** manager both receives agents and runs as an agent to an upstream manager.
Use ``ossec-hids-hybrid.service``, which points at the nested agent control script under
``${DIRECTORY}/ossec-agent/bin/ossec-control``.

Agent enrollment (authd)
------------------------

``ossec-authd`` is **not** started by ``ossec-control``. It runs as a separate unit,
``ossec-hids-authd.service``:

.. code-block:: ini

   ExecStartPre=/usr/bin/env ${DIRECTORY}/bin/ossec-authd -t
   ExecStart=/usr/bin/env ${DIRECTORY}/bin/ossec-authd -f

Enable on managers that accept agent registration:

.. code-block:: console

   systemctl enable ossec-hids-authd
   systemctl start ossec-hids-authd

Tune worker concurrency with ``authd.worker_pool`` and ``authd.max_connections`` in
``internal_options.conf``. See :ref:`intopt_authd`.

Environment file
----------------

Units read ``/etc/ossec-init.conf`` for ``DIRECTORY`` (default ``/var/ossec``). This file
is created by ``install.sh``.

See also
--------

* :ref:`install`
* :ref:`ossec-authd`
* :ref:`ossec-control`
* :ref:`intopt_authd`
