Zeus web server
---------------

Failed logins:
^^^^^^^^^^^^^^

.. code-block:: console

  [26/Jun/2006:05:02:57 +0100] WARN:admin:Authentication failure, url=/index.cgi, host=xx.yy.com, user=admin
  [03/Aug/2006:18:43:11 +0100] WARN:admin:Authentication failure, url=/index.cgi, host=1.2.3.4, user=admin



Informational:
^^^^^^^^^^^^^^

.. code-block:: console
  [09/Dec/2006:05:04:15 +0000] INFO:https://1.2.3.4:9091
  [09/Dec/2006:05:04:15 +0000] INFO:Child started - pid 5800
  [09/Dec/2006:05:04:15 +0000] INFO:Zeus Admin Server running
  [09/Dec/2006:05:08:39 +0000] INFO:Server shutdown requested
  [10/Dec/2006:16:59:26 +0000] INFO:Zeus Admin Server started
  [10/Dec/2006:16:59:26 +0000] INFO:Version 4.3r3, Build date: Jun 16 2006 09:20:11



Fatal:
^^^^^^

.. code-block:: console
  [11/Mar/2007:00:26:18 +0000] FATAL:Zeus Admin Server already running (PID: 13709)
  [11/Mar/2007:00:26:52 +0000] FATAL:Zeus Admin Server already running (PID: 26890)
  [14/Mar/2007:14:10:01 +0000] SERIOUS:Node 1.2.3.3 (1.2.3.3:80) has failed - A monitor has detected a failure
  [14/Mar/2007:14:10:01 +0000] SERIOUS:Pool 'HTTP' has no back-end nodes responding
  [14/Mar/2007:21:37:12 +0000] SERIOUS:Pool 'ws00' has no back-end nodes responding


