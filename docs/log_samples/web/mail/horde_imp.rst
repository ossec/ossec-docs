Log Samples from Horde IMP
--------------------------

Login failed:
^^^^^^^^^^^^^

.. code-block:: console

  Mar 19 20:11:06 HORDE [error] [imp] FAILED LOGIN 1.2.3.4 to imap.lab.ossec.net:143[imap] as ccrazy [on line 287 of "/home/webmail/horde/imp/lib/IMP.php"]
  Mar 19 20:11:50 HORDE [error] [imp] FAILED LOGIN 192.168.20.50 to imap.lab.ossec.net:143[imap] as julia [on line 287 of "/home/webmail/horde/imp/lib/IMP.php"]


Login sucess:
^^^^^^^^^^^^^

.. code-block:: console

  Jan 30 09:19:58 HORDE [notice] [imp] Login success for lcid@lab.ossec.net [192.168.200.201] to {imap.lab.ossec.net:143} [on line 92 of "/home/webmail/horde/imp/redirect.php"]


Critical events:
^^^^^^^^^^^^^^^^

.. code-block:: console

  May 10 16:45:16 HORDE [emergency] [imp] DB Error: connect failed:  [nativecode=Lost connection to MySQL server during query] ** Array [on line 108 of "/home/webmail/horde/lib/Prefs/sql.php"]


Informational events:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Feb 10 03:57:59 HORDE [info] [imp] 1.2.3.4 Message sent to Sergio <xx@xx.com> from yy [on line 881 of "/home/webmail/horde/imp/compose.php"]
  Feb 10 03:59:15 HORDE [info] [imp] 1.2.3.4 Message sent to yy <aa@aa.com> from zz [on line 881 of "/home/webmail/horde/imp/compose.php"]

