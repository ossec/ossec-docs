Web Scan sample 2
  -----------------

Example of web scan detected by ossec (looking for Wordpress, xmlrpc and awstats):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Mar 23 19:57:38

  Received From: teletubbies->/var/log/httpd/error_log
  Rule: 30114 fired (level 10) -> "Multiple attempts to access non-existent files (web scan) from same source."
  Portion of the log(s):

  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/wordpress
  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/b2evo
  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/b2
  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/blogtest
  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/blog
  [Fri Mar 23 19:57:37 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/blogs
  [Fri Mar 23 19:57:36 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/community
  [Fri Mar 23 19:57:33 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/drupal
  [Fri Mar 23 19:57:30 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/blog
  [Fri Mar 23 19:57:30 2007] [error] [client 207.44.184.96] File does not exist: /var/www/html/xmlsrv



 --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2007 Mar 23 19:57:38

  Received From: teletubbies->/var/log/httpd/access_log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /b2/xmlsrv/xmlrpc.php HTTP/1.0" 404 297 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /blogtest/xmlsrv/xmlrpc.php HTTP/1.0" 404 303 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /blog/xmlsrv/xmlrpc.php HTTP/1.0" 404 299 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /blogs/xmlsrv/xmlrpc.php HTTP/1.0" 404 300 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /blogs/xmlrpc.php HTTP/1.0" 404 293 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:36 -0300] "GET /community/xmlrpc.php HTTP/1.0" 404 297 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:33 -0300] "GET /drupal/xmlrpc.php HTTP/1.0" 404 294 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:30 -0300] "GET /blog/xmlrpc.php HTTP/1.0" 404 292 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:30 -0300] "GET /xmlsrv/xmlrpc.php HTTP/1.0" 404 294 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:30 -0300] "GET /xmlrpc/xmlrpc.php HTTP/1.0" 404 294 "-" "-"



 --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2007 Mar 23 19:57:38

  Received From: teletubbies->/var/log/httpd/access_log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /scripts/awstats.pl HTTP/1.0" 404 295 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /scgi/awstats/awstats.pl HTTP/1.0" 404 300 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /cgi/awstats/awstats.pl HTTP/1.0" 404 299 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /scgi-bin/awstats/awstats.pl HTTP/1.0" 404 304 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /cgi-bin/awstats/awstats.pl HTTP/1.0" 404 303 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /awstats/awstats.pl HTTP/1.0" 404 295 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /scgi-bin/awstats.pl HTTP/1.0" 404 296 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /cgi/awstats.pl HTTP/1.0" 404 291 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /cgi-bin/awstats.pl HTTP/1.0" 404 295 "-" "-"
  207.44.184.96 - - [23/Mar/2007:19:57:37 -0300] "GET /phpgroupware/xmlrpc.php HTTP/1.0" 404 300 "-" "-"



 --END OF NOTIFICATION




Web scan sample 4:
^^^^^^^^^^^^^^^^^^

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Aug 15 15:50:43

  Received From: xx->/var/log/httpd/error_log
  Rule: 30114 fired (level 10) -> "Multiple attempts to access non-existent files (web scan) from same source."
  Portion of the log(s):

  [Wed Aug 15 15:50:42 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/phpadmin
  [Wed Aug 15 15:50:42 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/mysqladmin
  [Wed Aug 15 15:50:42 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/phpmyadmin2
  [Wed Aug 15 15:50:41 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/phpMyAdmin 2.6.4-rc1
  [Wed Aug 15 15:50:41 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/admin
  [Wed Aug 15 15:50:40 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/web
  [Wed Aug 15 15:50:40 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/dbadmin
  [Wed Aug 15 15:50:40 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/db
  [Wed Aug 15 15:50:40 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/admin
  [Wed Aug 15 15:50:39 2007] [error] [client 202.143.138.46] File does not exist: /var/www/html/mysql



 --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2007 Aug 15 15:50:43

  Received From: xx->/var/log/httpd/access_log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  202.143.138.46 - - [15/Aug/2007:15:50:42 -0300] "GET /mysqladmin/read_dump.php HTTP/1.1" 404 285 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:42 -0300] "GET /phpmyadmin2/read_dump.php HTTP/1.1" 404 286 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:41 -0300] "GET /phpMyAdmin%202.6.4-rc1/read_dump.php HTTP/1.1" 404 295 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:41 -0300] "GET /admin/phpmyadmin/read_dump.php HTTP/1.1" 404 291 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:41 -0300] "GET /admin/pma/read_dump.php HTTP/1.1" 404 284 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:40 -0300] "GET /web/phpMyAdmin/read_dump.php HTTP/1.1" 404 289 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:40 -0300] "GET /dbadmin/read_dump.php HTTP/1.1" 404 282 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:40 -0300] "GET /db/read_dump.php HTTP/1.1" 404 277 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:40 -0300] "GET /admin/read_dump.php HTTP/1.1" 404 280 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"
  202.143.138.46 - - [15/Aug/2007:15:50:39 -0300] "GET /mysql/read_dump.php HTTP/1.1" 404 280 "-" "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)"



SSHD brute force:
^^^^^^^^^^^^^^^^^

Example of a SSHD brute force attack.

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Jun 26 17:40:29

  Received From: xx->/var/log/secure
  Rule: 5712 fired (level 10) -> "SSHD brute force trying to get access to the system."
  Portion of the log(s):

  Jun 26 17:40:27 xx sshd[7629]: Failed password for invalid user admin from 61.146.178.13 port 42107 ssh2
  Jun 26 17:40:25 xx sshd[7629]: Invalid user admin from 61.146.178.13
  Jun 26 17:40:23 xx sshd[7625]: Failed password for invalid user admin from 61.146.178.13 port 41983 ssh2
  Jun 26 17:40:20 xx sshd[7625]: Invalid user admin from 61.146.178.13
  Jun 26 17:40:18 xx sshd[7621]: Failed password for invalid user guest from 61.146.178.13 port 41889 ssh2
  Jun 26 17:40:15 xx sshd[7621]: Invalid user guest from 61.146.178.13
  Jun 26 17:40:14 xx sshd[7617]: Failed password for invalid user test from 61.146.178.13 port 41797 ssh2


  OSSEC HIDS Notification.
  2007 Jun 25 15:53:47

  Received From: xx->/var/log/secure
  Rule: 5712 fired (level 10) -> "SSHD brute force trying to get access to the system."
  Portion of the log(s):

  Jun 25 15:53:46 xx sshd[15840]: Failed password for invalid user alias from 210.6.69.117 port 56138 ssh2
  Jun 25 15:53:43 xx sshd[15840]: Invalid user alias from 210.6.69.117
  Jun 25 15:53:41 xx sshd[15836]: Failed password for invalid user recruit from 210.6.69.117 port 56031 ssh2
  Jun 25 15:53:39 xx sshd[15836]: Invalid user recruit from 210.6.69.117
  Jun 25 15:53:37 xx sshd[15832]: Failed password for invalid user sales from 210.6.69.117 port 55924 ssh2
  Jun 25 15:53:34 xx sshd[15832]: Invalid user sales from 210.6.69.117
  Jun 25 15:53:32 xx sshd[15828]: Failed password for invalid user staff from 210.6.69.117 port 55820 ssh2




FTP Scan:
^^^^^^^^^

Example of FTP scan detected by monitoring MS FTP logs.

.. code-block:: console
  OSSEC HIDS Notification.
  2006 Oct 19 04:57:59

  Received From: (ftp-server-1) 172.16.1.99->\WINNT\System32\LogFiles\MSFTPSVC1\ex061019.log
  Rule: 11511 fired (level 10) -> "Multiple connection attempts from same source."Portion of the log(s):

  2006-10-19 08:57:53 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:52 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:49 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:47 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:45 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:43 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:41 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:39 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:37 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -



 --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2006 Oct 19 04:57:59

  Received From: (ftp-server-1) 172.16.1.99->\WINNT\System32\LogFiles\MSFTPSVC1\ex061019.log
  Rule: 11510 fired (level 10) -> "FTP brute force (multiple failed logins)."
  Portion of the log(s):

  2006-10-19 08:57:55 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:54 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:52 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:49 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:47 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:45 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -
  2006-10-19 08:57:44 210.11.216.256 - MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]PASS - - 530 1326 0 0 0 FTP - - - -



 --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2006 Oct 19 04:57:59

  Received From: (ftp-server-1) 172.16.1.99->\WINNT\System32\LogFiles\MSFTPSVC1\ex061019.log
  Rule: 11511 fired (level 10) -> "Multiple connection attempts from same source."Portion of the log(s):

  2006-10-19 08:57:55 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:54 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:52 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:49 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:47 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:45 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:43 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:41 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -
  2006-10-19 08:57:39 210.11.216.256 Administrator MSFTPSVC1 FTP-SERVER 172.16.1.99 21 [423]USER Administrator - 331 0 0 0 0 FTP - - - -



Multiple firewall denies on the Windows firewall:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of multiple firewall denies detected.
.. code-block:: console
  Received From: (ossec64) 192.168.2.25->\Windows\pfirewall.log
  Rule: 4151 fired (level 10) -> "Multiple Firewall drop events from same source."
  Portion of the log(s):

  2006-10-17 09:25:03 DROP UDP 192.168.2.190 192.168.2.255 137 137 78 - - - - - - - RECEIVE
  2006-10-17 09:25:01 DROP UDP 192.168.2.190 192.168.2.255 138 138 229 - - - - - - - RECEIVE
  2006-10-17 09:25:00 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:25:00 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:59 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:59 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:59 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:59 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:58 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE
  2006-10-17 09:24:58 DROP UDP 192.168.2.190 192.168.2.255 137 137 96 - - - - - - - RECEIVE

  --END OF NOTIFICATION


Multiple spam attempts:
^^^^^^^^^^^^^^^^^^^^^^^

Example of spam attempts detected (postix log analysis)

.. code-block:: console
  OSSEC HIDS Notification.
  2006 Oct 24 18:46:29

  Received From: (xx) 200.1.2.a->/var/log/maillog
  Rule: 3354 fired (level 12) -> "Multiple misuse of SMTP service (bad sequence of commands)."
  Portion of the log(s):

postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<x@x.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<x@xl.org.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<y@y.org.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<z@l.org.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<a@slala.org.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<b@l.org.br> proto=SMTP helo=<ran-2h991bqbujq>
postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<c@y.org.br> proto=SMTP helo=<ran-2h991bqbujq>


SQL Injection attempt detected:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of an SQL injection detected by ossec:

.. code-block:: console
  OSSEC HIDS Notification.
  2006 Sep 12 09:45:56

  Received From: (spongebob) 1.2.3.4->/usr/pages/xx/logs/access_log
  Rule: 31106 fired (level 12) -> "A web attack returned code 200 (success)."
  Portion of the log(s):

  200.96.104.241 - - [12/Sep/2006:09:44:28 -0300] "GET /modules.php?name=Downloads&d_op=modifydownloadrequest&%20lid=-1%20UNION%20SELECT%200,username,user_id,user_password,name,%20user_email,user_level,0,0%20FROM%20nuke_users HTTP/1.1" 200 9918 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"



 --END OF NOTIFICATION



Internal system possibly compromised with IrnBot:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

http://www.offensivecomputing.net/?q=node/378

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Jan 30 04:38:37

  Received From: (xxx) 2.2.3.4->/usr/local/squid/var/logs/access.log
  Rule: 35051 fired (level 10) -> "Multiple attempts to access forbidden file or directory from same source ip."
  Portion of the log(s):

  1170076710.819    774 x9.68.xx.1 TCP_DENIED/403 1426 GET http://www.matchav.com/deny2/azenv.php - NONE/- text/html
  1170076709.340   2608 x9.68.xx.1 TCP_DENIED/403 1414 GET http://www.proxy.us.pl/azenv.php - NONE/- text/html
  1170076708.126    419 x9.68.xx.1 TCP_DENIED/403 1412 GET http://kaox.php0h.com/azenv.php - NONE/- text/html
  1170076707.123   3129 x9.68.xx.1 TCP_DENIED/403 1422 GET http://www.internetsec.org/azenv.php - NONE/- text/html
  1170076705.993      0 x9.68.xx.1 TCP_DENIED/403 1384 CONNECT www.google.com:80 - NONE/- text/html
  1170076705.198    751 x9.68.xx.1 TCP_DENIED/403 1440 GET http://www.anonymitytest.com/cgi-bin/azenv.pl - NONE/- text/html



 --END OF NOTIFICATION



==Multiple WordPress (blog) comment spam attempts==

Attempts to submit spammer comments to the ossec blog:

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Jun 22 09:02:41

  Received From: xx->/var/log/httpd/xx.access.log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  124.87.40.203 - - [22/Jun/2007:09:02:39 -0300] "POST /dcid/wp-trackback.php?p=9 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:38 -0300] "POST /dcid/wp-trackback.php?p=79 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:37 -0300] "POST /dcid/wp-trackback.php?p=53 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:36 -0300] "POST /dcid/wp-trackback.php?p=5 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:35 -0300] "POST /dcid/wp-trackback.php?p=37 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:31 -0300] "POST /dcid/wp-trackback.php?p=35 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:29 -0300] "POST /dcid/wp-trackback.php?p=26 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:28 -0300] "POST /dcid/wp-trackback.php?p=23 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:27 -0300] "POST /dcid/wp-trackback.php?p=19 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
  124.87.40.203 - - [22/Jun/2007:09:02:26 -0300] "POST /dcid/wp-trackback.php?p=18 HTTP/1.0" 401 464 "" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"




