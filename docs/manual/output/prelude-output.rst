
.. _manual-out-prelude:

Sending output to prelude
=========================

Prelude is a Hybrid IDS that uses IDMEF to receive alert information from external devices.
If you are a Prelude user and wish to send your OSSEC alerts to Prelude, do the following:

Enabling Prelude Support
------------------------

.. note::

    You must have the Prelude libraries installed on the OSSEC server.

Before you run the "./install.sh" script execute the following to compile OSSEC with
prelude support. 

.. code-block:: console 

    # cd ossec-hids-*
    # cd src; make setprelude; cd ..
    # ./install.sh 

Enable Prelude output in the configuration
------------------------------------------

Just add the following entry to your ossec.conf inside the <global> section.

.. code-block:: xml 

    <prelude_output>yes</prelude_output>

Prelude extra options
---------------------

You can define your own profile and set the log level from which you can send alerts to 
prelude with those parameters.  Once again in the <global> section.

.. code-block:: xml 

     <prelude_profile>MyOssecProfile</prelude_profile>
     <prelude_log_level>6</prelude_log_level>

