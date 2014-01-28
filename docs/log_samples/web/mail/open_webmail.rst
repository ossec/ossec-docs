Log samples from OpenWebmail
----------------------------

Login sucessuful:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sun May  8 09:53:22 2005 - [11719] (1.2.3.4) xx - login - xx*yy.zz.com-session-0.518807460359437 - active=0,0,0
  Sun May  8 13:06:05 2005 - [22905] (1.2.3.4) yy - login - zz*www.bb.cc-session-0.518807460359437 - active=0,0,0


Logout:
^^^^^^^

.. code-block:: console

  Sat May  7 07:37:06 2005 - [15347] (1.2.3.4) lcid - logout - lcid*www.ossec.net-session-0.685629963447479
  Sat May  7 15:26:11 2005 - [7082] (1.2.3.4) l.cid - logout - l.cid*www.ossec.net-session-0.782612791556073


Invalid access:
^^^^^^^^^^^^^^^

.. code-block:: console

  Mon Jun 28 13:28:02 2004 - [1087] (1.2.3.4) llc - session error - request doesn't have proper cookie, access denied!


Invalid user:
^^^^^^^^^^^^^

.. code-block:: console

  Fri May  6 13:37:27 2005 - [8564] (1.2.3.4) testu - userinfo error - auth_unix.pl, ret -4, User testu doesn't exist


Samples:
^^^^^^^^

.. code-block:: console

  Thu Apr 22 09:34:48 2004 - [15900] (81.168.75.13) sehh - login - sehh*altered.com-session-0.319089010198699 - active=0,0,0
  Fri Apr 23 02:51:26 2004 - [21049] (81.168.75.13) sehh - filter message - filter 1 msgs from INBOX to mail-trash
  Tue Jun 27 08:59:01 2006 - [7540] (127.0.0.1) spamd@www.mingdaw.com - userinfo error - auth_unix.pl, ret -4, User spamd@www.mingdaw.com doesn't exist
  Tue Jun 27 08:59:01 2006 - [7540] (127.0.0.1) sshd@www.mingdaw.com - userinfo error - auth_unix.pl, ret -4, User sshd@www.mingdaw.com doesn't exist
  Tue Jun 27 08:59:01 2006 - [7540] (127.0.0.1) toor@www.mingdaw.com - userinfo error - auth_unix.pl, ret -4, User toor@www.mingdaw.com doesn't exist 