E-mail scan (vpopmail):
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Aug 15 21:22:53

  Received From: mail->/var/log/messages
  Rule: 9952 fired (level 10) -> "POP3 brute force (email harvesting)."
  Portion of the log(s):

  Aug 12 11:52:56 mail vpopmail[4258]: vchkpw-pop3: vpopmail user not found account@:69.3.64.3
  Aug 12 11:52:55 mail vpopmail[4241]: vchkpw-pop3: vpopmail user not found abuse@:69.3.64.3
  Aug 12 11:52:55 mail vpopmail[4228]: vchkpw-pop3: vpopmail user not found abraham@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4208]: vchkpw-pop3: vpopmail user not found abigail@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4203]: vchkpw-pop3: vpopmail user not found abby@:69.3.64.3
  Aug 12 11:52:54 mail vpopmail[4198]: vchkpw-pop3: vpopmail user not found aaron@:69.3.64.3
  Aug 12 11:52:53 mail vpopmail[4191]: vchkpw-pop3: vpopmail user not found spam@:69.3.64.3
  Aug 12 11:52:53 mail vpopmail[4187]: vchkpw-pop3: vpopmail user not found help@:69.3.64.3
  Aug 12 11:52:52 mail vpopmail[4171]: vchkpw-pop3: vpopmail user not found info@:69.3.64.3




