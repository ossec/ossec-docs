.. _faq_ossec_wui:

OSSEC-WUI: FAQ
--------------

.. contents:: 
    :local:


Why does the OSSE-WUI appear to be dead?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Because it is. No one has worked on it for quite a while. There may be some ongoing work with it, but as of this writing it is considered a dead project.


Why does the src ip field contain strange information instead of an IP?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Users who have installed OSSEC-WUI 0.3, have not applied the necessary patches, and are using OSSEC 2.6 or later may see alerts like the following:

   .. code-block:: console

      2013 Feb 02 10:48:42 Rule Id: 2901 level: 3
      Location: ubuntu->/var/log/dpkg.log 
      Src IP: 02 10:48:41 install libapr1 <none> 1.4.6-1
      New dpkg (Debian Package) requested to install.
      ** Alert 1359830922.3553: - syslog,dpkg,
      2013 Feb 02 10:48:42 ubuntu->/var/log/dpkg.log
      Rule: 2901 (level 3) -> 'New dpkg (Debian Package) requested to install.'
      2013-02-02 10:48:41 install libaprutil1 <none> 1.3.12+dfsg-3

    
   The alert format changed in 2.6, and since OSSEC-WUI is essentially abandonware it was not updated to handle the changes. 
   A number of users have provided patches to correct the issues, and the OSSEC team is planning on releasing an updated WUI containing these patches.
   You can find a patched version of the OSSEC-WUI at a `bitbucket repository <https://bitbucket.org/ddpbsd/ossec-wui>_`.
 

