
########################
Output and Alert options
########################

Contents:
---------

.. toctree::
    :maxdepth: 2

    syslog-output
    email-output 
    json-alert-log-output
    database-output 
    reports-email-output
    picviz-output
    prelude-output


Overview:
---------

OSSEC includes a number of ways to send alerts to other systems or applications. 
Syslog, email, and sending the alerts to an SQL database are the typical methods.
These output methods send only alerts, not full log data.
Since the agents do not generate alerts, these options are server side only.



