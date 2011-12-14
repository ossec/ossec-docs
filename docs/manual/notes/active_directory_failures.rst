Why am I getting multiple 675 events from AD + Samba?
-----------------------------------------------------

*by `Daniel B. Cid <http://www.ossec.net/dcid>`_


If you have Windows AD and Linux with Samba in the same network, you may be  getting multiple 675 logon failures every time a Linux user tries to access the AD. 
This `link <http://blog.scottlowe.org/2006/10/23/event-logging-in-ad-integration-scenarios/#comment-5840>`_ explains the reason:

.. code-block:: console

   These errors are logged because the MS Kerberos implementation expects the initial TGT request to contain a
  "preauthentication" blob which is a time stamp encrypted using the user.s password hash as an encryption key
  (PA_ENC_TIMESTAMP in Kerberos-speak) - this preauthentication is used to prevent replay attacks. The Linux Kerberos 
  libraries dont send this blob in their initial TGT request. When it receives the TGT without the preauthentication 
  blob, the AD server:
  1. Rejects the initial request
  2. In the reject response, indicates that Preauthentication is required and hints with a list of acceptable preauthtcation types.
  3. Logs the 675 error in the Event log.


To avoid receving multiple ``18152 fired (level 10) -> "Multiple Windows Logon Failures."`` on OSSEC, you can ignore this specific event id, with the following local rule (ignoring 675 error with Failure code 0x19):

.. code-block:: console

  <rule id="xyz" level="0">
    <if_sid>18106</if_sid>
    <id>^675</id>
    <match>Failure Code:0x19</match>
  </rule>



*This behavior was reported by Nicolas Arias <nicolas.arias at xx.com> at the OSSEC mailing list.*


