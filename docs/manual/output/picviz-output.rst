
.. _manual-out-picviz:

Sending alerts to picviz
========================

.. warning:: 

    PicViz support is very experimental, and not fully supported.  Bug reports and 
    improvements are needed. 

Installation of PicViz
---------------------- 

This is out of the scope for this document, but the development version from 
svn is required for PicViz to work with OSSEC.  

Setup OSSEC for PicViz 
----------------------

Configure OSSEC to send events to PicViz.  The following configuration 
needs to be added to /var/ossec/etc/ossec.conf. 

.. code-block:: xml

    <ossec_config> 
        <global> 
            <picviz_output>yes</picviz_output>
            <picviz_socket>/var/ossec/picviz.socket</picviz_socket>

For more full details on this section of the config see :ref:`ossec_config.global`. 

Start up PicViz 
--------------- 

On the picviz side, an OSSEC template is available in the template directory and Picviz should be run like this:

.. code-block:: console 

    # pcv -Tpngcairo -o ossec.png -s /var/ossec/picviz.socket -t templates/ossec.pgdt -a 
