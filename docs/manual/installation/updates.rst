.. _manual-updates:

OSSEC Updates
=============

Prefer **package upgrades** (RPM/DEB from Atomicorp) when they are available for
your platform. Packages update binaries through the normal package manager and
restart OSSEC via the systemd (or SysV) service unit, which is cleaner than a
hand-rolled source tree swap.

Before any major upgrade, back up at least:

* ``/var/ossec/etc/ossec.conf``
* ``/var/ossec/etc/client.keys`` (managers)
* ``/var/ossec/rules/local_rules.xml``
* ``/var/ossec/etc/local_decoder.xml`` (or ``etc/decoders/local_decoder.xml``)
* Any other local customizations under ``/var/ossec``

For breaking changes between major versions (for example 3.x → 4.x crypto and
FIM defaults), see :ref:`upgrade-migration`.

Package upgrades (recommended)
-------------------------------

If OSSEC was installed from the Atomicorp repositories (see
:ref:`manual-install-package`), upgrade with the system package manager.

**RPM (RHEL, CentOS, Fedora, and similar):**

.. code-block:: console

   # yum update ossec-hids ossec-hids-server    # manager
   # yum update ossec-hids ossec-hids-agent     # agent

On newer systems, ``dnf upgrade`` is equivalent.

**DEB (Debian, Ubuntu):**

.. code-block:: console

   # apt-get update
   # apt-get install --only-upgrade ossec-hids-server
   # apt-get install --only-upgrade ossec-hids-agent

What the package path gives you
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Config files marked as package config are preserved across upgrades.
* The ``ossec-hids`` systemd unit (or init script) handles **stop/start around
  the upgrade** so processes come back under the packaged layout.
* You avoid mixing an old source ``install.sh`` tree with newer binaries.

A manager upgrade still implies a **short service restart window**. That is not
true zero-downtime high availability. For continuous coverage during a cutover,
stand up a second manager, copy keys/config, point agents at it, then retire the
old manager (see also :ref:`manager_backup`).

Upgrade managers before agents when the release notes require it (notably for
4.x agent encryption). Agents are **not** upgraded automatically by the
manager; run the same package upgrade on each agent host (or your agent fleet
tooling).

Source upgrades
---------------

If you installed from source, download the latest release and run the usual
installer. It detects an existing install and asks:

.. code-block:: console

    - You already have OSSEC installed. Do you want to update it? (y/n): y

Answer ``yes`` to update the OSSEC binaries. ``local_rules.xml`` and
``local_decoder.xml`` are not modified during this upgrade.

The script also prompts:

.. code-block:: console

   - Do you want to update the rules? (y/n): y

Answering ``yes`` updates the ``<rules>`` section of the system's
``ossec.conf``.

After a source upgrade, restart OSSEC explicitly (for example
``/var/ossec/bin/ossec-control restart`` or ``systemctl restart ossec-hids``)
so all daemons load the new binaries.

Checklist
---------

1. Read the release notes / :ref:`changelog` and :ref:`upgrade-migration` for
   your target version.
2. Back up configuration and keys.
3. Upgrade the **manager** first (package preferred).
4. Confirm agents reconnect and alerts look normal.
5. Upgrade **agents** in batches.
6. Re-check custom syslog CEF, ``database_output``, or other integrations after
   major version jumps.
