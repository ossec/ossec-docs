Why is OSSEC not seeing my iptables messages?
---------------------------------------------

* By `Daniel B. Cid <http://www.dcid.me/>`_

The most common reason why ossec would not see your `iptables <http://www.iptables.org/>`_ logs is
because you didn't configure it properly to log. By default iptables will ``NOT log anything``. 

There is some `good <http://iptables-tutorial.frozentux.net/iptables-tutorial.html>`_ `documents <http://www.iptables.org/documentation/index.html>`_ online on how to configure iptables, but for ossec to understand 
them, you need to set the ``log-prefix`` option in addition to the ``log`` action.


For accept rules, the following action (with prefix) should be set:
.. code-block:: console

  -j LOG --log-prefix="ACCEPT "


They will generate the following log (or similar):

.. code-block:: console

  Jan 11 20:44:49 hostname kernel: [89463.101343] ACCEPT IN=lo OUT= MAC=00:00:00:00:00:00:00:00:00:00:00:00:08:00 SRC=127.0.0.1 DST=127.0.0.1 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=33772 DF PROTO=TCP SPT=43961 DPT=81 WINDOW=32767 RES=0x00 SYN URGP=0



For deny rules, the following action should be set:

.. code-block:: console

  -j LOG --log-prefix="DROP "


They will generate the following log (or similar):

.. code-block:: console

Jan 11 20:44:49 xxx kernel: [89463.101343] DROP IN=lo OUT= MAC=00:00:00:00:00:00:00:00:00:00:00:00:08:00 SRC=127.0.0.1 DST=127.0.0.1 LEN=60 TOS=0x10 PREC=0x00 TTL=64 ID=33772 DF PROTO=TCP SPT=43961 DPT=81 WINDOW=32767 RES=0x00 SYN URGP=0


Note that ossec will based its action based on the "DROP" or ALLOW that you configured.
For more information about iptables log, take a look `here <http://logi.cc/linux/netfilter-log-format.php3>`_ .

