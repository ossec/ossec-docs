.. _rules.rules:


Rules Syntax
============

Overview 
--------

Order of execution
^^^^^^^^^^^^^^^^^^

First, the rules with 0 levels are tried, and then all the other rules in a decreasing order by their level.
If the level is the same, the order will be decided based on the rules list in /var/ossec/etc/ossec.conf file.
Note, for rules which have some requirement (for example if_sid), the requirement is tried first.

Options 
------- 

.. include:: ./rules.trst
