
.. _install_req:

Installations requirements
==========================

UNIX
==== 

For UNIX systems, OSSEC just requires gcc and libc. However, 
you always have the option to pre-compile it on one system and 
move the binaries to the final box. 

Ubuntu
------

On Ubuntu you will need the *build-essential* package in order to compile and install OSSEC. 

To install the package run the following command.  

.. code-block:: console

    # apt-get install build-essential 

If database support is needed *mysql-dev* or *postgresql-dev* should be installed. 
Run the following command to install these packages. 

.. code-block:: console 

    # apt-get install mysql-dev postgresql-dev  

RedHat
------ 

RedHat should have all packages needed by default, but if database support is needed
the package mysql-devel and/or postgresql-devel will need to be installed. 

.. code-block:: console 

    # yum install mysql-devel postgresql-devel 


