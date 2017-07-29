.. _install-mingw: 

This is an example of installing MinGW and required packages for compiling the OSSEC Windows Agent on CentOS 7.

.. code-block:: console

   # yum install epel-release
   # yum makecache fast
   # yum install mingw32-gcc.x86_64
   # yum install mingw32-nsis.x86_64
   # cd /home/user/ossec-hids-master/src
   # make clean
   # make TARGET=winagent
   # cd win32
