
.. _manual-win-install: 

Windows Agent Installation 
==========================

.. note::

   OSSEC only supports Windows systems as agents, and they
   will require an OSSEC server to function.

Step 1: Opening the Agent Manger menu
-------------------------------------
The first step of this process is to get into the Agent Manager menu. From the ossec server, type the following command::

/var/ossec/bin/manage_agents

The menu should look like this::

         ****************************************
         * OSSEC HIDS v2.5-SNP-100809 Agent manager.*
         * The following options are available:*
         ***************************************

         (A)dd an agent (A).
         (E)xtract key for an agent (E).
         (L)ist already added agents (L).   
         (R)emove an agent (R).   
         (Q)uit.
         Choose your action: A,E,L,R or Q:


Step 2: Adding an Agent
-----------------------
Adding an agent is the first thing that needs to be done. Choose action "A". 

The agent manager first asks for a name::

            Adding a new agent (use '\q' to return to the main menu).  
            Please provide the following:   * A name for the new agent: 


Next, it asks for the IP address of the client::

         The IP Address of the new agent:


After that, it asks for a unique ID to assign to the client. The ID must be all numerical with a maximum of eight digits::

         An ID for the new agent[001]:


Lastly, it asks for confirmation of all the information provided. Then it appends all of the agent information to /var/ossec/etc/client.keys and returns to the main menu.  

Step 3: Extracting a Key
------------------------
Now, the client key needs to be extracted. From the main menu, choose action "E". A list of agents will be displayed::
        
         Available agents:   ID: 001, Name: agent1, IP: 10.10.50.2
         Provide the ID of the agent to extract the key (or '\q' to quit): 

Enter the full ID of the agent to extract the key for. It will display the entire key. Copy that to the clipboard, for it will be needed later:: 

         Agent key information for '001' is:MDAyIGFnZW50MSAxOTIuMTY4LjIuMC8yNCBlNmY3N2RiMTdmMTJjZGRmZjg5YzA4ZDk5m


Step 4: The Windows Side
------------------------
Next up, download the executable from https://ossec.github.io/downloads.html. Run through the install wizard with all defaults. It should launch the Ossec Agent Manager when it's done. The Ossec Agent Manager looks like this: 

![Screenshot](OSSEC-Agent-Manager-Windows.png)

Enter the IP address of your ossec server in the first text field, and enter the extracted key that was copied to the clipboard earlier to the second textfield. Finally, click on the manage tab and hit restart. 
