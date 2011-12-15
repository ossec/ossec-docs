Question: How does the decoder.xml relate to the rules?
-------------------------------------------------------

Answer:
^^^^^^^

The decoder.xml file can be used to capture certain bits of information from the logs that ossec is monitoring.  These bits of information can be passed to rules as XML objects.  Take for example, the pair of rules below:

.. code-block:: console

  <rule id="3100" level="0">
    <decoded_as>web-accesslog</decoded_as>
    <category>web-log</category>
    <description>Access log messages grouped.</description>
  </rule>

  <rule id="3101" level="5">
    <if_sid>3100</if_sid>
    <id>^40</id>
    <description>Web server 400 error code.</description>
  </rule>

The first rule acts as a "collector" for specific log messages.  As part of the rule construct, the ``<decoded_as></decoded_as>`` tags are used to determine how the log entry will be decoded, and aspects of it captured.  In this case, it will be a web-accesslog.  The corresponding construct in decoder.xml (shown below) matches the log entry and captures certain parts of the entry to be used later.  

.. code-block:: console

 <decoder name="web-accesslog">
   <type>web-log</type>
   <prematch>^\d+.\d+.\d+.\d+ - </prematch>
   <regex>^(\d+.\d+.\d+.\d+) - \S+ [\S+ -\d+] </regex>
   <regex>"\w+ (\S+) HTTP\S+ (\d+) </regex>
   <order>srcip,url,id</order>
 </decoder>

Looking at the regular expression we can see that the source IP, the URL, and the HTTP Result Code are captured.  The first set of parentheses denotes that this part of the expression is the source IP, the second set denotes the URL, and the last set is the ID code, which for the example is the HTTP result code.  Going back to the second rule above, its construct contains the ``<id></id>`` tags, which, in this case (rule #3101), is used to match a 400 HTTP result code.  Something else worth noting is the multiple <regex> tags in this example.  This is simply done to provide enhanced clarity and preventing lines over 80 characters.  The values inside both tags are concatenated before being processed by ossec.

These regex variables can also be passed to active-response command constructs like the one show below:

.. code-block:: console

  <command>
    <name>host-deny</name>
    <executable>host-deny.sh</executable>
    <expect>srcip</expect>
    <timeout_allowed>yes</timeout_allowed>
  </command>  

The ``<expect></expect>`` tags are used here to specify which variable is expected as an argument to the executable being used for the active-response action.  A list of available variables is shown below:

* location
* hostname
* log_tag
* srcip
* dstip
* srcport
* dstport
* protocol
* action
* user
* dstuser
* id
* command
* url
* data

Not all of these will be available for every decoder type, but you can check the decoder.xml to see which ones are available for which decoders.


.. note::

  If you are creating custom rules to monitor logs, almost all of your editing will occur in the rules files.  The decoder.xml is just another way to make your rules more powerful, pass specific information to your active-response commands.


