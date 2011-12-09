Log Samples for Symantec Web Security
-------------------------------------


Generic entries:
^^^^^^^^^^^^^^^^

.. code-block:: console

  20070717,30020,1=3,41=SWS-3.0.1.86/lists,100=Version 3.0.3299,3=7,2=29
  20070717,30024,100=SWS-3.0.1.86,2=36
  20070717,30044,1=3,3=1,2=302
  20070717,30044,1=3,1202=20070715.002,1203=20070715.002,3=7,2=301
  20070717,30225,1=3,41=SWS-3.0.1.86/dictionaries,100=Version 3.0.638,3=7,2=29
  20070717,30517,1=3,41=SWS-3.0.1.86/vendor-config,100=Version 3.0.6,3=7,2=29
  20070717,40031,1=3,41=SWS-3.0.1.86/lists,100=Version 3.0.3299,3=7,2=29


Session timeout (3=1,2=2):
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  20070717,73559,1=5,11=1.2.3.4,100=Logoff due to timeout.,10=user2,3=1,2=2
  20070717,73559,1=5,11=5.6.7.8,100=Logoff due to timeout.,10=user3,3=1,2=2
  20070717,73559,1=5,11=6.7.8.9,100=Logoff due to timeout.,10=user4,3=1,2=2


Login success (3=2,2=1):
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  20070717,73613,1=5,11=10.1.1.3,10=userc,3=1,2=1
  20070717,103426,1=5,11=1.2.3.4,10=virtadmin,3=1,2=1


Login failures: (3=2,2=1):
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  20070717,73559,1=5,11=10.1.1.1,10=usera,3=2,2=1
  20070717,73604,1=5,11=10.1.1.2,10=userb,3=2,2=1
  20070717,103330,1=5,11=1.2.3.4,10=virtadmin,3=2,2=1


URLs:
^^^^^

.. code-block:: console

  20070717,73614,1=5,11=1.2.3.4,1106=News,60=http://news.bbc.co.uk/,10=userX,1000=212.58.240.42,2=27
  20070717,115252,1=5,11=1.2.3.4,1106=Miscellaneous,60=https://ad.doubleclick.net/,10=userY,1000=216.73.87.52,2=27
  20070717,122017,1=5,11=2.3.4.5,1106=Finance,60=http://www.esl.org/,10=userB,1000=208.2.188.219,2=27



Example of ossec parsing it:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  ** Alert 1184856821.41038: - symantec,authentication_success,
  2007 Jul 19 11:53:41 xyz->file
  Rule: 7415 (level 3) -> 'Login success accessing the web proxy.'
  Src IP: 10.1.1.3
  User: userc
  20070717,73613,1=5,11=10.1.1.3,10=userc,3=1,2=1

  ** Alert 1184856843.41290: - symantec,authentication_success,
  2007 Jul 19 11:54:03 abc->file
  Rule: 7415 (level 3) -> 'Login success accessing the web proxy.'
  Src IP: 10.1.1.3
  User: userc
  20070717,73613,1=5,11=10.1.1.3,10=userc,3=1,2=1


