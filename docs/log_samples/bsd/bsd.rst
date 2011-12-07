Log Samples from BSD systems
----------------------------

OpenBSD file system full:
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Dec 30 21:01:13 bsd1 /bsd: uid 0 on /: file system full
  Dec 30 21:07:01 bsd1 /bsd: uid 0 on /tmp: file system full
  Dec 30 21:09:25 bsd1 pflogd[1234]: Logging suspended: fwrite: No space left



FreeBSD authentication failures:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jan  9 14:00:28 t123 login: pam_ldap: error trying to bind as user "uid=xx,ou=Users,dc=yy,dc=zz,dc=com" (Invalid credentials)
  Jan  9 14:00:37 t123 login: pam_ldap: error trying to bind as user "uid=xx,ou=Users,dc=yy,dc=zz,dc=com" (Invalid credentials)
  Jan  9 14:00:41 t123 login: 2 LOGIN FAILURES FROM xx.yy.net.pl



FreeBSD NTP sync messages:
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jan  9 18:00:11 t123 ntpdate[92110]: adjust time server 1.2.3.4 offset 0.053179 sec
  Jan  9 19:00:04 t123 ntpdate[92238]: adjust time server 1.2.3.4 offset 0.095983 sec
  Jan  9 20:00:04 t123 ntpdate[92364]: adjust time server 1.2.3.4 offset 0.048435 sec



