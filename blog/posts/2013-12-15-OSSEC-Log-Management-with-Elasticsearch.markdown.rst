.. post:: Oct 15, 2013
   :tags: siem
   :category: Integrations
   :author: Vic Hargrave

=======================================
OSSEC Log Management with Elasticsearch
=======================================

Among the many useful features of OSSEC is its capability to send alerts
to any system that can consume syslog data. This makes it easy to
combine OSSEC with a number of 3rd party SIEMs to store, search and
visualize security events. `Splunk for
OSSEC <http://apps.splunk.com/app/300/>`_ is one such system that works
on top of the Splunk platform.

Splunk can be expensive though, particularly if you collect a lot of log
data. So I’ve been working on a solution for collecting OSSEC security
alerts based on Elasticsearch that provides a cost effective alternative
to Splunk.

`Read more <https://vichargrave.github.io/articles/2013-11/ossec-log-management-with-elasticsearch>`_
