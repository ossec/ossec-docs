.. _ossec_config.rootcheck: 

ossec.conf: Rootcheck options
=============================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

rootcheck options are avaiable in the the following installation types:

* server
* local 
* agent

Location 
^^^^^^^^

All rootcheck options must be configured in the /var/ossec/etc/ossec.conf or 
/var/ossec/etc/shared/agents.conf and used within the <ossec_config> tag.  

XML excerpt to show location if part of ossec.conf:

.. code-block:: xml 

    <ossec_config> 
        <rootcheck> 
            <!-- 
            rootcheck options here
            --> 
        </rootcheck> 
    </ossec_config> 

XML excerpt to the Location if part of agent.conf 


.. code-block:: xml 

    <agent_config> 
        <rootcheck> 
            <!-- 
            rootcheck options here
            --> 
        </rootcheck> 
    </agent_config> 

Options
-------

.. include:: ossec_config.rootcheck.trst 
