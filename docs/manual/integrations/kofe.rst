####
KOFE
####

About
=====

KOFE is an opensource, SIEM-like experience powered by Kibana, OSSEC Filebeat, and Elasticsearch


Installation
============

1. Download and add the Atomic repository to your local system by executing the following command:

  .. code-block:: sh

      wget -q -O - https://updates.atomicorp.com/installers/atomic | bash

2. Install KOFE by executing the following command:

  .. code-block:: sh

      yum install -y kofe


Configuration
=============

After successful installation of KOFE, users must first configure KOFE.
To configure KOFE users can execute the following command:

    .. code-block:: sh

        kofe setup

Listing Dashboards
==================

KOFE provides default dashboards that can be installed at the user's request.
To list dashboards that can be installed with KOFE, users can execute the following
command:

    .. code-block:: sh

       kofe list

Installing Dashboards
=====================

To install dashboards provided with KOFE users can execute the following command:

    .. code-block:: sh

       kofe install dashboard_name

Troubleshooting
===============

Troubleshooting coming soon...

Credits
=======

KOFE is an opensource project located on Github! The project maintainers of the
KOFE project are always looking for community contribution. If you would like to
contribute, please visit the `project <https://github.com/ossec/kofe>`_ page.
