Log Samples from ProFTPD
------------------------

Startup message:
^^^^^^^^^^^^^^^^

..code-block:: console

  May 21 20:20:44 slacker proftpd[25526] proftpd.lab.ossec.net: ProFTPD 1.2.10 (stable) (built Tue Aug 2 22:33:07 PDT 2005) standalone mode STARTUP


Connection attempt:
^^^^^^^^^^^^^^^^^^^

..code-block:: console

  May 21 20:21:18 slacker proftpd[25530] proftpd.lab.ossec.net (192.168.20.10[192.168.20.10]): FTP session opened.



Connection closed:
^^^^^^^^^^^^^^^^^^

..code-block:: console

  May 21 20:22:14 slacker proftpd[25530] proftpd.lab.ossec.net (192.168.20.10[192.168.20.10]): FTP session closed.



Login sucessful:
^^^^^^^^^^^^^^^^

..code-block:: console

  May 21 20:22:28 slacker proftpd[25556] proftpd.lab.ossec.net (192.168.20.10[192.168.20.10]): USER dcid-test: Login successful.


Login failed:
^^^^^^^^^^^^^

..code-block:: console

  May 21 20:22:44 slacker proftpd[25557] proftpd.lab.ossec.net (192.168.20.10[192.168.20.10]): USER dcid-test (Login failed): Incorrect password.


Invalid user login attempt:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..code-block:: console

  May 21 20:21:21 slacker proftpd[25530] proftpd.lab.ossec.net (192.168.20.10[192.168.20.10]): no such user 'dcid-inv'

  May 21 20:21:21 slacker proftpd[31806] proftpd.lab.ossec.net (190.48.150.156[190.48.150.156]): USER abad: no such user found from 190.48.150.156 [190.48.150.156] to proftpd.lab.ossec.net:21


Full samples:
^^^^^^^^^^^^^

.. code-block:: console

  Jul 14 04:44:46 opala proftpd[30812] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 14871 usecs
  Jul 14 04:44:46 opala proftpd[30813] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): no such user 'guest' 
  Jul 14 04:44:46 opala proftpd[30813] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): USER guest: no such user found from sieapp.ufpel.edu.br [200.17.161.73] to 192.168.2.5:21
  Jul 14 04:44:46 opala proftpd[30813] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 86 usecs
  Jul 14 04:44:46 opala proftpd[30815] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session opened.
  Jul 14 04:44:46 opala proftpd[30814] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): no such user 'guest'
  Jul 14 04:44:46 opala proftpd[30814] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): USER guest: no such user found from sieapp.ufpel.edu.br [200.17.161.73] to 192.168.2.5:21
  Jul 14 04:44:46 opala proftpd[30813] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session closed.
  Jul 14 04:44:46 opala proftpd[30812] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session closed.
  Jul 14 04:44:46 opala proftpd[30815] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 33 usecs
  Jul 14 04:44:46 opala proftpd[30814] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session closed.
  Jul 14 04:44:47 opala proftpd[30816] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session opened.
  Jul 14 04:44:47 opala proftpd[30817] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session opened.
  Jul 14 04:44:47 opala proftpd[30818] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session opened.
  Jul 14 04:44:47 opala proftpd[30815] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): no such user 'guest'
  Jul 14 04:44:47 opala proftpd[30815] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): USER guest: no such user found from sieapp.ufpel.edu.br [200.17.161.73] to 192.168.2.5:21
  Jul 14 04:44:47 opala proftpd[30816] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 21 usecs
  Jul 14 04:44:47 opala proftpd[30817] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 129 usecs
  Jul 14 04:44:47 opala proftpd[30818] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 113 usecs
  Jul 14 04:44:47 opala proftpd[30815] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session closed.
  Jul 14 04:44:47 opala proftpd[30819] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): FTP session opened.
  Jul 14 04:44:47 opala proftpd[30816] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): no such user 'guest'
  Jul 14 04:44:47 opala proftpd[30816] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): USER guest: no such user found from sieapp.ufpel.edu.br [200.17.161.73] to 192.168.2.5:21
  Jul 14 04:44:47 opala proftpd[30816] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): mod_delay/0.5: delaying for 129 usecs
  Jul 14 04:44:47 opala proftpd[30817] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): no such user 'guest'
  Jul 14 04:44:47 opala proftpd[30817] opala.xxxxxx.edu.br (sieapp.ufpel.edu.br[200.17.161.73]): USER guest: no such user found from sieapp.ufpel.edu.br [200.17.161.73]


