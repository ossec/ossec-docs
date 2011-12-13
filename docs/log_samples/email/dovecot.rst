Dovecot log samples
-------------------

IMAP:
^^^^^

Login: 
^^^^^^

.. code-block:: console
  Oct 18 14:23:37 host dovecot: imap-login: Login: user=<uuuuu>, method=PLAIN, rip=y.y.y.y, lip=x.x.x.x, TLS


Error time change: 
^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Oct 19 05:55:18 host dovecot: imap-login: Time just moved backwards by 3 seconds. I'll sleep now until we're back in present. http://wiki.dovecot.org/TimeMovedBackwards



Logout/Connection close:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Oct 19 14:14:38 host dovecot: imap-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x, TLS handshake
  Oct 19 14:14:38 host dovecot: imap-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x, TLS
  Oct 19 14:14:49 host dovecot: imap-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x
  Oct 21 03:33:37 host dovecot: IMAP(uuuuu): Disconnected for inactivity
  Oct 21 01:20:28 host dovecot: IMAP(uuuuu): Connection closed


Error auth: 
^^^^^^^^^^^

.. code-block:: console
  Oct 19 14:16:51 host dovecot: imap-login: Aborted login (1 authentication attempts): user=<uuuuu>, method=PLAIN, rip=y.y.y.y, lip=x.x.x.x
  Oct 19 14:17:22 host dovecot: imap-login: Aborted login (0 authentication attempts): rip=y.y.y.y, lip=x.x.x.x, TLS
  Oct 19 14:16:53 host dovecot: imap-login: Aborted login (tried to use disabled plaintext authentication): method=PLAIN, rip=y.y.y.y, lip=x.x.x.x


Attacks: 
^^^^^^^^

.. code-block:: console
  Oct 19 14:18:15 host dovecot: imap-login: Disconnected: method=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..., rip=y.y.y.y, lip=y.y.y.y, TLS
  Oct 19 14:18:15 host dovecot: imap-login: Disconnected: method=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..., rip=y.y.y.y, lip=y.y.y.y



POP3:
^^^^^

Login: 
^^^^^^

.. code-block:: console
  Oct 18 17:54:03 host dovecot: pop3-login: Login: user=<uuuuu>, method=PLAIN, rip=y.y.y.y, lip=x.x.x.x, TLS



Logout/Connection close: 
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Oct 18 17:54:07 host dovecot: POP3(uuuuu): Disconnected: Logged out top=0/0, retr=1/10014, del=1/8, size=55676
  Oct 19 14:15:29 host dovecot: pop3-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x
  Oct 19 14:15:29 host dovecot: pop3-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x, TLS handshake
  Oct 19 14:15:29 host dovecot: pop3-login: Disconnected: rip=y.y.y.y, lip=x.x.x.x, TLS
  Oct 21 19:58:22 host dovecot: pop3-login: Disconnected: method=PLAIN, rip=y.y.y.y, lip=x.x.x.x, TLS



Error time change: 
^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Oct 19 05:55:18 host dovecot: pop3-login: Time just moved backwards by 3 seconds. I'll sleep now until we're back in present. http://wiki.dovecot.org/TimeMovedBackwards



Error auth: 
^^^^^^^^^^^

.. code-block:: console
  Oct 19 14:16:53 host dovecot: pop3-login: Aborted login (tried to use disabled plaintext authentication): rip=y.y.y.y, lip=x.x.x.x, TLS
  Oct 19 14:16:55 host dovecot: pop3-login: Aborted login (1 authentication attempts): user=<uuuuu>, method=PLAIN, rip=y.y.y.y, lip=x.x.x.x, TLS



AUTH:
^^^^^

Error time change: 
^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Oct 19 05:55:18 host dovecot: auth(default): Time just moved backwards by 2 seconds. I'll sleep now until we're back in present. http://wiki.dovecot.org/TimeMovedBackwards


Errors: 
^^^^^^^

.. code-block:: console
  Oct 19 14:37:40 host dovecot: auth(default): LDAP: ldap_result() failed: Can't contact LDAP server
  Oct 19 14:37:40 host dovecot: auth(default): io_loop_handle_remove: epoll_ctl(2, 9): Bad file descriptor
  Oct 19 14:37:40 host dovecot: auth(default): LDAP: Can't connect to server: ldap://127.0.0.1
  Oct 21 10:25:03 host dovecot: auth(default): ldap(uuuuu,y.y.y.y): ldap_search((&(objectClass=CourierMailAccount)(uid=uuuuu))) failed: Invalid DN syntax
  Oct 21 10:25:03 host dovecot: auth(default): ldap(uuuuu,y.y.y.y): ldap_search((&(objectClass=CourierMailAccount)(uid=uuuu))) failed: No such object



OTHERS:
^^^^^^^
.. code-block:: console
  Oct 19 14:33:55 host dovecot: Killed with signal 15
  Oct 19 14:33:55 host dovecot: Dovecot v1.0.10 starting up
  Oct 21 10:04:18 host dovecot: ssl-build-param: SSL parameters regeneration completed


