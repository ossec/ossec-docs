
Log Samples from sshd
---------------------

If the system is using pam, authentication events from sshd may also be logged in the `pam format <../auth/pam.html>`_

Always make sure to disable DNS lookup to have the IP address logged instead of the hostname (sshd_config):

.. code-block:: console

  UseDNS no



Did not receive identification string (occurs during some forms of sshd DoS):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Mar  8 06:08:23 stamina sshd[7713]: Did not receive identification string from 190.97.xx.199
  Mar  8 06:08:26 stamina sshd[7758]: Did not receive identification string from 190.97.xx.199
  Mar  8 06:08:26 stamina sshd[7739]: Did not receive identification string from 190.97.xx.199
  Mar  8 06:08:27 stamina sshd[7770]: Did not receive identification string from 190.97.xx.199


Rule to catch multiple instances (insert into local_rules.xml):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

  <rule id="100031" level="10" frequency="4" timeframe="360">
    <if_matched_sid>5706</if_matched_sid>
    <description>Possible DDoS attempt </description>
    <description>(high number of non-existent identification strings).</description>
  </rule>



Software caused connection abort (occurs during some forms of sshd DoS):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Mar  8 06:09:56 stamina sshd[82181]: error: accept: Software caused connection abort
  Mar  8 06:13:11 stamina sshd[82181]: error: accept: Software caused connection abort
  Mar  8 06:13:42 stamina sshd[82181]: error: accept: Software caused connection abort


Rule to help OSSEC recognise this error as nothing serious:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  <rule id="100032" level="0">
    <if_sid>5700</if_sid>
    <match>Software caused connection abort</match>
    <description>Software caused connection abort.</description>
  </rule>



Login sucessful:
^^^^^^^^^^^^^^^^

.. code-block:: console

  May 21 20:22:28 slacker2 sshd[8813]: Accepted password for root from 192.168.20.185 port 1066 ssh2
  May 21 20:22:28 sol2 sshd[23857]: [ID 702911 auth.notice] User test1, coming from 192.168.2.185,  -  authenticated.
  Oct 11 08:05:46 hostname auth|security:info sshd[323808]: Accepted publickey for usr1 from 2.3.4.5 port 37909 ssh2


Login failed:
^^^^^^^^^^^^^

.. code-block:: console

  May 21 20:22:28 slacker sshd[21487]: Failed password for root from 192.168.20.185 port 1045 ssh2



Invalid user login attempt:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jul  7 10:51:24 chaves sshd[19537]: Invalid user admin from spongebob.lab.ossec.net
  Jul  7 10:53:24 chaves sshd[12914]: Failed password for invalid user test-inv from spongebob.lab.ossec.net
  Jul  7 10:53:24 kiko sshd[3251]: User dcid not allowed because listed in DenyUsers



