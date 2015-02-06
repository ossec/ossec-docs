.. _cis_debian:

Center for Internet Security Benchmark for Debian Linux v1.0
============================================================

OSSEC Policy monitor can check if a system is in compliance with the
`CIS Security Benchmark for Debian <http://www.cisecurity.org/bench_linux.html>`_.
OSSEC will only test Debian and Ubuntu/Kubuntu/Xubuntu systems according to this
standard.


Understand the test
-------------------

For every test that failed, you will receive an alert describing which section
of the benchmark that failed. For example:

.. code-block:: console

  System Audit: CIS - Debian Linux 1.4 - Robust partition scheme - /var not on its own partition.


The above alert says that the system doesn't have a robust partition scheme as required
by the section ``1.4`` of the benchmark.


To receive more information about each section,
please visit `http://www.cisecurity.org <http://www.cisecurity.org/>`_ to download the benchmarks 
and learn how to solve the problem.


Downloading the Benchmark
-------------------------

The CIS Debian Benchmark v1.0 is available at: `http://www.cisecurity.org/tools2/linux/CIS_Debian_Benchmark_v1.0.pdf <http://www.cisecurity.org/tools2/linux/CIS_Debian_Benchmark_v1.0.pdf>`_.

