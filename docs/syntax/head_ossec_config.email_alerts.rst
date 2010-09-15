.. _ossec_config.email_alerts: 

ossec.conf: Granular Email options
==================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Global options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All global options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <email_alerts> 
            <!-- 
            Email_alerts options here
            --> 
        </email_alerts> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.email_alerts.trst
