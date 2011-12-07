Nessus scan in a web server log
-------------------------------

.. code-block::console

  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /tools/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /ticket/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usr/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /upload/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trees/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /transpolar/ HTTP/1.1" 404 316 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trabajo/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /tools/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuarios/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /upload/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trees/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /transpolar/ HTTP/1.1" 404 316 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trabajo/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /utils/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /upload/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trees/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /transpolar/ HTTP/1.1" 404 316 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w-agora/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /upload/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /trees/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /way-board/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w3perl/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /upload/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /web800fo/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /web/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w3perl/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /us/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webapps/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webMathematica/ HTTP/1.1" 404 320 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /web/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w3perl/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /user/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webcart/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webboard/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webMathematica/ HTTP/1.1" 404 320 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /web/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w3perl/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /usuario/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webdata/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webcart-lite/ HTTP/1.1" 404 318 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webboard/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webMathematica/ HTTP/1.1" 404 320 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /web/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /w3perl/ HTTP/1.1" 404 312 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /vfs/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /util/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webimages/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webdb/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webcart-lite/ HTTP/1.1" 404 318 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webboard/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webMathematica/ HTTP/1.1" 404 320 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /weblogs/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webimages2/ HTTP/1.1" 404 316 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /webdb/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /word/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /windows/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /website/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /xGB/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /wwwjoin/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /www/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /work/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /windows/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /website/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /~log/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /~1/ HTTP/1.1" 404 308 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /zb41/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /xml/ HTTP/1.1" 404 309 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  192.168.100.55 - - [16/Aug/2006:14:29:58 -0300] "GET /wwwjoin/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"

How ossec would alert
^^^^^^^^^^^^^^^^^^^^^

.. code-block::console

  OSSEC HIDS Notification.
  2006 Aug 16 14:29:58

  Received From: copacabana->/var/log/apache2/access.log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shipping/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shell-cgi/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /share/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /session/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servlet/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servicio/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /service/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servers/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"



  --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2006 Aug 16 14:29:58

  Received From: copacabana->/var/log/apache2/access.log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shopper/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shop/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shell-cgi/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /share/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /session/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servlet/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servicio/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /service/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"



  --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2006 Aug 16 14:29:58

  Received From: copacabana->/var/log/apache2/access.log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /sitemgr/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /site/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shop/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shell-cgi/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /share/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /session/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servlet/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.10.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servicio/ HTTP/1.1" 404 314 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"



  --END OF NOTIFICATION



  OSSEC HIDS Notification.
  2006 Aug 16 14:29:58

  Received From: copacabana->/var/log/apache2/access.log
  Rule: 31151 fired (level 10) -> "Mutiple web server 400 error codes from same source ip."
  Portion of the log(s):

  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /siteminderagent/ HTTP/1.1" 404 321 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /siteminder/ HTTP/1.1" 404 316 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /site/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shop/ HTTP/1.1" 404 310 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /shell-cgi/ HTTP/1.1" 404 315 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /share/ HTTP/1.1" 404 311 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /session/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"
  10.1.50.21 - - [16/Aug/2006:14:29:58 -0300] "GET /servlet/ HTTP/1.1" 404 313 "-" "Mozilla/4.75 [en] (X11, U; Nessus)"



  --END OF NOTIFICATION


