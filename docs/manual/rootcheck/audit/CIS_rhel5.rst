.. cis_rhel5:


Center for Internet Security Benchmark for Red Hat Enterprise Linux 5 v1.1
==========================================================================


OSSEC Policy monitor can check if a system is in compliance with the
`CIS Security Benchmark for Red Hat Linux 5 <http://www.cisecurity.org/bench_linux.html>`_.

.. note:: 

  This benchmark only covers RHEL 5.0 and OSSEC will only test this system according to this standard.



Understand the test
-------------------

For every test that failed, you will receive an alert describing which section
of the benchmark that failed. For example:

.. code-block:: console

  System Audit: CIS - RHEL5 1.4 - Robust partition scheme - /var not on its own partition.

The above alert says that the system doesn't have a robust partition scheme as required
by the section ``1.4`` of the benchmark.

To receive more information about each section,
please visit `http://www.cisecurity.org/ <http://www.cisecurity.org/>`_ to download the benchmarks 
and learn how to solve the problem.


Downloading the Benchmark
-------------------------

The CIS RHEL Benchmark v1.1 is available at: `http://www.cisecurity.org/tools2/linux/CIS_RHEL5_Benchmark_v1.1.pdf <http://www.cisecurity.org/tools2/linux/CIS_RHEL5_Benchmark_v1.1.pdf>`_.



Update for RHEL6
----------------

the latest CIS benchmark for RHEL6 can be found here `https://github.com/ossec/ossec-hids/blob/master/src/rootcheck/db/cis_rhel6_linux_rcl.txt<https://github.com/ossec/ossec-hids/blob/master/src/rootcheck/db/cis_rhel6_linux_rcl.txt>`_.
