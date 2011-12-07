
Su log samples
--------------

OpenBSD:
^^^^^^^^

.. code-block:: console

  Feb 12 19:11:27 enigma su: dcid to root on /dev/ttyp0
  Feb 12 19:11:41 enigma su: BAD SU dcid to root on /dev/ttyp0
  Feb 12 19:11:48 enigma su: dcid to root on /dev/ttyp0



Solaris 10:
^^^^^^^^^^^

.. code-block:: console

  SU 07/23 00:57 + ??? root-root
  SU 07/23 01:24 + pts/4 lcid-root
  SU 07/23 19:12 + pts/2 lcid-root
  SU 07/23 19:30 + pts/3 lcid-root
  SU 07/23 19:32 - pts/3 lcid-root
  SU 07/23 19:32 + pts/3 lcid-root
  SU 02/12 19:27 + pts/2 lcid-root
  SU 02/12 19:16 + pts/2 lcid-root



Slackware:
^^^^^^^^^^

.. code-block:: console

  Jul  5 22:13:15 lili su[2614]: - pts/6 dcid-root
  Jul  5 22:13:36 lili su[2711]: + pts/6 dcid-root



Ubuntu:
^^^^^^^

.. code-block:: console
  Feb 12 15:47:40 localhost su[29149]: - pts/5 dcid:root
  Feb 12 15:47:45 localhost su[29150]: + pts/5 dcid:root
  Feb 12 15:11:41 enigma su[2936]: failed: ttyq4 changing from xx to root



