.. _ossec_101_intro:


OSSEC 101: Installation
-----------------------

What are the different types of installations?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* local - A local installation includes everything necessary to monitor a single system. For local installations an agent is not necessary. Most of the documentation for the server installation is also applicable to the local install.

* server - A server installation is useful for monitoring multiple systems. It helps centralize configuration and analysis. Agents pass log messages and syscheck information to the server for analysis. OSSEC servers are often referred to as managers to help avoid confusion. Servers should always have agents associated with them. A server install requires a unix-like system, various Linux distributions being the best tested.

* agent - An agent is a client system being monitored by an OSSEC manager. The OSSEC agent processes will forward information to the manager for analysis. Agents can be unix-like systems or Windows systems.

* agentless - This isn't really a type os OSSEC installation, but an option for monitoring embedded systems, or other systems a full OSSEC installation doesn't make sense. 

* hybrid - A hybrid installation is both a server and an agent. This allows for a tiered architecture of agents pushing to servers which forward alerts on to other servers for consolidation.

What type of installation should I perform ...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This depends on what your requirements are. 
  * Is this a standalone system? **local**
  * Do you want to monitor a large number of systems from a central location? Install a central **server** and perform **agent** installations on the clients.
  * Windows system? **agent**

What type of installation should I perform on my single webserver?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are installing OSSEC on only one system you should use the local installation. You will not need to add an agent or perform any other installations.


What are the installation pre-requisites?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ./installation/pre-requisites.trst


Installation Walk Throughs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 3
    :glob:

    installation/install_server
    installation/install_agent_linux
    installation/install_agent_windows
    installation/install_local
    installation/binary_install
    installation/oneway_install




