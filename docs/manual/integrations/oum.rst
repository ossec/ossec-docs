#############################
OSSEC Updater Modified (OUM)
#############################

About
=====

OUM is an interactive rule and CDB updater for OSSEC. Loosely based on the yum package manager,
it can be used to update OSSEC rules/decoders and threat intelligence CDB files.

.. warning::

   OUM requires a valid OSSEC+ subscription - a **FREE** subscription for all
   users prior to installing, configuring, and updating OUM.
   Please `register <https://www.ossec.net/register-for-ossec/>`_ for an OSSEC+
   account before attempting to install OUM.

Installation
============

Download and execute the OUM installer by executing the following command:

    .. code-block:: sh

        wget -q -O - https://updates.atomicorp.com/installers/oum | bash

Configuration
=============

After successful installation of OUM, users must first configure OUM before
utilizing the interactive rule and CDB updater for OSSEC. To configure OUM users
can execute the following command:

    .. code-block:: sh

        oum configure

Updating Rulesets
=================

Rulesets and CDBs can be updated via OUM by executing the following command:

    .. code-block:: sh

        oum update

Troubleshooting
===============

Troubleshooting coming soon...

Credits
=======

OUM is an opensource project located on Github! The project maintainers of the
OUM project are always looking for community contribution. If you would like to
contribute, please visit the `project <https://github.com/ossec/oum>`_ page. 
