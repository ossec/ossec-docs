.. _manual_out_reports: 

Daily E-Mail Reports
====================

Daily E-Mail reports are summaries of the happening of the day from an OSSEC presepective.  


Configuration options
---------------------

All of these configurations options can be specified in the /var/ossec/etc/ossec.conf. 

.. include:: ../../syntax/ossec_config.reports.rst 

Examples
--------

Receive summary of all the authentication success alerts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example added to ossec.conf will send a daily report 
on all authentication_success alerts sorted by the related field srcip.

.. code-block:: xml 
    
    <ossec_config>
        <reports>
            <category>authentication_success</category>
            <user type="relation">srcip</user>
            <title>Daily report: Successful logins</title>
            <email_to>me@example.com</email_to>
            

Receive summary of all File integrity monitoring alerts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example added to the ossec.conf will send 
a report on all events related to syscheck.  

.. code-block:: xml 

    <ossec_config>
        <reports>
            <category>syscheck</category>
            <title>Daily report: File changes</title>
            <email_to>me@example.com</email_to>
