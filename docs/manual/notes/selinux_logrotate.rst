.. _selinux_logrotate:

SELinux and logrotate for OSSEC logs
====================================

Some OSSEC packages ship a ``logrotate`` configuration for ``/var/ossec/logs/``.
When SELinux is **enforcing**, logrotate may be denied access to OSSEC log files,
causing rotation to fail silently or log AVC denials in ``/var/log/audit/audit.log``.

Option 1: Fix file contexts
---------------------------

Label OSSEC logs with the ``var_log_t`` context so logrotate can read them:

.. code-block:: console

   ls -aZ /var/ossec/logs
   semanage fcontext -a -t var_log_t "/var/ossec/logs(/.*)?"
   restorecon -R -v /var/ossec/logs
   ls -aZ /var/ossec/logs

Option 2: Custom SELinux module
-------------------------------

Install ``policycoreutils-python`` (or the Python 3 equivalent on your
distribution) if ``audit2allow`` is not available.

Generate a module from denials (after a failed logrotate run):

.. code-block:: console

   grep ossec /var/log/audit/audit.log | grep denied | audit2allow -m ossec-hids -o ossec-hids.te

Or create ``/etc/selinux/targeted/ossec-hids/ossec-hids.te`` manually.

RHEL 6 style:

.. code-block:: none

   module ossec-hids 1.0;

   require {
       type var_t;
       type logrotate_t;
       class file getattr;
   }

   allow logrotate_t var_t:file getattr;

RHEL 7+ style:

.. code-block:: none

   module ossec-hids 1.0;

   require {
       type user_home_t;
       type logrotate_t;
       class file read;
   }

   allow logrotate_t user_home_t:file read;

Install the module:

.. code-block:: console

   checkmodule -M -m ossec-hids.te -o ossec-hids.mod
   semodule_package -o ossec-hids.pp -m ossec-hids.mod
   semodule -i ossec-hids.pp

Example logrotate snippet
-------------------------

OSSEC does not rotate ``ossec.log`` internally; use logrotate or ``newsyslog``
(see :ref:`faq_ossec`). Example ``/etc/logrotate.d/ossec``:

.. code-block:: none

   /var/ossec/logs/ossec.log {
       weekly
       rotate 12
       compress
       missingok
       notifempty
       copytruncate
   }

After adding or changing logrotate configuration, run logrotate in debug mode
and check for SELinux denials if rotation fails.
