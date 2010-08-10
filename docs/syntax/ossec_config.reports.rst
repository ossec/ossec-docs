.. object:: group

    Filter by group/catigory.  

    **Allowes:** Any catigory used within OSSEC Rules. 

.. object:: categories

    Filter by group/catigory. 

    .. note:: 

        This is the same as the group option above.  

    **Allowes:** Any catigory used within OSSEC Rules. 

.. object:: rule
        
    Rule ID to Filter for. 

    **Allowes:** Any Rule ID in OSSEC Rules. 

.. object:: level

    Alert level to filter for.  This is an inclusive option so all higher level 
    alerts will also match. 

    **Allowes:** Any Alert level 1 to 16 

.. object:: location

    Filter by the log location or agent name. 

    **Allowes:** Any file path or hostname or network.  

.. object:: srcip 

    Filter by the source ip of the event. 

    **Allowes:** Any hostname or network 

.. object:: user 

    Filter by the user name.  This will match on ether srcuser or dstuser 

    **Allowes:** Any username 

.. object:: title 

    The name of the report.  
    
    This is a required field for reports to function. 

    **Allowes:** Any Text 

.. object:: email_to 

    The email addres to send the completed report. 

    This is a required feild for a report to function.  


