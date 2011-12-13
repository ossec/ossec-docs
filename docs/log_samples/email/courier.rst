Courier Log samples
-------------------

Pop3 Login failed:
^^^^^^^^^^^^^^^^^^

.. code-block:: console

  May 30 00:01:02 server2 courierpop3login: LOGIN FAILED, ip=[::ffff:193.68.217.36]
  May 30 00:01:03 server2 courierpop3login: LOGIN FAILED, ip=[::ffff:193.68.217.36]
  May 30 00:01:02 server2 courierpop3login: LOGIN FAILED, ip=[::ffff:193.68.217.36]

  Dec 1 10:46:22 debian courierpop3login: LOGIN FAILED, ip=[::ffff:192.168.1.161]
  Dec 1 10:46:30 debian courierpop3login: Connection, ip=[::ffff:192.168.1.161]
  Dec 1 10:46:35 debian courierpop3login: LOGIN FAILED, ip=[::ffff:192.168.1.161]

  Nov 22 20:02:24 www courierpop3login: LOGIN FAILED, ip=[::ffff:192.168.0.188]
  Nov 22 20:02:26 www courierpop3login: LOGIN FAILED, ip=[::ffff:5.4.234.42]
  Nov 22 20:02:26 www courierpop3login: LOGOUT, ip=[::ffff:5.4.234.42]
  Nov 22 20:02:26 www courierpop3login: Connection, ip=[::ffff:5.4.234.42]
  Nov 22 20:02:30 www courierpop3login: LOGIN FAILED, ip=[::ffff:62.10.125.238]
  Nov 22 20:02:34 www courierpop3login: LOGIN FAILED, ip=[::ffff:5.4.234.42]
  Nov 22 20:02:34 www courierpop3login: LOGOUT, ip=[::ffff:5.4.234.42]


Pop3d-ssl Login failed:
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jan 3 02:07:37 web pop3d-ssl: Connection, ip=[::ffff:192.168.0.200]
  Jan 3 02:07:44 web pop3d-ssl: LOGIN FAILED, ip=[::ffff:192.168.0.200]



Imapd Login failed:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sep 21 00:40:57 server01 imaplogin: LOGIN FAILED, ip=[::ffff:127.0.0.1]
  Sep 21 00:41:17 server01 imaplogin: LOGIN FAILED, ip=[::ffff:127.0.0.1]
  Sep 21 00:42:21 server01 imaplogin: LOGIN FAILED, ip=[::ffff:127.0.0.1]
  Sep 21 00:42:21 server01 imaplogin: DISCONNECTED, ip=[::ffff:127.0.0.1], time=5
  Sep 21 00:42:28 server01 imaplogin: LOGIN FAILED, ip=[::ffff:127.0.0.1]
  Sep 21 00:44:23 server01 imaplogin: DISCONNECTED, ip=[::ffff:127.0.0.1], time=0
  Sep 21 00:48:58 server01 courierpop3login: LOGIN FAILED, ip=[::ffff:88.73.124.13]
  Sep 21 00:49:42 server01 imaplogin: LOGIN FAILED, ip=[::ffff:127.0.0.1]
  Sep 21 00:51:50 server01 courierpop3login: LOGIN FAILED, ip=[::ffff:88.73.124.13]
  Sep 21 00:53:42 server01 courierpop3login: LOGIN FAILED, ip=[::ffff:88.73.124.13]



Valid logins:
^^^^^^^^^^^^^

.. code-block:: console

  Jun 1 00:12:06 server1 courierpop3login: LOGIN, user=web10_mauricio, ip=[::ffff:192.168.0.100]
  Jun 1 00:12:06 server1 courierpop3login: LOGOUT, user=web10_mauricio, ip=[::ffff:192.168.0.100], top=0, retr=0, rcvd=24, sent=96, time=0
  Jun 1 00:21:40 server1 courierpop3login: Connection, ip=[::ffff:192.168.0.100]
  Jun 1 00:21:40 server1 courierpop3login: LOGIN, user=web10_mauricio, ip=[::ffff:192.168.0.100]
  Jun 1 00:21:40 server1 courierpop3login: LOGOUT, user=web10_mauricio, ip=[::ffff:192.168.0.100], top=0, retr=0, rcvd=24, sent=96, time=0
  Jun 1 00:30:15 server1 courierpop3login: Connection, ip=[::ffff:192.168.0.100]
  Jun 1 00:30:15 server1 courierpop3login: LOGIN, user=web10_mauricio, ip=[::ffff:192.168.0.100]
  Jun 1 00:30:15 server1 courierpop3login: LOGOUT, user=web10_mauricio, ip=[::ffff:192.168.0.100], top=0, retr=0, rcvd=24, sent=96, time=0
  Jun 1 00:31:40 server1 courierpop3login: Connection, ip=[::ffff:192.168.0.100]
  Jun 1 00:31:40 server1 courierpop3login: LOGIN, user=web10_mauricio, ip=[::ffff:192.168.0.100]
  Jun 1 00:31:40 server1 courierpop3login: LOGOUT, user=web10_mauricio, ip=[::ffff:192.168.0.100], top=0, retr=0, rcvd=24, sent=96, time=0


