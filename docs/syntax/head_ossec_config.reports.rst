
.. _ossec_config.global: 

ossec.conf: Global options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Global options are avaiable in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All global options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <global> 
            <!-- 
            Global options here
            --> 
        </global> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.global.rst 
