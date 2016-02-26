.. _ossec_config.active-response:


ossec.conf: Active Response Options
===================================

Overview 
--------

Supported types 
^^^^^^^^^^^^^^^

Most active-reponse options are available in the the following installation types:

* server
* local 

The ``disabled`` option is available on all installation types.

Configuration pieces
^^^^^^^^^^^^^^^^^^^^

There are two pieces to an active-response configuration. 
The first is the ``<command>`` section. 
This details the command to be run, and the options it will use.
There can be any number of command options.

The second is the ``<active-response>`` section.
This section defines when the command will be run.

Location 
^^^^^^^^

All active-response options must be configured in the /var/ossec/etc/ossec.conf 
and used within the <ossec_config> tag.  

XML excerpt to show location:

.. code-block:: xml 

    <ossec_config> 
        <command>
            <!--
            Command options here 
            --> 
        </command>
        <active-response> 
            <!-- 
            active-response options here
            --> 
        </active-response> 
    </ossec_config> 

.. include:: ./ossec_config.active-response.trst

