WIPFW
-----

Here is a log sample from the WIPFW firewall for Windows. More information about WIPFW can be found at http://wipfw.sourceforge.net. If you're using Windows, I can't recommend WIPFW highly enough. It is Open Source and is the most highly configurable firewall product I've found for Windows to date. (Understand WIPFW is a straight network firewall; it does no application access control or anything along those lines. If that's what you need, you'll need to use something else like [[Zone_Alarm|Zone Alarm]].)

.. code-block:: console

  0000000060 2006.12.07 08:49:58.002  ipfw: 1000 Deny TCP 75.126.23.220:80 192.168.47.1:9839 in via eth2
  0000000061 2006.12.07 08:50:13.095  ipfw: 1000 Deny TCP 66.135.40.79:80 192.168.47.1:9866 in via eth2
  0000000062 2006.12.07 08:50:32.025  ipfw: 1000 Deny TCP 66.135.40.79:80 192.168.47.1:9904 in via eth2
  0000000063 2006.12.07 08:50:34.018  ipfw: 1000 Deny TCP 66.135.40.79:80 192.168.47.1:9904 in via eth2
  0000000064 2006.12.07 08:51:54.032  ipfw: 1000 Deny TCP 68.142.200.232:80 192.168.47.1:9921 in via eth2
  0000000065 2006.12.07 08:51:54.032  ipfw: 1000 Deny TCP 68.142.200.232:80 192.168.47.1:9922 in via eth2
  0000000066 2006.12.07 08:51:54.032  ipfw: 1000 Deny TCP 68.142.200.232:80 192.168.47.1:9920 in via eth2
  0000000067 2006.12.07 08:52:37.200  ipfw: 1000 Deny TCP 68.142.200.232:80 192.168.47.1:9939 in via eth2
  0000000068 2006.12.07 08:52:44.060  ipfw: 1000 Deny TCP 68.142.200.232:80 192.168.47.1:9955 in via eth2
  0000000069 2006.12.07 08:58:04.027  ipfw: 1000 Deny TCP 8.10.179.132:80 192.168.47.1:9984 in via eth2
  0000000070 2006.12.07 08:58:43.018  ipfw: 1000 Deny TCP 66.135.40.79:80 192.168.47.1:9986 in via eth2


WIPFW puts these logs in your C:\Windows\security\logs directory. The log format is fairly simple. The first number is the log entry, followed by the date and the time. After "ipfw:" is the firewall rule number (1000 in the above example), followed by the action and the protocol. The rest is self-explanatory.