Full scan sample:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  Aug  1 18:27:45 knight sshd[20325]: Illegal user test from 218.49.183.17
  Aug  1 18:27:46 knight sshd[20325]: Failed password for illegal user test from 218.49.183.17 port 48849 ssh2
  Aug  1 18:27:46 knight sshd[20325]: error: Could not get shadow information for NOUSER
  Aug  1 18:27:48 knight sshd[20327]: Illegal user guest from 218.49.183.17
  Aug  1 18:27:49 knight sshd[20327]: Failed password for illegal user guest from 218.49.183.17 port 49090 ssh2
  Aug  1 18:27:49 knight sshd[20327]: error: Could not get shadow information for NOUSER
  Aug  1 18:27:52 knight sshd[20329]: Failed password for admin from 218.49.183.17 port 49266 ssh2
  Aug  1 18:27:56 knight sshd[20331]: Failed password for admin from 218.49.183.17 port 49468 ssh2
  Aug  1 18:27:58 knight sshd[20334]: Illegal user user from 218.49.183.17
  Aug  1 18:27:59 knight sshd[20334]: Failed password for illegal user user from 218.49.183.17 port 49680 ssh2
  Aug  1 18:27:59 knight sshd[20334]: error: Could not get shadow information for NOUSER
  Aug  1 18:28:02 knight sshd[20336]: Failed password for root from 218.49.183.17 port 49869 ssh2
  Aug  1 18:28:05 knight sshd[20347]: Failed password for root from 218.49.183.17 port 50063 ssh2
  Aug  1 18:28:12 knight sshd[20349]: Failed password for root from 218.49.183.17 port 50245 ssh2
  Aug  1 18:28:14 knight sshd[20352]: Illegal user test from 218.49.183.17
  Aug  1 18:28:19 knight sshd[20352]: Failed password for illegal user test from 218.49.183.17 port 50671 ssh2
  Aug  1 18:28:19 knight sshd[20352]: error: Could not get shadow information for NOUSER
  Aug  1 18:29:55 knight sshd[20402]: Illegal user test from 218.49.183.17
  Aug  1 18:29:56 knight sshd[20402]: Failed password for illegal user test from 218.49.183.17 port 52244 ssh2
  Aug  1 18:29:56 knight sshd[20402]: error: Could not get shadow information for NOUSER
  Aug  1 18:29:58 knight sshd[20404]: Illegal user guest from 218.49.183.17
  Aug  1 18:30:02 knight sshd[20406]: Illegal user test from 218.49.183.17
  Aug  1 18:30:03 knight sshd[20404]: Failed password for illegal user guest from 218.49.183.17 port 52416 ssh2
  Aug  1 18:30:03 knight sshd[20404]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:03 knight sshd[20406]: Failed password for illegal user test from 218.49.183.17 port 52558 ssh2
  Aug  1 18:30:03 knight sshd[20406]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:05 knight sshd[20439]: Failed password for illegal user guest from 218.49.183.17 port 52818 ssh2
  Aug  1 18:30:05 knight sshd[20439]: Illegal user guest from 218.49.183.17
  Aug  1 18:30:05 knight sshd[20439]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:06 knight sshd[20441]: Failed password for admin from 218.49.183.17 port 52851 ssh2
  Aug  1 18:30:08 knight sshd[20443]: Failed password for admin from 218.49.183.17 port 53014 ssh2
  Aug  1 18:30:09 knight sshd[20445]: Failed password for admin from 218.49.183.17 port 53040 ssh2
  Aug  1 18:30:11 knight sshd[20447]: Failed password for admin from 218.49.183.17 port 53192 ssh2
  Aug  1 18:30:11 knight sshd[20449]: Illegal user user from 218.49.183.17
  Aug  1 18:30:12 knight sshd[20449]: Failed password for illegal user user from 218.49.183.17 port 53230 ssh2
  Aug  1 18:30:12 knight sshd[20449]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:13 knight sshd[20451]: Illegal user user from 218.49.183.17
  Aug  1 18:30:14 knight sshd[20451]: Failed password for illegal user user from 218.49.183.17 port 53404 ssh2
  Aug  1 18:30:14 knight sshd[20451]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:14 knight sshd[20453]: Failed password for root from 218.49.183.17 port 53425 ssh2
  Aug  1 18:30:21 knight sshd[20455]: Failed password for root from 218.49.183.17 port 53571 ssh2
  Aug  1 18:30:22 knight sshd[20457]: Failed password for root from 218.49.183.17 port 53615 ssh2
  Aug  1 18:30:24 knight sshd[20476]: Failed password for root from 218.49.183.17 port 54033 ssh2
  Aug  1 18:30:24 knight sshd[20484]: Failed password for root from 218.49.183.17 port 54078 ssh2
  Aug  1 18:30:26 knight sshd[20488]: Illegal user test from 218.49.183.17
  Aug  1 18:30:27 knight sshd[20486]: Failed password for root from 218.49.183.17 port 54243 ssh2
  Aug  1 18:30:27 knight sshd[20488]: Failed password for illegal user test from 218.49.183.17 port 54285 ssh2
  Aug  1 18:30:27 knight sshd[20488]: error: Could not get shadow information for NOUSER
  Aug  1 18:30:29 knight sshd[20490]: Illegal user test from 218.49.183.17
  Aug  1 18:30:34 knight sshd[20490]: Failed password for illegal user test from 218.49.183.17 port 54423 ssh2
  Aug  1 18:30:34 knight sshd[20490]: error: Could not get shadow information for NOUSER
  Aug  1 18:35:53 knight sshd[20658]: Illegal user test from 218.49.183.17
  Aug  1 18:35:54 knight sshd[20658]: Failed password for illegal user test from 218.49.183.17 port 39604 ssh2
  Aug  1 18:35:54 knight sshd[20658]: error: Could not get shadow information for NOUSER
  Aug  1 18:35:56 knight sshd[20660]: Illegal user guest from 218.49.183.17
  Aug  1 18:35:57 knight sshd[20660]: Failed password for illegal user guest from 218.49.183.17 port 39811 ssh2
  Aug  1 18:35:57 knight sshd[20660]: error: Could not get shadow information for NOUSER
  Aug  1 18:36:00 knight sshd[20664]: Failed password for admin from 218.49.183.17 port 40009 ssh2
  Aug  1 18:36:04 knight sshd[20666]: Failed password for admin from 218.49.183.17 port 40217 ssh2
  Aug  1 18:36:06 knight sshd[20675]: Illegal user user from 218.49.183.17
  Aug  1 18:36:11 knight sshd[20675]: Failed password for illegal user user from 218.49.183.17 port 40470 ssh2
  Aug  1 18:36:11 knight sshd[20675]: error: Could not get shadow information for NOUSER
  Aug  1 18:36:14 knight sshd[20677]: Failed password for root from 218.49.183.17 port 40973 ssh2
  Aug  1 18:36:21 knight sshd[20679]: Failed password for root from 218.49.183.17 port 41159 ssh2
  Aug  1 18:36:24 knight sshd[20681]: Failed password for root from 218.49.183.17 port 41541 ssh2
  Aug  1 18:36:27 knight sshd[20683]: Illegal user test from 218.49.183.17
  Aug  1 18:36:28 knight sshd[20683]: Failed password for illegal user test from 218.49.183.17 port 41630 ssh
  Aug  1 18:36:28 knight sshd[20683]: error: Could not get shadow information for NOUSER



