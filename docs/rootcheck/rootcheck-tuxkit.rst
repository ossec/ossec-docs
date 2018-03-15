
Information about the Tuxkit Rootkit
====================================

This is a rootkit written by a Dutch group called Tuxtendo. It was found in 
some infected Redhat 6.0/7.0 systems. 


More Information
----------------

A complete analyse of Tuxkit, done by Spoonfork (spoonfork@hackinthebox.org).
For more info, look at this analyse (author unknown): :ref:`analysis-tuxkit`


Files
-----

-- ``dev/tux``
-- ``usr/bin/xsf``
-- ``usr/bin/xchk``
-- ``*/.log``
-- ``*/.file``
-- ``*/.addr``

Entries to search on file "/etc/rc.d/rc.sysinit": 

-- ``/usr/bin/xsf``
-- ``/usr/bin/xchk``

.. note::
    
    All files with an "*" need to be search in all system

