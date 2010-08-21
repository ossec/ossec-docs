.. _ossec_config.active-responce:


ossec.conf: Active Responce Options
===================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Alerts options are avaiable in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All active-responce options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <command>
            <!--
            Command options here 
            --> 
        </command>
        <active-responce> 
            <!-- 
            active-responce options here
            --> 
        </active-responce> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.active-responce.trst

