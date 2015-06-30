.. _faq_ar:

Active Response: FAQ
--------------------

.. contents:: 
    :local:


What is the scope of AR commands?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be a little confusing.

There is no native capability to express active-response
actions that execute **only** on the agent that originated
the rule-matching log line.

That is, if you want the agent web12.example.com to run
the AR command foo.sh when rule 23431 matches a log line that
only originated **at agent web12**, you cannot do it generically.
You would have to duplicate rule 23431 (say 23432) and make
sure the regex was such that rule 23432 would only match
if the log line originated at web12.example.com.

The following will execute the command do-something-with-local-file
on **all agents** when a log line from **any** agent matches the
built-in rule 550::

  <active-response>
    <command>do-something-with-local-file</command>
    <location>local</location>
    <rules_id>550</rules_id>
  </active-response>

The following will execute the command do-something-with-local-file
on **agent 032** when a log line from **any** agent matches the
built-in rule 550::

  <active-response>
    <command>do-something-with-local-file</command>
    <location>defined_agent</location>
    <agent_id>032</agent_id>
    <rules_id>550</rules_id>
  </active-response>

As you can see from this last example, doing something on a
host-local file (like /etc/passwd) due to rule 550 matching
a log line from an agent other than 032 is pretty odd and likely
unwanted.

**Workaround #1**: If you have a small number of agents (and
only those agents) that should take a certain action based on
a rule matching a log line from that respective agent, you
could define custom rules to suit the need. So if you want
to run "do-something-with-local-file" on agent 032 when
a rule is hit with origin of agent 032, you would
define that new rule as such::

  <rule id="999999" level="1">
    <match>myhosthere: some string to find</match>
    <description>Do my thing</description> 
  </rule>

and define the active-response as::

  <active-response>
    <command>do-something-with-local-file</command>
    <location>defined_agent</location>
    <agent_id>032</agent_id>
    <rules_id>999999</rules_id>
  </active-response>

**Workaround #2**: Add logic to your AR command (script) that
exits early if the srcip argument passed in does not match your
agent's IP address. This is not technically ideal, as the script is
still going to execute on all specified agents, but on agents where
the srcip does not match the agent's IP address, the script will
short-circuit early and do no real work before exiting.

The active-response block may look like this::

  <active-response>
    <command>do-something-with-local-file</command>
    <location>local</location>
    <rules_id>550</rules_id>
  </active-response>

Something like this (in bash)::

  #!/bin/sh
  #
  # Expect: srcip

  ACTION=$1
  USER=$2
  IP=$3
  LOCAL=`dirname $0`
  cd $LOCAL
  cd ../
  PWD=`pwd`

  # Logging the call
  echo "`date` $0 $1 $2 $3 $4 $5" >> ${PWD}/../logs/active-responses.log

  # IP Address must be provided
  if [ "x${IP}" = "x" ]; then
     echo "$0: Missing argument <action> <user> (ip)" 
     exit 1
  fi

  # Warning: 'hostname -i' May not work on non-Linux
  LOCAL_IPADDRESS=`hostname -i`

  if [ $IP = $LOCAL_IPADDRESS ]; then
    # My actual code here that will only run on this agent!
    # ...
    exit 0
  fi

  exit 1
