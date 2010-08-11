.. xml:element:: location 

    Specify the location of the log to be read.

    **Default:** Multiple (eg /var/log/messages)

    **Allowes:** Any log file 

.. xml:element:: log_format 

    The format of the log being read. 
    
    .. note:: 
    
        If the log has one entry per line, use syslog. 

    **Default:** syslog 

    **Allowes:** 

    - syslog 
    - snort-full 
    - snort-fast 
    - squid 
    - iis 
    - eventlog 
    - mysql_log 
    - postgresql_log 
    - nmapg 
    - apache
    - command 

.. xml:element:: command 

    The command to run a all output will be read as a log file.  

    **Allowes:** And commandline and arguments. 



