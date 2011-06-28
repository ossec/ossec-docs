
Configuring PgSQL
-----------------

Database Setup 
^^^^^^^^^^^^^^

Create a user for OSSEC within PgSQL 

.. code-block:: console 

    $ sudo -u postgres createuser -D -A -P ossec_user
    Enter password for new role:
    Enter it again:
    Shall the new role be allowed to create more new roles? (y/n) n
    CREATE ROLE

Create a database for OSSEC

.. code-block:: console 

    $ sudo -u postgres createdb -O ossec_user ossecdb
    CREATE DATABASE

Create the necessary tables from the PostgreSQL schema

.. code-block:: console 

    $ wget http://www.ossec.net/files/other/postgresql.schema
    $ psql -h 127.0.0.1 -U ossec_user -d ossecdb -f postgresql.schema 

OSSEC Setup 
^^^^^^^^^^^

In order for ossec to output alerts and other data into the database the 
/var/ossec/etc/ossec.conf will need to be updated and a <database_output> 
section will need to be added.

.. code-block:: xml

    <ossec_config>
        <database_output>
            <hostname>192.168.2.30</hostname>
            <username>ossecuser</username>
            <password>ossecpass</password>
            <database>ossec</database>
            <type>postgresql</type>
        </database_output>
    </ossec_config>

The values will need to be corrected for your installation's hostname, postgresql user, password, and 
database.  

Complete PgSQL Output 
^^^^^^^^^^^^^^^^^^^^^ 

All that is left is to restart ossec for the changes to take effect. 

.. code-block:: console 

    # /var/ossec/bin/ossec-control restart 



