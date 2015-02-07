
.. _manual-out-prelude:

Sending output to a Database
----------------------------

OSSEC supports MySQL and PostgreSQL database outputs.


Configuration options
^^^^^^^^^^^^^^^^^^^^^

These configurations options can be specified in the server or local install ossec.conf file.


.. include:: ../../syntax/ossec_config.database_output.trst 


Enabling Database Support
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    You must have the MySQL or PgSQL Client libraries installed on the OSSEC server.

Before you run the "./install.sh" script execute the following to compile OSSEC with
database support. 

.. code-block:: console 

    # cd ossec-hids-*
    # cd src; make setdb; cd ..
    # ./install.sh 

Enable Database output in the configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After installation is complete database support needs to be enabled. 
The following command will enable the database daemon on the next restart. 

.. code-block:: console 

    # /var/ossec/bin/ossec-control enable database 


Database Specific Setup
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    
    mysql-database-output 
    pgsql-database-outout


