
.. _ossec_config.syslog_output: 

ossec.conf: Syslog Output options
=================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Syslog Output options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All syslog_output options must be configured in the /var/ossec/etc/ossec.conf and used within the <ossec_config> tag.

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <syslog_output> 
            <!-- 
            Syslog Output options here
            --> 
        </syslog_output> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.syslog_output.trst 
