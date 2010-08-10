.. _ossec_config.remote: 

ossec.conf: Remote Options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

remote options are avaiable in the the following installation types:

* server

Location 
^^^^^^^^

All remote options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML except to show location:

.. code-block:: xml 

    <ossec_config> 
        <remote> 
            <!-- 
            remote options here
            --> 
        </remote> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.remote.rst
