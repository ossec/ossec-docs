
.. _manual-procmon:

Process Monitoring
==================

We love logs. Inside OSSEC we treat everything as if it was a log and parse it
appropriately with our rules. However, some information is not available in log
files but we still want to monitor them. To solve that gap, we added the ability
to monitor the output of commands via OSSEC and treat those just like they were
log files.

For example, if you wanted to monitor the disk space utilization, you would need
to setup a cron job to dump the output of "df -h" to a log file (maybe
/var/log/df.log) and configure OSSEC to look at it.

Now, with the new version of OSSEC you can do it directly in there with the
following configuration:

.. code-block:: xml 

    <localfile>
        <log_format>command</log_format>
        <command>df -h</command>
    </localfile>

Since we already have a sample rule for df -h included into OSSEC you would see
the following when any partition reached 100%::

    ** Alert 1257451341.28290: mail - ossec,low_diskspace,
    2009 Nov 05 16:02:21 (home-ubuntu) 192.168.0.0->df -h

    Rule: 531 (level 7) -> "Partition usage reached 100% (disk space monitor)."
    Src IP: (none)
    User: (none)
    ossec: output: "df -h": /dev/sdb1 24G 12G 11G 100% /var/backup

Another example, if you want to monitor the load average, you can configure
OSSEC to monitor the "uptime" command and alert when it is higher than 2, for
example: 

.. code-block:: xml 

    <localfile>
        <log_format>command</log_format>
        <command>uptime</command>
    </localfile>

And in the rule:

.. code-block:: xml 

    <rule id="100101" level="7" ignore="7200">
        <if_sid>530</if_sid>
        <match>ossec: output: "uptime": </match>
        <regex>load averages: 2.</regex>
        <description>Load average reached 2..</description>
    </rule>

Lots of possibilities with this feature. If you have ideas of commands to
monitor and rules, please comment.
