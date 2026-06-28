===================
OSSEC Documentation
===================

OSSEC is an Open Source Host-based Intrusion Detection System. It performs log analysis,
integrity checking, Windows registry monitoring, rootkit detection, real-time alerting
and active response. It runs on most operating systems, including Linux, OpenBSD,
FreeBSD, Mac OS X, Solaris and Windows. A list with all supported platforms is available
at: :ref:`supported-systems`

.. note::

   `OSSEC+ <https://www.ossec.net/ossec-downloads/>`_ extends OSSEC with additional
   capabilities such as ELK integration, community threat sharing, and machine learning.
   Registration is free.

Getting Started
===============

.. toctree::
   :maxdepth: 2

   docs/manual/non-technical-overview
   docs/manual/ossec-architecture
   docs/manual/supported-systems

Manual
======


.. toctree::
   :maxdepth: 2
   :glob:

   docs/manual/index

Reference
=========

.. toctree::
    :maxdepth: 2

    docs/syntax/index
    docs/programs/index
    docs/formats/index
    docs/examples/index
    docs/log_samples/index

Release Notes
=============

.. toctree::
    :maxdepth: 1

    changelog

FAQ & Cookbooks
===============

.. toctree::
   :maxdepth: 2
   :glob:

   docs/faq/index
   docs/cookbooks/index

Development
===========

.. toctree::
   :maxdepth: 2
   :glob:

   docs/development/build/index
   docs/development/gpg/index
   docs/development/oRFC/index
   docs/development/doc-maintenance
   about/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
