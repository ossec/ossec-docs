Active-response Internal Logic Flow
-----------------------------------

This is taken directly from the documentation in the source.

.. code-block:: console

  OSSEC HIDS 0.6
  Copyright (c) 2004-2006 Daniel B. Cid   <daniel.cid@gmail.com> <dcid@ossec.net>
                                        

How the active response works internally:

* Read active-respose-doc.txt for details on configuration


#. The analysis server receives an event that matches the active response policy.
#. The analysis server verifies that all required fields are provided with the event. It means that the analysis server was able to decode the event and extract the necessary information. One example is if it was able to extract the IP address from the event to send to the firewall to be blocked.
#. If the active response policy specify that the action must be executed locally on the AS, a message is sent to the execd directly.
#. If the active response policy specify that the action must be executed remotelly, a message is sent to the "Active response forwarder" (remoted) to forward the event to the specified agent.



