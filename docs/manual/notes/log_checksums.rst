How do the log checksums work?

*by `Daniel B. Cid <http://www.ossec.net/dcid Daniel B. Cid>`_*
*Taken from `OSSEC blog <http://www.ossec.net/dcid/?p=74>`_*


Starting with version 1.2, OSSEC will come with support for daily/chained checksums enabled by default. 

Basically, what it means is that at the end of each day, ossec will generate the md5/sha1 sum of the 
currently logs plus the md5/sha1 sum of the checksum from the logs of the previous day.

To exemplify, at the end of Apr 23, ossec will create the following file:

.. code-block:: console

  # pwd
  /var/ossec/logs/alerts/2007/Apr
  # cat ossec-alerts-23.log.sum
  Current checksum:
  MD5  (/logs/alerts/2007/Apr/ossec-alerts-23.log) =
  7a275b2d07a5aac500c78c7af51de457
  SHA1 (/logs/alerts/2007/Apr/ossec-alerts-23.log) =
  af560a60bfb9fde5944c4bfc36fedfb16a1956d5

  Chained checksum:
  MD5  (/logs/alerts/2007/Apr/ossec-alerts-22.log.sum) =
  2ab5d8637e9f63493d2f3f3a9b06b17f
  SHA1 (/logs/alerts/2007/Apr/ossec-alerts-22.log.sum) =
  6b1f3c29abc9e37ddb6b1a53ac83b0fe20830140


If you look at the checksum of Apr 22, it will have its own plus the one from the day 21 
(and the same will happen back until the first day that the chain started).

What do we get from that? First, any modification on the old logs will require changing all 
the next checksums. Second, if you e-mail them to you every day (or post somewhere publicly), 
you can have a valid case to prove that they were not tampered.


