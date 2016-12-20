=========
Downloads
=========

Source Downloads
~~~~~~~~~~~~~~~~

+--------------+-----------------------------------------------+-------------+
| Latest development snapshots                                               |
+==============+===============================================+=============+
| Server/Agent | https://github.com/ossec/ossec-hids/releases                |
+--------------+-----------------------------------------------+-------------+
| Web UI       | https://github.com/ossec/ossec-wui/releases                 |
+--------------+-----------------------------------------------+-------------+
| Docs         | https://github.com/ossec/ossec-docs                         |
+--------------+-----------------------------------------------+-------------+

+---------------------+-----------------------------------------------+--------------------------+--------------+
| Latest Stable Release (2.8.3)                                                                  |              |
+=====================+===============================================+==========================+==============+
| Server/Agent Unix   | `ossec-hids-2.8.3.tar.gz`_ – `Release Notes`_ | `Unix Checksum`_         | `signature`_ |      
+---------------------+-----------------------------------------------+--------------------------+--------------+
| Agent Windows       | `ossec-agent-win32-2.8.3.exe`_                | `Win Checksum`_          |              |
+---------------------+-----------------------------------------------+--------------------------+--------------+
| Virtual Appliance   | `ossec-vm-2.8.3.ova`_ – `README`_             | `VA Checksum`_           |              |
+---------------------+-----------------------------------------------+--------------------------+--------------+
| Docker Container    | `wazuh/docker-ossec`_                         |                          |              |
+---------------------+-----------------------------------------------+--------------------------+--------------+

.. _ossec-hids-2.8.3.tar.gz: https://bintray.com/artifact/download/ossec/ossec-hids/ossec-hids-2.8.3.tar.gz
.. _Release Notes: https://bintray.com/ossec/ossec-hids/ossec-hids/view#release
.. _Unix Checksum: https://github.com/ossec/ossec-docs/blob/master/docs/whatsnew/checksums/2.8.3/ossec-hids-2.8.3.tar.gz.sha256
.. _signature: https://github.com/ossec/ossec-hids/releases/download/v2.8.3/ossec-hids-2.8.3.tar.gz.asc
.. _ossec-agent-win32-2.8.3.exe: https://bintray.com/artifact/download/ossec/ossec-hids/ossec-agent-win32-2.8.3.exe
.. _Win Checksum: https://github.com/ossec/ossec-docs/blob/master/docs/whatsnew/checksums/2.8.3/ossec-agent-win32-2.8.3.exe.sha256
.. _ossec-vm-2.8.3.ova: http://ossec.wazuh.com/vm/ossec-vm-2.8.3.ova
.. _README: http://ossec.wazuh.com/vm/ossec-vm-2.8.3.README
.. _VA Checksum: http://ossec.wazuh.com/vm/ossec-vm-2.8.3-checksum.txt
.. _wazuh/docker-ossec: https://hub.docker.com/r/wazuh/docker-ossec/


RPMs for RHEL, CentOS, Fedora and others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Available in the `Atomicorp repository <http://updates.atomicorp.com/channels/ossec/>`_.

+------------------------------------------------------------------------------------------------+
| CentOS / Redhat                                                                                |
+==============+=================================================================================+
| el5          | `i386 <http://updates.atomicorp.com/channels/ossec/centos/5/i386/RPMS/>`_       |
+--------------+---------------------------------------------------------------------------------+
| el5          | `x86_64 <http://updates.atomicorp.com/channels/ossec/centos/5/x86_64/RPMS/>`_   |
+--------------+---------------------------------------------------------------------------------+
| el6          | `i386 <http://updates.atomicorp.com/channels/ossec/centos/6/i386/RPMS/>`_       |
+--------------+---------------------------------------------------------------------------------+
| el6          | `x86_64 <http://updates.atomicorp.com/channels/ossec/centos/6/x86_64/RPMS/>`_   |
+--------------+---------------------------------------------------------------------------------+
| el7          | `i386 <http://updates.atomicorp.com/channels/ossec/centos/7/i386/RPMS/>`_       |
+--------------+---------------------------------------------------------------------------------+
| el7          | `x86_64 <http://updates.atomicorp.com/channels/ossec/centos/7/x86_64/RPMS/>`_   |
+--------------+---------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------------+
| Fedora                                                                                         |
+==============+=================================================================================+
| fc23         | `x86_64 <http://updates.atomicorp.com/channels/ossec/fedora/23/x86_64/RPMS/>`_  |
+--------------+---------------------------------------------------------------------------------+
| fc24         | `x86_64 <http://updates.atomicorp.com/channels/ossec/fedora/24/x86_64/RPMS/>`_  |
+--------------+---------------------------------------------------------------------------------+
| fc25         | `x86_64 <http://updates.atomicorp.com/channels/ossec/fedora/25/x86_64/RPMS/>`_  |
+--------------+---------------------------------------------------------------------------------+
| Legacy       | `6 - 22 <http://updates.atomicorp.com/channels/ossec/fedora/>`_                 |
+--------------+---------------------------------------------------------------------------------+

