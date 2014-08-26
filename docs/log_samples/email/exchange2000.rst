Exchange Log Samples
--------------------

Here are two different formats of the Exchange 2000 SMTP logs.  

W3C Extended format:
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  #Software: Microsoft Internet Information Services 5.0
  #Version: 1.0
  #Date: 2006-10-09 05:00:15
  #Fields: date time c-ip cs-username s-sitename s-computername s-ip s-port cs-method cs-uri-stem cs-uri-query sc-status sc-win32-status sc-bytes cs-bytes time-taken cs-version cs-host cs(User-Agent) cs(Cookie) cs(Referer) 
  2006-10-09 05:00:15 24.118.118.106 36A42160 SMTPSVC1 MEE-PDC 192.168.1.2 0 HELO - +36A42160 250 0 48 13 0 SMTP - - - -
  2006-10-09 05:00:16 24.118.118.106 36A42160 SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +FROM:+<EldonpyzWestoncusk@sbcglobal.net> 250 0 57 45 0 SMTP - - - -
  2006-10-09 05:00:16 24.118.118.106 36A42160 SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +TO:+<pamb@meelift.com> 250 0 29 27 0 SMTP - - - -
  2006-10-09 05:00:19 24.118.118.106 36A42160 SMTPSVC1 MEE-PDC 192.168.1.2 0 DATA - +<4F5002F2.860022@web.de> 250 0 108 1399 1922 SMTP - - - -
  2006-10-09 05:00:19 24.118.118.106 36A42160 SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - 36A42160 240 6219 68 4 0 SMTP - - - -
  2006-10-09 05:00:42 192.168.1.247 notify.ossec.net SMTPSVC1 MEE-PDC 192.168.1.2 0 HELO - +notify.ossec.net 250 0 47 21 0 SMTP - - - -
  2006-10-09 05:00:42 192.168.1.247 notify.ossec.net SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +From:+<ossecm@HULK> 250 0 36 24 16 SMTP - - - -
  2006-10-09 05:00:42 192.168.1.247 notify.ossec.net SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +To:+<dbveto@meelift.com> 250 0 31 29 0 SMTP - - - -
  2006-10-09 05:00:42 192.168.1.247 notify.ossec.net SMTPSVC1 MEE-PDC 192.168.1.2 0 DATA - <MEE-PDCfSDGAIXWb9DY00001e05@mee-pdc.meelift.com> 250 0 132 29518 62 SMTP - - - -
  2006-10-09 05:00:42 192.168.1.247 notify.ossec.net SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - notify.ossec.net 240 78 68 4 0 SMTP - - - -
  2006-10-09 05:00:50 192.168.1.22 REDBARRON SMTPSVC1 MEE-PDC 192.168.1.2 0 EHLO - +REDBARRON 250 0 275 14 93 SMTP - - - -
  2006-10-09 05:00:50 192.168.1.22 REDBARRON SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +FROM:<Kiwisyslog@meelift.com> 250 0 47 34 0 SMTP - - - -
  2006-10-09 05:00:50 192.168.1.22 REDBARRON SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +TO:<dbveto@meelift.com> 250 0 31 28 0 SMTP - - - -
  2006-10-09 05:00:50 192.168.1.22 REDBARRON SMTPSVC1 MEE-PDC 192.168.1.2 0 DATA - <MEE-PDCccSN00ktmzmV00001e06@mee-pdc.meelift.com> 250 0 132 2413 531 SMTP - - - -
  2006-10-09 05:00:50 192.168.1.22 REDBARRON SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - REDBARRON 240 1015 68 4 0 SMTP - - - -
  2006-10-09 05:01:04 24.95.255.99 - SMTPSVC1 MEE-PDC 192.168.1.2 0 xxxx - +rr.com 500 0 32 11 0 SMTP - - - -
  2006-10-09 05:01:04 24.95.255.99 - SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - - 240 375 68 4 16 SMTP - - - -
  2006-10-09 05:01:19 70.114.247.230 - SMTPSVC1 MEE-PDC 192.168.1.2 0 xxxx - +rr.com 500 0 32 11 0 SMTP - - - -
  2006-10-09 05:01:19 70.114.247.230 - SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - - 240 172 68 4 0 SMTP - - - -
  2006-10-09 05:01:26 24.174.89.177 - SMTPSVC1 MEE-PDC 192.168.1.2 0 xxxx - +rr.com 500 0 32 11 0 SMTP - - - -
  2006-10-09 05:01:26 24.174.89.177 - SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - - 240 188 68 4 0 SMTP - - - -
  2006-10-09 05:01:33 80.64.22.8 - SMTPSVC1 MEE-PDC 192.168.1.2 0 xxxx - +sveta 500 0 32 10 0 SMTP - - - -
  2006-10-09 05:01:33 80.64.22.8 sveta SMTPSVC1 MEE-PDC 192.168.1.2 0 HELO - +sveta 250 0 44 10 0 SMTP - - - -
  2006-10-09 05:01:33 80.64.22.8 sveta SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +FROM:<malaquias@fu-berlin.de> 250 0 47 34 0 SMTP - - - -
  2006-10-09 05:01:33 80.64.22.8 sveta SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +TO:<heyrmanmheyrman@meelift.com> 250 0 40 37 0 SMTP - - - -
  2006-10-09 05:01:37 80.64.22.8 sveta SMTPSVC1 MEE-PDC 192.168.1.2 0 DATA - +<000b01c6eb60$0511fad0$4507a8c0@sveta> 250 0 122 22786 3297 SMTP - - - -
  2006-10-09 05:01:37 80.64.22.8 sveta SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - sveta 240 4735 68 4 0 SMTP - - - -
  2006-10-09 05:02:11 71.127.86.239 isyndicate.com SMTPSVC1 MEE-PDC 192.168.1.2 0 HELO - +isyndicate.com 250 0 47 19 0 SMTP - - - -
  2006-10-09 05:02:11 71.127.86.239 isyndicate.com SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +FROM:<grazia@isyndicate.com> 250 0 46 33 0 SMTP - - - -
  2006-10-09 05:02:11 71.127.86.239 isyndicate.com SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +TO:<jgrub@meelift.com> 250 0 30 27 0 SMTP - - - -
  2006-10-09 05:02:11 71.127.86.239 isyndicate.com SMTPSVC1 MEE-PDC 192.168.1.2 0 DATA - +<000001c6eb5f$c56726d0$8c12a8c0@usbty> 250 0 122 1754 406 SMTP - - - -
  2006-10-09 05:02:11 71.127.86.239 isyndicate.com SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - isyndicate.com 240 500 68 4 0 SMTP - - - -
  2006-10-09 05:02:46 72.185.9.146 - SMTPSVC1 MEE-PDC 192.168.1.2 0 xxxx - +cpe-72-185-9-146.tampabay.res.rr.com 500 0 32 41 0 SMTP - - - -
  2006-10-09 05:02:46 72.185.9.146 - SMTPSVC1 MEE-PDC 192.168.1.2 0 QUIT - - 240 125 32 41 62 SMTP - - - -
  2006-10-09 05:03:13 83.34.136.228 altimaxns.com SMTPSVC1 MEE-PDC 192.168.1.2 0 HELO - +altimaxns.com 250 0 47 18 0 SMTP - - - -
  2006-10-09 05:03:13 83.34.136.228 altimaxns.com SMTPSVC1 MEE-PDC 192.168.1.2 0 MAIL - +FROM:<veste@altimaxns.com> 250 0 44 31 0 SMTP - - - -
  2006-10-09 05:03:13 83.34.136.228 altimaxns.com SMTPSVC1 MEE-PDC 192.168.1.2 0 RCPT - +TO:<jheyrman@meelift.com> 250 0 33 30 0 SMTP - - - -

