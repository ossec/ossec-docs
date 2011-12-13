Log Samples from Sendmail
-------------------------

Error code 553, rejected due to spam:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  sm-mta[11761]: k79IaGJL011761: ruleset=check_mail, arg1=<direto@mkt.submarino.com.br>, relay=mkt1.submarino.com.br [1.2.3.4], reject=553 5.3.0 <direto@mkt.submarino.com.br>... SPAM REJECT

  sm-mta[11761]: k79IaGJK011761: ruleset=check_mail, arg1=<direto@mkt.submarino.com.br>, relay=mkt1.submarino.com.br [1.2.3.4], reject=553 5.3.0 <direto@mkt.submarino.com.br>... SPAM REJECT

  Sep  7 05:40:15 mail sm-mta[64376]: ruleset=check_relay, arg1=adsl196-97-91-206-196.adsl196-3.iam.net.ma, arg2=196.206.91.97, relay=adsl196-97-91-206-196.adsl196-3.iam.net.ma [196.206.91.97], reject=553 5.3.0 196.206.91 Rejected due to abuse - see http://dnsbl.sorbs.net.10102005

  Sep  7 02:43:30 mail sm-mta[63495]: k876hJS0063495: Milter: data, reject=550 5.7.1 Blocked by SpamAssassin

  Sep  7 04:31:10 mail sm-mta[64143]: ruleset=check_relay, arg1=60-240-56-231.tpgi.com.au, arg2=127.0.0.3, relay=60-240-56-231.tpgi.com.au [60.240.56.231], reject=553 5.3.0 Message from 60.240.56.231 blocked - see http://dynablock.njabl.org/



Connection rate limit exceeded (421 4.3.2):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Sep  7 01:20:46 mail sm-mta[62946]: ruleset=check_relay, arg1=h188.175.141.67.ip.alltel.net, arg2=67.141.175.188, relay=h188.175.141.67.ip.alltel.net [67.141.175.188], reject=421 4.3.2 Connection rate limit exceeded.



Pre-greeting traffic (rejected):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
Jul 20 16:21:24 mx0 sendmail[7818]: j6KKHo2d007818: rejecting commands from sv.e103gng.com [66.62.19.10] due to pre-greeting traffic



SMF-SAV Sendmail Milter decoder:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
smf-sav[513]: [ID 987462 mail.notice] sender check failed: <xkyjywqvophshu@mypersonalemail.com>, 125.133.22.112, [125.133.22.112], [00:00:01]
smf-sav[513]: [ID 407019 mail.info] sender check succeeded (cached): <asterisk-users-bounces@lists.digium.com>, 216.207.245.17, lists.digium.com
smf-sav[513]: [ID 987894 mail.notice] sender check tempfailed: <31363****-org@targetedpages.com>, 69.8.190.101, smtp101.tramailer.info, [00:00:05]



Save mail panic:
^^^^^^^^^^^^^^^^

.. code-block:: console
  Sep 24 01:32:57 gatekeeper sendmail[19921]: h8O5WptI019921: Losing ./qfh8O5WptI0 19921: savemail panic


