.. _ossec_config.agentless:


ossec.conf: Agentless Options
=============================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Agentless options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All agentless options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <agentless> 
            <!-- 
            agentless options here
            --> 
        </agentless> 
    </ossec_config> 

Options 
------- 

.. include:: ./ossec_config.agentless.trst
