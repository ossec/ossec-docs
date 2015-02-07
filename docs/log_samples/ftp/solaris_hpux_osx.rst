Log Samples from Solaris/HP-UX FTPD
-----------------------------------

Connection attempt:
^^^^^^^^^^^^^^^^^^^

..code-block:: console

  May 28 15:50:36 sol1 ftpd[28370]: connection from slacker.lab.ossec.net at Sun May 28 15:50:36 2006
  May 28 15:50:36 sol1 ftpd[28370]: FTP LOGIN FROM slacker.lab.ossec.net, test-user


Connection refused:
^^^^^^^^^^^^^^^^^^^

..code-block:: console

  Jun  3 13:37:10 sol2 ftpd[327802]: refused connect from spongebob.lab.ossec.net



Login failed:
^^^^^^^^^^^^^

..code-block:: console

  Jun  2 16:44:05 sol2 ftpd[28662]: repeated login failures from spongebob.lab.ossec.net
  Sep 11 08:59:41 xxx ftpd[18658]:  PAM_ERROR_MSG: Account is disabled - see Account Administrator.


Login failed:
^^^^^^^^^^^^^

..code-block:: console

  Jun  2 16:44:05 sol2 ftpd[28662]: repeated login failures from spongebob.lab.ossec.net


Transactions:
^^^^^^^^^^^^^

..code-block:: console

  May 28 19:38:24 sol1 ftpd[24474]: FTPD: IMPORT file local /home/test/file2.tgz, remote
  Jun  1 22:50:26 sol2 ftpd[22898]: FTPD: IMPORT file local file1.tgz, remote
  May 28 15:14:02 sol2 ftpd[28616]: FTPD: EXPORT file local , remote aka.html


Mac OS X Server 10.5 FTP logs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jun 20 09:00:42 File-Server ftpd[65613]: Failed authentication from: [U2FsdGVkX18af1PrJ6KSUhskC8ikccfvTqyjjJI/qtk=] @ 58.211.16.202 [58.211.16.202] 
  Jun 20 09:00:52 File-Server ftpd[65625]: Failed authentication from: [U2FsdGVkX1+RbLXPa7lV2Ly9a3Bir9x88RdjF2oWkg4=] @ 58.211.16.202 [58.211.16.202] 
  Jun 20 09:01:02 File-Server ftpd[65639]: Failed authentication from:  [U2FsdGVkX18V16WdD4Z7rcx6tv0zBiUG6bok2Y3IQGQ=] @ 58.211.16.202 [58.211.16.202] 
  Jun 25 10:24:06 File-Server ftpd[29807]: Failed authentication from: 1.Red-88-2-137.staticIP.rima-tde.net [88.2.137.1] 
  Jun 25 10:24:25 File-Server ftpd[29871]: Failed authentication from:   1.Red-88-2-137.staticIP.rima-tde.net [88.2.137.1]
  Jul  4 02:11:44 File-Server ftpd[54844]: FTP LOGIN REFUSED (PASS  before USER) FROM 202.113.244.42 [202.113.244.42]


