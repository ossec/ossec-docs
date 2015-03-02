

Storing alerts as JSON
=========================

.. note::

   This feature first appeared in OSSEC 2.9.


Sometimes you want to easily consume OSSEC alerts in other programs.
With the json output, you can write alerts as a newline separated json file which other programs can easily consume.

For example, you can pair OSSEC with logstash-forwarder to effortlessly export your alerts to logstash, elasticsearch, and kibana (ELK).

This can provide the simplest method of exporting the entire alert message to other programs without any limitations or dependencies. For example the syslog output can write json, but is limited to the maximum syslog message size and excludes the full_log information like integrity checking diffs. You also do not need syslog, zeromq or any other dependencies.


Configuration
-------------

Turning it on or off is easy as setting a single configuration parameter in the ossec.conf.
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

.. code-block:: console 

    # tail /var/ossec/logs/alerts/alerts.json


You will still have the legacy alerts.log and any custom log formats you've created will remain.
The files are md5 and sha1 checksummed and compressed once daily (just like the legacy alerts.log).

That's it. 

