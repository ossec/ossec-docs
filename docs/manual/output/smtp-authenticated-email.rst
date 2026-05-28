
.. _manual-out-smtp-auth:

SMTP authentication and TLS
===========================

.. versionadded:: 4.1.0

Starting with OSSEC 4.1.0, ``ossec-maild`` and ``ossec-monitord`` can send email through SMTP servers
that require authentication and TLS. This requires OSSEC to be built with libcurl (``USE_CURL=yes``).
The installer sets this automatically when you enable SMTP authentication, secure SMTP, a custom port,
or disable TLS certificate verification during ``install.sh``.

All options are configured in the ``<global>`` section of ``ossec.conf``. See :ref:`ossec_config.global`
for the full syntax reference.

Build requirements
------------------

Install libcurl development packages on the build host before compiling:

Red Hat family:

.. code-block:: console

   yum install libcurl-devel

Debian / Ubuntu:

.. code-block:: console

   apt-get install libcurl4-openssl-dev

If you build manually without ``install.sh``, pass ``USE_CURL=yes`` to ``make``:

.. code-block:: console

   cd ossec-hids-*
   make USE_CURL=yes
   ./install.sh

Submission port with STARTTLS (port 587)
----------------------------------------

Typical configuration for providers that use authenticated submission with STARTTLS
(``auth_smtp=yes``, ``secure_smtp=no``):

.. code-block:: xml

    <ossec_config>
        <global>
            <email_notification>yes</email_notification>
            <email_to>alerts@example.com</email_to>
            <email_from>ossec@example.com</email_from>
            <smtp_server>smtp.example.com</smtp_server>
            <auth_smtp>yes</auth_smtp>
            <secure_smtp>no</secure_smtp>
            <smtp_port>587</smtp_port>
            <smtp_user>ossec@example.com</smtp_user>
            <smtp_password>your-secret-here</smtp_password>
            <smtp_tls_verify>yes</smtp_tls_verify>
        </global>
        <alerts>
            <email_alert_level>7</email_alert_level>
        </alerts>
    </ossec_config>

If ``smtp_port`` is omitted and ``auth_smtp`` is ``yes``, port **587** is used automatically.

SMTPS (implicit TLS, port 465)
------------------------------

Use ``secure_smtp=yes`` when the server expects TLS from the first byte (SMTPS):

.. code-block:: xml

    <ossec_config>
        <global>
            <email_notification>yes</email_notification>
            <email_to>alerts@example.com</email_to>
            <email_from>ossec@example.com</email_from>
            <smtp_server>smtp.example.com</smtp_server>
            <secure_smtp>yes</secure_smtp>
            <smtp_port>465</smtp_port>
            <smtp_user>ossec@example.com</smtp_user>
            <smtp_password>your-secret-here</smtp_password>
        </global>
    </ossec_config>

If ``smtp_port`` is omitted and ``secure_smtp`` is ``yes``, port **465** is used automatically.

Plain SMTP (port 25)
--------------------

Legacy servers without authentication continue to work as before. Do not set ``auth_smtp`` or
``secure_smtp`` unless the server requires them:

.. code-block:: xml

    <ossec_config>
        <global>
            <email_notification>yes</email_notification>
            <email_to>alerts@example.com</email_to>
            <smtp_server>192.168.1.10</smtp_server>
        </global>
    </ossec_config>

Testing and restarting
----------------------

Test the configuration without sending mail:

.. code-block:: console

    # /var/ossec/bin/ossec-maild -t

Restart OSSEC after changing mail settings:

.. code-block:: console

    # /var/ossec/bin/ossec-control restart

Unattended installation
-----------------------

For unattended installs, set the following in ``etc/preloaded-vars.conf`` in addition to
``USER_ENABLE_EMAIL``, ``USER_EMAIL_ADDRESS``, and ``USER_EMAIL_SMTP``:

.. code-block:: console

   USER_SMTP_AUTH="y"
   USER_SMTP_USER="user@example.com"
   USER_SMTP_PASS="secret"
   USER_SMTP_SECURE="n"
   USER_SMTP_PORT="587"
   USER_SMTP_TLS_VERIFY="y"

See :ref:`install_source_unattended` for the full preloaded-vars example.

Security notes
--------------

- Restrict permissions on ``ossec.conf`` because ``smtp_password`` is stored in plain text.
- Avoid ``smtp_tls_verify=no`` in production; it disables certificate and hostname verification.
- If ``smtp_server`` is a hostname, ensure name resolution works from ``/var/ossec/etc`` (copy
  ``/etc/resolv.conf`` when needed).
