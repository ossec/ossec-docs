.. _install:

Manager/Agent Installation
==========================


Installation of the OSSEC HIDS is very simple. Just follow these few steps to have 
it working.  Please make sure that you understand the type of installation you are choosing 
(manager, agent, local, or hybrid) and are also aware of the order (always install the manager 
first). If you donâ€™t know what Iâ€™m talking about, itâ€™s a good idea to visit the `install types
page`.

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
        # md5sum ossec-hids-2.7.1.tar.gz 
        MD5 (ossec-hids-2.7.1.tar.gz) = f4140ecf25724b8e6bdcaceaf735138a
        # sha1sum ossec-hids-2.7.1.tar.gz
        SHA1 (ossec-hids-2.7.1.tar.gz) = 258b9a24936e6b61e0478b638e8a3bfd3882d91e


#. Extract the compressed package and run the ``install.sh`` script. It will guide you 
   through the installation.

    .. code-block:: console 

        # tar -zxvf ossec-hids-*.tar.gz (or gunzip -d; tar -xvf)
        # cd ossec-hids-* 
        # ./install.sh

#. Remember to open port 1514 (UDP) if there is a firewall between the server and 
   the agents (not applicable to the local installation type).

#. If you are installing the server or the agent, remember to follow the `Managing 
   the agents section <../agent/agent-management.html>`_.

#. Start OSSEC HIDS 

    .. code-block:: console 

        # /var/ossec/bin/ossec-control start  


install.sh walkthrough
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console
   
   # ./install.sh
   
     ** Para instalaÃ§Ã£o em portuguÃªs, escolha [br].
     ** è¦ä½¿ç¨ä¸­æè¿¡å®è£, \xe8\xaf\xb7\xe9\xe6\xa9 [cn].
     ** Fur eine deutsche Installation wohlen Sie [de].
     ** ÎÎ¹Î± ÎµÎ³ÎºÎ±Ï\xce\xac\xcf\xcf\xce\xb1\xcf\xce\xb7 \xcf\xcf\xce\xb1 \xce\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac, \xce\xb5\xcf\xce\xb9\xce\xbb\xce\xad\xce\xbe\xcf\xce\xb5 [el].
     ** For installation in English, choose [en].
     ** Para instalar en EspaÃ±ol , eliga [es].
     ** Pour une installation en franÃ§ais, choisissez [fr]
     ** A Magyar nyelvÅ± telepÃ­tÃ©shez vÃ¡lassza [hu].
     ** Per l'installazione in Italiano, scegli [it].
     ** æ¥æ¬èª§ã¤ã³ã¹ãã¼ã«ãã¾ãï¼é¸æã¦ä¸ãã\xef\xbc[jp].
     ** Voor installatie in het Nederlands, kies [nl].
     ** Aby instalowaÄ w jÄzyku Polskim, wybierz [pl].
     ** ÐÐ»Ñ Ð¸Ð½ÑÑÑÑÐºÑÐ¸Ð¹ Ð¿Ð¾ ÑÑÑÐ°Ð½Ð¾Ð²ÐºÐµ Ð½Ð° ÑÑÑÑÐºÐ¾Ð¼ ,Ð²Ð²ÐµÐ´Ð¸ÑÐµ [ru].
     ** Za instalaciju na srpskom, izaberi [sr].
     ** TÃ¼rkÃ§e kurulum iÃ§in seÃ§in [tr].
     (en/br/cn/de/el/es/fr/hu/it/jp/nl/pl/ru/sr/tr) [en]: 
   
   
   OSSEC HIDS v2.7.1 Installation Script - http://www.ossec.net
    
    You are about to start the installation process of the OSSEC HIDS.
    You must have a C compiler pre-installed in your system.
    If you have any questions or comments, please send an e-mail
    to dcid@ossec.net (or daniel.cid@gmail.com).
   
     - System: OpenBSD arrakis.example.com 5.5
     - User: root
     - Host: arrakis.example.com
   
     -- Press ENTER to continue or Ctrl-C to abort. --
   
   1- What kind of installation do you want (server, agent, local, hybrid or help)? 
   
     - Server installation chosen.
   
    - Choose where to install the OSSEC HIDS [/var/ossec]:
   
       - Installation will be made at  /var/ossec
   
   2- Setting up the installation environment.
   
    - Choose where to install the OSSEC HIDS [/var/ossec]: /var/ossec
   
       - Installation will be made at  /var/ossec .
   
   3- Configuring the OSSEC HIDS.
   
     3.1- Do you want e-mail notification? (y/n) [y]: 
      - What's your e-mail address? ddp@localhost
      - What's your SMTP server ip/host? 127.0.0.1
   
     3.2- Do you want to run the integrity check daemon? (y/n) [y]: 
   
      - Running syscheck (integrity check daemon).
   
     3.3- Do you want to run the rootkit detection engine? (y/n) [y]: 
   
      - Running rootcheck (rootkit detection).
   
     3.4- Active response allows you to execute a specific 
          command based on the events received. For example,
          you can block an IP address or disable access for
          a specific user.  
          More information at:
          http://www.ossec.net/en/manual.html#active-response
          
      - Do you want to enable active response? (y/n) [y]: 
   
        - Active response enabled.
      
      - By default, we can enable the host-deny and the 
        firewall-drop responses. The first one will add
        a host to the /etc/hosts.deny and the second one
        will block the host on iptables (if linux) or on
        ipfilter (if Solaris, FreeBSD or NetBSD).
      - They can be used to stop SSHD brute force scans, 
        portscans and some other forms of attacks. You can 
        also add them to block on snort events, for example.
   
      - Do you want to enable the firewall-drop response? (y/n) [y]:
   
        - firewall-drop enabled (local) for levels >= 6
   
      - Default white list for the active response:
         - 127.0.0.1
         - 127.0.0.1
   
      - Do you want to add more IPs to the white list? (y/n)? [n]: 
   
     3.5- Do you want to enable remote syslog (port 514 udp)? (y/n) [y]: n
   
      --- Remote syslog disabled.
   
     3.6- Setting the configuration to analyze the following logs:
       -- /var/log/messages
       -- /var/log/authlog
       -- /var/log/secure
       -- /var/log/xferlog
       -- /var/log/maillog
   grep: repetition-operator operand invalid
       -- /var/log/snort/alert (snort-fast file)
   
    - If you want to monitor any other file, just change 
      the ossec.conf and add a new localfile entry.
      Any questions about the configuration can be answered
      by visiting us online at http://www.ossec.net .
      
      
      --- Press ENTER to continue ---
   
   5- Installing the system
    - Running the Makefile
   INFO: Little endian set.
   
    *** Making zlib (by Jean-loup Gailly and Mark Adler)  *** 
   gcc -c -g -Wall -I../../ -I../../headers  -DDEFAULTDIR=\"/var/ossec\" -DUSE_OPENSSL      -DARGV0=\"zlib\" -DXML_VAR=\"var\" -DOSSECHIDS *.c
   
   COMPILATION COMPILATION COMPILATION
   
   
   
    - System is OpenBSD.
    - Init script modified to start OSSEC HIDS during boot.
   
    - Configuration finished properly.
   
    - To start OSSEC HIDS:
                   /var/ossec/bin/ossec-control start
   
    - To stop OSSEC HIDS:
                   /var/ossec/bin/ossec-control stop
   
    - The configuration can be viewed or modified at /var/ossec/etc/ossec.conf
   
   
       Thanks for using the OSSEC HIDS.
       If you have any question, suggestion or if you find any bug,
       contact us at contact@ossec.net or using our public maillist at
       ossec-list@ossec.net
       ( http://www.ossec.net/main/support/ ).
   
       More information can be found at http://www.ossec.net
   
       ---  Press ENTER to finish (maybe more information below). ---
  



 
