.. _aes_encryption:

AES Encryption Support
======================

Starting with version 4.0.0, OSSEC supports AES-256 encryption for agent-manager communications. This provides a more secure alternative to the legacy Blowfish encryption.

**Key Features:**

*   **Algorithm:** AES-256-CBC
*   **Key Size:** 256 bits
*   **Initialization Vector (IV):** Randomly generated per message

**Configuration:**

AES encryption is supported alongside the existing encryption methods. The specific encryption algorithm used is determined by the key format managed by the `manage_agents` tool.

.. note::
   Both the OSSEC manager and agent must be running version 4.0.0 or later to support AES encryption.

Configuration Examples
----------------------

By default, OSSEC 4.0.0 agents use AES encryption, and the manager accepts both AES and Blowfish. You can explicitly configure these settings in `ossec.conf`.

**Manager Configuration (ossec.conf):**

To restrict the manager to only accept AES connections:

.. code-block:: xml

   <remote>
     <crypto_accept>aes</crypto_accept>
   </remote>

**Agent Configuration (ossec.conf):**

To force an agent to use Blowfish (legacy mode):

.. code-block:: xml

   <client>
     <crypto_method>blowfish</crypto_method>
   </client>
