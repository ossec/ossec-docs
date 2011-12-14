How to add multiple log files to be monitored?
----------------------------------------------

By `Daniel B. Cid <http://www.ossec.net/dcid>`_

For Unix Agents
^^^^^^^^^^^^^^^

If you have multiple log files to be monitored by OSSEC and don't 
want to add each one of them manually, you can configure them using 
posix regular expressions. 

For example, if you have a directory structure like this: 

.. code-block:: console

  /var/log/host1/xx.log, yy.log, zz.log
  /var/log/host2/xx.log, aa.log
  /var/log/host3/zz.log, abc.log
  /var/log/hostn/bb.log, xyz.log

You can just add one entry in the localfile to monitor all these logs:
.. code-block:: console

  <localfile>
   <log_format>syslog</log_format>
   <location>/var/log/host*/*.log</location>
  </localfile>

This tip can make large configurations much simpler.

For Windows Agents
^^^^^^^^^^^^^^^^^^

For the Windows agent, the built-in globing doesn't work. At time of writing (OSSEC version 1.5) you have to use a script to auto-generate ``ossec.conf`` if you want to monitor many log files without having to manually enter them. Here's an example batch file to get you started:

.. code-block:: console
  @echo off

  set targetfile="C:\Program Files\ossec-agent\ossec.conf"

  copy "%~dp0\ossec_template.conf" %targetfile%

  echo ^<ossec_config^> >> %targetfile%
  echo. >> %targetfile%
  for /D %%l in (D:\Logs\W3SVC*) do echo ^<localfile^>^<location^>%%l\ex%%y%%m%%d.log^</location^>^<log_format^>iis^</log_format^>^</localfile^> >> %targetfile%
  echo ^</ossec_config^> >> %targetfile%
  net stop "OSSEC Hids"
  net start "OSSEC Hids"

Adjust the "for..in" globbing line as needed. In this example, I'm monitoring logs for multiple IIS sites which are all in D:\Logs. Save it into a file with a .bat extension and put it somewhere on your hard drive. Create a file named ``ossec_template.conf`` in the **`same directory** as the batch file. You can probably just copy your current ``ossec.conf`` for this file, as this script will only append to it. You can then set up a scheduled task to run the batch file to automatically keep your ossec.conf up to date. 

.. note:

  This will overwrite your ``ossec.conf`` every time it is run, so make sure that you make all your changes in your ``ossec_template.conf`` file.


