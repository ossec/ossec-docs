.. _faq_alerts:

Alerts: FAQ
-------------

.. contents:: 
    :local:


How do you monitor for usb storage?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The first step is to configure the agents to check a registry entry with the ``reg`` command:

    .. code-block:: xml

      <agent_config os="Windows">
        <localfile>
          <log_format>full_command</log_format>
          <command>reg QUERY HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR</command>
          <alias>usb-check</alias>
        </localfile>
      </agent_config>

    Next create a local rule for that command:

    .. code-block:: xml

      <rule id="140125" level="7">
        <if_sid>530</if_sid>
        <match>ossec: output: 'usb-check':</match>
        <check_diff />
        <description>New USB device connected</description>
      </rule>

    When a USB drive is inserted into a Windows machine, an alert will not be triggered. 
    The alert will contain a diff of the registry entry before the USB device was inserted and after.


    Originally from: 'http://dcid.me/2010/03/detecting-usb-storage-usage-with-ossec/'

    Also some data from: 'http://blog.rootshell.be/2010/03/15/detecting-usb-storage-usage-with-ossec/'


Why does my frequency rule get triggered by 8 events when frequency is set to 6?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




