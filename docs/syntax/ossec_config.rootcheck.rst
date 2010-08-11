.. object:: base_directory

    The base directory that will be append to the following options:

    - rootkit_files 
    - rootkit_trojans 
    - windows_malware 
    - windows_audit 
    - windows_apps 
    - systems_audit 

    **Allowed:** Path to a directory 

.. object:: rootkit_files

    You should change this file if you want rootcheck to read the signatures from somewhere else.

    **Allowed:** A file with the rootkit files signatures 

    **Default:** /etc/shared/rootkit_files.txt

.. object:: rootkit_trojans

    You should change this file if you want rootcheck to read the signatures from somewhere else.

    **Default:** /etc/shared/rootkit_trojans.txt

    **Allowed:** A file with the trojans signatures

.. object:: windows_audit 

.. object:: system_audit 

.. object:: windows_apps

.. object:: windows_malware 

.. object:: scanall 
    
    Tells rootcheck to scan the whole system (may lead to some false positives).

    **Default:** no

    **Allowed:** yes/no 

.. object:: frequency

    Frequency that the rootcheck is going to be executed (in seconds).

    **Defaults:** 36000 (10 hours)

    **Allowed:** Time (in seconds) 

.. object:: disabled

    Disables the execution of rootcheck.

    **Default:** no

    **Allowed:** yes/no 
