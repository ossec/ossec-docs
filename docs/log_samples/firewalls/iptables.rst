Log Samples from iptables
-------------------------

Martian log enabled:
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Feb  1 17:45:05 gatlan kernel: martian source 90.20.131.158 from 192.168.0.2, on dev ppp0
  Feb  1 17:45:05 gatlan kernel: ll header: 45:48:00:28:c8:6a:40:00:72:06:a1:c0:c0:a8:00:02:5a:14:83:9e:12:36
  Feb  1 17:45:26 gatlan kernel: martian source 90.20.131.158 from 192.168.0.2, on dev ppp0
  Feb  1 17:45:26 gatlan kernel: ll header: 45:48:00:28:cc:f9:40:00:72:06:9d:31:c0:a8:00:02:5a:14:83:9e:12:36
  Feb  1 17:46:10 gatlan kernel: martian source 90.20.131.158 from 192.168.0.2, on dev ppp0
  Feb  1 17:46:10 gatlan kernel: ll header: 45:48:00:28:d6:f2:40:00:72:06:93:38:c0:a8:00:02:5a:14:83:9e:12:36


UDP warning (netfilter module):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  kernel: UDP: short packet: From 2.0.0.0:3800 37860/38 to 72.17.117.129:20969


TCP shrunk window (netfilter module):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Jan 24 20:01:36 Lab3 kernel: TCP: Peer 93.97.112.201:50524/6960 unexpectedly shrunk window 930362701:930364976 (repaired)


