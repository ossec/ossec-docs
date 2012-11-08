
.. _ossec-logtest: 

ossec-logtest 
=============

ossec-logtest is the single most useful tool when working with ossec.  This tool allows oneself 
to test and verify log files in the exact same way that `ossec-anaylistd` does.  

Something ossec-logtest can help with: 

- Writing rules (Debugging your custom rules) 
- Troubleshooting false positives or false negatives 

ossec-logtest accepts standard input for all log to test.  

osssec-logtest argument options
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

.. option:: -v 

    Full output of all details and matches.  

    .. note:: 

        This the key argument to troubleshoot a rule, decoder problem.  

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

.. option:: -a 

    Analyze of input lines as if they are live events.  


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

Example 2: Using OSSEC for the forensic analysis of log files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have one old log file that you want to check or if you are doing a 
forensics analysis of a box and wants to check the logs with OSSEC, we 
now have a solution too.

Let’s say you have a file /var/log/secure that you want to analyze with OSSEC. 
You need to use the ossec-logtest tool with the “``-a``” flag to reproduce 
the alerts:

.. code-block:: console 

    # cat /var/log/secure | /var/ossec/bin/ossec-logtest -a

    ** Alert 1264788284.11: - syslog,sshd,authentication_success,
    2010 Jan 29 14:04:44 enigma->stdin
    Rule: 5715 (level 3) -> ‘SSHD authentication success.’
    Src IP: a.b.2.15
    User: dcid
    Jan 15 10:25:01 enigma sshd[17594]: Accepted password for dcid from a.b.2.15 port 47526 ssh2

    ** Alert 1264788284.12: - syslog,sshd,authentication_success,
    2010 Jan 29 14:04:44 enigma->stdin
    Rule: 5715 (level 3) -> ‘SSHD authentication success.’
    Src IP: 127.0.0.1
    User: dcid
    Jan 15 11:19:20 enigma sshd[18853]: Accepted publickey for dcid from 127.0.0.1 port 6725 ssh2

You will get the alerts just like you would at /var/ossec/logs/alerts.log. The 
benefit now is that you can pipe this output to :ref:`ossec-reported` to get a 
better view of what is going on:

.. code-block:: console 

    # cat /var/log/secure | /var/ossec/bin/ossec-logtest -a |/var/ossec/bin/ossec-reported
    Report completed. ==
    ————————————————
    ->Processed alerts: 522
    ->Post-filtering alerts: 522

    Top entries for ‘Source ip’:
    ————————————————
    89.200.169.170 |41 |
    127.0.0.1 |33 |
    83.170.106.142 |20 |
    204.232.206.109 |16 |
    ..

    Top entries for ‘Username’:
    ————————————————
    root |247 |

    Top entries for ‘Level’:
    ————————————————
    Severity 5 |406 |
    Severity 3 |41 |
    Severity 10 |32 |

    Top entries for ‘Group’:
    ————————————————
    syslog |522 |
    sshd |509 |
    authentication_failed |369 |
    invalid_login |146 |

    Top entries for ‘Rule’:
    ————————————————
    5716 - SSHD authentication failed. |223 |
    5710 - Attempt to login using a non-existent.. |146 |
    5715 - SSHD authentication success. |41 |
    5702 - Reverse lookup error (bad ISP or atta.. |37 |

To get a report of all brute force attacks (for example) that scanned my 
box:

.. code-block:: console 

    # cat /var/log/secure | /var/ossec/bin/ossec-logtest -a |/var/ossec/bin/ossec-reported -f group authentication_failures

    Report completed. ==
    ————————————————
    ->Processed alerts: 522
    ->Post-filtering alerts: 25

    Top entries for ‘Source ip’:
    ————————————————
    83.170.106.142 |2 |
    89.200.169.170 |2 |
    114.255.100.163 |1 |
    117.135.138.183 |1 |
    124.205.62.36 |1 |
    173.45.108.230 |1 |
    200.182.99.59 |1 |
    202.63.160.50 |1 |
    210.21.225.202 |1 |
    211.151.64.220 |1 |
    213.229.70.12 |1 |
    218.30.19.48 |1 |
    221.12.12.3 |1 |
    59.3.239.114 |1 |
    61.168.227.12 |1 |
    61.233.42.47 |1 |
    67.43.61.80 |1 |
    72.52.75.228 |1 |
    77.245.148.196 |1 |
    79.125.35.214 |1 |
    85.21.83.170 |1 |
    92.240.75.6 |1 |
    94.198.49.185 |1 |

    Top entries for ‘Username’:
    ————————————————
    root |24 |

    Top entries for ‘Level’:
    ————————————————
    Severity 10 |25 |

    Top entries for ‘Group’:
    ————————————————
    authentication_failures |25 |
    sshd |25 |
    syslog |25 |

    Top entries for ‘Location’:
    ————————————————
    enigma->stdin |25 |

    Top entries for ‘Rule’:
    ————————————————
    5720 - Multiple SSHD authentication failures. |24 |
    5712 - SSHD brute force trying to get access.. |1 |
