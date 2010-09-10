.. _ossec_config.active-response:


ossec.conf: Active Response Options
===================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Alerts options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All active-response options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <command>
            <!--
            Command options here 
            --> 
        </command>
        <active-response> 
            <!-- 
            active-response options here
            --> 
        </active-response> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.active-response.trst

