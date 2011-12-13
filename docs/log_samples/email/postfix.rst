Log Samples for postfix
-----------------------


Postfix internal error:
^^^^^^^^^^^^^^^^^^^^^^^

 postfix/bounce[21172]: fatal: lock file defer 4438F62ECB: Resource temporarily unavailable
 postfix/smtpd[21779]: warning: connect to private/policy: Resource temporarily unavailable
 postfix/smtp[30785]: warning: 75FEC31D36: defer service failure
 postfix/postfix-script: fatal: the Postfix mail system is not running



Email rejected (source blacklisted):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 postfix/smtpd[10419]: NOQUEUE: reject: RCPT from unknown[200.71.50.65]: 554 Service unavailable; Client host [200.71.50.65] blocked using sbl-xbl.spamhaus.org; http://www.spamhaus.org/query/bl?ip=200.71.50.65; from=<kpxbeiu@superig.com.br> to=<cleresilva@lac.ossec.net> proto=SMTP helo=<Static-IP-cr200715065.cable.net.co>

 postfix/smtpd[13496]: NOQUEUE: reject: RCPT from pool-71-121-135-165.sttlwa.dsl-w.verizon.net[71.121.135.165]: 554 Service unavailable; Client host [71.121.135.165] blocked using sbl-xbl.spamhaus.org; http://www.spamhaus.org/query/bl?ip=71.121.135.165; from=<vxznjomowm@directnet.com.br> to=<lala@lac.ossec.net> proto=SMTP helo=<pool-71-121-135-165.sttlwa.dsl-w.verizon.net>


Spam attempts:
^^^^^^^^^^^^^^

 postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<x@x.br> proto=SMTP helo=<ran-2h991bqbujq>

 postfix/smtpd[6741]: NOQUEUE: reject: RCPT from unknown[201.82.55.24]: 503 <nplxfbtk@fbi.com>: Sender address rejected: Improper use of SMTP command pipelining; from=<nplxfbtk@fbi.com> to=<x@xl.org.br> proto=SMTP helo=<ran-2h991bqbujq>


Insufficient storage:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Sep  4 01:14:35 vector postfix/smtpd[15337]: NOQUEUE: reject: MAIL from 89.pool85-60-78.dynamic.orange.es[85.60.78.89]: 452 4.3.1 Insufficient system storage; proto=ESMTP helo=<89.pool85-60-78.dynamic.orange.es>
  Sep  4 02:24:39 vector postfix/smtpd[16863]: NOQUEUE: reject: MAIL from 217-133-56-239.b2b.tiscali.it[217.133.56.239]: 452 4.3.1 Insufficient system storage; proto=ESMTP
helo=<217-133-56-239.b2b.tiscali.it>
  Jun 29 17:28:38 linuxserver postfix/smtpd[27712]: NOQUEUE: reject: MAIL from localhost[127.0.0.1]: 452 Insufficient system storage; proto=ESMTP helo=<localhost>



Some postfix errors:
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Mar 15 06:25:12 mframe1 postfix/postfix-script[23423]: fatal: the Postfix mail system is already running
  Jan 24 06:32:47 mframe1 postfix/smtp[8377]: fatal: unknown service: smtp/tcp
  Jan 14 16:30:24 mframe1 postfix[662]: fatal: usage: postfix [-c config_dir] [-Dv] command
  Jun 20 19:16:46 mframe1 postfix/smtpd[25854]: warning: valid_hostname: invalid character 92(decimal): \@
  Jun 20 19:16:46 mframe1 postfix/smtpd[25854]: warning: malformed domain name in resource data of MX record for dondino.de: \@
  Jun 26 02:39:40 mframe1 postfix/smtpd[20570]: warning: non-SMTP command from localhost[127.0.0.1]: Content-Type: text/html;
  Feb 25 15:57:27 mframe1 postfix/smtpd[25140]: warning: Illegal address syntax from localhost[127.0.0.1] in RCPT command: <name@62.157.140.137>
  Feb 20 22:56:51 mframe1 postfix/postfix-script[4735]: fatal: the Postfix mail system is already running



