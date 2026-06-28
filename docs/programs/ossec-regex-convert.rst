
.. _ossec-regex-convert:

ossec-regex-convert
===================

``ossec-regex-convert`` converts OSSEC legacy regex XML tags to PCRE2 equivalents in
decoder and rule files. Use it when migrating custom decoders from pre-PCRE2 formats.

Synopsis
~~~~~~~~

.. code-block:: console

   ossec-regex-convert [-b] [-r|-m] [-t] [pattern]

Options
~~~~~~~

.. program:: ossec-regex-convert

.. option:: -h, --help

   Display help and exit.

.. option:: -b, --batch

   Batch mode: read patterns from stdin, one per line.

.. option:: -r, --regex

   Convert ``regex`` / ``prematch`` style patterns (default).

.. option:: -m, --match

   Convert ``match`` style patterns.

.. option:: -t, --tags

   List supported XML tag mappings and exit.

Tag mappings
~~~~~~~~~~~~

Common conversions include ``regex`` → ``pcre2``, ``match`` → ``match_pcre2``,
``program_name`` → ``program_name_pcre2``, ``prematch`` → ``prematch_pcre2``, and
similar mappings for GeoIP, port, user, url, and status fields.

Examples
~~~~~~~~

Convert a single pattern:

.. code-block:: console

   ossec-regex-convert "failed password for"

List all supported tag names:

.. code-block:: console

   ossec-regex-convert -t

See also
~~~~~~~~

* :ref:`regex`
* :ref:`rules_decoders`
* :ref:`rules.rules`
