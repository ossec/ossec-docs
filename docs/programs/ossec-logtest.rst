
.. _ossec-logtest: 

ossec-logtest 
=============

ossec-logtest is the single most useful tool when working with ossec.  This tool allows oneself 
to test and verify logfiles in the excate same way that `ossec-anaylistd` does.  

Something ossec-logtest can help with: 

- Writing rules (Debugging your custom rules) 
- Troubleshooting false possitives or false negaitives 

ossec-logtest accepts standard input for all log to test.  

osssec-logtest augument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: ossec-logtest 

.. option:: -d 

   Print debug output to the terminal.   

.. option:: -V
 
   Print the Version and license message for OSSEC and ossec-logtest. 

.. option:: -h 
   
   Print the help message to the console.  

.. option:: -t 

    Test configuration.  This will print file details on the ossec-anaylistd rules, 
    decoders, and lists as they are loaded and the order they were processed.  

.. option:: -f 

    Full output of all details and matches.  

    .. note:: 

        This the key augument to trouble a rule, decoder problem.  

    .. note:: 

        This is argument was incorrectly displayed as running in the foreground 
        in all version before version 2.5 


.. option:: -u <user> 

    Run as <user>: ossec-logtest will change uid to the user specified as part of this 
    argument. 

    Often used with `ossec-logtest -g`

.. option:: -g <group>

    Run as <group>: ossec-logtest will change gid to the group specified as part of this 
    argument. 

    Often used with `ossec-logtest -u`

.. option:: -c <config> 

    <config> is the path and filename to load in place of the default /var/ossec/etc/ossec.conf. 

.. option:: -D <dir> 

    This is the path that ossec-logtest will chroot to before it completes loading all rules, 
    decoders, and lists and processing standard input.  


ossec-logtest example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Testing standard rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. code-block:: console 

        # echo "Aug 29 15:33:13 ns3 named[464]: client 217.148.39.3#1036: query (cache) denied" | /var/ossec/bin/ossec-logtest -f
        2010/08/10 06:57:06 ossec-testrule: INFO: Reading decoder file loadables/decoders/00_decoders.xml.
        2010/08/10 06:57:06 ossec-testrule: INFO: Reading decoder file loadables/decoders/50_named.xml.
        2010/08/10 06:57:06 ossec-testrule: INFO: Reading decoder file loadables/decoders/50_pam.xml.
        2010/08/10 06:57:06 ossec-testrule: INFO: Reading decoder file loadables/decoders/50_sshd.xml.
        2010/08/10 06:57:06 ossec-testrule: INFO: Reading loading the lists file: 'loadables/lists/rfc1918-privateaddresses'
        2010/08/10 06:57:06 ossec-testrule: INFO: Started (pid: 78828).
        ossec-testrule: Type one log per line.



        **Phase 1: Completed pre-decoding.
               full event: 'Aug 29 15:33:13 ns3 named[464]: client 217.148.39.3#1036: query (cache) denied'
               hostname: 'ns3'
               program_name: 'named'
               log: 'client 217.148.39.3#1036: query (cache) denied'

        **Phase 2: Completed decoding.
               decoder: 'named'
               srcip: '217.148.39.3'

        **Rule debugging:
            Trying rule: 1 - Generic template for all syslog rules.
               *Rule 1 matched.
               *Trying child rules.
            Trying rule: 30100 - Apache messages grouped.
            Trying rule: 7200 - Grouping of the arpwatch rules.
            Trying rule: 6200 - Asterisk messages grouped.
            Trying rule: 9600 - cimserver messages grouped.
            Trying rule: 4700 - Grouping of Cisco IOS rules.
            Trying rule: 3900 - Grouping for the courier rules.
            Trying rule: 9700 - Dovecot Messages Grouped.
            Trying rule: 11100 - Grouping for the ftpd rules.
            Trying rule: 9300 - Grouping for the Horde imp rules.
            Trying rule: 3600 - Grouping of the imapd rules.
            Trying rule: 3700 - Grouping of mailscanner rules.
            Trying rule: 3800 - Grouping of Exchange rules.
            Trying rule: 6300 - Grouping for the MS-DHCP rules.
            Trying rule: 6350 - Grouping for the MS-DHCP rules.
            Trying rule: 11500 - Grouping for the Microsoft ftp rules.
            Trying rule: 50100 - MySQL messages grouped.
            Trying rule: 12100 - Grouping of the named rules
               *Rule 12100 matched.
               *Trying child rules.
            Trying rule: 12107 - DNS update using RFC2136 Dynamic protocol.
            Trying rule: 12101 - Invalid DNS packet. Possibility of attack.
            Trying rule: 12109 - Named fatal error. DNS service going down.
            Trying rule: 12102 - Failed attempt to perform a zone transfer.
            Trying rule: 12103 - DNS update denied. Generally mis-configuration.
            Trying rule: 12104 - Log permission misconfiguration in Named.
            Trying rule: 12105 - Unexpected error while resolving domain.
            Trying rule: 12106 - DNS configuration error.
            Trying rule: 12108 - Query cache denied (maybe config error).
               *Rule 12108 matched.

        **Phase 3: Completed filtering (rules).
               Rule id: '12108'
               Level: '4'
               Description: 'Query cache denied (maybe config error).'
               Info - Link: 'http://www.reedmedia.net/misc/dns/errors.html'
        **Alert to be generated.

