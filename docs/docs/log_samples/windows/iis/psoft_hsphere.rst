Psoft H-Sphere IIS Log File Format
----------------------------------

   1. Software: Psoft H-Sphere running on Microsoft Internet Information Services 6.0
   2. Version: 1.0
   3. Date: 2007-03-04
   4. Fields: date time c-ip cs-username s-sitename s-computername s-ip s-port cs-method cs-uri-stem cs-uri-query sc-status sc-win32-status sc-bytes cs-bytes time-taken cs-version cs(User-Agent) cs(Cookie) cs(Referer)

IIS Logs saved on E:\hslogfiles\www\W3SVC*\ex%y%m%d.log (where W3SVC* is sites 1-254 and ex070304.log):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  #Software: H-Sphere log plugin
  #Date: 2007-03-03 01:17:39
  #Fields: date time c-ip cs-username s-sitename s-computername s-ip s-port cs-method cs-uri-stem cs-uri-query sc-status sc-win32-status sc-bytes cs-bytes time-taken cs-version cs(User-Agent) cs(Cookie) cs(Referer)
  2007-03-03 01:17:39 66.194.6.79 - W3SVC3 SERVER55 192.168.1.15 80 GET /index.html - 200 0 17691 117 15 HTTP/1.1 Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+Q312460) - -
  2007-03-03 10:23:40 24.252.248.163 - W3SVC3 SERVER55 192.168.1.15 80 GET /images/9a.jpg - 200 0 32022 324 47 HTTP/1.1 Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322) - http://www.yahoo.com/

