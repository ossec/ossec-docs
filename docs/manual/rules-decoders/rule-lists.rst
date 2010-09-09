
.. _manual-rule-lists:

CDB List lookups from within Rules
===================================

Allow for CDB lookups from within rules in OSSEC (ossec-analysisd) of all possible 
fields.

Use cases
---------

Anything that has a large number of items. Some examples:

- named with recursive logs checking the www.malwaredomains.com list for suspicious domains
- lists of approved users by server
- mstark (on irc) originally came up with suggestion for approved software based on a md5 list
- IP address lookups - there are a large number of lists of suspicious or known bad IP addresses to match inside of ossec rules

Syntax for Lists 
----------------

Rules 
~~~~~

A rule would use the following syntax to look up a key within a CDB database.

Positive key match
^^^^^^^^^^^^^^^^^^

This example is a search for the key within the ``rules/cdb_record_file`` and will match 
if they key is present:

.. code-block:: xml

     <list field="program_name" lookup="match_key">rules/records</list>

The ``lookup="match_key"`` is the default and can be left out as in this example:

.. code-block:: xml 

     <list field="program_name">rules/records</list> 

Negative key match 
^^^^^^^^^^^^^^^^^^

This example is a search for the key stored in field attribute and will match if 
it *IS NOT* present in the database:

.. code-block:: xml 

    <list field="program_name" lookup="not_match_key">rules/records</list>

Key and Value match
^^^^^^^^^^^^^^^^^^^

This example is a search for a key stored in the field attribute, and on a positive
match the returned value of the key will be processed using the regex in the
check_value attribute:

.. code-block:: xml 

     <list field="program_name" lookup="match_key_value" check_value="^reject">rules/records</list> 

Positive IP address match 
^^^^^^^^^^^^^^^^^^^^^^^^^

This example is a search for the IP address stored in the field attribute and 
will match if it *IS* present in the database.

.. code-block:: xml 

    <list field="srcip" lookup="address_match_key">rules/records</list> 

Negative IP address match 
^^^^^^^^^^^^^^^^^^^^^^^^^

This example is a search for the IP address stored in the field attribute and 
will match if it *IS NOT* present in the database.

.. code-block:: xml 

    <list field="srcip" lookup="not_address_match_key">rules/records</list> 

Key and Value Address Match
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example is a search for a key stored in the field attribute, and on a positive 
match the returned value of the key will be processed using the regex in the
check_value attribute:

.. code-block:: xml 

      <list field="srcip" lookup="address_match_key_value" check_value="^reject">rules/records</list>
      
    
ossec.conf 
~~~~~~~~~~

Each list will need to be defined and told to be available using the ossec.conf file. 
Using the following syntax:

.. code-block:: xml 

    <ossec_config>
        <rules>
            <list>list/cdb_record_file</list>

Commands
~~~~~~~~

CDB files must be compiled before they can be used.  :ref:`ossec-makelists` is used 
to compile lists.  

The command :ref:`ossec-makelists` will process and compile all lists if the master text 
rules have been changed. Basicly logic is as follows:

- Read ossec.conf for all lists 
- Check the mtime of each list and compare it to the mtime of the compiled .cdb file
- if mtime is newer create new database file ending in .tmp
- use atomic rename to change the .tmp to .cdb. This will invalidate all mmap pages 
  currently in use by ossec-analysisd and will cause them to be reloaded with the new 
  data as needed

List text file format
~~~~~~~~~~~~~~~~~~~~~

Creating cdb lists the following file format is specified: ::

    key1:value
    key2:value
    key3:diff value 

Each key must be unique and is terminated with a colon ``:``.

For IP addresses the dot notation is used for subnet matches ::

    key         CIDR             Possible matches
    10.1.1.1    10.1.1.1/32      10.1.1.1
    192.168.    192.168.0.0/16   192.168.0.0 - 192.168.255.255
    172.16.19.  172.16.19.0/24   172.16.19.0 - 172.16.19.255
        

Due to address lookups being based on the class boundary extra scripts are suggested 
for creating lists that need fine control. Example of IP address list file::

    192.168.: RFC 1918 Address space
    172.16.:RFC 1918 Address space
    172.17.:RFC 1918 Address space
    172.18.:RFC 1918 Address space
    172.19.:RFC 1918 Address space
    172.20.:RFC 1918 Address space
    172.21.:RFC 1918 Address space
    172.22.:RFC 1918 Address space
    172.23.:RFC 1918 Address space
    172.24.:RFC 1918 Address space
    172.25.:RFC 1918 Address space
    172.26.:RFC 1918 Address space
    172.27.:RFC 1918 Address space
    172.28.:RFC 1918 Address space
    172.29.:RFC 1918 Address space
    172.30.:RFC 1918 Address space
    172.31.:RFC 1918 Address space
    10.:RFC 1918 Address space 