File system full:
^^^^^^^^^^^^^^^^^

Not really an attack, but a serious issue if your web server is out of space.


.. code-block:: console
  OSSEC HIDS Notification.
  2007 Aug 16 22:49:38

  Received From: enigma->/var/log/messages
  Rule: 1007 fired (level 7) -> "File system full."
  Portion of the log(s):

  Aug 16 22:49:37 enigma /bsd: uid 1000 on /var/www: file system full



 --END OF NOTIFICATION




Custom SQL injection against ossec.net:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Someone trying our web application to display the latest rules. Of course, it didn't work<br />
(but we return code 200 on all cases).

.. code-block:: console
  OSSEC HIDS Notification.
  2007 Aug 27 21:43:48

  Received From: teletubbies->/var/log/httpd/ossec.access.log
  Rule: 31106 fired (level 12) -> "A web attack returned code 200 (success)."
  Portion of the log(s):

  221.200.107.218 - - [27/Aug/2007:21:43:48 -0300] "GET /rules/?f=decoder.xml'%20and%20user%3E0%20and%20''=' HTTP/1.1" 200 2099 "-" "-"



 --END OF NOTIFICATION




Application being installed:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An alert when an application is installed on Windows. Not always an attack, but may indicate
a computer misuse.

.. code-block:: console
  OSSEC HIDS Notification.
  2008 Aug 27 14:37:36

  Received From: (lili3win) 192.168.2.0->WinEvtLog
  Rule: 18147 fired (level 5) -> "Application Installed."
  Portion of the log(s):

  WinEvtLog: Application: INFORMATION(11707): MsiInstaller: lac: OSSEC64: OSSEC64: Product: Microsoft Office Live Meeting 2007 -- Installation completed successfully. (NULL) (NULL) (NULL)



Virtual machine being shut down:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By monitoring VMware ESX logs, you can get alerts when a virtual machine is stopped:

.. code-block:: console
  OSSEC HIDS Notification.
  2008 Aug 28 15:53:11

  Received From: enigma->/var/log/messages
  Rule: 19120 fired (level 8) -> "Virtual machine state changed to OFF."
  Portion of the log(s):

  [2008-07-26 10:09:56.601 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 
  123898800 info] State Transition (VM_STATE_RECONFIGURING -> VM_STATE_OFF)



