Log Samples from Solaris 8/9
----------------------------

Solaris doesn't include the source server name in their Syslog message.  So you can't forward Solaris Syslog message directly to Ossec.



.. note:
  Samples from from Andre Lorbach.

The Problem: The problem exists in the way, the Syslog messages are formatted from Solaris 8/9. As an example, we take the following sample Syslog message:

.. code-block:: console

    Aug  2 11:49:23 su: [ID 366847 auth.info] 'su root' succeeded for root on /dev/console 

This message is missing the source, which has to be before the Syslogtag, as it is defined in RFC3164. So correctly, the Syslog would have to look like this:

.. code-block:: console

    Aug  2 11:49:23 mymaschine su: [ID 366847 auth.info] 'su root' succeeded for root on /dev/console  




In order to format the Syslog message to be compliant with RFC3164, you need to set-up Syslog-ng and forward the Syslog message to it.  Make sure you change the syslog receiving port of ossec or syslog-ng.


SU:
^^^

.. code-block:: console

  Dec 12 00:00:00 machinename su: [ID 366847 auth.info] 'su oracle' succeeded for root on /dev/???

  Dec 12 00:23:28 machinename su: [ID 366847 auth.info] 'su oracle' failed for root on /dev/???


SENDMAIL:
^^^^^^^^^

.. code-block:: console

  Dec 12 00:00:02 machinename sendmail[20512]: [ID 801593 mail.info] kBC502520512: from=root, size=301, class=0, nrcpts=1, msgid=<200612120500.kBC502520512@name.domain.com>, relay=root@localhost

  Dec 12 00:00:03 machinename sendmail[20514]: [ID 801593 mail.info] kBC502520512: to=root, ctladdr=root (0/1), delay=00:00:01, xdelay=00:00:01, mailer=local, pri=120301, relay=local, dsn=2.0.0, stat=Sent


SSHD:
^^^^^

.. code-block:: console

  Dec 12 00:10:55 machinename sshd[21698]: [ID 800047 auth.info] User blablabla not allowed because account is locked

  Dec 12 00:10:55 machinename sshd[21698]: [ID 800047 auth.info] Failed none for invalid user blablabla from 192.168.0.1 port 40410 ssh2

  Dec 12 00:10:55 machinename sshd[21698]: [ID 800047 auth.info] Failed password for invalid user blablabla from 192.168.0.1 port 40410 ssh2

  Dec 12 09:33:48 machinename sshd[18195]: [ID 800047 auth.info] Failed keyboard-interactive for blablabla from 192.168.0.1 port 1530 ssh2

  Dec 12 09:33:50 machinename sshd[18195]: [ID 800047 auth.info] Accepted password for blablabla from 192.168.0.1 port 1530 ssh2

  Dec 12 23:59:54 machinename sshd[24191]: [ID 800047 auth.info] User blablabla not allowed because account is locked

  Dec 12 09:33:25 machinename sshd[18094]: [ID 800047 auth.info] User blablabla password has expired (root forced)

  Dec 12 01:30:04 machinename sshd[11819]: [ID 800047 auth.info] Accepted publickey for blablabla from 192.168.0.1 port 4527 ssh2

  Dec 12 01:30:04 machinename sshd[11821]: [ID 800047 auth.info] subsystem request for sftp

  Dec 12 01:30:06 machinename sshd[15907]: [ID 800047 auth.info] Postponed publickey for blablabla from 192.168.0.1 port 4528 ssh2

  Dec 12 08:00:03 machinename sshd[3399]: [ID 800047 auth.info] Authentication tried for root with correct key but not from a permitted host (host=hostname, ip=10.11.10.8).


FTP:
^^^^

.. code-block:: console

  Dec 12 01:09:29 machinename inetd[301]: [ID 317013 daemon.notice] ftp[8378] from 192.168.0.1 25143

  Dec 12 01:22:23 machinename inetd[301]: [ID 317013 daemon.notice] ftp[10504] from 192.168.0.1 6719


IN.FTPD:
^^^^^^^^

.. code-block:: console

  Dec 12 01:09:29 machinename in.ftpd[8378]: [ID 373804 daemon.info] connection from name.domain.com at Tue Dec 12 01:09:29 2006

  Dec 12 01:22:24 machinename in.ftpd[10504]: [ID 373804 daemon.info] connection from name.domain.com at Tue Dec 12 01:22:24 2006


