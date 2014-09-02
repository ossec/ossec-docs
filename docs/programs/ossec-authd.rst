
.. _ossec-authd:

ossec-authd
=============

The ossec-authd daemon will automatically add an agent to an OSSEC manager and provide the key to the agent.
The :ref:`agent-auth` application is the client application used with ossec-authd. 
`ossec-authd` will create an agent with an ip address of `any` instead of using its actual IP.

.. warning::

    There is no authentication or authorization involved in this transaction, so it is recommended that 
    this daemon only be run when a new agent is being added.

ossec-authd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-authd

.. option:: -D <dir>

    chroot to ``<dir>``.

.. option:: -d

    Execute ossec-authd in debug mode. This option can be used multiple times to increase the verbosity of the debug messages.

.. option:: -g <group>

    Run as ``group``.

.. option:: -h

    Display a help message.

.. option:: -i

    Add agents with a specific IP address instead of using ``any``.

.. option:: -k <path>

    Full path to the server key.

.. option:: -p <port>

   Listen on port.

   **Default** 1515

.. option:: -t

    Test the configuration.

.. option:: -V 

    Display OSSEC Version and license information.

.. option:: -v <path>

    Full path to the CA certificate used to verify the clients.

.. option:: -x <path>

    Full path to the server certificate.


Creating SSL keys
~~~~~~~~~~~~~~~~~

``ossec-authd`` requires SSL keys to run. This process will create the necessary keys in ``/var/ossec/etc`` and allow ``ossec-authd`` to start:

.. code-block:: console

  # openssl genrsa -out /var/ossec/etc/sslmanager.key 2048
  # openssl req -new -x509 -key /var/ossec/etc/sslmanager.key -out /var/ossec/etc/sslmanager.cert -days 365


Without the key ``ossec-authd`` will give the following error:

.. code-block:: console

  [user@ossec-manager] :; sudo /var/ossec/bin/ossec-authd  
  2012/04/18 11:05:01 ossec-authd: INFO: Started (pid: 20669).
  2012/04/18 11:05:01 ossec-authd: ERROR: Unable to read certificate file (not found): /var/ossec/etc/sslmanager.cert
  2012/04/18 11:05:01 ossec-authd: ERROR: SSL error. Exiting.



ossec-authd example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example: Running ossec-authd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /var/ossec/bin/ossec-authd -p 1515 >/dev/null 2>&1 &

And the logs when an agent is added:

.. code-block:: console

    2011/01/19 15:04:40 ossec-authd: INFO: New connection from 192.168.10.5
    2011/01/19 15:04:41 ossec-authd: INFO: Received request for a new agent (example-agent) from: 192.168.10.5
    2011/01/19 15:04:41 ossec-authd: INFO: Agent key generated for example-agent (requested by 192.168.10.5)
    2011/01/19 15:04:41 ossec-authd: INFO: Agent key created for example-agent (requested by 192.168.10.5) 


