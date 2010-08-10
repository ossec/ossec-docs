
.. _install_req:

Installations requirements
==========================

UNIX
==== 

For UNIX systems, ossec just requires gcc and glibc. However, 
you always have the option to pre-compule it on any other system and 
move the binaries to the final box. 

Ubuntu
------

Ubuntu you will need build *build-essential* in order to compile and install ossec. 

To install the package run the following command.  

.. code-block:: console

    # apt-get install build-essential 

If database support is needed also run the following command. 

.. code-block:: console 

    # apt-get install mysql-dev postgresql-dev  

RedHat
------ 

RedHat should have all packages needed by default, but if database support is need 
the package mysql-devel and/or postgresql-devel will need to be installed. 

.. code-block:: console 

    # yum install mysql-devel postgresql-devel 


