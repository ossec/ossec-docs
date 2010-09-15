.. _ossec_config.rules: 


ossec.conf: Rules options
=========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Rules options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All global options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <rules> 
            <!-- 
            Rules options here
            --> 
        </rules> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.rules.rst 
