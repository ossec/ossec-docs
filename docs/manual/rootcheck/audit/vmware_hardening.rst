.. _vmware_hardening:


VMware Infrastructure 3 Security Hardening for ESX 3.5
======================================================

OSSEC Policy monitor can check if a system is in compliance with the
`VMware Infrastructure 3 Security Hardening guidelines for ESX 3.5 <http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf>`_.
This benchmark covers the virtual machines settings for ESX 3.0 and 3.5. In addition to that, since
the ESX runs on Red Hat Linux, we also perform the `Center for Internet Security Benchmark for Red Hat Enterprise Linux <CIS_rhel.html>`_ at the same time.



Understand the test
-------------------

For every test that failed, you will receive an alert describing which section
of the benchmark that failed. For example:

.. code-block:: console

  System Audit: System Audit: VMware ESX - VM settings - Copy operation between guest and console enabled. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/bart-RHEL5-svm/bart-RHEL5-svm.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .


The above alert says that the specified virtual machine enables copy operations between itself and the VM console.


To receive more information about each section,
please visit `http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf <http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf>`_ and look for guidelines on how to solve each issue reported.


Downloading the Benchmark
-------------------------

The `VMware Infrastructure 3 Security Hardening guidelines for ESX 3.5 <http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf>`_ is available at: `http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf <http://www.vmware.com/pdf/vi3_security_hardening_wp.pdf>`_.


Example output from the test
----------------------------

.. code-block:: console

  # /var/ossec/bin/rootcheck_control -i local

  System Audit: System Audit: VMware ESX - Testing against the Security Harderning benchmark VI3 for ESX 3.5. 
  File: /etc/vmware-release. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .

  System Audit: System Audit: VMware ESX - VM settings - Copy operation between guest and console enabled. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .

  System Audit: System Audit: VMware ESX - VM settings - Copy operation between guest and console enabled. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/bart-RHEL5-svm/bart-RHEL5-svm.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .

  System Audit: System Audit: VMware ESX - VM settings - Data Flow from the Virtual Machine to the Datastore not limited - Rotate size not 100KB. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/bart-RHEL5-build/bart-RHEL5-build.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .

  System Audit: System Audit: VMware ESX - VM settings - Unauthorized Removal or Connection of Devices allowed. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .

  System Audit: System Audit: VMware ESX - VM settings - Avoid Denial of Service Caused by Virtual Disk Modification Operations - diskWiper enabled. 
  File: /vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx. 
  Reference: http://www.ossec.net/wiki/index.php/SecurityHardening_VMwareESX .



