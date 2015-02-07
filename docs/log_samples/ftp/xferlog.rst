Log Samples from xferlog (by default at /var/log/xferlog)
---------------------------------------------------------

The xferlog file contains logging information from the FTP
server daemon, ftpd.  This file  usually  is  found  at
``/var/log/xferlog``, but can be anywhere else.


Each server entry is composed of a  single  line
of  the following form, with all fields being separated by
spaces.


.. code-block:: console

  current-time   transfer-time   remote-host    file-size   filename    transfer-type   special-action-flag   direction  access-mode    username    ser\xadvice-name    authentication-method  authenticated-user-id   completion-status 


Samples:
^^^^^^^^ 

.. code-block:: console

  Thu Sep  2 09:52:00 2004 50 192.168.20.10 896242 /home/test/file1.tgz b _ o r suporte ftp 0 * c
  Thu Sep  2 09:57:16 2004 289 192.168.20.10 8045867 /home/test2.tgz b _ o r suporte ftp 0 * c


