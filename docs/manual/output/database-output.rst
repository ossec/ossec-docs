
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
You must have the MySQL or PgSQL Client libraries installed on the OSSEC server. Typically something like

.. code-block:: console

    Ubuntu
    # apt install mysql-server libmysqld-dev
      or
    # apt install postgresql libpq-dev 

    RedHat / CentOS
    # yum install mysql-devel
      or
    # yum install postgresql-devel


You then need to set the DATABASE environment variable and run the "./install.sh" script, to compile OSSEC with the appropriate database support. 

.. code-block:: console 

    # DATABASE=mysql ./install.sh
      or
    # DATABASE=pgsql ./install.sh
  
    

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


