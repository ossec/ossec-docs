.. _manual-ar:

###############
Active Response
###############

The Active Response feature within OSSEC can run applications on an agent or server in response to certain triggers.
These triggers can be specific alerts, alert levels, or rule groups.

The active response framework is also what allows an OSSEC administrator to start a syscheck scan or restart OSSEC on a remote agent.

Disabling active response
-------------------------

Different configuration elements disable active response at different scopes:

``<active-response>`` with ``<disabled>yes</disabled>``
    Skips **one** command binding; other bindings still run.

``<client>`` with ``<disable-active-response>yes</disable-active-response>``
    Stops **all** active-response execution on that agent.

See :ref:`ossec_config.active-response` and :ref:`ossec_config.client` for syntax.

Bundled active-response scripts are documented in :ref:`manual-ar-scripts`.

.. toctree::
    :maxdepth: 2
    :glob:

    *

    systems/*

    
   