RPM Installation
================

Automated installer:

.. code:: console

    # wget -q -O – https://www.atomicorp.com/installers/atomic | sh
    # yum install ossec-hids ossec-hids-server (or ossec-hids-client for the agent)


PGP key
~~~~~~~

Before you install any package from our project, we recommend that you
verify it using our PGP key. Follow these two steps if you are not used
to using gpg. You first need to import our public key:

.. code:: console

    # wget https://ossec.github.io/files/OSSEC-ARCHIVE-KEY.asc
    # gpg –import OSSEC-ARCHIVE-KEY.asc

And then verify each file against its signature:

.. code:: console

    ossec-test# gpg –verify file.asc 

You should get the following result:


.. code:: console

    gpg: Signature made Tue 20 Dec 2016 11:35:58 AM EST using RSA key ID 2D8387B7
    gpg: Good signature from "Scott R. Shinn <scott@atomicorp.com>"
    Primary key fingerprint: B50F B194 7A0A E311 45D0  5FAD EE1B 0E6B 2D83 87B7


Note that the signing key was changed in December 2016. The previous signing key
"6F11 9E06 487A AF17 C84C E48A 456B 17CF A390 1351" has expired. If you get an warning 
saying “gpg: Note: This key has expired!”, make sure to update the key and run the 
“import” command again (as specified above).

Presentation Slides
~~~~~~~~~~~~~~~~~~~

Several of the OSSEC Project Team members have presented at conferences. 
Here is a collection of materials from some of those presentations.

+----------------------------------------------------------------------+
| `Decoding AWS CloudTrail with OSSEC`_                                |
+----------------------------------------------------------------------+
| `Log Analysis Using OSSEC`_                                          |
+----------------------------------------------------------------------+
| `Making the Most of OSSEC`_                                          |
+----------------------------------------------------------------------+
| `Malware Detection with OSSEC`_                                      |
+----------------------------------------------------------------------+
| `Open Source Security`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Active Response and Self Healing`_                            |
+----------------------------------------------------------------------+
| `OSSEC and OSSIM Unified Open Source Security`_                      |
+----------------------------------------------------------------------+
| `OSSEC at Scale`_                                                    |
+----------------------------------------------------------------------+
| `OSSEC Con 2012 Day 1`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Con 2012 Day 2`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Log Management with Elasticsearch`_                           |
+----------------------------------------------------------------------+
| `OSSEC PCI Solution 2.0`_                                            |
+----------------------------------------------------------------------+
 
.. _Decoding AWS CloudTrail with OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Decoding_AWS_CloudTrail_with_OSSEC.pptx
.. _Log Analysis Using OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Log_Analysis_using_OSSEC.pdf
.. _Making the Most of OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Making_the_Most_of_OSSEC.pdf 
.. _Malware Detection with OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Malware_Detection_with_OSSEC.pptx
.. _Open Source Security: https://bintray.com/artifact/download/ossec/ossec-presentations/OpenSourceSecurity_2013.pptx
.. _OSSEC Active Response and Self Healing: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Active_Response_and_Self_Healing.pdf
.. _OSSEC and OSSIM Unified Open Source Security: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_and_OSSIM_Unified_Open_Source_Security.pdf
.. _OSSEC at Scale: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_at_Scale.pdf
.. _OSSEC Con 2012 Day 1: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Con_2012-day-1.pdf
.. _OSSEC Con 2012 Day 2: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Con_2012-day-2.pdf
.. _OSSEC Log Management with Elasticsearch: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Log_Mangement_with_Elasticsearch.pptx
.. _OSSEC PCI Solution 2.0: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_PCI_Solution_2.0.pdf

Contribute back!
~~~~~~~~~~~~~~~~

If you find ossec useful and would like to contribute back to the
community, please contact us. We have a lot of work to do and any help
is appreciated.


|
