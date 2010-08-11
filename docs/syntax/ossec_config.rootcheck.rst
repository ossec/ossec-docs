.. xml:element:: base_directory

    The base directory that will be append to the following options:

    - rootkit_files 
    - rootkit_trojans 
    - windows_malware 
    - windows_audit 
    - windows_apps 
    - systems_audit 

    **Allowes:** Path to a directory 

.. xml:element:: rootkit_files

    You should change this file if you want rootcheck to read the signatures from somewhere else.

    **Allowed:** A file with the rootkit files signatures 

    **Default:** /etc/shared/rootkit_files.txt

.. xml:element:: rootkit_trojans

    You should change this file if you want rootcheck to read the signatures from somewhere else.

    **Default:** /etc/shared/rootkit_trojans.txt

    **Allowed:** A file with the trojans signatures

.. xml:element:: windows_audit 

.. xml:element:: system_audit 

.. xml:element:: windows_apps

.. xml:element:: windows_malware 

.. xml:element:: scanall 
    
    Tells rootcheck to scan the whole system (may lead to some false positives).

    **Default:** no

    **Allowed:** yes/no 

.. xml:element:: frequency

    Frequency that the rootcheck is going to be executed (in seconds).

    **Defaults:** 36000 (10 hours)

    **Allowed:** Time (in seconds) 

.. xml:element:: disabled

    Disables the execution of rootcheck.

    **Default:** no

    **Allowed:** yes/no 
