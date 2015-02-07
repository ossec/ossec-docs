OSSEC and Splunk


Here's how I configured OSSEC to send alerts to Splunk:

In ossec.conf add a syslog_output block specifying your Splunk system IP address and the port your network input is listening on:

  <syslog_output>
    <server>172.10.2.3</server>
    <port>10002</port>
  </syslog_output>


Now you need to enable the syslog_output module and restart OSSEC:

  #/var/ossec/bin/ossec-control enable client-syslog
  #/var/ossec/bin/ossec-control restart

On restart you'll see ossec-csyslogd starting up. Now for the Splunk side.


You have a few options on how to receive OSSEC alerts. The two options I've looked at are a standard Splunk network input or syslog-ng. I would suggest using syslog-ng and either the FIFO or file destination method. This way when you need to restart Splunk, which can be rather frequent, you won't lose events like you would with the Splunk network input. The Splunk for OSSEC application uses the network input method for simplicity.


Grab the Splunk for OSSEC app which can be found here: http://www.splunkbase.com/apps/All/Security/app:Splunk+for+OSSEC#.



The OSSEC app for  is currently designed for SPLUNK 3.x. There is a work around. Install it in  SPLUNK, then use the SPLUNK Search tool, and the OSSEC dashboards are all there. (it works) 

One other addition: 

When you edit the opt/splunk/etc/system/local/inputs.conf  file
Splunk is happier when you add the host listing on line 3 of the file below, else it thinks you have two ossec servers...


[default]

host = mymachine

mymachine=10.1.100.141

[udp://10.1.100.141:10002]

disabled=false

sourcetype=ossec


The .spl is actually just a .tgz so all you need to do is extract it to $SPLUNK_HOME/etc/apps/.


Make sure you update any local or network firewalls that this communication is traversing and then restart Splunk.

  #$SPLUNK_HOME/bin/splunk restart

If you have any tweaks or improvements to configuration or the Splunk for OSSEC app please let me know! (canuck.eh[at]gmail[dot]com)


