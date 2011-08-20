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

    Additional data from: 'http://blog.rootshell.be/2010/03/15/detecting-usb-storage-usage-with-ossec/'


Why do I see alerts for agent2 in an email about agent1?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    When an email is being prepared alerts will be grouped together. The only real criteria for grouping alerts together is the timeframe.
    To prevent alerts from being grouped together you can set ``maild.groupping`` to 0 in ``/var/ossec/etc/internal_options.conf``.
    If this is set, alerts will be sent out individually. By default OSSEC will only send 12 emails per hour.
    To increase this limit, modify or add the <email_maxperhour> setting in the ``<global>`` section of the ``ossec.conf``. (see: email_maxperhour_ .)



    .. code-block:: xml
        <global>
          <email_maxperhour>100</email_maxperhour>



Why does my frequency rule get triggered by 8 events when frequency is set to 6?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

