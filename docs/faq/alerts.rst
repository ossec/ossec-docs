.. _faq_alerts:

Alerts: FAQ
-------------

.. contents:: 
    :local:

.. _usb_storage:

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

.. _grouped_email_alerts:

Why do I see alerts for agent2 in an email about agent1?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    When an email is being prepared alerts will be grouped together. The only real criteria for grouping alerts together is the timeframe.
    To prevent alerts from being grouped together you can set ``maild.groupping`` to 0 in ``/var/ossec/etc/internal_options.conf``.
    If this is set, alerts will be sent out individually. By default OSSEC will only send 12 emails per hour.
    To increase this limit, modify or add the <email_maxperhour> setting in the ``<global>`` section of the ``ossec.conf``.
    (see: `email_maxperhour <../syntax/head_ossec_config.global.html#element-email_maxperhour>`_ .)



    .. code-block:: xml

        <global>
          <email_maxperhour>100</email_maxperhour>

.. _herp_derp_grouping:

Alerts for different sensors are appearing in the same email, how do I stop this from happening?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Read the previous FAQ entry.



.. _ignore_1002:

How do I ignore rule 1002?
^^^^^^^^^^^^^^^^^^^^^^^^^^

    Rule 1002 is a catch-all rule. It looks for keywords that are generally considered "bad."
    It also means there is not currently a rule that deals with the log message.
    It is configured to always send an email when it's triggered, and many users have found it annoying.
    The best thing to do when you encounter something that triggers rule 1002 is write a rule. 
    Contributing the logs and/or rules back to the project is also encouraged.
    Unless the application creating the log is an internal application, someone else may find the rule useful.


.. _too_many_emails:

I set the <email_alert_level> to 10, why do I keep seeing rules with lower levels?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Some rules have an option set to force OSSEC into sending an alert email. This option is ``<options>alert_by_email</options>``. 
   One of these rules is 1002. To ignore these rules you will have to create a rule to specifically ignore it,
   or overwrite the rule without the ``alert_by_email`` option. 

.. _too_much_1002:

Why are all of my Windows alerts showing up as rule 1002?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This is a known issue when using an older version on the OSSEC manager and newer versions on the agents.
   The manager should never be an older version than the agents. Using the same version is ideal, but when 
   that is not possible, the manager should be the newest version.


.. _MARK:

I keep getting log messages that start with ``--MARK``, what do I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **Example:**

   .. code-block:: console

      OSSEC HIDS Notification.
      2014 Sep 21 08:36:11

      Received From: (services01.qrios.com) 10.10.0.01->ossec-keepalive
      Rule: 1002 fired (level 2) -> "Unknown problem somewhere in the system."
      Portion of the log(s):

      --MARK--: cB82L!#'zr%lQfGUE))-7Q#Tj4fp+KG=@Wbq^wXiN)7L;ha!JB0kA_mJT5g-j[v_R@TAbk-,/fHEnHjerroRgAIh?OLWJ6LIL/q[Wg-cl#H#n/&(3NDr$@#v8r*l;!b*qru$@YxEE4Zak=(wEqN0JuDlLo!*HtlXKF(3.kQ&wj&+aklF%YNsA&*#Mef)xq'qd@)P+Dz0[jP]70%Q6vqbfbv?fA)D?#bc?_R+6y.i+MdXUzhucx9V#MV($-3uk4!ja!MocJx;D%P=We0Y^DoV&r+fha$rmRA1v$^y4U4cD1'H5T?OF1R3(Hq'H.YcO'3soM/(P2_A@w7K^6G2C=z2#.W2[24=VBXrvVe!5;eKotCM[8W!hE_CB;/!Vk1k'sCov_H[u'(=no*VEH$'@1vVU7zj*I7s0RHD)w@ipX?&@y)X50Q'w#OyN$+$pW?xW_0JYFRwK/g3wIuKc!D#Q*eMg'79/oaURi.j].))JIQ6&!k(O]ZN#lHATidRwRTvhQFQ]6DFiBT;fltbg(OALDi/LlPqkcL5bypK?axVByOGJp+.P(@[p)'j 
      

   This is a keep alive message, sent from an OSSEC agent to the manager. Thie prevents the manager from marking the agent as disconnected. These log messages should be filtered out, but sometimes one slips through (this one has the string ``erroR`` which may be the cause). These should be safe to ignore.



