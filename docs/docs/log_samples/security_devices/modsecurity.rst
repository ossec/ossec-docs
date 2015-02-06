Modsecurity samples
-------------------

Access denied:
^^^^^^^^^^^^^^

.. code-block:: console

  [Sun Jan 16 10:56:49 2005] [error] [client 192.168.2.10] mod_security: Access denied with code 403. Pattern match "111" at THE_REQUEST [hostname "192.168.2.101"] [uri "/index.html?111"]


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

