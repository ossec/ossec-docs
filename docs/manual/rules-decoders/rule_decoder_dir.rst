.. _manual_rule_decoder_dir:

Directory path loading of rules and decoders
============================================

To allow whole directories of files to be loaded as decoders, lists, or rules
by ossec-anaylistd.

Use case
--------

Great simplifies working with decoders as their can be as many files as needed.
Also will make packaging of rules and decoders a simple unzip/untar and restart
operations. This will also greatly reduce the amount of code needed to manage
the upgrade scripts of ossec.

Details
-------

Syntax for OSSEC
~~~~~~~~~~~~~~~~

All Directory loading is done in alphabetical form. This is much like init.d
where the use of numeric prefixes on file names can effect the order of
loading. Example of file names and the order they would be loaded:

#. 00_sshd_rules.xml
#. 01_local_sshd_rules.xml
#. 99_shun_rules.xml

Directory loading 
^^^^^^^^^^^^^^^^^

The basic for selection of rules file is as follows. This will load all files in
the rules dir that match the regex ``_rules.xml$``

.. code-block:: xml

    <ossec_config>
        <rules>
            <rules_dir pattern="_rules.xml">rules</rules_dir>

The pattern is optional and defaults to _rules.xml for rules loading so this
could be writen as:

.. code-block:: xml 

    <ossec_config>
        <rules>
            <rules_dir>rules</rules_dir>

Order of the directives in ossec.conf is still respected, and duplicate files
will not be loaded. In the following example 00_setup_rules.xml is always
loaded first, and will *NOT* be loaded a second time by the rules_dir
directive.

.. code-block:: xml 

    <ossec_config>
        <rules>
            <include>rules/00_setup_rules.xml</include>
            <rules_dir>rules</rules_dir>

For full details on all the Syntax see :xml:`rule_dir` and :xml:`decoder_dir`

Compete Examples of syntax 
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an example where the decoders and rules have been broken out into
subdirectories.

* rules/ 

    * 00_rules_config.xml 
    * 50_apache_rules.xml
    * 50_arpwatch_rules.xml
    * plugins/ 

        * 50_wimax_rules.xml
        * 50_wimax_decoders.xml 

* etc/

    * decoder.xml 
    * local_decoder.xml 


.. code-block:: xml 

    <ossec_config>
        <rules>
            <decoder>etc/decoder.xml</decoder>
            <decoder_dir>rules/plugins</decoder_dir>

            <rule>rules/rules/00_rules_config.xml</rule>
            <rules_dir pattern=".xml$">rules/</rules_dir>
            <rules_dir>rules/plugins</rules_dir>
        </rules>  
    </ossec_config>

        


