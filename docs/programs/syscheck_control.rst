
.. _syscheck_control:

syscheck_control
================

syscheck_control provides an interface for managing and viewing the integrity checking database.

syscheck_control argument options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: syscheck_control 

.. option:: -h

    Display the help message.

.. option:: -l 

    List available agents. 

.. option:: -lc 

    List only currently connected agents. 

.. option:: -u AGENT_ID

    Updates (clear) the database for the agent.

.. option:: -u all 

    Updates (clear) the database for all agents.

.. option:: -i AGENT_ID

    Prints database for the agent.

.. option:: -r -i 

    List modified registry entries for the agent (Windows only).

.. option:: -f <file>

    Used with -i. Prints information about a modified file.

.. option:: -z

    Used with -f, zeroes the auto-ignore counter.

.. option:: -d

    Used with -f, ignores that file.

.. option:: -s

    Changes the output to CSV (comma delimited).

syscheck_control example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example 1: Getting a list of modified files for an agent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve information about files that were monitored by OSSEC and modified after OSSEC was deployed, run `syscheck_control -i AGENT_ID`.

.. code-block:: console 

    # /var/ossec/bin/syscheck_control -i 002

    Integrity changes for agent 'ossec-agent (002) - 192.168.1.86':

    Changes for 2009 Dec 21:
    2009 Dec 21 13:52:40,0 - /etc/authorization
    2009 Dec 21 13:52:42,0 - /etc/cups/printers.conf
    2009 Dec 21 13:52:42,0 - /etc/cups/printers.conf.O
    2009 Dec 21 13:52:58,0 - /etc/postfix/main.cf.default

    Changes for 2010 Jan 04:
    2010 Jan 04 10:13:58,0 - /etc/authorization

    Changes for 2010 Jan 06:
    2010 Jan 06 09:45:43,0 - /etc/postfix/main.cf.default

    Changes for 2010 Jan 18:
    2010 Jan 18 09:18:51,0 - /etc/cups/printers.conf
    2010 Jan 18 09:18:51,0 - /etc/cups/printers.conf.O

    Changes for 2010 Feb 23:
    2010 Feb 23 09:17:22,2 - /etc/cups/printers.conf
    2010 Feb 23 09:17:22,2 - /etc/cups/printers.conf.O

    Changes for 2010 Mar 24:
    2010 Mar 24 08:42:52,3 - /etc/cups/printers.conf
    2010 Mar 24 08:42:52,3 - /etc/cups/printers.conf.O

As you can see this command provides an overview about file modifications.

Example 2: Getting more detailed information about a modified file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to get more detailed information about a file that was modified you can use syscheck_control to view

- the time stamp when the file was added to the syscheck database
- the integrity checking values when the file was added to the syscheck database
- the time stamps when OSSEC detected a modification
- the integrity checking values for every time OSSEC detected a modification.

The integrity checking values include

- how often the file has changed
- file size
- file permissions
- owner and group id of the file
- MD5 and SHA1 hashes of the file.

To retrieve this information, run `syscheck_control -i AGENT_ID -f FILENAME`:

.. code-block:: console 

    # /var/ossec/bin/syscheck_control -i 002 -f /etc/authorization

    Integrity changes for agent 'ossec-agent (002) - 192.168.1.86':
    Detailed information for entries matching: '/etc/authorization'

    2009 Dec 21 13:52:40,0 - /etc/authorization
    File added to the database. 
    Integrity checking values:
       Size: 27771
       Perm: rw-r--r--
       Uid:  0
       Gid:  0
       Md5:  dd62912576ae05d611d7469be809cf1d
       Sha1: 530df0283df52f0152b9e7ce1a518119b06ceebc

    2010 Jan 04 10:13:58,0 - /etc/authorization
    File changed. - 1st time modified.
    Integrity checking values:
       Size: >28050
       Perm: rw-r--r--
       Uid:  0
       Gid:  0
       Md5:  >50da55def41bcede7d42ac5ee8fe12c9
       Sha1: >97f4b2b48a97321a3e245221e0ea4353cf4fa8ef

Example 3: Clearing the syscheck database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To clear the syscheck database for a certain agent run the following command:

.. code-block:: console

    # /var/ossec/bin/syscheck_control -u 002

    ** Integrity check database updated.

`syscheck_control -i 002` will now show that no modified files for that agent are in the database:

.. code-block:: console

    # /var/ossec/bin/syscheck_control -i 002

    Integrity changes for agent 'ossec-agent (002) - 192.168.1.86':

    ** No entries found.

To clear the database for all agents and the server run the following command:

.. code-block:: console

    # /var/ossec/bin/syscheck_control -u all

    ** Integrity check database updated.

The next time syscheck is run, the database will be populated again.
