Log Samples from vpopmail
-------------------------

Failed logins:
^^^^^^^^^^^^^^

.. code-block:: console

  Sep 14 07:21:42 iron vpopmail[939]: vchkpw-pop3: password fail user1@xxxx.com:192.168.2.1
  Sep 14 07:21:42 iron vpopmail[937]: vchkpw-pop3: password fail user2@xxxx.com:192.168.2.1
  Sep 14 07:21:42 iron vpopmail[935]: vchkpw-pop3: password fail user3@xxxx.com:192.168.2.1
  Jun 9 08:56:30 www vpopmail[65827]: vchkpw-smtp: password fail (pass: '<65825.1118321790@mail.xxx.com>') myuserid@xxx.com:208.210.222.68


Invalid user:
^^^^^^^^^^^^^

.. code-block:: console

  vpopmail[2100]: vchkpw-pop3: vpopmail user not found abc@xxx.com:x.x.x.x
  vpopmail[65851]: vchkpw-pop3: vpopmail user not found myuserid@:208.210.222.68


Full samples:
^^^^^^^^^^^^^

.. code-block:: console
  Jun 9 08:56:03 www vpopmail[65826]: vchkpw-pop3: vpopmail user not found postmaster@:208.210.222.68
  Jun 9 08:56:30 www vpopmail[65827]: vchkpw-smtp: password fail (pass: '<65825.1118321790@mail.xxx.com>') myuserid@xxx.com:208.210.222.68
  Jun 9 09:04:16 www vpopmail[65851]: vchkpw-pop3: vpopmail user not found myuserid@:208.210.222.68
  Jun 9 09:04:23 www vpopmail[65853]: vchkpw-pop3: vpopmail user not found myuserid@:208.210.222.68
  Jun 9 09:05:00 www vpopmail[65855]: vchkpw-smtp: password fail (pass: '<65854.1118322299@mail.xxx.com>') myuserid@xxx.com:208.210.222.68
  Jun 9 09:14:41 www vpopmail[65880]: vchkpw-pop3: vpopmail user not found myuserid@:208.210.222.6
  Feb 24 06:48:03 circle vpopmail[12039]: vchkpw-pop3: password fail [EMAIL PROTECTED]:67.109.191.46
  Feb 24 06:49:03 circle vpopmail[12043]: vchkpw-pop3: password fail [EMAIL PROTECTED]:67.109.191.46
  Feb 24 06:50:03 circle vpopmail[12099]: vchkpw-pop3: password fail [EMAIL PROTECTED]:67.109.191.46
  Feb 24 08:13:31 circle vpopmail[13042]: vchkpw-pop3: password fail [EMAIL PROTECTED]:70.104.21.208
  Feb 24 08:13:32 circle vpopmail[13046]: vchkpw-pop3: password fail [EMAIL PROTECTED]:70.104.21.208
  May 24 11:45:03 mail01 vpopmail[40833]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 11:50:03 mail01 vpopmail[41401]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 11:55:04 mail01 vpopmail[42117]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 12:00:04 mail01 vpopmail[42735]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 12:50:06 mail01 vpopmail[51623]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 12:55:07 mail01 vpopmail[52208]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 13:00:06 mail01 vpopmail[52799]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 13:20:16 mail01 vpopmail[55953]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22
  May 24 13:48:23 mail01 vpopmail[13650]: vchkpw-pop3: vpopmail user not found dlb@example.net:67.92.111.22


