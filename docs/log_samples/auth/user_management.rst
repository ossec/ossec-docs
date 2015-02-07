Messages from useradd, userdel, etc
-----------------------------------

Suse Linux useradd:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sep 15 17:11:27 myserver useradd[13542]: new account added - account=fred, uid=1016, gid=100, home=/home/fred, shell=/bin/bash, by=0
  Sep 15 17:11:27 myserver useradd[13542]: account added to group - account=fred, group=video, gid=33, by=0
  Sep 15 17:11:27 myserver useradd[13542]: account added to group - account=fred, group=dialout, gid=16, by=0
  Sep 15 17:11:27 myserver useradd[13542]: home directory created - account=fred, uid=1016, home=/home/fred, by=0
  Sep 15 17:11:27 myserver useradd[13542]: running USERADD_CMD command - script=/usr/sbin/useradd.local, account=fred, uid=1016, gid=100, home=/home/fred, by=0


Suse Linux userdel:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sep 15 16:37:13 myserver userdel[12584]: running USERDEL_PRECMD command - script=/usr/sbin/userdel-pre.local, account=mary, uid=1014, gid=100, home=/home/mary, by=0
  Sep 15 16:37:13 myserver crontab[12586]: (root) DELETE (mary)
  Sep 15 16:37:13 myserver userdel[12584]: account removed from group - account=mary, group=video, gid=33, by=0
  Sep 15 16:37:13 myserver userdel[12584]: account removed from group - account=mary, group=dialout, gid=16, by=0
  Sep 15 16:37:13 myserver userdel[12584]: account deleted - account=mary, uid=1014, by=0
  Sep 15 16:37:13 myserver userdel[12584]: running USERDEL_POSTCMD command - script=/usr/sbin/userdel-post.local, account=mary, uid=1014, gid=100, home=/home/mary, by=0


useradd&passwd fail:
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  May 28 16:04:10 server2 useradd[30245]: failed adding user 'avahi', data deleted
  May 28 16:04:10 server2 passwd[30246]: password for 'avahi' changed by 'root'
  May 28 16:04:12 server2 passwd[30263]: password for 'hal' changed by 'root'
  May 28 16:07:10 server2 useradd[30523]: failed adding user 'mysql', data deleted
  May 28 16:11:48 server2 passwd[32532]: password for 'gdm' changed by 'root'
  May 28 16:16:07 server2 useradd[633]: failed adding user 'privoxy', data deleted



