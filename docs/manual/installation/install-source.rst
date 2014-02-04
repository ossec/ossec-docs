.. _install:

Manager/Agent Installation
==========================


Installation of OSSEC HIDS is very simple. Just follow these few steps to have 
it working.  
 
It is important to choose the correct installation type: server, agent, local, or hybrid.
More information on thse can be found on the `OSSEC Architecture page <../ossec-architecture.html>`_.

.. warning::

    Remember that when following this installation the commands only start after the # Everything 
    before that is just the information about the prompt

.. note::
   
    If you have experience with Unix, just download the latest version, uncompress it and run the 
    "./install.sh" script.

#. Download the latest version and verify its checksum.

    .. note:: 

        On some systems, the command md5, sha1 or wget may not exist, so try md5sum, sha1sum 
        or lynx respectively instead.

    .. code-block:: console

        # wget http://www.ossec.net/files/ossec-hids-2.7.1.tar.gz
        # wget http://www.ossec.net/files/ossec-hids-2.7.1_checksum.txt
        # cat ossec-hids-2.7.1_checksum.txt
        MD5 (ossec-hids-2.7.1.tar.gz) = f4140ecf25724b8e6bdcaceaf735138a
        SHA1 (ossec-hids-2.7.1.tar.gz) = 258b9a24936e6b61e0478b638e8a3bfd3882d91e
        MD5 (ossec-agent-win32-2.7.1.exe) = 7d2392459aeab7490f28a10bba07d8b5
        SHA1 (ossec-agent-win32-2.7.1.exe) = fdb5225ac0ef631d10e5110c1c1a8aa473e62ab4
        # md5sum ossec-hids-2.7.1.tar.gz 
        MD5 (ossec-hids-2.7.1.tar.gz) = f4140ecf25724b8e6bdcaceaf735138a
        # sha1sum ossec-hids-2.7.1.tar.gz
        SHA1 (ossec-hids-2.7.1.tar.gz) = 258b9a24936e6b61e0478b638e8a3bfd3882d91e


#. Extract the compressed package and run the “./install.sh” script (It will guide you 
   through the installation).

    .. code-block:: console 

        # tar -zxvf ossec-hids-*.tar.gz (or gunzip -d; tar -xvf)
        # cd ossec-hids-* 
        # ./install.sh

#. Remember to open port 1514 (UDP) if there is a firewall between the server and 
   the agents (not applicable to the local installation type).

#. If you are installing the server or the agent, remember to follow the `Managing 
   the agents section`.

#. Start OSSEC HIDS 

    .. code-block:: console 

        # /var/ossec/bin/ossec-control start  




