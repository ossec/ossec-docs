
.. _manual-out-picvis:

Sending alerts to picvis
========================

.. warning:: 

    PicVis support is experimnetal, and not fully supported.  Bug reports and 
    improvements are needed. 

Installation of PicVis 
---------------------- 

This is out of the scope for this document, but the development version from 
svn is required for PicVis to work with OSSEC.  

Setup OSSEC for PicVis 
----------------------

Configure OSSEC to send events to PicVis.  The following configuation 
needs to be added to /var/ossec/etc/ossec.conf. 

.. code-block:: xml

    <ossec_config> 
        <global> 
            <picviz_output>yes</picviz_output>
            <picviz_socket>/var/ossec/picviz.socket</picviz_socket>

For more full details on this section of the config see :ref:`ossec_config.global`. 

Start up PicVis 
--------------- 

On picviz side, an OSSEC template is available in the template directory and Picviz should be run like this:

.. code-block:: console 

    # pcv -Tpngcairo -o ossec.png -s /var/ossec/picviz.socket -t templates/ossec.pgdt -a 
