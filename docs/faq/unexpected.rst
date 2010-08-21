
When the unexpected happens: FAQ
--------------------------------

#. How do I troubleshoot ossec?
    
    If you are having problems with ossec, the first thing to do is to look at 
    your logs. 
    
    * Unix/Linux: The logs will be at /var/ossec/logs/ossec.log
    * Windows: The logs are at  C:\Program Files\ossec-agent\ossec.log. 

    If by looking at them, you can't find out the error, we suggest you to send an 
    e-mail to one of our mailling lists with the following information: 

    * OSSEC version number.

        Run the following to get the version installation. 

        .. code-block:: console

            # /var/ossec/bin/ossec-analysisd -V

    * Content of /etc/ossec-init.conf
    * Content of /var/ossec/etc/ossec.conf or (or C:\Program Files\ossec-agent\ossec.log if Windows)
    * Content of /var/ossec/logs/ossec.log 
    * Operating system name/version (uname -a if Unix)
    * Any other relevant information. 


#. How to debug ossec?

    .. warning::

        Only read this section if you tried to troubleshoot ossec already, but 
        didn't have lucky solving your problem.  Most of the users will never need 
        to enable debugging, since it can significantly hurt performance. 

    **Debug Logging** 

    You can also enable debugging mode on ossec to extract more data about 
    what is going on. To do so, you will need to modify the file 
    /var/ossec/etc/internal_options.conf (or 
    C:\\Program Files\\ossec-agent\\internal_options.conf on Windows) and change 
    the debug level from the default "0" to "1" or "2". 

    For example, if you wish to debug your windows agent, just change the option 
    windows.debug from 0 to 2. Bellow is the list of all the debug options:

    .. code-block:: console 

        # Debug options.
        # Debug 0 -> no debug
        # Debug 1 -> first level of debug
        # Debug 2 -> full debugging

        # Windows debug (used by the windows agent)
        windows.debug=0

        # Syscheck (local, server and unix agent)
        syscheck.debug=0

        # Remoted (server debug)
        remoted.debug=0

        # Analysisd (server or local)
        analysisd.debug=0

        # Log collector (server, local or unix agent)
        logcollector.debug=0

        # Unix agentd
        agent.debug=0


    **Getting more log data** 

    If you are up to editing the source and recompiling, you can use the verbose() 
    function to add entries to the log. This has been helpful on at least one occasion 
    to help pinpoint where a problem was occurring. Something along these lines should 
    work (at least in 1.3):

    .. code-block:: c 

        verbose("MyName: inside the_file.c the_function() %s ..", the_string); 

    * If you tag all your extra logs with something, MyName, in this example, they 
      stand out better.
    * If you need to get information from several source files, including the file 
      name the_file.c, in this example is helpful.
    * You will almost surely want information from more than one fuction, including 
      the name, the_fuction() will show which function sent the log.
    * Finally, you can include a variable string with the printf format specifier %s 
      in the log entry and the_string is the name of the string variable to send to the log.
    
    With some calls to verbose, recompile and replace the stock binary with your edited 
    one. Restart ossec and tail the log.

#. The communication between my agent and the server is not working. What to do? 

    There are multiple reasons for it to happen. First, you should look at 
    your agent and server logs to see what they say.  If you don't know where they 
    are, go to our Troubleshooting page for more information. 

    In addition to that, follow the step by step at the end, if you need to add/re-add 
    the authentication keys.

    **There is a firewall between the agent and the server.**

    If you have the following message on the agent log:

    .. code-block:: console 

        2007/04/19 12:42:54 ossec-agentd(4101): Waiting for server reply (not started).
        2007/04/19 12:43:10 ossec-agentd(4101): Waiting for server reply (not started).
        2007/04/19 12:43:41 ossec-agentd(4101): Waiting for server reply (not started).
        2007/04/19 12:44:27 ossec-agentd(4101): Waiting for server reply (not started).

    And nothing on the server log, you probably have a firewall between the two 
    devices. Make sure to open port 1514 UDP between them (keeping state --the 
    agent connects to the server and expects a reply back).

    .. note:: 

        The way the agent/server communication works is that the agent starts a 
        connection to the server using any random high port. So, the only port that 
        OSSEC opens is in the server side (port 1514 UDP). It works similar to DNS, 
        where the DNS client connects to UDP port 53 and expects a reply back.

    **Wrong authentication keys configured (you imported a key from a different agent).**

    If that's the case, you would be getting logs similar to the above on the agent 
    and the following on the server (see also Errors:1403):

    .. code-block:: console 

        2007/05/23 09:27:35 ossec-remoted(1403): Incorrectly formated message from 'xxx.xxx.xxx.xxx'.
        2007/05/23 09:27:35 ossec-remoted(1403): Incorrectly formated message from 'xxx.xxx.xxx.xxx'.''

    **The IP address you configured the agent is different from what the server is seeing.**

    Same as above (see also see Errors:1403). 

    **Step by Step -- adding the authentication keys**

    For most of the errors (except the firewall issue), removing and re-adding the authentication keys 
    fix the problem. Do the following if you are having issues:

    #. 'Stop the server and the agent.'
        
        *  Make sure they are really stopped (ps on Unix or sc query ossecsvc on Windows)

    #. Run the manage-agents tool on the server and remove the agent.
    #. Still on the server, add the agent using manage-agents. Make sure the IP is correct.
    #. Start the server. 
    #.  Run manage-agents on the agent and import the newly generated key.
    #. Start the agent.

    If after that, it still doesn't work, contact our mailing list for help.

#. What does "1403 - Incorrectly formated message" means? 

    
