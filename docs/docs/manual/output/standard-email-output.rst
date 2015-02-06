
Alerts to a single E-Mail Address 
---------------------------------

In order to send notifications to a single address three items need to be setup 
within ossec.conf 

Global E-Mail address destination 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The destination email address and mail host should be configured inside the 
<global> section of the /var/ossec/etc/ossec.conf.

.. code-block:: xml 

    <ossec_config>
        <global>
            <email_notification>yes</email_notification>
            <email_to>me@example.com</email_to>
            <smtp_server>mx.example.com..</smtp_server>
            <email_from>ossec@example.com</email_from>

Full details on all the options are avaiable at :ref:`ossec_config.global`

Set the alert levels that will send notifications 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The minimum email_alert_level can be set inside the <alerts> section of the 
/var/ossec/etc/ossec.conf file.

.. code-block:: xml 

    <ossec_config> 
        <alerts>
            <email_alert_level>10</email_alert_level> 

Full details on all the options are avaiable at :ref:`ossec_config.alerts`


Restart OSSEC to complete the changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OSSEC needs to be restarted for the change to take effect. 

.. code-block:: console 

    # /var/ossec/bin/ossec-control restart 

