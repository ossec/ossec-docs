.. _manual_rules_decoder_custom:

.. note:: 
    
    This page orgianl was created by @j_hen on her blog http://jentalkstoomuch.blogspot.com/2010/09/writing-custom-ossec-rules-for-your.html


Create Custom decoder and rules 
===============================

OSSEC monitors system logs, checks for rootkits and system configuration changes, 
and does a pretty good job of letting us know what's happening on our systems. 
OSSEC provides a slew of helpful components and rules for commonly-used services, 
but of course, it can't parse our custom log files out-of-the-box. While 
setting our custom rules up, I thought I'd go ahead and document the process, 
as I was having trouble finding a comprehensive beginning-to-end tutorial (this 
will also help me when I forget it later, of course).

Add the log files you want to monitor to ossec.conf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Open up ``/var/ossec/etc/ossec.conf`` and, near the end of the file (before 
``</ossec_config>``), add the following:

.. code-block:: xml 

    <localfile>
      <log_format>syslog</log_format>
      <location>/var/log/my_app_log.log</location>
    </localfile>

I used syslog here as it's recommended for log files that have one entry per line. 
Available values for log_format are syslog, snort-full, snort-fast, squid, iis, 
eventlog (for Windows event logs), mysql_log, postgresql_log, nmapg or apache.

If you're monitoring log files that contain changeable dates, OSSEC understands 
strftime variables, so, for example, if your log file is 
``/var/log/apache2/access.log.2010-09-25``, you can set location to 
``<location>/var/log/apache2/access.log.%Y-%m-%d.``

.. note:: 
    You can render a strftime variable at the command line to verify it quickly. Just 
    type ``date +%X`` at the command line, where X is the stftime variable. ``date +%Y-%m-%d``
    gives us the string we need for our access logs, ``date +%s`` gives us Epoch time UTC.


Create a custom decoder
~~~~~~~~~~~~~~~~~~~~~~~


OSSEC uses decoders to parse log files. After it finds the proper decoder for a log, it 
will parse out fields defined in ``/var/ossec/etc/decoders.xml``, then compare these values 
to values in rule files - and will trigger an alert when values in the deciphered log 
file match values specified in rule files. These values can also be passed to 
active-response commands, if you've got them enabled.

The log line I want to trigger an alert for looks something like this: ::

    2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!


Open up ``/var/ossec/etc/local_decoder.xml`` (you can also use ``decoder.xml``, which 
already exists, but using ``local_decoder.xml`` will assure that you don't overwrite 
it on upgrade). First, we want to create a decoder that will match the first part of 
the log entry. We'll use the date and first few characters to grab it using a regular 
expression. 

.. note::

    Note that OSSEC has its own sort of interpretation of regex, so don't try to get fancy. 
    I spent a lot of time pulling my hair out after using \d{4} type regex syntax - think 
    simpler and you'll have more success: you have to use \d\d\d\d instead.

In the following decoder, we start at the beginning of the line (^), then match the digits 
in YYYY-MM-DD HH:MM:SS. After the date and time, I may have a few different log levels 
listed, INFO, WARN, DEBUG, etc., so I'll just match any number of characters greater 
than 0 (\w+). We also want to end on something relatively unique since the log level 
regex I used is so loosy-goosy, and I know this is a ForceField alert and all ForceField 
alerts will contain ForceField, so I'll use the following.

.. code-block:: xml

    <decoder name="forcefield">
      <prematch>^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d \w+ ForceField</prematch>
    </decoder>

Let's take a break here, and see if this triggers our alert. Save and exit ``local_decoder.xml``, 
then run ``/var/ossec/bin/ossec-logtest``.

When it comes up, paste your log line: ::

    2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield

    **Phase 1: Completed pre-decoding.
    full event: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    hostname: 'my_system'
    program_name: '(null)'
    log: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    **Phase 2: Completed decoding.
    decoder: 'forcefield'

You should see forcefield show up as the decoder. Great! Now, let's parse out the values 
we care about.

Re-open ``local_decoder.xml`` and, beneath your forcefield decoder, create a new decoder:

.. code-block:: xml 

    <decoder name="forcefield-alert">
      <parent>forcefield</parent>
      <regex offset="after_parent">IP:(\d+.\d+.\d+.\d+)@(\w+): (forcefield \w+); (\.*)</regex>
      <order>srcip,url,action,extra_data</order>
    </decoder>

So, what'd we do here?

The obvious stuff first: We gave it a name, and designated forcefield-alert as a child of 
forcefield. Whenever a log matches the forcefield decoder, it'll then be decoded using 
forcefield-alert to extract the data fields to match on.

Now for the fun stuff...First, we set the offset to "``after_parent``" - this means that 
OSSEC starts looking for matches after the 'prematch' stuff (date, time, & ForceField) 
we specified inside the parent forcefield.

So our log line actually looks like this: ::

    2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!

