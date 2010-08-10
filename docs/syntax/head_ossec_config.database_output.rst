
.. _ossec_config.database_output: 

ossec.conf: Database Output options
===================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Database Output options are avaiable in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All database_output options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML except to show location:

.. code-block:: xml 

    <ossec_config> 
        <database_output> 
            <!-- 
            Database Output options here
            --> 
        </database_output> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.database_output.rst 
