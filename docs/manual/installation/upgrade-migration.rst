.. _upgrade-migration:

Upgrading to OSSEC 4.x
======================

This guide covers breaking changes and recommended upgrade order when moving from
OSSEC 3.8.x or earlier to 4.0.0 and later, including 4.1.0.

Recommended upgrade order
-------------------------

1. **Upgrade all managers first** (server and local installs) to 4.0.0 or later.
2. **Verify manager connectivity** and that ``ossec-authd`` (if used) is running.
3. **Upgrade agents** one group at a time, validating connectivity after each batch.
4. **Review FIM baselines** after upgrade; SHA-256 defaults may produce one-time change alerts.

.. warning::

   OSSEC 4.0.0 agents use **AES-256** encryption by default. This is **not** compatible
   with managers running 3.8.0 or older. Always upgrade managers before agents.

Agent encryption (4.0.0+)
-------------------------

Starting with 4.0.0, agent-manager traffic uses AES-256-CBC by default. Legacy Blowfish
keys and connections are still supported on 4.0+ managers when configured.

Crypto interoperability matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+------------------+---------------------------+
| Manager          | Agent            | Result                    |
+==================+==================+===========================+
| 4.0+ (default)   | 4.0+ (default)   | AES — works               |
| 4.0+ (default)   | 3.8 or older     | **Fails** — upgrade agent |
| 4.0+ (default)   | 4.0+ blowfish    | Works if manager accepts  |
| 3.8 or older     | 4.0+ (default)   | **Fails** — upgrade mgr   |
+------------------+------------------+---------------------------+

Manager configuration
^^^^^^^^^^^^^^^^^^^^^

Restrict the manager to AES-only connections:

.. code-block:: xml

   <remote>
     <crypto_accept>aes</crypto_accept>
   </remote>

Accept both AES and Blowfish during a transition (default on 4.0+):

.. code-block:: xml

   <remote>
     <crypto_accept>any</crypto_accept>
   </remote>

Agent configuration
^^^^^^^^^^^^^^^^^^^

Force legacy Blowfish on a 4.0+ agent (temporary migration aid only):

.. code-block:: xml

   <client>
     <crypto_method>blowfish</crypto_method>
   </client>

New agent keys generated with ``manage_agents`` on 4.0+ use AES. See also
:ref:`aes_encryption` for background on key formats.

File integrity monitoring (4.0.0+)
----------------------------------

SHA-256 checksums are **enabled by default** for all monitored directories in 4.0.0.
No configuration change is required for new installations.

Disable SHA-256 on specific paths (compatibility only):

.. code-block:: xml

   <syscheck>
     <directories check_sha256sum="no">/path</directories>
   </syscheck>

Large files (>2GB) are supported starting with 4.1.0 when the platform build enables
64-bit file offsets.

Re-keying agents after crypto changes
-------------------------------------

If agents fail to connect after a manager upgrade:

1. Confirm the manager ``<remote>`` ``crypto_accept`` setting allows the agent's method.
2. On the manager, use ``manage_agents`` to list and verify the agent key exists.
3. If keys were generated on an older version, extract a fresh key and re-import on the agent.
4. Restart ``ossec-agentd`` on the agent after updating ``client.keys``.

Email and reporting (4.1.0+)
----------------------------

SMTP TLS and authentication options in ``<global>`` apply to both ``ossec-maild`` and
``ossec-monitord`` report email. See :ref:`manual-out-email` and
:ref:`ossec_config.global`.

See also
--------

* :ref:`aes_encryption`
* :ref:`ossec_config.client`
* :ref:`ossec_config.remote`
* :ref:`ossec_config.syscheck`
* :ref:`changelog`
