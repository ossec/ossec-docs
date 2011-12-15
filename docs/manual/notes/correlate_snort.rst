Correlating multiple snort IDS with ossec
-----------------------------------------

* Taken from `OSSEC blog <http://dcid.me/2006/12/correlating-multiple-snort-ids-with-ossec/>`_ by `Daniel Cid <http://www.dcid.me/>`_


I was asked recently what is the best way to correlate multiple `snort <http://www.snort.org>`_ events with OSSEC. 
The idea would be to generate an ossec alert (by e-mail and possible an active response) 
if a specific number of snort rules are fired from the same source IP address (in any order)..

The easiest way to solve this is by creating a local ossec rule (inside ``local_rules.xml``) to match 
if any of the desired snort signatures are fired:

.. code-block:: console
<rule id="100015" level="6">
  <if_sid>20101</if_sid>
  <decoded_as>snort</decoded_as>
  <id>1:xx|1:yy|1:zz</id>
  <description>Watched snort ids</description>
</rule>

Note that ``1:xx``, ``1:yy`` are the snort ids that you are interested to watch. We use the ``<if_sid>`` to 
make sure that this rule is only tested if it is an IDS event (see rule 20101).

Now, we create another ossec rule with a higher severity that will only be fired if the above rule
(100015) is generated at least 4 times from the same source ip within 3 minutes (180 seconds):

.. code-block:: console

  <rule id="100016" frequency="4" level="10" timeframe="180">
    <if_matched_sid>100015</if_matched_sid>
    <same_source_ip />
    <description>Multiple snort alerts with the watched ids</description>
  </rule>

This idea can be extended to any other log format that you want to monitor.




