.. _doc-maintenance:

Documentation maintenance
=========================

When changing ``ossec-hids``, update ``ossec-docs`` in the same release cycle when:

* **Config parsers** (``src/config/*.c``) gain or change XML elements → update the
  matching ``docs/syntax/ossec_config.*.trst`` file.
* **``internal_options.conf``** keys change → update ``docs/syntax/internal_options.*.trst``.
* **Breaking changes** → update :ref:`upgrade-migration` and ``changelog.rst``.
* **New CLI tools** in ``src/util/`` → add a page under ``docs/programs/``.

Build locally:

.. code-block:: console

   pip install -r requirements.txt
   make html

HTML output is written to ``_build/html/``.

Config audit checklist
----------------------

Compare parser XML tag names in ``src/config/`` against ``docs/syntax/*.trst``:

+----------------------+--------------------------------+
| Parser               | Documentation                  |
+======================+================================+
| ``global-config.c``  | ``ossec_config.global.trst``   |
| ``localfile-config.c`` | ``ossec_config.localfile.trst`` |
| ``remote-config.c``  | ``ossec_config.remote.trst``   |
| ``client-config.c``  | ``ossec_config.client.trst``   |
| ``syscheck-config.c`` | ``ossec_config.syscheck.trst`` |
+----------------------+--------------------------------+

Compare ``etc/internal_options.conf`` keys against ``docs/syntax/internal_options.*.trst``.
