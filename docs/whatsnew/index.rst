
##########
What's new
##########

2.8.3
-----

Released November 5, 2015:

.. note::

   This is a bug fix release.

* Fix eventchannel support for Windows agents.
* Fix hybrid mode.

.. include:: checksums/2.8.3/index.trst

2.8.2
-----

Released June 10, 2015:

.. note::

   This is a bug fix release.

* SECURITY fix for CVE-2015-322

2.8.1
-----

Released Sept 9, 2014:

.. note::

   This is a bug fix release.

* SECURITY fix for CVE-2014-5284 found by Jeff Petersen of Roka Security LLC.
* Bug fixes


2.8
---

* Bug fixes
* manage_agents: Added manage_agents -r <id> to remove an agent (awiddersheim)
* Windows: Added eventchannel support for Windows agent on Vista or later (gaelmuller)
* syscheckd: Extended filesize from an integer to a long integer
* Active Response: Fix active-response on MAC OS Firewall (jknockaert)
* Log monitoring/analysis: Add option to allow the outputing of all alerts to a zeromq PUB socket in JSON format, using cJSON library (jrossi, justintime32)
* Log monitoring/analysis: Add TimeGenerated to the output of Windows Event logs (awiddersheim)
* Rules/decoders: Added some additional sshd rules in sshd_rules.xml (joshgarnett)
* Rules/decoders: Removed bro-ids_rules.xml (ddpbsd)
* Removed event ID 676, 672 in msauth_rules.xml (mstarks01)
* contrib: zeromq_pubsub.py - No description (jrossi)
* contrib: ossec-eps.sh, a script to calculate events-per-second (mstarks01)



2.7.1
-----

* Bug fixes
* Extended filesize from an integer to a long integer in syscheck
* Heartbeat interval is now configurable:

  * `notify_time <../syntax/head_ossec_config.client.html#element-notify_time>`_

  * `time-reconnect <../syntax/head_ossec_config.client.html#element-time-reconnect>`_

* `custom_alert_output <../syntax/head_ossec_config.global.html#element-custom_alert_output>`_ added
* ``ip-customblock.sh`` active-response script added
* ossec2snorby scripts added to contrib



2.7
---

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


