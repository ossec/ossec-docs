
Log Samples from Pam
--------------------

Logs from PAM_Unix can be in different formats depending on the operating system. It can
cause a lot of trouble when parsing it. 

The available formats are:
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  process_name(pam_unix)[pid]:
  process_name[pid]: (pam_unix)
  process_name: pam_unix(process_name): 



Login sucessful:
^^^^^^^^^^^^^^^^

.. code-block:: console

  Jul  7 10:51:24 srbarriga su(pam_unix)[14592]: session opened for user test2 by (uid=10101)
  Jul  7 10:52:14 srbarriga sshd(pam_unix)[17365]: session opened for user test by (uid=508)
  Nov 17 21:41:22 localhost su[8060]: (pam_unix) session opened for user root by (uid=0)
  Nov 11 22:46:29 localhost vsftpd: pam_unix(vsftpd:auth): authentication failure; logname= uid=0 euid=0 tty= ruser= rhost=1.2.3.4


Session closed:
^^^^^^^^^^^^^^^

.. code-block:: console

  Jul  7 10:53:07 srbarriga su(pam_unix)[14592]: session closed for user test



Login failed:
^^^^^^^^^^^^^

.. code-block:: console

  Jul  7 10:55:56 srbarriga sshd(pam_unix)[16660]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=192.168.20.111  user=root
  Jul  7 10:59:12 srbarriga vsftpd(pam_unix)[25073]: authentication failure; logname= uid=0 euid=0 tty= ruser= rhost=192.168.20.111


Invalid user login attempt:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jul  7 10:59:49 srbarriga vsftpd(pam_unix)[25073]: check pass; user unknown

