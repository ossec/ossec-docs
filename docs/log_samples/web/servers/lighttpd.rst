Log Samples from lighttpd
-------------------------

Simple GET:
^^^^^^^^^^^
.. code-block:: console

  86.75.32.44 www.mysite.com - [20/Jun/2010:09:35:41 +0200] "GET /robots.txt HTTP/1.1" 404 345 "-" "Googlebot-Image/1.0"



DFind scan probe:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  166.71.12.34 - - [20/Jun/2010:09:59:48 +0200] "GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1" 400 349 "-" "-"



mod_proxy_backend_fastcgi:
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2010-01-03 17:49:20 (trace) (mod_proxy_backend_fastcgi.c:650) (stderr from unix:/tmp/php-fastcgi.sock for /base/base_graph_display.php) /localwww/base/base/base_graph_display.php
  2010-01-03 17:49:22 (trace) (mod_proxy_backend_fastcgi.c:650) (stderr from unix:/tmp/php-fastcgi.sock for /base/base_graph_display.php) /localwww/base//base/base_graph_display.php
  2010-06-19 02:54:36 (trace) (mod_proxy_backend_fastcgi.c:650) (stderr from unix:/tmp/php-fastcgi.sock for /wp-cron.php) Invalid document end at line 2, column 1



http_auth.c:
^^^^^^^^^^^^

.. code-block:: console

  2010-01-03 17:48:25 (http_auth.c:922) password doesn't match for / webmonitor



mode_evasive connection flood attempt:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  2010-04-22 07:37:43 (mod_evasive.c:174) 82.194.122.1 turned away. Too many connections.



request.c:
^^^^^^^^^^

.. code-block:: console

  2010-06-20 09:50:14: (request.c.1141) POST-request, but content-length missing -> 411
  2010-04-06 09:37:58 (trace) (request.c:448) Host header is duplicate (Status: 400)
  2010-03-31 00:37:31 (trace) (request.c:440) Host header is invalid (Status: 400), was [inet_ntoa error]


server.c:
^^^^^^^^^

.. code-block:: console

  2010-06-20 06:25:04 (trace) (server.c:813) [note] graceful shutdown started by UID=0, PID=32003
  2010-06-20 06:25:05 (trace) (server.c:1778) server stopped by UID=0, PID=32003
  2010-10-13 15:03:57: (server.c.961) WARNING: unknown config-key: proxy-core.balancer (ignored)

log.c:
^^^^^^

.. code-block:: console

  2010-01-03 17:47:10 (trace) (log.c:166) server started


connections.c:
^^^^^^^^^^^^^^

.. code-block:: console

  2010-06-20 07:41:53 (error) (connections.c:1180) Warning: Either the error-handler returned status 404 or the error-handler itself was not found: /www/www.myhost.de/index.html
  2010-06-20 07:41:53 (error) (connections.c:1181) returning the original status: 404
  2010-06-20 09:35:41 (error) (connections.c:1182) If this is a rails app: check your production.log


http_req.c:
^^^^^^^^^^^

.. code-block:: console

  2010-06-20 10:15:07 (trace) (http_req.c:283) parsing failed at token ( [1]), header: ^E^A
  2010-06-18 13:57:59 (trace) (http_req.c:283) parsing failed at token (Accept [1]), header: GET  HTTP/1.1
  Accept: */*
  Accept-Language: en-us
  Accept-Encoding: gzip, deflate
  User-Agent: Toata dragostea mea pentru diavola
  Host: 88.198.52.246
  Connection: Close
  2010-05-09 10:52:29 (trace) (http_req.c:283) parsing failed at token (Host [1]), header: GET  HTTP/1.1
  Host: www.myhost.com
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
  Via: 1.1 192.168.133.200
  Connection: Keep-Alive



