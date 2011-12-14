Log Samples from Squid
----------------------


404 error (non-existent file):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  644 1.2.3.4 TCP_CLIENT_REFRESH_MISS/404 4456 GET http://www.ossec.net/x1 - DIRECT/2.3.4.5 text/html
  1292 1.2.3.4 TCP_CLIENT_REFRESH_MISS/404 4456 GET http://www.ossec.net/x2 - DIRECT/2.3.4.5 text/html

403 error (forbidden) -- Attempting to proxy SMTP over the web:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  5 59.59.106.40 TCP_DENIED/403 1382 CONNECT 202.43.200.11:25 - NONE/- text/html
  15 59.59.106.40 TCP_DENIED/403 1382 CONNECT 202.43.200.11:25 - NONE/- text/html
  0 59.59.106.40 TCP_DENIED/403 1380 CONNECT 203.84.195.1:25 - NONE/- text/html
  8 59.59.106.40 TCP_DENIED/403 1380 CONNECT 203.84.195.1:25 - NONE/- text/html



Squid syslog errors:
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  squid[10384]: sslReadServer: FD 16: read failure: (104) Connection reset by peer


Invalid HTTP headers:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  squid[248]: WARNING: suspicious CR characters in HTTP header {Location: http://aroundthesims.online.fr/errors/404.html^MErrorDocument 500 http://aroundthesims.online.fr/errors/500.html}

