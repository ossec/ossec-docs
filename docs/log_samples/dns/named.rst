Log Samples from Named
----------------------

Some information about named logs can be found at:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

http://www.netadmintools.com/art233.html
`List of errors <http://www.reedmedia.net/misc/dns/errors.html>`_
`List of Bind 8 and 9 errors <http://www.menandmice.com/knowledgehub/bindlogmsgs>`_



Query cache denied (attempt to use server not authorized):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Aug 29 15:33:13 ns3 named[464]: client 217.148.39.3#1036: query (cache) denied
  Aug 29 15:33:13 ns3 named[464]: client 217.148.39.4#32769: query (cache) denied
  Aug 29 15:33:13 ns3 named[464]: client 217.148.39.3#1036: query (cache) denied
  Aug 29 15:33:13 ns3 named[464]: client 217.148.39.4#32769: query (cache) denied



Fatal errors:
^^^^^^^^^^^^^

.. code-block:: console

  named[17546]: loading configuration: failure
  named[17546]: exiting (due to fatal error)



Zone transfer errors:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jul  4 10:31:39 internet-gw named[7136]: zone dominio.com.br/IN/external: expired



