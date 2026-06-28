
.. _manual-out-email:

Sending alerts via E-Mail
=========================

There are currently three types of email alerts:

* Single Notification E-Mail addresses 
* Granular Notifications to any number of E-mail addresses
* Daily E-mail Reports 

.. warning::

   **Consumer and hosted SMTP providers** (Gmail, Outlook.com, Yahoo, and similar)
   generally do **not** allow unauthenticated relay from arbitrary servers. OSSEC sends
   plain SMTP by default unless you configure authenticated mail (see
   :ref:`manual-out-smtp-auth`). For Gmail you typically need an app password, OAuth,
   or a relay service — not a bare ``smtp_server`` pointing at ``smtp.gmail.com``.

   **Microsoft 365 / Exchange Online** requires authenticated SMTP or a connector;
   see `Microsoft's SMTP setup guide
   <https://support.microsoft.com/en-us/office/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365-69f58e99-c550-4274-ad18-c805d654b4c4>`_.
   Use :ref:`manual-out-smtp-auth` when your provider requires TLS and credentials.

.. warning:: 

    Single E-Mail Notification must be setup before Granular Notification
    will work.


.. toctree::

    standard-email-output
    smtp-authenticated-email
    granular-email-output
    reports-email-output
