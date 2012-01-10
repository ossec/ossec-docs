Monitoring a command:
---------------------


OSSEC can monitor commands in the same way it monitors log files.






Monitoring the listening ports on a system:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  <ossec_config>
    <localfile>
      <log_format>full_command</log_format>
      <command>netstat -an | grep LISTEN | grep -v '127.0.0.1'</command>
      <frequency>600</frequency>
      <alias>netstat</alias>
    </localfile>
  </ossec_config>


