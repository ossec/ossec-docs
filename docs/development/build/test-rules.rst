.. _test-rules:

test-rules:
===========

OSSEC includes the facilities to test rules in bulk.
These checks should ensure there are no regressions after changes have been made.
``ossec-logtest -U`` is used to test the outcome of rules. If ``ossec-logtest`` 
exits with any code but 0 it is considered a failure.


Requirements:
^^^^^^^^^^^^^

This feature currently requires python, a copy of the OSSEC source code,
and the tools required to build OSSEC.

.. note::

   This requirement may change in the future.
   There is interest in utilizing the embedded lua.


How to run:
^^^^^^^^^^^

Running the current tests is as simple as running ``make test-rules`` in the ``src`` directory.

.. code-block:: console

   [ddpbsd@ossec-build:ossec-hids/src] $ more /tmp/ttt                                                                                                                                        
   ( cd ../contrib/ossec-testing && sudo python runtests.py) 
   - [ File = ./tests/named.ini ] ---------
   .....
   - [ File = ./tests/sshd.ini ] ---------
   ...........
   - [ File = ./tests/apparmor.ini ] ---------
   .....
   - [ File = ./tests/cimserver.ini ] ---------
   ..
   - [ File = ./tests/cisco_ios.ini ] ---------
   .....
   - [ File = ./tests/firewalld.ini ] ---------
   ..
   - [ File = ./tests/netscreen.ini ] ---------
   ...
   - [ File = ./tests/ossec.ini ] ---------
   ....
   - [ File = ./tests/pam.ini ] ---------
   .....
   - [ File = ./tests/rsh.ini ] ---------
   ..
   - [ File = ./tests/samba.ini ] ---------
   ....
   - [ File = ./tests/su.ini ] ---------
   .....
   - [ File = ./tests/sudo.ini ] ---------
   ..
   - [ File = ./tests/syslog.ini ] ---------
   ..
   - [ File = ./tests/systemd.ini ] ---------
   .
   - [ File = ./tests/unbound.ini ] ---------


File format:
^^^^^^^^^^^^

The rule checks are configured in ``ini`` files. These files are in the ``contrib/ossec-testing/tests`` directory.
Each file contains the configuration to check the rules for one program, for example ``named.ini`` contains checks
for the named rules.

Example:

.. code-block:: ini

   [su: failed ]
   log 1 pass = Apr 27 15:22:23 niban su[2921936]: failed: ttyq4 changing from ldap to root
   rule = 5302
   alert = 9
   decoder = su

   [su: bad pass]
   log 1 pass = Apr 27 15:22:23 niban su[234]: BAD SU ger to fwmaster on /dev/ttyp0
   rule = 5301
   alert = 5
   decoder = su

   [su: pam - auth fail]
   log 1 fail = Apr 27 15:22:23 niban su(pam_unix)[23164]: authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=osaudit
   log 2 fail = Apr 27 15:22:23 niban su(pam_unix)[2298]: authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=root
   rule = 5503
   alert = 5
   decoder = su

   [su: work]
   log 1 pass = Apr 22 17:51:51 enigma su: dcid to root on /dev/ttyp1
   rule = 5303
   alert = 3
   decoder = su


Each entry has a number of configuration elements:

  * ``[su: - bad pass]`` - This is a heading, it usually contains the rule description.

  * ``log 1 pass =`` - This is the first log, and the ``ossec-logtest`` should pass. Noting failures is also possible by using ``fail`` instead of ``pass``.

  * ``Apr 27 15:22:23 niban su[234]: BAD SU ger to fwmaster on /dev/ttyp0`` - This is the log message to be checked.

  * ``rule = 5301`` - This is the expected rule, if the log message triggers a different rule the test will return a failure.

  * ``alert = 5`` - This is the expected rule level. A failure to match this level will result in a failure.

  * ``decoder = su`` - This is the expected decoder. A failure to match this decoder will result in a failure.

The above entry can be verified by running the log message through ossec-logtest:

.. code-block:: console

   [ddpbsd@ossec-build:/var/ossec] $ sudo /var/ossec/bin/ossec-logtest
   2014/10/31 10:37:38 ossec-testrule: INFO: Reading local decoder file.
   2014/10/31 10:37:38 ossec-testrule: INFO: Started (pid: 25545).
   ossec-testrule: Type one log per line.

   Apr 27 15:22:23 niban su[234]: BAD SU ger to fwmaster on /dev/ttyp0


  **Phase 1: Completed pre-decoding.
          full event: 'Apr 27 15:22:23 niban su[234]: BAD SU ger to fwmaster on /dev/ttyp0'
          hostname: 'niban'
          program_name: 'su'
          log: 'BAD SU ger to fwmaster on /dev/ttyp0'

   **Phase 2: Completed decoding.
          decoder: 'su'
          srcuser: 'ger'
          dstuser: 'fwmaster'

   **Phase 3: Completed filtering (rules).
          Rule id: '5301'
          Level: '5'
          Description: 'User missed the password to change UID (user id).'
   **Alert to be generated.

The rule triggered is indeed 5301, it is a level 5 alert, and the decoder was su.

Here is an example of a planned failure:

.. code-block:: ini

   [su: pam - auth fail]
   log 1 fail = Apr 27 15:22:23 niban su(pam_unix)[23164]: authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=osaudit
   rule = 5503
   alert = 5
   decoder = su

Running the above log message through ossec-logtest:

.. code-block:: console

   Apr 27 15:22:23 niban su(pam_unix)[23164]: authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=osaudit

   **Phase 1: Completed pre-decoding.
          full event: 'Apr 27 15:22:23 niban su(pam_unix)[23164]: authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=osaudit'
          hostname: 'niban'
          program_name: 'su(pam_unix)'
          log: 'authentication failure; logname= uid=1342 euid=0 tty= ruser=dcid rhost=  user=osaudit'

   **Phase 2: Completed decoding.
          decoder: 'pam'
          dstuser: 'dcid'

   **Phase 3: Completed filtering (rules).
          Rule id: '5503'
          Level: '5'
          Description: 'User login failed.'
   **Alert to be generated.

The rule and level are correct, but the decoder is not. This triggers the expected failure.

An unexpected failure will produce output like the following:

.. code-block:: console

   ( cd ../contrib/ossec-testing && sudo python runtests.py) 
   - [ File = ./tests/named.ini ] ---------

   ------------------------------------------------------------
   Failed: Exit code = 0
           Alert     = 0
           Rule      = 12108
           Decoder   = named
           Section   = Query cache denied
           line name = log 1 fail
 
   2014/10/31 10:49:47 ossec-testrule: INFO: Reading local decoder file.
   2014/10/31 10:49:47 ossec-testrule: INFO: Started (pid: 16533).
   ossec-testrule: Type one log per line.



   **Phase 1: Completed pre-decoding.
          full event: 'Aug 29 15:33:13 ns3 named[464]: client 217.148.39.3#1036: query (cache) denied'
          hostname: 'ns3'
          program_name: 'named'
          log: 'client 217.148.39.3#1036: query (cache) denied'

   **Phase 2: Completed decoding.
          decoder: 'named'
          srcip: '217.148.39.3'

   **Phase 3: Completed filtering (rules).
          Rule id: '12108'
          Level: '0'
          Description: 'Query cache denied (probably config error).'
          Info - Link: 'http://www.reedmedia.net/misc/dns/errors.html'
   0

   ....
   - [ File = ./tests/sshd.ini ] ---------
   ...........

The named rule failed because it was expecting a failure in decoding, but did not trigger one.