But after extracting the pre-match data, our log line, in OSSEC's brain, looks like this: ::

    IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!

So what do we care about? What fields do we want to test again? A good rule is to decode 
any data that you want to match inside a rule as well as any data you might need to 
initiate an active response. I set these items to bold below: ::

    IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!

OSSEC only allows specific field definitions. These can be found at the top of the 
``local_decoder.xml`` file. For the purposes of our log file, we'll want the IP, 
the script, the action taken by the system, and the additional data. 

When creating the regex for OSSEC, we extract all data inside parenthesis, so we 
build our regex like this: ::

    IP:(\d+.\d+.\d+.\d+)@(\w+): (forcefield \w+); (\.*)

Then, to specify which parenthetical regex is which field, you add the ``<order>`` line, 
using available fields in decoders.xml:

.. code-block:: xml 

    <order>srcip,url,action,extra_data</order>

Save your local_decoder.xml and let's run the log file through ossec-logtest again.

.. code-block:: sh 

    ossec-testrule: Type one log per line.
    2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!
    **Phase 1: Completed pre-decoding.
    full event: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    hostname: 'my_system'
    program_name: '(null)'
    log: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    **Phase 2: Completed decoding.
    decoder: 'forcefield'
    srcip: '127.0.0.1'
    url: 'script_x'
    action: 'forcefield on'
    extra_data: 'enabled forcefield arbitrarily!'

Looks good! It found our decoder and extracted the fields the way we want 'em. Now, 
we're ready to write local rules.

Write custom rules
~~~~~~~~~~~~~~~~~~

Open ``/var/ossec/local_rules.xml`` and add rules. First, we create a group, and a 
"catch-all" rule to run against any log that is decoded by our forcefield decoder. We set 
this as level 0 because we don't want it to trigger an alert:

.. code-block:: xml

    <group name="forcefield">
        <rule id="700005" level="0">
            <decoded_as>forcefield</decoded_as>
            <description>Custom Forcefield Alert</description>
        </rule>
    </group>

Next, we add dependent rules that trigger if the action matches what's specified in the rule. 
<if_sid> specifies the dependency:

.. code-block:: xml 

    <group name="forcefield">
        <rule id="700005" level="0">
            <decoded_as>forcefield</decoded_as>
            <description>Custom Forcefield Alert</description>
        </rule>
        <!-- Alert if forcefield enabled -->
        <rule id="700006" level="12">
            <if_sid>700005</if_sid>
            <action>forcefield on</action>
            <description>Forcefield enabled!</description>
        </rule>
        <!-- Alert if forcefield disabled -->
            <rule id="700007" level="7">
            <if_sid>700005</if_sid>
            <action>forcefield off</action>
            <description>Forcefield off!</description>
        </rule>
        <rule id="700008" level="14">
            <if_sid>700005</if_sid>
            <action>forcefield hyperdrive</action>
            <description>Forcefield in hyperdrive, watch out!</description>
        </rule>
    </group>

Save your local_rules.xml file, and let's test it again:

.. code-block:: sh 

    ossec-testrule: Type one log per line.
    2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!
    **Phase 1: Completed pre-decoding.
    full event: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    hostname: 'my_system'
    program_name: '(null)'
    log: '2010-09-25 15:28:42 WARN ForceField IP:127.0.0.1@script_x: forcefield on; enabled forcefield arbitrarily!'
    **Phase 2: Completed decoding.
    decoder: 'forcefield'
    srcip: '127.0.0.1'
    url: 'script_x'
    action: 'forcefield on'
    extra_data: 'enabled forcefield arbitrarily!'
    **Phase 3: Completed filtering (rules).
    Rule id: '700006'
    Level: '12'
    Description: 'Forcefield enabled!'
    **Alert to be generated.

Cool - now we're ready to restart OSSEC and check alerts. When restarting OSSEC, you 
may find that the new log file that you're using should exist before you restart 
OSSEC--if it doesn't find it, it ignores it. Also, when writing your own rules, 
set levels specific to your OSSEC deployment - for example, if you've enabled active 
response and want to trigger it, make sure you extract the srcip using your decoder 
and set the level in the rule to match the level specific to your active response 
command in ossec.conf.

You'll probably find that you need to do some tuning, and that some of the alerts you 
receive will trigger unwanted alerts if they fall through the decoder sieve. I haven't 
figured out a way to exclude the file from inspection if it fails to match any decoder 
(if you know of one, let me know!), but the solution I've used is to create a new local 
rule that matches based on the syslog sid and match, like so:

.. code-block:: xml 

    <rule id="100009" level="0">
        <if_sid>1002</if_sid>
        <match>Some string in the log I don't want to see</match>
        <description>Don't syslog alert on this one</description>
    </rule>

Repeat for each false positive. It'd be really useful to only allow a single decoder to 
work on a log file - if anyone knows how to do that, let me know!

