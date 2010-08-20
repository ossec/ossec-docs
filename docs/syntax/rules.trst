
.. element:: rule 

    Defines a rule 

    **Attrubutes:** 

    - *level* 

        - Specifies the level of the rule. Alerts and responses use this value. 
        - **Allowed:** Any number (0 to 16) 


    - *id* 

        - Specifies the ID of the rule. 
        - **Allowed:** Any number from 100 to 99999 

    - *accuracy* 

        - Specifies if the rule is accurate or not (0 is not, 1 is yes)
        - **Allowed:** 0/1 

    - *maxsize* 

        - Specifies the maximum size of the event. 
        - **Allowed:** Any number from 1 to 99999 

    - *frequency* 

        - Specifies the number of times the rule must have matched before firing it.
        - **Allowed:** Any number from 1 to 999

    - *timeframe* 

        - The timeframe used for the frequency. 
        - **Allowed:** Any number from 1 to 9999

    - *ignore* 

        - The time to ignore this rule after firing it (to avoid floods). 
        - **Allowed:** Any number from 1 to 9999

.. element:: match

    Any string to match against the event (log).

    **Allowed:** Any :ref:`os_match` 

.. element:: regex 

    Any regex to match against the event(log). 

    **Allowed:** Any :ref:`os_regex`

.. element:: decoded_as 

    Any pre-matched string (see :ref:`syntax_decoders`)

    **Allowed:** Any string 

.. element:: category

    The decoded category to match (ids, syslog, firewall, web-log, squid or windows). 

    **Allowed:** Any category :ref:`categories` 

.. element:: srcip 

    Any IP address (decoded as the source ip). Use "!" to negate it.

    **Allowed:** Any srcip 

.. element:: dstip 

    Any IP address (decoded as the dst ip). Use “!” to negate it.

    **Allowed:** Any dstip 

.. element:: user 

    any username (decoded as the username).

    **Allowed:** any :ref:`os_match` 

.. element:: program_name

    Program name is decoded from syslog process name. 

    **Allowed:** any :ref:`os_match` 

.. element:: hostname 

    Any hostname (decoded as the syslog hostname).

    **Allowed:** any :ref:`os_match` 

.. element:: time 

    Time that the event was generated.

    **Allowed:** Any time range (hh:mm-hh:mm) 

.. element:: weekday 

    Week day that the event was generated. 

    **Allowed:** monday - sunday, weekday, weekend 

.. element:: id 

    Any ID (decoded as the ID). 

    **Allowed:** any :ref:`os_match` 

.. element:: url 

    Any URL (decoded as the URL).
    
    **Allowed:** any :ref:`os_match` 

.. element:: if_sid 

    Matches if the ID has matched. 

    **Allowed:** Any rule id 

.. element:: if_group 

    Matches if the group has matched before. 

    **Allowed:** Any Group 

.. element:: if_level 

    Matches if the level has matched before. 

    **Allowed:** Any level from 1 to 16 

.. element:: if_matched_sid 

    Matches if the ID has matched. 

    **Allowed:** Any rule id 

.. element:: if_matched_group 

    Matches if the group has matched before. 

    **Allowed:** Any group 


.. element:: if_matched_level 

    Matches if the level has matched before. 

    **Allowed:** Any level from 1 to 16 

.. element:: same_source_ip 

    Used together with frequency. Specifies that the source ip must be the same. 

.. element:: same_source_port 

    Used together with frequency. Specifies that the source port must be the same. 

.. element:: same_location 

    Used together with frequency. Specifies that the location must be the same.

.. element:: description 

    Rule description. 

    **Allowed:** Any string 

.. element:: info 

    Extra information about the rule.

    **Attrubutes:**

    - *type* 

        - Value: text 

            This is the default when no type is selected.  Just used for addintional 
            infomation about the alert/event. 

        - Value: link

            Link to more infomation about the alert/event.  

        - Value: cve 

            The CVE Number related to this alert/event.  

        - Value: ovsdb 

            The osvdb id related to this alert/event. 

    **Allowed:** String but content is dependant on the type attrubute. 

    **Example:** 

    .. code-block:: xml

        <rule id="502" level="3">
            <if_sid>500</if_sid>
            <options>alert_by_email</options>
            <match>Ossec started</match>
            <description>Ossec server started.</description>
            <info type="link">http://ossec.net/wiki/Rule:205</info>
            <info type="cve">2009-1002</info>
            <info type="osvdb"> 61509</info>
            <info type="text">Internal Why we are running this run in our company</info>
            <info>Type text is the default</info>
        </rule>

.. element:: cve 

    CVE related to the rule. 

    This element is no longer used.  Please use :xml:`info` with the cve type. 

.. element:: options 

    Additional rule options (to do not e-mail/log) 

    **Allowed:** 

    - alert_by_email 
    - no_email_alert 
    - no_log
