
.. _manual-out-syslog:

Sending alerts via syslog
=========================

Syslog output allows you to send the OSSEC alerts to one or more syslog servers
(granularly).

You can configure OSSEC with the syslog servers of your choice. In my example
here, I am sending everything to server 192.168.4.1 and only the alerts above
level 10 to 10.1.1.1:

.. code-block:: xml

    <syslog_output>
        <server>192.168.4.1</server>
    </syslog_output>

    <syslog_output>
        <level>10</level>
        <server>10.1.1.1</server>
    </syslog_output>


After that, run the following command and restart OSSEC:

.. code-block:: console 

    # /var/ossec/bin/ossec-control enable client-syslog
    # /var/ossec/bin/ossec-control start

You should see now ossec-csyslog starting:

.. code-block:: console 

    OSSEC HIDS v1.5.1 Stopped
    Starting OSSEC HIDS v1.5.1 (by Third Brigade, Inc.)
    Started ossec-csyslogd...
    ..

And on the logs:

.. code-block:: console 

    # tail -n 1000 /var/ossec/logs/ossec.log | grep csyslog
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Started (pid: 19412).
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Forwarding alerts via syslog to: ‘192.168.4.1:514′.
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Forwarding alerts via syslog to: ‘10.1.1.1:514′.

On the syslog server, this is what you should get (every log separated by level,
rule, location and the actual event that generated it):

.. code-block:: console
    
    Jul 25 12:17:41 enigma ossec: Alert Level: 3; Rule: 5715 - SSHD authentication success.; Location: (jul) 192.168.2.0->/var/log/messages;
    srcip: 192.168.2.190; user: root; Jul 25 13:26:24 slacker sshd[20440]: Accepted password for root from 192.168.2.190 port 49737 ssh2

