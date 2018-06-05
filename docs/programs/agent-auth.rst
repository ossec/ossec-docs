
.. _agent-auth:

agent-auth
==========

The agent-auth program is the client application used with :ref:`ossec-authd` to automatically add agents to an OSSEC manager.

.. warning::

    By default there is no authentication or authorization involved in this transaction, so it is recommended that 
    this daemon only be run when a new agent is being added.

agent-auth argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: agent-auth

.. option:: -A <agent_name>

    Agent name to be used.
    **Default** hostname

.. option:: -D

    Directory where OSSEC is installed.
    **Default** /var/ossec

.. option:: -d
      
    Execute agent-auth in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -g <group>

    Run as ``group``.

.. option:: -h

    Display the help message 

.. option:: -k <path>

    Full path to the agent key.

.. option:: -m <manager_ip>

    IP address of the manager.

.. option:: -p <port>

    Port ossec-authd is running on.

    **Default** 1515

.. option:: -V 

    Display OSSEC Version and license information.

.. option:: -v <path>

    Full path to the CA certificate used to verify the server.

   .. note::

      This option was added after 2.8.1.

.. option:: -x <path>

    Full path to the agent certificate.

.. note::

   The following options are only necessary if verification of server or client certificates is desired. See :ref:`optional-server-authentication` and
   :ref:`optional-client-authentication` below.

   .. note::

      This option was added after 2.8.1.

.. option:: -x </path/to/certificate>

   Load the PEM encoded certificate that will be presented to :ref:`ossec-authd` during establishment of the SSL connection.

   .. note::

      This option was added after 2.8.1.

.. option:: -k </path/to/private_key>

   Load the certificate's corresponding PEM encoded private key.

   .. note::

      This option was added after 2.8.1.

.. option:: -v </path/to/CA_certificate>

   Load the PEM encoded CA Certificate that will be used to verify :ref:`ossec-authd` if desired. If this option is used then
   :ref:`ossec-authd` must present a valid certificate signed by this CA.

   .. note::

      This option was added after 2.8.1.


.. _optional-server-authentication:

Optional Server Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``agent-auth`` can verify that the server it's connecting to presents a valid X.509 certificate when requesting
a key. This is optional and is only useful if hosts in your environment have access to the root certificate of
the CA that signed the certificate presented by :ref:`ossec-authd`. If server certificate verification is desired
then the relevant CA certificate must be loaded with the -v option, then if the server does not present a valid
certificate the agent will not be allocated a key.

A certificate presented by the server may be found to be invalid for the following reasons:

- It was not signed by the specified CA.
- It doesn't contain the IP address or hostname given with the -m option in the subject's common name field or a
  subject alternative name extension field.
- It is expired.

While server authentication is optional it is highly recommended that it be used if possible when running ossec-authd
and agent-auth.

.. _optional-client-authentication:

Optional Client Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``agent-auth`` can present its own certificate to the server for verification. This is mandatory if :ref:`ossec-authd` 
was run with the -v option and optional otherwise. This is only useful if hosts in your environment are assigned
certificates when they're provisioned (or at some point before being added to OSSEC). Use the -x and -k options
to load a certificate and private key.


agent-auth example usage
~~~~~~~~~~~~~~~~~~~~~~~~

Example: Adding an agent with a hostname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/agent-auth -m 192.168.1.1 -p 1515 -A example-agent
    INFO: Connected to 192.168.1.1:1515
    INFO: Using agent name as: melancia
    INFO: Send request to manager. Waiting for reply.
    INFO: Received response with agent key
    INFO: Valid key created. Finished.
    INFO: Connection closed. 

Example: Adding an agent and verifying the certificate presented by ossec-authd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/agent-auth -m ossec-manager.localdomain -p 1515 -v /etc/pki/CA/certs/internal_CA.cert
    INFO: Connected to 192.168.1.1:1515
    INFO: Verifying manager's certificate
    INFO: Using agent name as: melancia
    ...

Example: Adding an agent and presenting a certificate to ossec-authd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/agent-auth -m ossec-manager.localdomain -p 1515 -x /var/ossec/etc/client.cert -k /var/ossec/etc/client.key
    INFO: Connected to 192.168.1.1:1515
    INFO: Using agent name as: melancia
    ...

