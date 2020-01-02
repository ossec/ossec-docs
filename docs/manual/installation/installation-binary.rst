.. _manual-install-binary:

Compiling OSSEC for a Binary Installation 
=========================================

OSSEC is typically compiled on each system it is installed on, but this may not always be easy. 
To help in these cases there are a few methods of binary installation available. OSSEC can be 
compiled on one system, and copied to the destination systems. This installation method still 
requires GNU make on the target system.

There are also RPM and deb packages available for some systems.



.. note:: 

    OSSEC has very limited cross compiling facilities. Windows binaries can be built on Linux systems, 
    but binaries for other systems should be built on a system of the same OS and CPU platform.

.. _manual-install-binary-build: 

Compiling OSSEC for install on a second server 
----------------------------------------------

First download the OSSEC package corresponding to the version you want to 
install and unpack it (on the system with a compiler).

.. code-block:: console 

    # wget -U ossec http://www.ossec.net/files/ossec-hids-2.8.1.tar.gz
    # tar -zxvf ossec-hids-latest.tar.gz 

    
Enter in the source directory of the downloaded package, and configure OSSEC to build the ``agent`` version.
The ``make`` commands should compile the correct binaries.

.. code-block:: console 

    # cd ossec-*/src
    # make setagent
    # make all
    # make build

Modify `ossec-hids-*/etc/preloaded-vars.conf` to set BINARY_INSTALL to yes. 

.. code-block:: console 

    # echo "USER_BINARYINSTALL=\"y\"" >> ossec-hids*/etc/preloaded-vars.conf

Finally create an OSSEC package.

.. code-block:: console 

    # tar -cvf ossec-binary.tar ossec-hids*

.. _manual-install-binary-install: 

Installation of the binary OSSEC package 
----------------------------------------

On the target system (that does not have a C compiler) download your ossec-binary.tar 
created in the steps above. 

Complete the installation by unarchiving the binary package and running ./install.sh. 

.. code-block:: console 

    # tar xfv ossec-binary.tar
    # cd ossec-* 
    # ./install.sh 

After following the installation prompts the install will be complete.  



.. Installing the OSSEC RPM
.. ------------------------

.. Installing the OSSEC deb
.. ------------------------
