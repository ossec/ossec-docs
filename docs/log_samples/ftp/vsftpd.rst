Log Samples from vsftpd
-----------------------

If the system is using pam, authentication events from vsftp may also be logged in the
[[pam|pam  format]]. <br />The following are from the vsftpd.log file.


Connection attempt:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Mon Jul 10 15:51:17 2006 [pid 26152] CONNECT: Client "192.168.2.10"

Failed login:
^^^^^^^^^^^^^

.. code-block:: console

  Mon Aug 21 14:33:24 2006 [pid 20175] [dcid] FAIL LOGIN: Client "127.0.0.1"

Login OK:
^^^^^^^^^

.. code-block:: console

  Mon Aug 21 14:37:23 2006 [pid 20293] [dcid] OK LOGIN: Client "127.0.0.1"

Anonymous login:
^^^^^^^^^^^^^^^^

.. code-block:: console

  Mon Aug 21 14:32:06 2006 [pid 20127] [ftp] OK LOGIN: Client "127.0.0.1", anon password "lala@"

File upload:
^^^^^^^^^^^^

.. code-block:: console

  Sun Aug 27 16:28:20 2006 [pid 13962] [xx] OK UPLOAD: Client "1.2.3.4", "/a.php", 8338 bytes, 18.77Kbyte/sec


