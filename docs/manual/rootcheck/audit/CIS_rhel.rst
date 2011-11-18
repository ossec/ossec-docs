.. _cis_rhel:


Center for Internet Security Benchmark for Red Hat Enterprise Linux v1.0.5
==========================================================================


OSSEC Policy monitor can check if a system is in compliance with the
`CIS Security Benchmark for Red Hat Linux <http://www.cisecurity.org/bench_linux.html>`_.

.. note::

  This benchmark only covers RHEL 2.1, 3.0, 4.0 and Fedora Core 1,2,3,4 and 5. Because of that, OSSEC will only test these systems according to this standard.


Understand the test
-------------------

For every test that failed, you will receive an alert describing which section
of the benchmark that failed. For example:

.. code-block:: console

  System Audit: CIS - Red Hat Linux 1.4 - Robust partition scheme - /var not on its own partition.

The above alert says that the system doesn't have a robust partition scheme as required
by the section ``1.4`` of the benchmark.

To receive more information about each section,
please visit `http://www.cisecurity.org/ <http://www.cisecurity.org/>`_ to download the benchmarks 
and learn how to solve the problem.


Downloading the Benchmark
-------------------------

The CIS RHEL Benchmark v1.0.5 is available at: `http://www.cisecurity.org/tools2/linux/CIS_RHLinux_Benchmark_v1.0.5.pdf <http://www.cisecurity.org/tools2/linux/CIS_RHLinux_Benchmark_v1.0.5.pdf>`_.

