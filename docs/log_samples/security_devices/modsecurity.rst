Modsecurity samples
-------------------

Access denied:
^^^^^^^^^^^^^^

.. code-block:: console

  [Sun Jan 16 10:56:49 2005] [error] [client 192.168.2.10] mod_security: Access denied with code 403. Pattern match "111" at THE_REQUEST [hostname "192.168.2.101"] [uri "/index.html?111"]


Nginx / libmodsecurity error log:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2019/08/29 09:59:06 [error] 13#13: *1031 [client 203.0.113.10] ModSecurity: Access denied with code 403 (phase 2). Matched "Operator" against variable "ARGS:q" [id "941100"] [hostname "example.com"] [uri "/"] [unique_id "abc123"]


Serial audit log (``modsec-audit``):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure logcollector with ``<log_format>modsec-audit</log_format>`` so each
transaction (``--id-A--`` … ``--id-Z--``) is one event. Example sections:

.. code-block:: console

  --fbd13fc1-A--
  [22/Dec/2015:15:25:00 +0000] VnhlYH8AAQEAADYdAUkAAAAA 127.0.0.1 55275 127.0.0.1 80
  --fbd13fc1-B--
  GET /?q=test HTTP/1.1
  Host: localhost

  --fbd13fc1-H--
  Message: Access denied with code 403 (phase 2). Pattern match "test" at ARGS:q
  Action: Intercepted (phase 2)
  --fbd13fc1-Z--


Access denied by pattern:
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  mod_security-message: Access denied with code 412. Pattern match "flashget" at HEADER
  mod_security-message: Access denied with code 412. Pattern match "getright" at HEADER
  mod_security-message: Access denied with code 412. Pattern match "^Download" at HEADER
  mod_security-message: Access denied with code 412. Pattern match "^DA d.d+" at HEADER


Access denied by pattern (invalid user agent):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/admin/pma/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/web/phpMyAdmin/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/dbadmin/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/db/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/admin/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/mysql/main.php"]
  [Mon Jun 11 03:17:22 2007] [error] [client 68.76.16.11] mod_security: Access denied with code 406. Pattern match "^$" at HEADER("USER-AGENT") [severity "EMERGENCY"] [hostname "192.168.1.1"] [uri "/PMA/main.php"]

