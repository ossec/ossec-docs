###########
JSON Format
###########

OSSEC can write alerts in JSON format to ``/var/ossec/logs/alerts/alerts.json`` when
``jsonout_output`` is enabled in ``<global>``. Each line is one JSON object.

Enable JSON output
------------------

.. code-block:: xml

   <global>
     <jsonout_output>yes</jsonout_output>
   </global>

Example alert
-------------

.. code-block:: json

   {
     "timestamp": "2026-06-28T12:00:00.000+0000",
     "rule": {
       "level": 5,
       "description": "SSHD authentication success.",
       "id": "5715",
       "groups": ["syslog", "sshd", "authentication_success"]
     },
     "agent": {
       "id": "001",
       "name": "agent01"
     },
     "manager": {
       "name": "ossec-manager"
     },
     "id": "1234567890.12345",
     "full_log": "Jun 28 12:00:00 agent01 sshd[1234]: Accepted publickey for user",
     "decoder": {
       "name": "sshd"
     },
     "location": "/var/log/auth.log"
   }

Common fields
-------------

+------------------+----------------------------------------------------------+
| Field            | Description                                              |
+==================+==========================================================+
| ``timestamp``    | When OSSEC processed the event                           |
| ``rule.level``   | Alert severity (0–16)                                    |
| ``rule.id``      | Rule ID that matched                                     |
| ``rule.description`` | Rule text                                            |
| ``rule.groups``  | Rule groups (also exposed as ``rule.group`` in some builds) |
| ``agent.id``     | Agent ID (manager/local if absent)                       |
| ``agent.name``   | Agent hostname                                           |
| ``full_log``     | Original log line or message                             |
| ``srcip``        | Source IP when extracted by decoder                      |
| ``dstuser``      | Destination user when extracted                          |
| ``location``     | Log source path or label                                 |
| ``syscheck``     | FIM details when present (hashes, paths, ownership)      |
| ``GeoLocation``  | Present when GeoIP is enabled and ``analysisd.geoip_jsonout=1`` |
+------------------+----------------------------------------------------------+

File integrity (syscheck) alerts may include ``md5``, ``sha1``, and ``sha256`` before/after
fields inside the ``syscheck`` object.

Also see :ref:`manual-out-json` and :doc:`alerts </docs/formats/alerts>`.
