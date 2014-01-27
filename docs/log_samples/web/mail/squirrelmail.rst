Log samples from SquirrelMail
-----------------------------

SquirrelMail mostly connects with IMAP server 127.0.0.1 and the only one place where is information about client host is the Apache web server log. Successful login returns error code 302 (Found - redirection), unsuccessful login returns error code 200 (OK).

Login successful:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  192.168.1.99 - - [10/Jul/2009:11:30:17 +0200] "POST /webmail/src/redirect.php HTTP/1.0" 302 - "http://my_mail_host/webmail/src/login.php" "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.1) Gecko/20090630 Fedora/3.5-1.fc11 Firefox/3.5"


Login unsuccessful:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  192.168.1.99 - - [09/Jul/2009:15:26:58 +0200] "POST /webmail/src/redirect.php HTTP/1.0" 200 1105 "http://my_mail_host/webmail/src/login.php" "Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.1) Gecko/20090630 Fedora/3.5-1.fc11 Firefox/3.5"


Corresponding lines from /var/log/maillog:

Success:
^^^^^^^^

.. code-block:: console

  Jul 10 11:30:17 srv vpopmail[3676]: vchkpw-webmail: (PLAIN) login success mail_account:127.0.0.1
  Jul 10 11:30:17 srv dovecot: imap-login: Login: user=<mail_account>, method=PLAIN, rip=127.0.0.1, lip=127.0.0.1, secured


Failure:
^^^^^^^^

.. code-block:: console

  Jul  9 15:26:58 srv vpopmail[16745]: vchkpw-webmail: password fail (pass: 'test') mail_account:127.0.0.1
  Jul  9 15:27:00 srv dovecot: imap-login: Aborted login (auth failed, 1 attempts): user=<mail_account>, method=PLAIN, rip=127.0.0.1, lip=127.0.0.1, secured


My local rules:
^^^^^^^^^^^^^^^

.. code-block:: xml

  <group name="squirrelmail,">
    <rule id="131100" level="0">
      <if_sid>31108</if_sid>
      <url>/webmail/src/redirect.php</url>
      <description>Squirrelmail logins grouped.</description>
    </rule>
  
    <rule id="131101" level="1">
      <if_sid>131100</if_sid>
      <id>^302</id>
      <description>Squirrelmail: successfull login.</description>
      <group>authentication_success,</group>
    </rule>
  
    <rule id="131102" level="5">
      <if_sid>131100</if_sid>
      <id>^200</id>
      <description>Squirrelmail: authentication failed.</description>
      <group>authentication_failures,</group>
    </rule>

    <rule id="131103" level="10" frequency="6" timeframe="300">
      <if_matched_sid>131102</if_matched_sid>
      <same_source_ip />
      <description>Squirrelmail brute force attack.</description>
      <group>attack, authentication_failures,</group>
    </rule>
  </group> <!-- SQUIRRELMAIL -->


Separate group "squirrelmail" allowing to get report about webmail logins:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  cat /var/ossec/logs/alerts/alerts.log|/var/ossec/bin/ossec-reportd -f group squirrelmail


