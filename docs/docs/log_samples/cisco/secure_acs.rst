Cisco Secure ACS
----------------

Cisco Secure ACS is an access control server which can be used for centralized authentication, authorization and accounting. The log files from this product can be very useful in security analysis and correlation.

Information about the logging facilities in the Windows version of the product (version 3.2) can be found `here <http://www.cisco.com/en/US/products/sw/secursw/ps2086/products_user_guide_chapter09186a0080205a5e.html>`_.

Here is a sample of the log file tracking failed login attempts : filename = Failed Attempt 2004-05-18.csv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Date,Time,Message-Type,User-Name,Group-Name,Caller-ID,Authen-Failure-Code,Author-Failure-Code,Author-Data,NAS-Port,NAS-IP-Address
  05/18/2004,02:11:03,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,15,10.27.3.1
  05/18/2004,02:11:31,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,16,10.27.3.1
  05/18/2004,02:12:40,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,17,10.27.3.1
  05/18/2004,02:12:50,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,18,10.27.3.1
  05/18/2004,02:13:00,Authen failed,bscorpio,punks,122.55.32.13,Windows password change failed,,,19,10.27.3.1
  05/18/2004,02:13:31,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,20,10.27.3.1
  05/18/2004,02:13:41,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,21,10.27.3.1
  05/18/2004,02:14:16,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,22,10.27.3.1
  05/18/2004,02:14:37,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,23,10.27.3.1
  05/18/2004,02:15:15,Authen failed,bscorpio,punks,122.55.32.13,External DB user invalid or bad password,,,24,10.27.3.1
  05/18/2004,08:14:32,Authen failed,bscorpio,punks,122.55.32.35,External DB user invalid or bad password,,,25,10.27.3.1

Here is a sample of the log file tracking successful logins : filename = Passed Authentications 2004-07-08.csv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Date,Time,Message-Type,User-Name,Group-Name,Caller-ID,NAS-Port,NAS-IP-Address
  07/08/2004,08:13:54,Authen OK,bplack,punks,198.47.27.99,106,10.27.3.1
  07/08/2004,08:19:17,Authen OK,bplack,punks,198.47.27.99,107,10.27.3.1
  07/08/2004,08:24:21,Authen OK,bplack,punks,198.47.27.99,108,10.27.3.1
  07/08/2004,08:31:17,Authen OK,bplack,punks,198.47.27.99,109,10.27.3.1
  07/08/2004,10:25:32,Authen OK,Dandre,punks,198.47.27.99,110,10.27.3.1
  07/08/2004,11:12:23,Authen OK,bplack,punks,198.47.27.99,111,10.27.3.1
  07/08/2004,11:15:59,Authen OK,bplack,punks,198.47.27.99,113,10.27.3.1
  07/08/2004,11:27:31,Authen OK,bplack,punks,198.47.27.99,114,10.27.3.1
  07/08/2004,11:38:25,Authen OK,bplack,punks,198.47.27.99,115,10.27.3.1
  07/08/2004,11:39:38,Authen OK,bplack,punks,198.47.27.99,116,10.27.3.1
  07/08/2004,13:15:08,Authen OK,bplack,punks,198.47.27.99,117,10.27.3.1
  07/08/2004,14:29:25,Authen OK,bplack,punks,198.47.27.99,118,10.27.3.1
  07/08/2004,14:47:56,Authen OK,bplack,punks,198.47.27.99,119,10.27.3.1
  07/08/2004,14:54:39,Authen OK,bretuwu,punks,198.47.27.99,120,10.27.3.1


The log files are stored in CSV (comma delimited). 

These samples were taken from the Cisco Secure ACS version 3.2 for Windows


