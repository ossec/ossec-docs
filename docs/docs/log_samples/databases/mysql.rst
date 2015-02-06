Log Samples for MySQL
---------------------


Notes:
^^^^^^

The timestamp of MySQL logs only appear in the first event during that time. It means that <br />
if you have two logs within the same second, only the first one will have the timestamp.



Startup:
^^^^^^^^

.. code-block:: console

  060516 22:38:46  mysqld started
  InnoDB: The first specified data file ./ibdata1 did not exist:
  InnoDB: a new database to be created!
  060516 22:38:54  InnoDB: Started; log sequence number 0 0


Shutdown:
^^^^^^^^^

.. code-block:: console

  060516 22:38:54  mysqld ended
  070823 20:58:09 [Note] /usr/libexec/mysqld: Shutdown complete


Error:
^^^^^^

.. code-block:: console

  060516 22:38:54 [ERROR] Fatal error: Can't open privilege tables: Table 'mysql.host' doesn't exist

Connections,queries:

.. code-block:: console

  070823 21:00:32       1 Connect     root@localhost on test1
  070823 21:00:48       1 Query       show tables
  070823 21:00:56       1 Query       select * from category
  070917 16:29:01      21 Query       select * from location
  070917 16:29:12      21 Query       select * from location where id = 1 LIMIT 1




