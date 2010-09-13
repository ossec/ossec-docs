
.. _ossec_config.localfile: 

ossec.conf: Localfile options
==========================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Localfile options are available in the the following installation types:

* server
* local 

Location 
^^^^^^^^

All localfile options must be configured in the /var/ossec/etc/ossec.conf or 
/var/ossec/etc/shared/agent.conf and used within the <ossec_config> or 
<agent_config> tags.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <localfile> 
            <!-- 
            Localfile options here
            --> 
        </localfile> 
    </ossec_config> 


Options
-------

.. include:: ossec_config.localfile.trst 
