
.. _ossec-reportd:

ossec-reportd
==============

  ``ossec-reportd`` is a program to create reports from OSSEC alerts.
  ``ossec-reportd`` accepts alerts on ``stdin``, and outputs a report on ``stderr``.

  .. note::
    Since ``ossec-reportd`` outputs to stderr some utilities like ``less`` will not work if you do not redirect the output.
    End the ossec-reportd with ``2>&1`` to redirect stderr to stdout. ``more`` or ``less`` can be easily used after the stderr redirect.

ossec-reportd argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-reportd

.. option:: -h

    Display the help message

.. option:: -f <filter> <value>

    Filter the results.

.. option:: -r <filter> <value>

    Show related entries.

.. option:: -n <string>

    Create a description for the report.

.. option:: -s

    Show the alerts related to the summary.


ossec-reportd example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Show Successful Logins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # cat /var/ossec/logs/alerts/alerts.log | /var/ossec/bin/ossec-reportd -f group authentication_success

Example 2: Show Alerts Level 10 and Greater
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # cat /var/ossec/logs/alerts/alerts.log | /var/ossec/bin/ossec-reportd -f level 10

Example 3: Show the srcip for all users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # cat /var/ossec/logs/alerts/alerts.log | /var/ossec/bin/ossec-reportd -f group authentication -r user srcip

Example 4: Show Changed files as reported by Syscheck
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # cat /var/ossec/logs/alerts/alerts.log | /var/ossec/bin/ossec-reportd -f group syscheck -r location filename


Example output
~~~~~~~~~~~~~~

.. code-block:: none

  # cat /var/ossec/logs/alerts/alerts.log | /var/ossec/bin/ossec-reportd 2>&1 | more
  2011/07/11 21:01:36 ossec-reportd: INFO: Started (pid: 1444).
  2011/07/11 21:01:41 ossec-reportd: INFO: Report completed. Creating output...

  Report completed. ==
  ------------------------------------------------
  ->Processed alerts: 17
  ->Post-filtering alerts: 17
  ->First alert: 2011 Jul 11 00:00:46
  ->Last alert: 2011 Jul 11 00:16:52


  Top entries for 'Username':
  ------------------------------------------------
  _nrpe                                           |6       |
  SYSTEM                                          |2       |


  Top entries for 'Level':
  ------------------------------------------------
  Severity 3                                      |13      |
  Severity 2                                      |4       |


  Top entries for 'Group':
  ------------------------------------------------
  syslog                                          |10      |
  sudo                                            |6       |
  dropbearrecon                                   |4       |
  ossec                                           |4       |
  sshd                                            |4       |
  authentication_success                          |2       |
  windows                                         |2       |
  clamd                                           |1       |
  freshclam                                       |1       |
  virus                                           |1       |


  Top entries for 'Location':
  ------------------------------------------------
  ix->/var/log/secure                             |4       |
  ix->ossec-logcollector                          |3       |
  (vistapc) 192.168.17.0->WinEvtLog               |2       |
  buffalo1->/var/log/secure                       |2       |
  buffalo2->/var/log/secure                       |2       |
  (junction) 192.168.17.17->/var/log/secure       |1       |
  (junction) 192.168.17.17->ossec-logcollector    |1       |
  ix->/var/log/local6                             |1       |
  junction->/var/log/secure                       |1       |


  Top entries for 'Rule':
  ------------------------------------------------
  5402 - Successful sudo to ROOT executed         |6       |
  51006 - Client exited before authentication.    |4       |
  591 - Log file rotated.                         |4       |
  18107 - Windows Logon Success.                  |2       |
  52507 - ClamAV database update                  |1       |





