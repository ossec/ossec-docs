Log Samples from Nginx
by default nginx writes logs to access.log and error.log, similarly to apache.

= access log samples =
.. code-block:: console
66.75.252.36 - - [14/Aug/2008:04:54:45 +0000] "GET /wiki/skins/common/shared.css?116 HTTP/1.1" 200 818 "http:// example.com/wiki/index.php?title=Main_Page" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us)           AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"
66.75.252.36 - - [14/Aug/2008:04:54:45 +0000] "GET /wiki/skins/common/commonPrint.css?116 HTTP/1.1" 200 1980    "http://example.com/wiki/index.php?title=Main_Page" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us)   AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"


= error log samples =
.. code-block:: console
2008/08/14 12:59:05 [error] 7419#0: *625 directory index of "/var/www/example.com/wiki/skins/" is forbidden,    client: 66.249.71.183, server: example.com, request: "GET /wiki/skins/ HTTP/1.1", host: "example.com"
2008/08/14 14:37:31 [error] 7418#0: *820 open() "/var/www/example.com/robots.txt" failed (2: No such file or    directory), client: 66.249.71.184, server: example.com, request: "GET /robots.txt HTTP/1.1", host: "example.com"


