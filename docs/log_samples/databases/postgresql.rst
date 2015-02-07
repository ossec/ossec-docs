Log Samples for PostgreSQL
--------------------------


Login/Logout:
^^^^^^^^^^^^^

.. code-block:: console

  [2007-08-31 19:22:21.469 ADT] :[unknown] LOG:  connection received: host=192.168.2.99 port=52136
  [2007-08-31 19:22:21.485 ADT] 192.168.2.99:ossecdb LOG:  connection authorized: user=ossec_user database=ossecdb
  [2007-08-31 19:22:22.427 ADT] 192.168.2.99:ossecdb LOG:  disconnection: session time: 0:00:00.95 user=ossec_user database=ossecdb host=192.168.2.99 port=52136
  [2007-09-27 11:02:44.941 ADT] 192.168.2.10:ossecdb ERROR:  relation "lala" does not exist
  [2007-09-27 11:02:46.444 ADT] 192.168.2.10:ossecdb LOG:  disconnection: session time: 0:00:35.79 user=ossec_user database=ossecdb host=192.168.2.10 port=3584



Log messages:
^^^^^^^^^^^^^

.. code-block:: console

  [2007-09-01 07:14:41.062 ADT] : LOG:  autovacuum: processing database "template1"
  [2007-09-01 07:15:41.079 ADT] : LOG:  autovacuum: processing database "ossecdb"



Query log:
^^^^^^^^^^

.. code-block:: console

  [2007-09-01 16:44:49.244 ADT] 192.168.2.10:ossecdb LOG:  duration: 4.550 ms  statement: SELECT id FROM location WHERE name = 'enigma->/var/log/messages' AND server_id = '1'
  [2007-09-01 16:44:49.251 ADT] 192.168.2.10:ossecdb LOG:  duration: 5.252 ms  statement: INSERT INTO location(server_id, name) VALUES ('1', 'enigma->/var/log/messages')
  [2007-09-01 16:44:49.252 ADT] 192.168.2.10:ossecdb LOG:  duration: 0.016 ms  statement: SELECT id FROM location WHERE name = 'enigma->/var/log/messages' AND server_id = '1'
  [2007-09-27 11:02:51.611 ADT] 192.168.2.10:ossecdb LOG:  statement: INSERT INTO alert(id,server_id,rule_id,timestamp,location_id,src_ip) VALUES ('3577', '1', '50503','1190916566', '140', '0')



Query error:
^^^^^^^^^^^^

.. code-block:: console

  [2007-08-31 19:17:42.128 ADT] 192.168.2.99:test ERROR:  relation "alertaaa" does not exist
  [2007-08-31 19:17:46.375 ADT] 192.168.2.99:test ERROR:  syntax error at or near "a" at character 1
  [2007-09-27 11:02:44.941 ADT] 192.168.2.10:ossecdb ERROR:  relation "lala" does not exist



Authentication error:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  [2007-09-01 19:08:49.862 ADT] : LOG:  connection received: host=192.168.2.99 port=37142
  [2007-09-01 19:08:49.869 ADT] 192.168.2.99: FATAL:  password authentication failed for user "ossec_user"



