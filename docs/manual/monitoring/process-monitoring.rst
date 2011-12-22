
.. _manual-procmon:

Process Monitoring
==================

Overview 
--------

We love logs. Inside OSSEC we treat everything as if it is a log and parse it
appropriately with our rules. However, some information is not available in log
files but we still want to monitor it. To solve that gap, we added the ability
to monitor the output of commands via OSSEC, and treat the output of those commands
 just like they were log files.

Configuration examples
---------------------- 

Disk space utilization (df -h) example 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, if you wanted to monitor the disk space utilization, you would need
to setup a cron job to dump the output of ``df -h`` to a log file (maybe
/var/log/df.log) and configure OSSEC to look at it.

As of OSSEC version 2.3 you can monitor commands directly in OSSEC 
following configuration:

.. code-block:: xml 

    <localfile>
        <log_format>command</log_format>
        <command>df -h</command>
    </localfile>

Since we already have a sample rule for df -h included with OSSEC you would see
the following when any partition reached 100%::

    ** Alert 1257451341.28290: mail - ossec,low_diskspace,
    2009 Nov 05 16:02:21 (home-ubuntu) 192.168.0.0->df -h

    Rule: 531 (level 7) -> "Partition usage reached 100% (disk space monitor)."
    Src IP: (none)
    User: (none)
    ossec: output: 'df -h': /dev/sdb1 24G 12G 11G 100% /var/backup

Load average (uptime) Example 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
        <match>ossec: output: 'uptime': </match>
        <regex>load averages: 2.</regex>
        <description>Load average reached 2..</description>
    </rule>

There are lots of possibilities with this feature. If you have ideas for commands to
monitor and rules, please comment.


Alerting when output of a command changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to create alerts when a log or the output of a command changes, take 
a look at the new <check_diff /> option in the rules (available on the latest 
snapshot).

To demonstrate with an example, we will create a rule to alert when there is 
a new port open in listening mode on our server.

First, we configure OSSEC to run the ``netstat -tan |grep LISTEN`` command 
by adding the following to ossec.conf:

.. code-block:: xml 

    <localfile>
        <log_format>full_command</log_format>
        <command>netstat -tan |grep LISTEN|grep -v 127.0.0.1</command>
    </localfile>

After that, I add a rule to alert when its output changes:

.. code-block:: xml 

    <rule id="140123" level="7">
        <if_sid>530</if_sid>
        <match>ossec: output: 'netstat -tan |grep LISTEN</match>
        <check_diff />
        <description>Listened ports have changed.</description>
    </rule>'

Note that we use the ``<check_diff />`` option. The first time it receives the 
event, it will store in an internal database. Every time it receives the same 
event, it will compare against what we have store and only alert if the output 
changes.

In our example, after configuring OSSEC, I started netcat to listen on port 
23456 and that’s the alert I got: ::

    OSSEC HIDS Notification.
    2010 Mar 11 19:56:30

    Received From: XYZ->netstat -tan |grep LISTEN|grep -v 127.0.0.1
    Rule: 140123 fired (level 7) -> "Listened ports have changed."
    Portion of the log(s):

    ossec: output: 'netstat -tan |grep LISTEN|grep -v 127.0.0.1':
    tcp4       0      0 *.23456           *.*               LISTEN
    tcp4       0      0 *.3306            *.*               LISTEN
    tcp4       0      0 *.25              *.*               LISTEN
    Previous output:
    ossec: output: 'netstat -tan |grep LISTEN|grep -v 127.0.0.1':
    tcp4       0      0 *.3306            *.*               LISTEN
    tcp4       0      0 *.25              *.*               LISTEN


Detecting USB Storage Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Xavier Mertens <http://blog.rootshell.be/2010/03/15/detecting-usb-storage-usage-with-ossec/>`_ wrote a very interesting article on Detecting USB Storage Usage with 
OSSEC. He used our policy auditing module for that, but I think USB monitoring 
can be done in a much easier way with our new :xml:`check_diff` feature. 

To get started, first configure your Windows agents to monitor the USBSTOR 
registry entry using the reg command:

.. code-block:: xml 

    <agent_config os="windows">
        <localfile>
            <log_format>full_command</log_format>
            <command>reg QUERY HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR</command>
        </localfile>
    </agent_config>



Next create a local rule for that command:

.. code-block:: xml 

    <rule id="140125" level="7">
        <if_sid>530</if_sid>
        <match>ossec: output: 'reg QUERY</match>
        <check_diff />
        <description>New USB device connected</description>
    </rule>

Now after a few minutes you will see a directory at 
``/var/ossec/queue/diff/[agent_name]/[rule_id]`` with the current snapshot of this 
command. Once someone adds a new USB device you will get this alert: ::

    ** Alert 1268687754.35062: mail  - local,syslog,
    2010 Mar 15 18:15:54 (xx-netbook) any->reg QUERY HKLMSYSTEMCurrentControlSetEnumUSBSTOR
    Rule: 140125 (level 7) -> 'New USB device connected'
    Src IP: (none)
    User: (none)
    ossec: output: 'reg QUERY HKLMSYSTEMCurrentControlSetEnumUSBSTOR':! REG.EXE VERSION 3.0

    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTOR
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_&Prod_USB_Flash_Memory&Rev_5.00
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Generic&Prod_Flash_Disk&Rev_8.0
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Hitachi&Prod_HTS543225L9A300&Rev_
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_LEXAR&Prod_JD_FIREFLY&Rev_1100
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_SAMSUNG&Prod_HM160JC&Rev_0000
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Sony&Prod_DSC&Rev_1.00
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_TomTom&Prod_ONE_XXL_IQ_Rts
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_USB_2.0&Prod_USB_Flash_Drive&Rev_0.00

    Previous output:

    ossec: output: 'reg QUERY HKLMSYSTEMCurrentControlSetEnumUSBSTOR':
    ! REG.EXE VERSION 3.0
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTOR
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_&Prod_USB_Flash_Memory&Rev_5.00
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Generic&Prod_Flash_Disk&Rev_8.07
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Hitachi&Prod_HTS543225L9A300&Rev_
    HKEY_LOCAL_ACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_SAMSUNG&Prod_HM160JC&Rev_0000
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_Sony&Prod_DSC&Rev_1.00
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_TomTom&Prod_ONE_XXL_IQ_Rts
    HKEY_LOCAL_MACHINESYSTEMCurrentControlSetEnumUSBSTORDisk&Ven_USB_2.0&Prod_USB_Flash_Drive&Rev_0.00
