
.. _ossec-regex:

ossec-regex
===========

``ossec-regex`` reads lines from stdin and prints the ones that match a pattern.
Put the pattern in single quotes so the shell does not change it.
Lines shorter than two characters are ignored. A line that does not match prints nothing.

By default the pattern is :ref:`OSSEC regex and match <regex>` syntax.
``-p`` tests the pattern as PCRE2, with the same flags as a ``<pcre2>`` rule
(caseless, and no OSSEC syntax translation). Use ``-p`` for ``<pcre2>`` and
``<match_pcre2>``. Without it, characters such as ``.``, ``*``, and ``{`` are
rewritten before matching.

Synopsis
~~~~~~~~

.. code-block:: console

   ossec-regex [-hp] [--] <pattern>

Options
~~~~~~~

.. program:: ossec-regex

.. option:: -h, --help

   Show help and exit.

.. option:: -p, --pcre2

   Match ``<pattern>`` as PCRE2. Compilation uses ``PCRE2_CASELESS``, the same
   flag analysisd uses for ``<pcre2>`` and ``<match_pcre2>``.

Output
~~~~~~

Without ``-p``, a match can print any of these lines:

* ``+OSRegex_Execute``
* ``+OS_Regex``
* ``+OSMatch_Compile``
* ``+OS_Match2``

With ``-p``, a match prints ``+OSPcre2_Execute`` (the rule path) and
``+OS_Pcre2`` (the one-shot helper, which also enables UTF matching).
Capture groups from ``+OSPcre2_Execute`` are printed as ``-Substring``.
A quantified group keeps its last capture.

Examples
~~~~~~~~

Legacy OSSEC regex:

.. code-block:: console

   # /var/ossec/bin/ossec-regex '^\d\d\d'
   333
   +OSRegex_Execute: 333
   +OS_Regex       : 333
   f44
   222
   +OSRegex_Execute: 222
   +OS_Regex       : 222

PCRE2, as used by a ``<pcre2>`` rule:

.. code-block:: console

   # /var/ossec/bin/ossec-regex -p 'user=(\w+)'
   login user=alice from 10.0.0.1
   +OSPcre2_Execute: login user=alice from 10.0.0.1
    -Substring: alice
   +OS_Pcre2       : login user=alice from 10.0.0.1

See also
~~~~~~~~

* :ref:`regex`
* :ref:`ossec-regex-convert`
