.. _ossec_config.alerts:


ossec.conf: Alerts Options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Alerts options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All alerts options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <alerts> 
            <!-- 
            alerts options here
            --> 
        </alerts> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.alerts.trst
