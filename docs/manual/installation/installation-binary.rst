.. _manual-install-binary:

Binary Installation 
===================

On some systems a compatible compiler is not available, this leads to problems for the
standard OSSEC install method. To work around this OSSEC supports multiple methods of binary installation.
One is building OSSEC on one system and installing it on another. A second method is installation via RPM.
Debian packages are also planned.

.. note:: 

    OSSEC has very limited cross compiling facilities. Windows binaries can be built on Linux systems, 
    but binaries for other systems should be built on a system of the same CPU platform.

.. _manual-install-binary-build: 

Compiling OSSEC for install on a second server 
----------------------------------------------

First download the OSSEC package corresponding to the version you want to 
install and unpack it (on the system with a compiler).

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

Modify ossec-hids-*/etc/preloaded-vars.conf to set BINARY_INSTALL to yes. 

.. code-block:: console 

    # echo "USER_BINARYINSTALL=\"y\"" >> ossec-hids*/etc/preloaded-vars.conf

Finally create an OSSEC package.

.. code-block:: console 

    # tar -cvzf ossec-binary.tgz ossec-hids* 

.. _manual-install-binary-install: 

Installation of the binary OSSEC package 
----------------------------------------

On the target system (that does not have a C compiler) download your ossec-binary.tgz 
created in the setups above. 

.. code-block:: console 

    # cd /tmp
    # scp root@builder-server.example.com:/tmp/ossec-binary.tgz . 

Complete the installation by unarchiving the binary package and running ./install.sh. 

.. code-block:: console 

    # tar xfvz ossec-binary.tgz 
    # cd ossec-* 
    # ./install.sh 

After following the installation prompts your install will be complete.  



