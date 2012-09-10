
##################
What's new for 2.7
##################


* agent profiles

  * `ossec.conf <../syntax/head_ossec_config.client.html#element-server-ip>`_

  * `agent.conf <../syntax/syntax/head_agent_config.html#element-agent_config_options>`_

* Allow the agents to run remote commands in agent.conf again  `internal_options.conf <../syntax/head_internal_options.analysisd.html#intopt-logcollector.remote_commands=0>`_
 
* New utility: `util.sh <../programs/util.sh.html>`_

* New hybrid mode: server + agent functionality on the same system

* contrib/ossec2rss.php: ossec alerts in an rss format

* GeoIP data in `alerts <../syntax/head_ossec_config.global.rst#geoip_db_path>`_

* License has been updated with the OpenSSL exception

* OSSEC server can be specified by hostname in the agent's ossec.conf `server-hostname <../syntax/head_ossec_config.client.html#element-server-hostname>`_

* ossec-authd can now add IP addresses to the client.keys file instead of using ``any`` with the `-i <../programs/ossec-authd.html#cmdoption-ossec-authd-i>`_