NCSA format:
^^^^^^^^^^^^

.. code-block:: console

  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:16:39 -0600] "- -?220-rly-yi06.mx.aol.com+ESMTP+mail_relay_in-yi6.1;+Wed,+11+Oct+2006+14:16:38+-0400 SMTP" 0 82
  205.188.158.121 - OutboundConnectionCommand [11/Oct/2006:13:16:39 -0600] "EHLO -?mee-pdc.meelift.com SMTP" 0 4
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:16:39 -0600] "- -?250-rly-yi06.mx.aol.com+207-250-64-66.static.twtelecom.net SMTP" 0 58
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:40 -0600] "HELO -?+207.250.64.66 SMTP" 250 46
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:41 -0600] "MAIL -?+FROM:+<Keith@boardermail.com> SMTP" 250 46
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:41 -0600] "RCPT -?+TO:+<s-r_kke@meelift.com> SMTP" 250 32
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:42 -0600] "RCPT -?+TO:+<s-r_mke@meelift.com> SMTP" 250 32
  83.44.189.146 - 1stallied.com [11/Oct/2006:13:16:43 -0600] "HELO -?+1stallied.com SMTP" 250 47
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:43 -0600] "RCPT -?+TO:+<dbveto@meelift.com> SMTP" 250 31
  83.44.189.146 - 1stallied.com [11/Oct/2006:13:16:43 -0600] "MAIL -?+FROM:<penwine@1stallied.com> SMTP" 250 46
  83.44.189.146 - 1stallied.com [11/Oct/2006:13:16:43 -0600] "RCPT -?+TO:<rcutsforth@meelift.com> SMTP" 250 35
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:44 -0600] "RCPT -?+TO:+<pamb@meelift.com> SMTP" 250 29
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:44 -0600] "RCPT -?+TO:+<tom@meelift.com> SMTP" 250 28
  83.44.189.146 - 1stallied.com [11/Oct/2006:13:16:45 -0600] "DATA -?+<000001c6ed61$33a7e690$97cfa8c0@edvhaov> SMTP" 250 124
  83.44.189.146 - 1stallied.com [11/Oct/2006:13:16:45 -0600] "QUIT -?1stallied.com SMTP" 240 68
  65.214.43.171 - - [11/Oct/2006:13:16:47 -0600] "xxxx -?+armin.techtarget.com SMTP" 500 32
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:47 -0600] "RCPT -?+TO:+<tkappers@meelift.com> SMTP" 250 33
  65.214.43.171 - armin.techtarget.com [11/Oct/2006:13:16:48 -0600] "HELO -?+armin.techtarget.com SMTP" 250 47
  65.214.43.171 - armin.techtarget.com [11/Oct/2006:13:16:49 -0600] "MAIL -?+FROM:<567507-dbveto=meelift.com@lists.techtarget.com> SMTP" 250 71
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:50 -0600] "DATA -?+<10100.marigold@cleat> SMTP" 250 106
  61.47.65.115 - 207.250.64.66 [11/Oct/2006:13:16:50 -0600] "QUIT -?207.250.64.66 SMTP" 240 68
  65.214.43.171 - armin.techtarget.com [11/Oct/2006:13:16:51 -0600] "RCPT -?+TO:<dbveto@meelift.com> SMTP" 250 31
  81.196.176.167 - - [11/Oct/2006:13:16:54 -0600] "xxxx -?+81-196-176-167.rdsnet.ro SMTP" 500 32
  81.196.176.167 - 81-196-176-167.rdsnet.ro [11/Oct/2006:13:16:54 -0600] "HELO -?+81-196-176-167.rdsnet.ro SMTP" 250 48
  81.196.176.167 - 81-196-176-167.rdsnet.ro [11/Oct/2006:13:16:55 -0600] "MAIL -?+FROM:<sshambeau@meelift.com> SMTP" 250 46
  81.196.176.167 - 81-196-176-167.rdsnet.ro [11/Oct/2006:13:16:55 -0600] "RCPT -?+TO:<sshambeau@meelift.com> SMTP" 250 34
  81.196.176.167 - 81-196-176-167.rdsnet.ro [11/Oct/2006:13:16:56 -0600] "DATA -?+<000901c6ed61$6e8f3f10$0271aa58@ktcysfoh> SMTP" 250 125
  81.196.176.167 - 81-196-176-167.rdsnet.ro [11/Oct/2006:13:16:56 -0600] "QUIT -?81-196-176-167.rdsnet.ro SMTP" 240 68
  205.188.158.121 - OutboundConnectionCommand [11/Oct/2006:13:17:02 -0600] "MAIL -?FROM:<pbourque@meelift.com> SMTP" 0 4
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:17:02 -0600] "- -?250+OK SMTP" 0 6
  205.188.158.121 - OutboundConnectionCommand [11/Oct/2006:13:17:02 -0600] "RCPT -?TO:<kbee923@aol.com> SMTP" 0 4
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:17:02 -0600] "- -?250+OK SMTP" 0 6
  205.188.158.121 - OutboundConnectionCommand [11/Oct/2006:13:17:02 -0600] "DATA - SMTP" 0 4
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:17:02 -0600] "- -?354+START+MAIL+INPUT,+END+WITH+"."+ON+A+LINE+BY+ITSELF SMTP" 0 54
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:17:04 -0600] "- -?250+OK SMTP" 0 6
  205.188.158.121 - OutboundConnectionCommand [11/Oct/2006:13:17:04 -0600] "QUIT - SMTP" 0 4
  205.188.158.121 - OutboundConnectionResponse [11/Oct/2006:13:17:04 -0600] "- -?221+SERVICE+CLOSING+CHANNEL SMTP" 0 27
  217.169.41.109 - outbound.emediausa.com [11/Oct/2006:13:17:13 -0600] "HELO -?+outbound.emediausa.com SMTP" 250 48
  217.169.41.109 - outbound.emediausa.com [11/Oct/2006:13:17:17 -0600] "MAIL -?+FROM:<Subscriber.108049.Bulletins@eb.emediaUSA.com> SMTP" 250 69
  217.169.41.109 - outbound.emediausa.com [11/Oct/2006:13:17:17 -0600] "RCPT -?+TO:<dbveto@meelift.com> SMTP" 250 3


