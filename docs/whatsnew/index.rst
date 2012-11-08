
##################
What's new for 2.7
##################


* agent profiles

  * `ossec.conf <../syntax/head_ossec_config.client.html#element-server-ip>`_

  * `agent.conf <../syntax/head_agent_config.html#element-agent_config_options>`_

* Allow the agents to run remote commands in agent.conf again  `internal_options.conf <../syntax/head_internal_options.analysisd.html#intopt-logcollector.remote_commands=0>`_
 
* New utility: `util.sh <../programs/util.sh.html>`_

* New hybrid mode: server + agent functionality on the same system (NOT REALLY DOCUMENTED, ARE ANY OF THE INSTALLATION TYPES WELL DOCUMENTED?)

* contrib/ossec2rss.php: ossec alerts in an rss format

* GeoIP data in `alerts <../syntax/head_ossec_config.global.html#geoip_db_path>`_

* OSSEC server can be specified by hostname in the agent's ossec.conf `server-hostname <../syntax/head_ossec_config.client.html#element-server-hostname>`_

* ossec-authd can now add IP addresses to the client.keys file instead of using ``any`` with `the -i flag <../programs/ossec-authd.html#cmdoption-ossec-authd-i>`_ from Jason Stelzer

* support for prelink to reduce false positives `refilter_cmd <../syntax/head_ossec_config.syscheck.html>`_

* Added knowbs to turn on or off rootcheck features `check_* <../syntax/head_ossec_config.syscheck.html>`_

* Added support for json and splunk output (along with syslog and cef) `format <../syntax/head_ossec_config.syslog_output.html>`_

* Changed ``-f`` to ``-v`` in ossec-logtest

* Added ``-f`` to manage_agents to create agent keys in bulk