NAMED-XFER:
^^^^^^^^^^^

.. code-block:: console

  Dec 12 02:23:45 machinename named-xfer[9924]: [ID 140103 daemon.info] send AXFR query 0 to 192.168.0.1

  Dec 12 03:13:10 machinename named-xfer[368]: [ID 140103 daemon.info] send AXFR query 0 to 192.168.0.1


NAMED:
^^^^^^

.. code-block:: console

  Dec 12 03:13:10 machinename named[311]: [ID 295310 local2.warning] default: warning: owner name "name.domain.com" IN (secondary) is invalid - proceeding anyway


LIMDAEMON:
^^^^^^^^^^

.. code-block:: console

  Dec 12 07:27:49 machinename limdaemon: [ID 701944 user.notice] login by blablabla (pid=24835,cost=1)

  Dec 12 07:27:52 machinename limdaemon: [ID 709948 user.notice] logout by blablabla (pid=24835)


PROFTPD:
^^^^^^^^

.. code-block:: console

  Dec 12 07:40:32 machinename proftpd[16601]: [ID 567783 daemon.info] qcdevasq (name.domain.com[192.168.0.1]) - FTP session opened.

  Dec 12 07:40:32 machinename proftpd[16601]: [ID 567783 auth.notice] qcdevasq (name.domain.com[192.168.0.1]) - USER blablabla: Login successful.

  Dec 12 07:40:32 machinename proftpd[16601]: [ID 567783 daemon.info] qcdevasq (name.domain.com[192.168.0.1]) - FTP session closed.

  Dec 12 09:33:46 machinename proftpd[20958]: [ID 567783 daemon.info] qcmtlasi (name.domain.com[192.168.0.1]) - FTP session closed.


FTPD:
^^^^^

.. code-block:: console

  Dec 12 07:41:11 machinename ftpd[10209]: [ID 210975 daemon.info] ANONYMOUS FTP LOGIN FROM name.domain.com [192.168.0.1], blablabla


LOGIN:
^^^^^^

.. code-block:: console

  Dec 12 08:43:50 machinename login: [ID 507249 auth.notice] Login failure on /dev/pts/7 from name.domain.com, blablabla


BSM:
^^^^

Some information about BSM:

http://seclab.cs.ucdavis.edu/projects/misuse/prototypes/bsm.html
http://abelew.web.wesleyan.edu/bsmaudit1.html

.. code-block:: console

  Nov 21 15:12:56 unknown audit: [ID 905220 audit.notice] system booted text booting kernel
  Nov 21 15:16:22 unknown audit: [ID 984917 audit.notice] login - telnet failed session 2740580090 by root as root:root from 1.254.168.192
  Nov 21 15:16:34 unknown audit: [ID 120101 audit.notice] login - telnet failed session 1843523234 by -1 as -1:-1 from 1.254.168.192
  Nov 21 15:37:24 unknown audit: [ID 338777 audit.notice] login - telnet failed session 3312149268 by root as root:root from 1.254.168.192
  Nov 21 15:43:26 unknown audit: [ID 905220 audit.notice] system booted text booting kernel
  Nov 21 15:44:11 unknown audit: [ID 216919 audit.notice] login - local ok session 627 by root as root:root from pc1305a.etri.re.kr text 
  Nov 21 15:45:14 unknown audit: [ID 866727 audit.notice] su ok session 3668504681 by kanthi as root:other from 1.254.168.192 text success for user root
  Nov 21 15:49:34 unknown audit: [ID 702844 audit.notice] su ok session 2714481116 by kanthi as root:other from 1.254.168.192 text success for user root
  Nov 21 15:50:35 unknown audit: [ID 816908 audit.notice] ftp access failed session 858 by root as root:root from 1.254.168.192 text excluded user
  Nov 21 15:50:37 unknown audit: [ID 887505 audit.notice] ftp access failed session 858 by root as root:root from 1.254.168.192 text misc failure
  Nov 21 16:04:32 unknown audit: [ID 905220 audit.notice] system booted text booting kernel


