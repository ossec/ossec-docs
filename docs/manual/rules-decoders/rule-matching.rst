.. _manual-rule-matching:

How OSSEC matches rules
=======================

OSSEC does **not** simply scan every rule from highest alert level to lowest.
Matching uses a **rule tree** filtered by the event's decoder category, with
sibling order influenced by level. Understanding that order helps when writing
overrides, suppressions (level 0), and custom child rules.

Overview
--------

When an event is decoded, analysisd:

1. Selects eligible **top-level** rules whose category matches the decoder type
   (for example syslog vs Windows vs web-log).
2. Walks a **parent/child tree**. Children are attached with ``if_sid``,
   ``if_group``, or related options; a more specific child that matches is
   preferred over stopping at the parent alone.
3. Among **siblings** (rules at the same depth under the same parent, or
   top-level peers), rules are ordered **higher level first**. At the same
   level, earlier load order wins (generally the order rules appear in the
   configured rules files).
4. If a matching rule has **level 0**, processing stops and no alert is
   generated (used to ignore or suppress events).

So “same alert level” ties are decided by tree position and load order, not by
rule id alone.

Parent and child rules
----------------------

Most useful rules are children of a grouping parent. For example, a parent may
match “sshd messages” at a low or zero level, and children match “failed
password,” “invalid user,” and so on via ``<if_sid>``.

When writing a custom suppression or more specific alert:

* Prefer a child of the existing parent (``<if_sid>`` of that parent or of the
  rule you want to refine).
* Use **level 0** on a child that matches the noisy case so that rule wins and
  stops further alerting for that event.

Level and load order
--------------------

Within a sibling list, analysisd inserts rules so that **higher levels come
first**. Equal levels keep the order they were loaded.

Practical consequences:

* Two unrelated top-level rules at the same level are not compared by id; the
  one that appears earlier in the loaded rule set is tried first (after
  category filtering).
* A high-level child under the correct parent is tried before lower-level
  siblings under that parent.
* Level 0 is special when it **matches**: it ends evaluation for that event.
  It is not a separate global “scan all level 0 rules first across every
  category” pass outside the normal tree walk.

Decoder category matters
------------------------

Rules are only considered when their category aligns with the decoder type for
the event. A perfectly written syslog rule will not match a Windows Event Log
event, and vice versa. If ``ossec-logtest`` never reaches your rule, check
decoding and category before worrying about level order.

Seeing the order for a real log line
------------------------------------

Use ``ossec-logtest`` with verbose rule debugging:

.. code-block:: console

    # /var/ossec/bin/ossec-logtest -v

Paste one log line. The output shows which rules are attempted and which
matched. That is the authoritative order for that event on your manager.

See also :doc:`testing` and :ref:`manual-rule-levels`.

Related discussion: `OSSEC mailing list thread on rule order
<https://groups.google.com/forum/#!topic/ossec-list/yi3Ts5MaqH4>`_.
