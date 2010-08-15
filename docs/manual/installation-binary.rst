.. _manual-install-binary:

Binary Installation 
===================

On some system a compatible compiler is not available, this leads to problems for OSSEC                                                                                      
standard install method. To work around this OSSEC supports being build on a different server
then it's been installed on. 

.. note:: 

    Due to they way OSSEC is built the system compiling OSSEC must be the same OS and the 
    same CPU platform for this work correctly. 

.. _manual-install-binary-build: 

Compiling OSSEC for install on a second server 
----------------------------------------------

First of all, download the OSSEC package corresponding to the version you want to 
install and unpack it (On the system with a compiler).

.. code-block:: console 

    # wget http://www.ossec.net/files/ossec-hids-latest.tar.gz  
    # tar -zxvf ossec-hids-latest.tar.gz 
    # rm ossec-hids-latest.tar.gz 

    
Enter in the source directory of the downloaded package and compile OSSEC. 

.. code-block:: console 

    # cd ossec-*/src
    # make setagent                
    # make all
    # make build
    # cd ../..

Change ossec-hids-*/etc/preloaded-vars.conf to set BINARY_INSTALL to yes. 

.. code-block:: console 

    # echo "USER_BINARYINSTALL=\"y\"" >> ossec-hids*/etc/preloaded-vars.conf

Finally create an OSSEC package.

.. code-block:: console 

    # tar -cvzf ossec-binary.tgz ossec-hids* 

.. _manual-install-binary-install: 

Installation of the binary OSSEC package 
----------------------------------------

On the target system (that does not have a c compiler) download your ossec-binary.tgz 
created in the setups above. 

.. code-block:: console 

    # cd /tmp
    # scp root@builder-server.example.com:/tmp/ossec-binary.tgz . 

Complete the installation by unarchiving the binary package and running ./install.sh. 

.. code-block:: console 

    # tar xfvz ossec-binary.tgz 
    # cd ossec-* 
    # ./install.sh 

After following the installation prompts you install will be complete.  



