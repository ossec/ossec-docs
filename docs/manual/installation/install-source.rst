.. _install:

Manager/Agent Installation
==========================


Installation of OSSEC HIDS is very simple, the ``install.sh`` shell script can automate most of it.
There are a few questions to be answered before the installation will occur, one of the most 
important being which type of installation is desired.
It is important to choose the correct installation type: server, agent, local, or hybrid.
More information on thse can be found on the `OSSEC Architecture page <../ossec-architecture.html>`_.

Installation steps:
^^^^^^^^^^^^^^^^^^^

.. note::

    In the following installation the commands follow the ``#``. 
    Everything else is either comments out output. 

1. Download the latest version and verify its checksum.

.. include:: getossec.trst

2. Extract the compressed package and run the ``install.sh`` script. It will guide you 
   through the installation and compile the source (not shown).

    .. code-block:: console 

        # tar -zxvf ossec-hids-*.tar.gz (or gunzip -d; tar -xvf)
        # cd ossec-hids-* 
        # ./install.sh

3. The OSSEC manager listens on UDP port 1514. Any firewall sbetween the agents and 
   the manager will need to allow this traffic.

4. The server, agent, and hybrid installations will require additional configuration. 
   More information can be found on the `Managing the agents page <../agent/agent-management.html>`_.

5. Start OSSEC HIDS by running the following command:

    .. code-block:: console 

        # /var/ossec/bin/ossec-control start  


Options to enable features in `install.sh`:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These options are enabled by passing them to the install.sh script as environment variables.
Examples are included at the end.

* `USE_ZEROMQ` - Enable `ossec-analysisd` to output alerts to a `ZeroMQ <http://zeromq.org/>`_ interface.

* `DATABASE` - Build `ossec-dbd` to insert alerts into a database. Available options are `mysql` and `pgsql`.

* `USE_PRELUDE` - Enable `ossec-analysisd` to output alerts to a `Prelude SIEM <https://www.prelude-siem.org/>`_.

* `USE_GEOIP` - Enable `ossec-analysisd` to gather GeoIP information on source IP addresses in alerts.

The last 2 are probably only useful for development:

* `V` - Enable verbose compilation information.

* `DEBUG` - Enable extra debugging information in the binaries.

Examples:
^^^^^^^^^

.. code-block:: console

    # DATABASE=mysql ./install.sh
    # USE_ZEROMQ=yes ./install.sh

