Creating Customized Active Responses
------------------------------------

*by `Daniel Cid <http://www.dcid.me/>`_*


OSSEC by default comes with a few active response scripts, but if you ever need to expand them, this 
tutorial can be of help.

As always, learning via examples is easier and faster. We will write a simple active response script to 
e-mail the alert to a specific address.


Creating the command:
^^^^^^^^^^^^^^^^^^^^^

The first thing we need to do is to create a new "command" entry in the ossec config.
.. code-block:: console

  <command>
    <name>mail-test</name>
    <executable>mail-test.sh</executable>
    <timeout_allowed>no</timeout_allowed>
    <expect />
  </command>

Since our script does not need a timeout, we set it to no. We also don't expect any input (like srcip or 
username), so we leave the "expect" tag empty. In the executable tag, we specify the name of the script 
to be executed (it must be inside ``/var/ossec/active-response/bin/`` ).

*If you do need a srcip or username, just add it, eg: ``<expect>srcip</expect>``*


===2- Configure the Active response===

Next, we need to configure ossec to run the active response. In my case, I want to run it on the ossec server 
(so I choose location server) and every time the rule 1002 is fired (see rules_id 1002). You can also specify 
the level or different locations.

.. code-block:: console

  <active-response>
     <command>mail-test</command>
     <location>server</location>
     <rules_id>1002</rules_id>
  </active-response>


Create active response script:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With that done, we can create the active response script. The ``mail-test.sh`` must be inside the 
``/var/ossec/active-response/bin/`` with the execution permissions set.

**What are the arguments are passed to the script?**

* action (delete or add)
* user name (or - if not set)
* src ip (or - if not set)
* Alert id (uniq for every alert)
* Rule id
* Agent name/host/filename

.. code-block:: console

  #!/bin/sh
  # E-mails an alert - copy at /var/ossec/active-response/bin/mail-test.sh
  # Change e-mail ADDRESSS
  # Author: Daniel Cid

  MAILADDRESS="xx@ossec.net"
  ACTION=$1
  USER=$2
  IP=$3
  ALERTID=$4
  RULEID=$5

  LOCAL=`dirname $0`;
  cd $LOCAL
  cd ../
  PWD=`pwd`


  # Logging the call
  echo "`date` $0 $1 $2 $3 $4 $5 $6 $7 $8" >> ${PWD}/../logs/active-responses.log


  # Getting alert time
  ALERTTIME=`echo "$ALERTID" | cut -d  "." -f 1`

  # Getting end of alert
  ALERTLAST=`echo "$ALERTID" | cut -d  "." -f 2`

  # Getting full alert
  grep -A 10 "$ALERTTIME" ${PWD}/../logs/alerts/alerts.log | grep -v ".$ALERTLAST: " -A 10 | mail $MAILADDRESS -s "OSSEC Alert"




Restart OSSEC and test it:
^^^^^^^^^^^^^^^^^^^^^^^^^^

After the configuration is done, you can restart OSSEC and test the configuration. For the above example, 
I can run the logger command to simular a segmentation fault message.

.. code-block:: console
  # /var/ossec/bin/ossec-control restart
  # logger "Segmentation Fault"


You should get in the /var/ossec/logs/active-response.log, the following:

.. code-block:: console
  Fri Jul 27 23:48:31 BRT 2007 /var/ossec/active-response/bin/mail-test.sh add - - 1185590911.25916 1002 /var/log/messages


And in your e-mail:

.. code-block:: console

  from: root <root@xx.org>
  to: xx@ossec.net	 
  date: Jul 27, 2007 11:48 PM	 
  subject: OSSEC Alert	 

  ** Alert 1185590911.25661: mail  - syslog,errors,
  2007 Jul 27 23:48:31 xx->/var/log/messages
  Rule: 1002 (level 7) -> 'Unknown problem somewhere in the system.'
  Src IP: (none)
  User: (none)
  Jul 27 23:48:30 xx dcid: Segmentation Fault 123



