.. _ossec_config.client:

ossec.conf: Client Options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

client options are available in the the following installation types:

* agent

Location 
^^^^^^^^

All client options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <client> 
            <!-- 
            client options here
            --> 
        </client> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.client.trst
