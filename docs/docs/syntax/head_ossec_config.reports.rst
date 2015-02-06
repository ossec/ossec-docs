
.. _ossec_config.reports: 

ossec.conf: Reports options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Reports options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All reports options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <reports> 
            <!-- 
            Reports options here
            --> 
        </reports> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.reports.trst 
