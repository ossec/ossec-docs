
.. _manual-out-syslog:

Sending alerts via syslog
=========================

Syslog output allows an OSSEC manager to send the OSSEC alerts to one or more syslog servers.

Configuration options
---------------------

These configurations options require a server or local installation.

.. include:: ../../syntax/ossec_config.syslog_output.trst 

Enable Syslog output in the configuration
-------------------------------------------

OSSEC can be configured to send the alerts via syslog to the servers of your choice. 
In this example all alerts are sent to 192.168.4.1, but only alerts of level 10 and 
above are sent to 10.1.1.1:

.. code-block:: xml

    <syslog_output>
        <server>192.168.4.1</server>
    </syslog_output>

    <syslog_output>
        <level>10</level>
        <server>10.1.1.1</server>
    </syslog_output>


After this change is made, the client-syslog process should be enabled:

.. code-block:: console 

    # /var/ossec/bin/ossec-control enable client-syslog

And finally restart the OSSEC processes:

.. code-block:: console 

    # /var/ossec/bin/ossec-control restart

ossec-csyslog should start along with the other OSSEC processes:

.. code-block:: console 

    OSSEC HIDS v1.5.1 Stopped
    Starting OSSEC HIDS v1.5.1 (by Third Brigade, Inc.)
    Started ossec-csyslogd...
    ..

And in the logs:

.. code-block:: console 

    # tail -n 1000 /var/ossec/logs/ossec.log | grep csyslog
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Started (pid: 19412).
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Forwarding alerts via syslog to: ‘192.168.4.1:514′.
    2008/07/25 12:55:16 ossec-csyslogd: INFO: Forwarding alerts via syslog to: ‘10.1.1.1:514′.

This is what the syslog server should receive (every log separated by level,
rule, location and the actual event that generated it):

.. code-block:: console
    
    Jul 25 12:17:41 enigma ossec: Alert Level: 3; Rule: 5715 - SSHD authentication success.; Location: (jul) 192.168.2.0->/var/log/messages;
    srcip: 192.168.2.190; user: root; Jul 25 13:26:24 slacker sshd[20440]: Accepted password for root from 192.168.2.190 port 49737 ssh2

