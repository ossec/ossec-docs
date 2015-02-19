

Storing alerts as JSON
=========================

Sometimes you want to easily consume OSSEC alerts in other programs for further analysis or storage.

With the json output, you can write alerts as a newline separated json file which other programs can consume.

For example, you can pair OSSEC with logstash-forwarder to effortlessly export your alerts to logstash, elasticsearch, and kibana (ELK).

This can provide the simplest method of exporting the entire alert message to other programs without any limitations or dependencies. For example the syslog output can write json, but is limited to the maximum syslog message size and excludes the full_log information like integrity checking diffs. You also do not need to install zeromq or any other dependencies.

Turning it on or off is easy as setting a single configuration parameter in the ossec.conf.

Configuration options
---------------------

These configurations options require a server or local installation.


Enabling json output
----------------------

An OSSEC server can be configured to write the alerts in json format. 

File: /var/ossec/logs/ossec.conf

.. code-block:: xml

    <ossec_config>
      <global>
        <jsonout_output>yes</syslog_output>
        ...
      </global>
      ...
    </ossec_config>


After this change is made, the alerts are written to alerts.json side-by-side with the legacy alerts.log file.

Yes, you will still have the legacy alerts.log and any custom log formats you've created will remain.

.. code-block:: console 

    # /var/ossec/logs/alerts/alerts.json


The files are md5 and sha1 checksummed and compressed once daily (just like the legacy alerts.log).

That's it. 