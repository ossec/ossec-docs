
.. _util.sh:

util.sh
=======

The ``util.sh`` script can add a file to be monitored by ``ossec-logcollector``.
 It can also add a full_command to check for changes to a website, or for changes to the name server of a domain.  

util.sh argument options
~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: util.sh

.. option:: addfile <filename> [<format>]

    Add a file to be monitored by ``ossec-logtest``. A ``localfile`` will be added to the ossec.conf.

.. option:: addsite <domain>

   Monitor a website for changes. A ``full_command`` will be added to the ``ossec.conf`` using lynx to dump the initial page.
   A rule can be written to monitor this output for changes.

   .. note::
      Requires `lynx <http://lynx.isc.org/current/>`_.

   .. warning::
      This may not be useful on pages with dynamic content.

.. option:: adddns <domain>

   Monitor the name server of a domain for changes. A ``full_command`` will be added to the ossec.conf using host

   .. note::
      Requites the ``host`` command.

util.sh example usage
~~~~~~~~~~~~~~~~~~~~~

Example: Running util.sh
^^^^^^^^^^^^^^^^^^^^^^^^

Running the following command:

.. code-block:: console

    # /var/ossec/bin/util.sh adddns ossec.net

will add the folling to that system's ``ossec.conf``:

.. code-block:: console

  <ossec_config>
     <localfile>
       <log_format>full_command</log_format>
       <command>host -W 5 -t NS ossec.net; host -W 5 -t A ossec.net | sort</command>
     </localfile>
   </ossec_config>


