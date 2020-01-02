.. manual_rule_testing:

Testing OSSEC rules/decoders
============================


The first problem most people have when troubleshooting OSSEC or trying to write new 
rules and decoders is how to test them. In the past, this would require
manually restarting OSSEC or creating a testing installation. As of 
version 1.6, there is a tool to simplify this task (ossec-logtest).

Testing using ossec-logtest
---------------------------

The tool `ossec-logtest` is installed into ``/var/ossec/bin``. 
It will read the current rules and decoder (from ``/var/ossec`` ) and accept 
log input from stdin:

.. code-block:: console 

    # /var/ossec/bin/ossec-logtest
    2008/07/04 09:57:28 ossec-testrule: INFO: Started (pid: 12683).
    ossec-testrule: Type one log per line.

    Jul 4 09:42:16 enigma sshd[11990]: Accepted password for dcid from 192.168.2.10 port 35259 ssh2

    **Phase 1: Completed pre-decoding.
    full event: "Jul 4 09:42:16 enigma sshd[11990]: Accepted password for dcid from 192.168.2.10 port 35259 ssh2"
    hostname: "enigma"
    program_name: "sshd"
    log: "accepted password for dcid from 192.168.2.10 port 35259 ssh2"

    **Phase 2: Completed decoding.
    decoder: ’sshd’
    dstuser: ‘dcid’
    srcip: ‘192.168.2.10′

    **Phase 3: Completed filtering (rules).
    Rule id: ‘10100′
    Level: ‘4′
    Description: ‘First time user logged in.’
    **Alert to be generated.

In the above example, we provided an authentication success log and 
ossec-logtest showed us how it would be decoded, what information was extracted 
and which rule fired. In the next example, we can see how it would extract a 
user logoff message from Windows:

.. code-block:: console 

    # /var/ossec/bin/ossec-logtest
    2008/07/04 09:57:28 ossec-testrule: INFO: Started (pid: 12683).
    ossec-testrule: Type one log per line.

    WinEvtLog: Security: AUDIT_SUCCESS(538): Security: lac: OSSEC-HM: OSSEC-HM: User Logoff: User Name: lac Domain: OSSEC-HM Logon ID: (0×0,0xF784D5) Logon Type: 2

    **Phase 1: Completed pre-decoding.
    full event: ‘WinEvtLog: Security: AUDIT_SUCCESS(538): Security: lac: OSSEC-HM: OSSEC-HM: User Logoff: User Name: lac Domain: OSSEC-HM Logon ID: (0×0,0xF784D5) Logon Type: 2′
    hostname: ‘enigma’
    program_name: ‘(null)’
    log: ‘WinEvtLog: Security: AUDIT_SUCCESS(538): Security: lac: OSSEC-HM: OSSEC-HM: User Logoff: User Name: lac Domain: OSSEC-HM Logon ID: (0×0,0xF784D5) Logon Type: 2′

    **Phase 2: Completed decoding.
    decoder: ‘windows’
    status: ‘AUDIT_SUCCESS’
    id: ‘538′
    extra_data: ‘Security’
    dstuser: ‘lac’
    system_name: ‘OSSEC-HM’

    **Phase 3: Completed filtering (rules).
    Rule id: ‘18149′
    Level: ‘3′
    Description: ‘Windows User Logoff.’
    **Alert to be generated.


In addition to the information above, `ossec-logtest -f` can be used 
to follow the log through the rule path:

.. code-block:: console 

    # /var/ossec/bin/ossec-logtest -v
    2008/07/04 10:05:43 ossec-testrule: INFO: Started (pid: 23007).
    ossec-testrule: Type one log per line.

    Jul 4 10:05:30 enigma sshd[27588]: Failed password for invalid user test2 from 127.0.0.1 port 19130 ssh2

    **Phase 1: Completed pre-decoding.
    full event: ‘Jul 4 10:05:30 enigma sshd[27588]: Failed password for invalid user test2 from 127.0.0.1 port 19130 ssh2′
    hostname: ‘enigma’
    program_name: ’sshd’
    log: ‘Failed password for invalid user test2 from 127.0.0.1 port 19130 ssh2′

    **Phase 2: Completed decoding.
    decoder: ’sshd’
    srcip: ‘127.0.0.1′

    **Rule debugging:
    Trying rule: 1 - Generic template for all syslog rules.
    *Rule 1 matched.
    *Trying child rules.
    Trying rule: 5500 - Grouping of the pam_unix rules.
    Trying rule: 5700 - SSHD messages grouped.
    *Rule 5700 matched.
    *Trying child rules.
    Trying rule: 5709 - Useless SSHD message without an user/ip.
    Trying rule: 5711 - Useless SSHD message without a user/ip.
    Trying rule: 5707 - OpenSSH challenge-response exploit.
    Trying rule: 5701 - Possible attack on the ssh server (or version gathering).
    Trying rule: 5706 - SSH insecure connection attempt (scan).
    Trying rule: 5713 - Corrupted bytes on SSHD.
    Trying rule: 5702 - Reverse lookup error (bad ISP or attack).
    Trying rule: 5710 - Attempt to login using a non-existent user
    *Rule 5710 matched.
    *Trying child rules.
    Trying rule: 5712 - SSHD brute force trying to get access to the system.

    **Phase 3: Completed filtering (rules).
    Rule id: ‘5710′
    Level: ‘5′
    Description: ‘Attempt to login using a non-existent user’
    **Alert to be generated.