Brute Force Attack:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Aug 12 11:52:52 mail vpopmail[4162]: vchkpw-pop3: vpopmail user not found support@:69.3.64.3
  Aug 12 11:52:52 mail vpopmail[4171]: vchkpw-pop3: vpopmail user not found info@:69.3.64.3
  Aug 12 11:52:53 mail vpopmail[4187]: vchkpw-pop3: vpopmail user not found help@:69.3.64.3
  Aug 12 11:52:53 mail vpopmail[4191]: vchkpw-pop3: vpopmail user not found spam@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4198]: vchkpw-pop3: vpopmail user not found aaron@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4203]: vchkpw-pop3: vpopmail user not found abby@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4208]: vchkpw-pop3: vpopmail user not found abigail@:69.3.64.3
  Aug 12 11:52:55 mail vpopmail[4228]: vchkpw-pop3: vpopmail user not found abraham@:69.3.64.3
  Aug 12 11:52:55 mail vpopmail[4241]: vchkpw-pop3: vpopmail user not found abuse@:69.3.64.3
  Aug 12 11:52:56 mail vpopmail[4258]: vchkpw-pop3: vpopmail user not found account@:69.3.64.3
  Aug 12 11:52:57 mail vpopmail[4267]: vchkpw-pop3: vpopmail user not found support@:69.3.64.3
  Aug 12 11:52:58 mail vpopmail[4289]: vchkpw-pop3: vpopmail user not found adm@:69.3.64.3


Log samples from vpopmail and qmailtoaster 

In qmailtoaster vpopmail can be use for: pop3, pop3s, imap, imaps, smtp, submission and webmail.
Therefore each record can include respectively:
* vchkpw-pop3:
* vchkpw-pop3s:
* vchkpw-imap:
* vchkpw-imaps:
* vchkpw-smtp:
* vchkpw-submission:
* vchkpw-webmail:


Succesfull login:
^^^^^^^^^^^^^^^^^

.. code-block:: console
  Jul  7 11:23:52 srv vpopmail[20057]: vchkpw-pop3: (PLAIN) login success user@my_domain:1.2.3.4
  Jul  7 12:57:06 srv vpopmail[21466]: vchkpw-pop3s: (PLAIN) login success user@my_domain:1.2.3.4
  Jul  5 07:45:29 srv vpopmail[31411]: vchkpw-imaps: (PLAIN) login success user@my_domain:1.2.3.4
  Jul  6 10:21:52 srv vpopmail[18917: vchkpw-smtp: (CRAM-MD5) login success user@my_domain:1.2.3.4
  Jul  7 11:08:51 srv vpopmail[19743]: vchkpw-submission: (CRAM-MD5) login success user@my_domain:1.2.3.4
  Jul  7 11:14:22 srv vpopmail[19938]: vchkpw-webmail: (PLAIN) login success user@my_domain:127.0.0.1



Bad password:
^^^^^^^^^^^^^

.. code-block:: console
  Jul  7 07:10:18 srv vpopmail[4800]: vchkpw-pop3: password fail (pass: 'test') user@my_domain:1.2.3.4
  Jul  7 12:37:11 srv vpopmail[21183]: vchkpw-pop3s: password fail (pass: 'test1') user1@my_domain:1.2.3.4
  Jul  6 10:22:55 srv vpopmail[18934]: vchkpw-imap: password fail (pass: 'aaaa') user@my_domain:192.168.1.19
  Jul  9 15:13:08 srv vpopmail[16542]: vchkpw-webmail: password fail (pass: 'test') user@my_domain:127.0.0.1


or if no password given:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Jul  5 16:02:13 srv vpopmail[4160]: vchkpw-pop3: null password given oneone1:121.243.18.134
  Jul  9 10:19:58 srv vpopmail[5676]: vchkpw-webmail: null password given user@my_domain:127.0.0.1



Invalid user:
^^^^^^^^^^^^^

.. code-block:: console
  Jun 22 16:30:50 srv vpopmail[8581]: vchkpw-smtp: vpopmail user not found webmaster@:58.62.86.10
  Jul  5 15:59:00 srv vpopmail[3840]: vchkpw-pop3: vpopmail user not found done@:121.243.18.134
  Jul 12 16:19:31 srv vpopmail[25240]: vchkpw-webmail: vpopmail user not found a@:127.0.0.1


