.. object:: email_to 

    E-Mail recipients of alerts 

    **Allowes:** Any valid e-mail address 

.. object:: level  

    Minimum alerting level to forward the e-mails.

    **Allowes:** Any alert level 0 to 16 

.. object:: group 

    The alert that must match this group to be forwarded.

    **Allowes:** Any group/category 

.. object:: event_location 

    The alert must match this event location to be forwarded.

    **Allowes:** Any agent name, ip address or log file 

.. object:: format 

    Specifies the format of the e-mail 
    
    - full: for normal e-mails 
    - sms: for reduced size suitable for SMS  

    **Default:** full 

    **Allowes:** full/sms 

.. object:: do_not_delay 

    Option to send the e-mail right away (no delay). 

.. object:: do_not_group

    Option to do not group this e-mail (send by itself). 


