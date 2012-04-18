Monitoring a command:
---------------------


OSSEC can monitor commands in the same way it monitors log files.

There are two ``log_format`` options available for commands: ``full_command`` and ``command``.
``full_command`` will treat the entire output of the command as one log message, while ``command`` will treat each line as a separate message.

Knowing about applications listening for network connections is important, and finding out about new applications quickly is something OSSEC can do. We want to check for new open ports on monitored systems, and the ``full_command`` option will make this easy. First we'll create a ``localfile`` of the ``full_command`` type in ``ossec.conf``. Next a rule will have to be created to check the output of the netstat command against the output of the previous netstat command. Any changes will trigger an alert.

The actual command we decided to use was ``netstat -an | grep LISTEN | grep -v '127.0.0.1' | sort -d``. The sort will help keep OSSEC from alerting when the order changes. The options provided to the netstat command in this example are simple and standard, other options might be available and desirable on other systems, for instance the ``-p`` flag on Linux systems. The greps will help us ignore ports that aren't listening on the network. We decide we want to know quickly, but not overload the system so we run the check every ten minutes.

Monitoring the listening ports on a system:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For this command we want to see a list of the listening ports as a single message.

.. code-block:: console

  <ossec_config>
    <localfile>
      <log_format>full_command</log_format>
      <command>netstat -an | grep LISTEN | grep -v '127.0.0.1' | sort -d</command>
      <frequency>600</frequency>
      <alias>netstat</alias>
    </localfile>
  </ossec_config>

The following rule uses the log message provided by the command above, and checks for differences between the current and previous runs. Using the ``<alias>`` option in the command above makes writing the rule a bit easier.

.. code-block:: console

  <rule id="510000" level="10">
    <if_sid>530</if_sid>
    <match>ossec: output: 'netstat'</match>
    <check_diff />
    <description>Listened ports have changed.</description>
  </rule>


An alert from this command shows that something is now listening to 

.. code-block:: console

  ** Alert 1328711914.0: mail  - local,syslog,
  2012 Feb 08 09:38:34 arrakis->netstat
  Rule: 510000 (level 7) -> 'Listened ports have changed.'
  ossec: output: 'netstat':
  tcp          0      0  *.6000                 *.*                    LISTEN
  tcp          0      0  *.22                   *.*                    LISTEN
  tcp6         0      0  *.6000                 *.*                    LISTEN
  tcp6         0      0  ::1.53                 *.*                    LISTEN
  tcp6         0      0  ::1.587                *.*                    LISTEN
  tcp6         0      0  ::1.25                 *.*                    LISTEN
  Previous output:
  ossec: output: 'netstat':
  tcp          0      0  *.6000                 *.*                    LISTEN
  tcp          0      0  *.22                   *.*                    LISTEN
  tcp6         0      0  ::1.53                 *.*                    LISTEN
  tcp6         0      0  *.6000                 *.*                    LISTEN
  tcp6         0      0  ::1.587                *.*                    LISTEN
  tcp6         0      0  ::1.25                 *.*                    LISTEN
  tcp6         0      0  *.22                   *.*                    LISTEN



Just like knowing the which daemons are listening on the network, knowing which applications are installed on an agent can be very useful. New applications being installed on the system without the knowledge of the admins can be a problem. This is a check that probably doesn't need to be run too often.

Check the RPM database for changes in the installed applications:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The defined command will look like the following:

.. code-block:: console

  <ossec_config>
    <localfile>
      <log_format>full_command</log_format>
      <command>rpm -qa | sort -d</command>
      <frequency>3600</frequency>
      <alias>rpmcheck</alias>
    </localfile>
  </ossec_config>

And the corresponding rule:

.. code-block:: console

  <rule id="510001" level="10">
    <if_sid>530</if_sid>
    <match>ossec: output: 'rpmcheck'</match>
    <check_diff />
    <description>Installed packages have changed.</description>
  </rule>



