.. xml:element:: group

    Filter by group/category.  

    **Allowed:** Any category used within OSSEC Rules. 

.. xml:element:: categories

    Filter by group/category. 

    .. note:: 

        This is the same as the group option above.  

    **Allowed:** Any category used within OSSEC Rules. 

.. xml:element:: rule
        
    Rule ID to Filter for. 

    **Allowed:** Any Rule ID in OSSEC Rules. 

.. xml:element:: level

    Alert level to filter for.  This is an inclusive option so all higher level 
    alerts will also match. 

    **Allowed:** Any Alert level 1 to 16 

.. xml:element:: location

    Filter by the log location or agent name. 

    **Allowed:** Any file path or hostname or network.  

.. xml:element:: srcip 

    Filter by the source ip of the event. 

    **Allowed:** Any hostname or network 

.. xml:element:: user 

    Filter by the user name.  This will match on ether srcuser or dstuser 

    **Allowed:** Any username 

.. xml:element:: title 

    The name of the report.  
    
    This is a required field for reports to function. 

    **Allowed:** Any Text 

.. xml:element:: email_to 

    The email addres to send the completed report. 

    This is a required feild for a report to function.  


