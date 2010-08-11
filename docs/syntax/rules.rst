.. element:: match

    Any string to match against the event (log).

    **Allowes:** Any :ref:`os_match` 

.. element:: regex 

    Any regex to match against the event(log). 

    **Allowes:** Any :ref:`os_regex`

.. element:: decoded_as 

    Any pre-matched string (see :ref:`syntax_decoders`)

    **Allowes:** Any string 

.. element:: category

    The decoded category to match (ids, syslog, firewall, web-log, squid or windows). 

    **Allowes:** Any category :ref:`categories` 

.. element:: srcip 

    Any IP address (decoded as the source ip). Use "!" to negate it.

    **Allowes:** Any srcip 

.. element:: dstip 

    Any IP address (decoded as the dst ip). Use “!” to negate it.

    **Allowes:** Any dstip 

.. element:: user 

    any username (decoded as the username).

    **Allowes:** any :ref:`os_match` 

.. element:: program_name

    Program name is decoded from syslog process name. 

    **Allowes:** any :ref:`os_match` 

.. element:: hostname 

    Any hostname (decoded as the syslog hostname).

    **Allowes:** any :ref:`os_match` 

.. element:: time 

    Time that the event was generated.

    **Allowes:** Any time range (hh:mm-hh:mm) 

.. element:: weekday 

    Week day that the event was generated. 

    **Allowes:** monday - sunday, weekday, weekend 

.. element:: id 

    Any ID (decoded as the ID). 

    **Allowes:** any :ref:`os_match` 

.. element:: url 

    Any URL (decoded as the URL).
    
    **Allowes:** any :ref:`os_match` 

.. element:: if_sid 

    Matches if the ID has matched. 

    **Allowes:** Any rule id 

.. element:: if_group 

    Matches if the group has matched before. 

    **Allowes:** Any Group 

.. element:: if_level 

    Matches if the level has matched before. 

    **Allowes:** Any level from 1 to 16 

.. element:: if_matched_sid 

    Matches if the ID has matched. 

    **Allowes:** Any rule id 

.. element:: if_matched_group 

    Matches if the group has matched before. 

    **Allowes:** Any group 


.. element:: if_matched_level 

    Matches if the level has matched before. 

    **Allowes:** Any level from 1 to 16 

.. element:: same_source_ip 

    Used together with frequency. Specifies that the source ip must be the same. 

.. element:: same_source_port 

    Used together with frequency. Specifies that the source port must be the same. 

.. element:: same_location 

    Used together with frequency. Specifies that the location must be the same.

.. element:: description 

    Rule description. 

    **Allowes:** Any string 

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

    **Allowes:** String but content is dependant on the type attrubute. 

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

    This element is no longer used.  Please use :element:`info` with the cve type. 

.. element:: options 

    Additional rule options (to do not e-mail/log) 

    **Allowes:** 

    - alert_by_email 
    - no_email_alert 
    - no_log
