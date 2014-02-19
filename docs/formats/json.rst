###########
JSON Format
###########

At this time we have one alert JSON formatted messages. 

.. code-block:: json

    {
      "rule":1000,
      "level":1,
      "comment":"This is a comment",
      "sidid":1111,
      "cve":"cve-1001-1000",
      "action":"drop",
      "srcip":"10.1.1.1",
      "srcport":"1000",
      "srcuser":"root",
      "dstip":"10.2.2.2",
      "dstport":"2000",
      "dstuser":"root",
      "location":"/var/log/auth.log",
      "full_log":"This is the full log message",
      "file":{
        "path":"/etc/",
        "md5_before":"XXXXXXXXXXXXXXXXXXXX",
        "md5_after":"YYYYYYYYYYYYYYYYYYYY",
        "sha1_before":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "sha1_after":"YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
        "owner_before":"root",
        "owwer_after":"nobody",
        "gowner_before":"root",
        "gowner_after":"nodody",
        "perm_before":660,
        "perm_after":777, 
      }
    }

