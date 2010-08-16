.. _ossec_config.syscheck: 

ossec.conf: Syscheck Options
============================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Syscheck options are avaiable in the the following installation types:

* server
* local 
* agent 

Location 
^^^^^^^^

All global options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <syscheck> 
            <!-- 
            Syscheck options here
            --> 
        </syscheck> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.syscheck.rst
