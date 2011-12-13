Log Samples from Exim
---------------------

I've included the ossec bad responses:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*error 450 (ossec should probably ignore) -- this particular line is blowback from spam delivery attempt elsewhere with one of our addresses spoofed as "From", and occurs many times in the log files

.. code-block:: console

  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[14700]: 2006-11-21 15:01:33 1Glsgv-0002wv-00 SMTP error from remote mailer after RCPT TO:<xxxxxxxxxxx@some-domain.com>: host gmail-smtp-in.l.google.com [1.1.1.1]: 450-4.2.1 The Gmail user you are trying to contact is receiving\n450-4.2.1 mail at a rate that prevents additional messages from\n450-4.2.1 being delivered. Please resend your message at a later\n450-4.2.1 time; if the user is able to receive mail at that time,\n450 4.2.1 your message will be delivered. 23si8340522nzn

*error 550 (ossec should ignore after the first time)
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[14706]: 2006-11-21 15:01:39 1Gmary-0002iA-00 ** xxxxxxxx@some-domain.com R=dnslookup T=remote_smtp: SMTP error from remote mailer after RCPT TO:<xxxxxxxx@some-domain.com>: host mx.some-domain.com [1.1.1.1]: 550 Mailbox unavailable <xxxxxxxxxxx@some-domain.com>

*frozen (probably okay to ignore)
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[15745]: 2006-11-21 15:17:10 1Gmc37-00045w-00 Frozen (delivery error message)

*local delivery error (unknown user most likely, probably okay to ignore) although parsing out the email address and IP could provide a trigger for an active response (e.g. a honeypot email address that triggers the sending IP address to be blocked for 24 hours)
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[15740]: 2006-11-21 15:16:57 1Gmc36-00045o-00 ** xxxxxxxxxxx@some-domain.com R=local_user_cyrus T=local_delivery_cyrus: Child process of local_delivery_cyrus transport returned 65 (could mean error in input data) from command: /usr/cyrus/bin/deliver


*this error 450 should be a 550 -- ossec could ignore (it's a temporary error message for a permanent error, but not much we can do about it)
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[16042]: 2006-11-21 15:24:02 1Gm2od-0001ay-00  xxxxxxxxxxx@some-domain.com R=dnslookup T=remote_smtp defer (0): SMTP error from remote mailer after RCPT TO:<xxxxxxxxxxx@some-domain.com>: host mail.some-domain.com [66.93.22.101]: 450 <xxxxxxxxxxx@some-domain.com>: User unknown in local recipient table


*Connection refused; not much we can do about this error either
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[14164]: 2006-11-21 14:55:07 1GlKR9-0003x0-00  xxxxxxx@some-domain.com R=dnslookup T=remote_smtp defer (111): Connection refused


*error 501 -- most likely the recipient's DNS is misconfigured; but this is most likely blowback from spam, so it's not terribly important
.. code-block:: console
  Received From: (mailserver) 192.168.1.21->/var/log/mail.log
  Rule: 1002 fired (level 7) -> "Unknown problem somewhere in the system."
  Portion of the log(s):

  exim[13428]: 2006-11-21 14:39:59 1GmbTK-0003UZ-00 ** xxxxxxxx@somedomain.com R=dnslookup T=remote_smtp: SMTP error from remote mailer after RCPT TO:<xxxxxxxx@somedomain.com>: host mail.somedomain.com [1.1.3.1]: 501 This system is not configured to relay mail (r) to <somedomain.com> for 2.2.1.5


