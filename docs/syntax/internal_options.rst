
.. _syntax_internal_config:

internal_options.conf: syntax and options
=========================================

The ``/var/ossec/etc/internal_options.conf`` file includes runtime tuning options not
present in ``ossec.conf``. Use ``/var/ossec/etc/local_internal_options.conf`` for local
overrides; that file is preserved during upgrades.

.. toctree::
    :maxdepth: 2

    head_internal_options.ossec
    head_internal_options.analysisd
    head_internal_options.remoted
    head_internal_options.logcollector
    head_internal_options.maild
    head_internal_options.authd
    head_internal_options.monitord
    head_internal_options.syscheck
    head_internal_options.agent
    head_internal_options.dbd
    head_internal_options.windows
