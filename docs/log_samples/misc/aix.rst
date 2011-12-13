Log Samples from AIX
--------------------

AIX SU:
^^^^^^^
.. code-block:: console

  Mar  2 15:14:36 WebServer1 su: BAD SU from 1.2.3.4 to root at /dev/pts/1



Examples AIX messages log:
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Mar  6 11:09:27 webserver1 librmad[12906]: librmad Tue Mar  6 11:09:27 2007 /project/rm410/build/rm410/src/rm/rmeif/lib/rmad.c Line: 371, rmad_send_message, HRMRM0017E Message formatting failed with a return code of -1.
  Mar  6 11:14:43 epopws1 xntpd[5676]: time reset (step) -0.199116 s


 
Examples AIX/IBM AccessManager request.log (weblog):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  1.2.3.4 - Unauth [04/Mar/2007:00:03:11 +0100] "HEAD / HTTP/1.0" 200 0
  2.3.4.5 - jMeter@is [04/Mar/2007:00:03:11 +0100] "GET /pkmslogout HTTP/1.1" 200 6691
  3.4.5.6 - Unauth [04/Mar/2007:00:03:11 +0100] "GET /cin HTTP/1.1" 200 12272



*Examples of AIX ipsec logs:
.. code-block:: console

  ipsec_logd: #:3 R:p  I:10.0.0.99 S:10.0.0.82 D:10.0.0.99     P:tcp/ack SP:50349 DP:22 R:l I:en0 F:n T:0 L:88
  ipsec_logd: #:1 R:p  O:10.0.0.99. S:10.0.0.99 D:10.0.0.25     P:udp SP:2063 DP:53 R:l I:en0 F:n T:0 L:81



Examples of AIX sshd logins:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Apr  3 04:46:53 aixhostname sshd[21174]: Accepted publickey for user1 from 2.3.4.5 port 59663 ssh2
  May 21 20:22:28 aixhostname sshd[21487]: Failed password for user2 from 2.3.4.5 port 1045 ssh2
  May 21 20:22:29 aixhostname sshd[21489]: Invalid user admin from 2.3.4.5
  Apr  6 08:11:12 <host> sshd[21900]: User <user> not allowed because not listed in AllowUsers
  Apr  6 08:12:54 <host> syslog: ssh: failed login attempt for <user> from <host>
  Apr  6 08:12:54 <host> sshd[6318]: Failed password for <host> from <host> port 59083 ssh2



AIX 5.3:
^^^^^^^^

.. code-block:: console

  Apr 24 10:40:38 aix03srv auth|security:info sshd[475526]: Login restricted for tesu: You entered an invalid login name or password.
  Apr 24 10:40:38 aix03srv auth|security:info sshd[475526]: Failed none for invalid user user1a from 127.0.0.1 port 58997 ssh2
  Apr 24 10:40:43 aix03srv auth|security:info sshd[475526]: Failed password for invalid user usa1 from 127.0.0.1 port 58997 ssh2
  Apr 24 10:40:43 aix03srv auth|security:info syslog: ssh: failed login attempt for UNKNOWN_USER from loopback
  Apr 12 15:19:47 lpar1 auth|security:info sshd[368754]: Failed password for root from 10.1.5.20 port 54747 ssh2
  Apr 12 15:19:47 lpar1 auth|security:info syslog: ssh: failed login attempt for root from csm01
  Apr 12 15:19:47 lpar1auth|security:info sshd[774360]: Failed password for root from 10.1.5.20 port 54748 ssh2
  Apr 12 15:19:47 lpar1 auth|security:info syslog: ssh: failed login attempt for root from csm01


  Jul 23 12:59:35 freescale auth.info sshd[1816]: User igotre password has expired (root forced)
  Jul 23 12:59:35 freescale  auth.info sshd[1816]: Accepted password for igotre from 10.1.20.9 port 36875 ssh2
  Jul 23 12:59:35 freescale auth.err sshd[1820]: error: setlogin failed: Function not implemented
  Jul 23 12:59:35 freescale auth.err sshd[1821]: error: open /dev/tty failed - could not set controlling tty: Permission denied
  Jul 23 12:59:44 freescale auth.info passwd[1821]: password for `igotre' changed by user `igotre' 

