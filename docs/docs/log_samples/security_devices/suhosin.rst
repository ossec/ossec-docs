Log samples for Suhosin
-----------------------


.. code-block:: console

  Apr  1 11:44:40 localhost suhosin[24239]: ALERT - configured request variable value length limit exceeded - dropped variable 'introtext' (attacker '192.168.1.2', file '/var/www/site/administrator/index2.php')
  Apr  1 11:47:20 localhost suhosin[23611]: ALERT - configured request variable value length limit exceeded - dropped variable 'content' (attacker '192.168.1.2', file '/var/www/site/index.php')
  Sep 15 14:18:47 enix suhosin[76367]: ALERT - canary mismatch on efree() - heap overflow detected (attacker '189.77.0.122', file '/srv/www/public_html/vbseo.php')
  Sep  8 10:28:23 xxyy suhosin[26338]: ALERT - tried to register forbidden variable 'GLOBALS' through GET variables (attacker '80.67.26.40', file '/home/htdocs/vbseo.php')
  Sep  8 07:11:30 aabb suhosin[14679]: ALERT - ASCII-NUL chars not allowed within request variables - dropped variable 'action' (attacker '209.51.140.58', file '')

