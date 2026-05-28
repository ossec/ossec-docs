
Granular E-Mail alerts to many E-Mail addresses 
-----------------------------------------------

OSSEC allows very granular options for the e-mail alerting and its format (full or SMS).

.. note:: 

    Note that there must be at least one <email_to> recipient mentioned in the <global> 
    section of the configuration or no emails will be sent at all.

If your mail provider requires authentication or TLS, configure the ``<global>`` section as
described in :ref:`manual-out-smtp-auth` before adding ``<email_alerts>`` entries.

.. include:: ../../examples/output/granular_email_examples.trst




