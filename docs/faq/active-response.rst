.. _faq_active_response:

Active response
===============

Why is active response not running?
-----------------------------------

Active response only runs **after** a matching alert is generated. If no rule fires,
no script executes — for example, a SYN flood may not produce SSH authentication
failure alerts unless you have rules for that traffic.

Checklist:

1. **Execd is running** — on the host where the script should run:

   .. code-block:: console

      /var/ossec/bin/ossec-control status

   ``ossec-execd`` must be listed as running.

2. **Rule and binding match** — the alert must meet ``level``, ``rules_id``, or
   ``rules_group`` in your ``<active-response>`` block. Test with
   :ref:`ossec-logtest`.

3. **Location is correct** — ``local`` runs on the agent that generated the event;
   ``server`` runs on the manager; ``defined-agent`` requires ``agent_id``.

4. **Command is configured** — a ``<command>`` block must define the ``executable``
   (script name under ``active-response/bin``) and link to the ``<active-response>``
   via ``<command>name</command>``.

5. **Script is executable** — the file must exist in ``/var/ossec/active-response/bin/``
   with execute permission for the ``ossec`` user.

6. **Not disabled** — check for ``<disabled>yes</disabled>`` on that binding or
   ``<disable-active-response>yes</disable-active-response>`` in the agent ``<client>``
   section. See :ref:`manual-ar`.

7. **Restart after changes** — restart OSSEC on affected hosts after editing
   ``ossec.conf``.

How do I test an active-response binding?
-----------------------------------------

Use :ref:`ossec-logtest` with a sample log line that triggers your rule, then
confirm ``ossec.log`` on the execution host shows the active-response command
invoked. For firewall blocks, verify the block script logged success and the IP
appears in the expected deny list or table.

Where are example active-response configurations?
---------------------------------------------------

See :ref:`manual-ar-unix`, :ref:`ossec_config.active-response`, and the bundled
scripts reference at :ref:`manual-ar-scripts`.

Why does my script see ``add`` and ``-`` instead of srcip/username?
-------------------------------------------------------------------

Active-response scripts always receive a fixed argument list. ``<expect>``
only chooses which decoded fields are filled (vs ``-``); it does **not** put
``srcip`` in ``$1``.

======= ==========================================================
Arg     Value
======= ==========================================================
``$1``  action (``add`` or ``delete``)
``$2``  username from the alert, or ``-``
``$3``  srcip from the alert, or ``-``
``$4``  alert id
``$5``  rule id
``$6``  agent / location
``$7``  filename, or ``-``
======= ==========================================================

So ``$1`` will be ``add`` even when expect is ``srcip, username``. Use ``$3``
for the IP and ``$2`` for the user. List ``srcip`` / ``user`` (or ``username``)
in ``<expect>`` so those fields are populated from the decoder. Username is
taken from ``dstuser``, or ``srcuser`` if ``dstuser`` is absent.
