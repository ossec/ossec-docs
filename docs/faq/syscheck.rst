
Syscheck: FAQ
-------------

#. How to force an immediate syscheck scan?

    Run agent control tool to perform a integrity checking immediately (option 
    -a to run on all the agents and -u to specify an agent id)

    .. code-block:: console 

        # /var/ossec/bin/agent_control -r -a
        # /var/ossec/bin/agent_control -r -u <agent_id>

    For more infomation see the `Tool: Agent Control` documentation. 

#. How to tell syscheck not to scan the system when OSSEC starts?

    Set the option <scan_on_start> to “no” on ossec.conf 

#. How to ignore a file that changes too often?

    Set the file/directory name in the <ignore> option or create a simple local rule. 
    
    The following one will ignore files /etc/a and /etc/b and the directory /etc/dir 
    for agents mswin1 and ubuntu-dns:

    .. code-block:: xml 

        <rule id="100345" level="0" >
            <if_group>syscheck</if_group>
            <description>Changes ignored.</description>
            <match>/etc/a|/etc/b|/etc/dir</match>
            <hostname>mswin1|ubuntu-dns</hostname>
        </rule>

#. How to know when the syscheck scan ran?

    Use the agent_control tool on the manager, to see this information.

    More information see the `Tool: Agent Control` documentation. 

#. How to get detailed reporting on the changes?

    Use the syscheck_control tool on the manager or the web ui for that. 

    More information see the `Tool: Syscheck Control` documentation. 

